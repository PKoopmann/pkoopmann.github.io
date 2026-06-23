#!/usr/bin/env python3
"""
dblp_to_markdown.py
====================
Fetches Patrick Koopmann's bibliography from DBLP and writes a nicely
formatted Markdown page with links to papers where available.

Usage:
    python3 dblp_to_markdown.py                  # fetch live from DBLP
    python3 dblp_to_markdown.py --local data.xml # use a local XML file
    python3 dblp_to_markdown.py --output out.md  # change output filename

The DBLP person ID is hard-coded below; change DBLP_PID to use for
any other author.
"""

import argparse
import sys
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from html import unescape

# ─── configuration ────────────────────────────────────────────────────────────

DBLP_PID    = "33/10169"     # Patrick Koopmann
OUTPUT_FILE = "koopmann_bibliography.md"

# Publication type → display order within a year (lower index = appears first)
TYPE_ORDER = [
    ("article",       "Journal Article"),
    ("inproceedings", "Conference / Workshop Paper"),
    ("proceedings",   "Edited Proceedings"),
    ("phdthesis",     "PhD Thesis"),
    ("mastersthesis", "Master's Thesis"),
    ("incollection",  "Book Chapter"),
    ("book",          "Book"),
    ("informal",      "Preprint"),
]
TYPE_PRIORITY = [t for t, _ in TYPE_ORDER]
TYPE_LABELS   = dict(TYPE_ORDER)

# ─── DBLP fetching ────────────────────────────────────────────────────────────

def fetch_xml_from_dblp(pid: str) -> ET.Element:
    """Download a DBLP person XML file and return the parsed root element."""
    url = f"https://dblp.org/pid/{pid}.xml"
    print(f"Fetching {url} ...", file=sys.stderr)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "dblp-bib-fetcher/1.0 (bibliography export script)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except urllib.error.HTTPError as exc:
        sys.exit(
            f"Error: DBLP returned HTTP {exc.code} for {url}.\n"
            "If you are running this in a sandboxed environment, DBLP may be\n"
            "blocking automated requests.  Try one of these alternatives:\n"
            "  1. Download the XML manually in your browser:\n"
            f"       {url}\n"
            "     then run:  python3 dblp_to_markdown.py --local <downloaded.xml>\n"
            "  2. Change DBLP_PID at the top of this script for a different author."
        )
    except urllib.error.URLError as exc:
        sys.exit(f"Network error: {exc.reason}")
    return ET.fromstring(data)


def load_xml_from_file(path: str) -> ET.Element:
    """Load a DBLP person XML file from disk."""
    print(f"Loading {path} ...", file=sys.stderr)
    try:
        tree = ET.parse(path)
        return tree.getroot()
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {path}")
    except ET.ParseError as exc:
        sys.exit(f"Error: could not parse XML in {path}: {exc}")

# ─── XML helpers ──────────────────────────────────────────────────────────────

def _text(elem: ET.Element, tag: str, default: str = "") -> str:
    node = elem.find(tag)
    return unescape(node.text or default) if node is not None and node.text else default


def _all_text(elem: ET.Element, tag: str) -> list[str]:
    return [unescape(n.text) for n in elem.findall(tag) if n.text]


def _best_url(pub: ET.Element) -> str | None:
    """Return the most useful URL for a publication (prefer DOI links)."""
    for ee in pub.findall("ee"):
        if ee.text and "doi.org" in ee.text:
            return ee.text
    for ee in pub.findall("ee"):
        if ee.text:
            return ee.text
    url_node = pub.find("url")
    if url_node is not None and url_node.text:
        return "https://dblp.org/" + url_node.text.lstrip("/")
    return None


def _classify(pub: ET.Element) -> str:
    """Map a pub element to its logical type (splitting CoRR out of 'article')."""
    tag = pub.tag
    if tag == "article":
        journal = _text(pub, "journal", "").upper()
        if journal in ("CORR", "ARXIV"):
            return "informal"
    return tag


def _type_sort_key(pub: ET.Element) -> int:
    classified = _classify(pub)
    try:
        return TYPE_PRIORITY.index(classified)
    except ValueError:
        return len(TYPE_PRIORITY)

# ─── Markdown formatting ──────────────────────────────────────────────────────

def _format_authors(pub: ET.Element) -> str:
    authors = _all_text(pub, "author") or _all_text(pub, "editor")
    if not authors:
        return "Unknown"
    if len(authors) == 1:
        return authors[0]
    return ", ".join(authors[:-1]) + ", and " + authors[-1]


