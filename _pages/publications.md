---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>,</u> as well as on <u><a href="https://dblp.org/pid/33/10169.html">DBLP</a>.</u>


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
