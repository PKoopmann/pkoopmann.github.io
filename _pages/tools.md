---
layout: archive
title: "Tools"
permalink: /tools/
author_profile: true
---

Smaller and larger tools and libraries developed as part of my research.

dl-lib - Working with Description Logics in Python and Scala
=============================================================

<img src='/images/dl-lib-screenshot.png'>


Simple library to work with description logic ontologies from
python or scala, without having to learn about OWL terminology.
All classes and method names use DL terminology, though one can
parse and export to OWL ontologies.



[Link](https://github.com/PKoopmann/dl-lib)


EVEE - Evincing Expressive DL Entailments
=====

<img src='/images/evee-screenshot.png'>

Although logic-based ontology languages offer the inherent possibility of explaining the process of deriving implicit knowledge, explaining complex Description Logic (DL) entailments to users is still a challenging task. So far, the ontology editor Protégé supports only (black-box) justifications and (glass-box) proofs for lightweight OWL 2 EL ontologies via the proof facilities of the reasoner Elk. To understand why something is not entailed by the ontology, and how this can be fixed in a suitable manner, there is currently no tool support in Protege. 

Evee is both a library and a collection of Protege plugins for explaining DL entailments. While the version 0.1 only provided explanations for positive entailments (why can something we inferred), the newer versin 0.2 also provides explanations for negative entailments (why can something not be inferred).Explanations for positive entailments are provided through proofs --- sequences of inference steps that lead from the statements in the ontology to the derived entailment --- which are generated using various methods. Negative entailments are explained in two ways: 1. by generating a counterexample, or 2. by showing missing axioms that would create the entailment.

[Link](https://github.com/de-tu-dresden-inf-lat/evee)

EVONNE
=====

<img src='/images/evonne-screenshot.png'>

Evonne is a powerful web application for explaining entailments from ontologies. These entailments are explained using proof trees, for which we offer a range of navigation possibilities to explore these inferences. This can be used to better understand reasoning result from an ontology, but it can also be used for teaching purposes (explaining how reasoning works), and for debugging (determining how an erroneous statement was derived). For the latter use case, we connect the proof visualization with a graph like visualization of a relevant fragment of the ontology, which allows to quickly localize axioms used in the proof and their role and impact within the greater context of the ontology. Evonne can also be used to compute diagnoses --- sets of axioms that need to be modified or removed in order to remove the entailment --- which are then shown together with their impact on other statements in the ontology.

The tool can be installed locally using docker, but also tried online.

[Link](https://mt.inf.tu-dresden.de/en/research/research-projects/evonne/)


GeMO - Extracting General Modules for ALC Ontologies
=====

This is a tool for extracting knowledge from an ontology that is relevant for a specified signature of concept and role names (classes and object properties). The term "general module" generalizes the notions of uniform interpolation and classical modules. In particular, given a signature and an ontology, GeMO computes a new ontology --- the general module --- that preserves all logical entailments of the ontology that can be expressed using only the names from that ontology. Different to a classical module, the general module does not have to be a subset of the ontology, but may contain axioms that are not in the original ontology, which can lead to more focussed results. However, different to a uniform interpolant, the general module may still contain names that are not in the specifed signature, which can lead to smaller axioms.   

[Link](https://hub.docker.com/r/yh1997/demo_gemo)


CAPI - Connection-minimal Abduction using Prime Implicates
=====

Performs TBox abduction for EL ontologies, which can be used to repair and explain missing entailments.

UPDATE 2022-12-13: new version 0.2 with additional post-processing.

[Link](https://lat.inf.tu-dresden.de/~koopmann/CAPI)

ELK Certifier
=====

Certify ELK classification results so that they can be verified with the LFSC proof-checker.

[Link](https://lat.inf.tu-dresden.de/~koopmann/ELK-Certifier/index.html)

LETHE-Abduction
=====

An extension of LETHE for performing signature-based abduction for ALC knowledge bases. To be used as library for Java.

[Link](https://lat.inf.tu-dresden.de/~koopmann/LETHE-Abduction/index.html)


lat-scala-dl-tools
=====

Collection of classes and objects to make work with OWL under Scala and Java more convenient.

[link](https://github.com/de-tu-dresden-inf-lat/lat-scala-dl-tools)


LETHE
=====

<img src='/images/lethe-screenshot.png'>


Uniform interpolation and forgetting for expressive description logics. (Supports SH knowledge bases, and with restrictions SHQ TBoxes.) Comes with a graphical front-end, but can also be used from the command line or as java library.

[link](https://lat.inf.tu-dresden.de/~koopmann/LETHE/index.html)