def format_pub(pub: ET.Element) -> str:
    """Format a single publication as a Markdown list item (without type badge)."""
    authors   = _format_authors(pub)
    title     = _text(pub, "title").rstrip(".")
    year      = _text(pub, "year", "????")
    url       = _best_url(pub)
    pub_type  = pub.tag   # original XML tag

    venue_parts: list[str] = []

    if pub_type == "article":
        journal = _text(pub, "journal")
        volume  = _text(pub, "volume")
        number  = _text(pub, "number")
        pages   = _text(pub, "pages")
        if journal:
            vol_str = f" {volume}" if volume else ""
            num_str = f"({number})" if number else ""
            pag_str = f": {pages}" if pages else ""
            venue_parts.append(f"*{journal}*{vol_str}{num_str}{pag_str}")

    elif pub_type in ("inproceedings", "incollection"):
        booktitle = _text(pub, "booktitle")
        pages     = _text(pub, "pages")
        if booktitle:
            pag_str = f": {pages}" if pages else ""
            venue_parts.append(f"In *{booktitle}*{pag_str}")

    elif pub_type == "proceedings":
        booktitle = _text(pub, "booktitle") or _text(pub, "title")
        venue_parts.append(f"*{booktitle}*")

    elif pub_type in ("phdthesis", "mastersthesis"):
        school = _text(pub, "school")
        if school:
            venue_parts.append(school)

    elif pub_type == "book":
        publisher = _text(pub, "publisher")
        if publisher:
            venue_parts.append(publisher)

    else:
        # informal / CoRR / arXiv
        journal = _text(pub, "journal")
        volume  = _text(pub, "volume")
        if journal:
            venue_parts.append(f"*{journal}*{(' ' + volume) if volume else ''}")

    venue_str  = (", ".join(venue_parts) + ", " if venue_parts else "")
    title_md   = f"[{title}]({url})" if url else title

    return f"- {authors}: {title_md}. {venue_str}{year}."


def build_markdown(root: ET.Element) -> str:
    """Build the full Markdown document organised by year."""
    person_node = root.find("person")
    person = person_node if person_node is not None else root
    names  = [n.text for n in person.findall("author") if n.text]
    display_name = names[0] if names else "Patrick Koopmann"

    # Collect all publications
    known_tags = {
        "article", "inproceedings", "proceedings",
        "phdthesis", "mastersthesis", "incollection", "book",
    }
    all_pubs: list[ET.Element] = [e for e in root.iter() if e.tag in known_tags]
    total = len(all_pubs)

    # Group by year; within each year sort by type priority
    pubs_by_year: dict[str, list[ET.Element]] = defaultdict(list)
    for pub in all_pubs:
        pubs_by_year[_text(pub, "year", "????")].append(pub)

    sorted_years = sorted(pubs_by_year.keys(), reverse=True)
    for year in sorted_years:
        pubs_by_year[year].sort(key=_type_sort_key)

    # ── Render Markdown ──────────────────────────────────────────────────────
    lines: list[str] = []
    lines.append(f"# Bibliography of {display_name}\n")
    lines.append(
        f"> Source: [DBLP](https://dblp.org/pid/{DBLP_PID}.html)  \n"
        f"> **{total} publications** across {len(sorted_years)} years\n"
    )

    # Table of contents
    lines.append("\n## Contents\n")
    for year in sorted_years:
        n = len(pubs_by_year[year])
        lines.append(f"- [{year} ({n} publication{'s' if n != 1 else ''})](#year-{year})")

    # One section per year
    for year in sorted_years:
        lines.append(f"\n## {year}\n")
        for pub in pubs_by_year[year]:
            classified = _classify(pub)
            type_label = TYPE_LABELS.get(classified, classified.capitalize())
            entry = format_pub(pub).rstrip(".")
            # Append a small italic type badge
            lines.append(f"{entry}. *{type_label}.*")

    return "\n".join(lines) + "\n"

# ─── Entry point ──────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--local",  metavar="FILE",
                   help="Use a local DBLP XML file instead of fetching from the web.")
    p.add_argument("--output", metavar="FILE", default=OUTPUT_FILE,
                   help=f"Output Markdown file (default: {OUTPUT_FILE})")
    p.add_argument("--pid",    metavar="PID",  default=DBLP_PID,
                   help=f"DBLP person ID (default: {DBLP_PID})")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    global DBLP_PID
    DBLP_PID = args.pid

    root = load_xml_from_file(args.local) if args.local else fetch_xml_from_dblp(args.pid)
    md   = build_markdown(root)

    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write(md)

    lines = md.splitlines()
    total_pubs = sum(1 for l in lines if l.startswith("- ") and not l.startswith("- [20"))
    year_sections = [l for l in lines if l.startswith("## Year")]
    print(f"\nDone! Written to '{args.output}'", file=sys.stderr)
    print(f"{total_pubs} publications across {len(year_sections)} year sections.", file=sys.stderr)


if __name__ == "__main__":
    main()
