---
layout: archive
title: "Theses"
permalink: /theses/
author_profile: true
---


If you want to do a bachelor or master thesis, don't be afraid to send
me an email. I have a range of topics listed below, and I can give
you additional information based on your experience, skills and
interests. If you have your own idea, we can discuss it to see whether
it is feasible, whether I am the right supervisor, or whether there
are similar directions that would be better suited. One warning: even
though my expertise is in a subfield of artificial intelligence, I
will not supervise theses with a focus on deep learning, large
language models or image recognition. My focus is on symbolic AI, that
is, knowledge representation and logic-based AI. Consequently, theses
topics will have to be related to those fields. 

This year, a majority of topics revolves around explanations for
description logic ontologies. This is in the context of a larger
project that aims at improving the experience of ontology developers
through better tool supports. We have developed a range of tools for
explainability already, that you can try out through the web
application Evonne, as well as through the Protege plugin collection
Evee. For some of the student projects, it is possible that the
results can get connected to these tools. It should be noted however
that the development of the user interface is not part of any project,
but rather the development of better explanation methods that can then
be used by these frontends.

There are also some exciting topics that are not related to
explanation. Scroll down to see what is there.

Most of the project are designed in a scalable way, so that they can
be adapted based on the skill sets of the student. For this reason,
there are also many projects that are available to both Bachelor and
Master students. This means that the project will have a different
character depending on whether it is for 
a Bachelor or for a Master thesis. The Bachelor project would look
at a simplified version of the problem, and often extend or use
existing tools, while the Master thesis will be more involved, and
even involve the development of new methods and prototypes.

Explanations for Ontologies
======


We offer a range of projects around the topic of explanations for
ontologies. We focus on ontologies based on description logics or
OWL. A main advantage of formulating knowledge in such a formalism is
that one can use a reasoner to derive implicit information. However,
not always is the result of this reasoning process easy to understand:
users might wonder why something was derived (explain positive
entailment), or why something was not derived (explain negative
entailments). Motivated by this, different methods have been developed
to provide explanations for positive and negative entailments. 


### Explaining Entailments using New Inference Rules 


The classical way of explaining why something follows from an ontology
is by providing a proof tree, that shows in small steps how the
positive entailment is derived from the statements in the
ontology. Such a proof is usually generated based on a set of
rules. We have a tool that can process user-defined sets of inference
rules to generate rules. Existing sets of rules are usually not
optimized for human understanding. The aim of this project is to
develop new sets of inference rules that lead to nicer proofs, and
provide an evaluation and comparion with existing explanation methods
based on realistic ontologies. 

This project is primarily intended for Bachelor students, but if a
Master student finds this topic interesting, there is also a Master
project version.  



### Explaining Positive Entailments using Universal Models 

The topic of this project is to explain queries to data that is used
together with an ontology. Specifically, the user asks for instances
of a concept C, and he would like to understand why individual name
"a" is an answer to this query. There are ontology languages where
this can be explained based on so-called universal models: a universal
model is a model of the ontology that captures all entailments. The
aim of this project would be to develop a method to generate
explanations based on such models. 

This project is suitable for Bachelor and Master students.


### Explaining Missing Entailments using Counter-Examples


One way to explain a missing entailment is by providing an counter
example. For example, a counterexample for the statement
"every pizza is vegetarian" 
from an ontology about pizzas would be a pizza with a salami topping,
which would be model of the concept "Pizza", but not of
"VegetarianPizza". The topic of this project is to develop and
evaluate a method for computing such counterexamples. The Master
version is towards developing a new method based on existing reasoning
procedures. The Bachelor version will be about improving and extending
an existing method.


This project is suitable for Bachelor and Master students.

### Explaining Missing Entailments using Connection-Minimal Abduction


Abduction is an approach to explain missing entailments by stating
"what is missing" - namely, suggesting statements that, when added to
the ontology, would make the entailment positive. There are many
different conditions one can give to such an explanation to make it
"useful". This project focusses on a recently discovered criterion
called "connection-minimality". Depending on the interests, there are
different directions possible. A more practically interested student
would get the task of developing a new method for performing
connection-minimal abduction, and compare it to the
state-of-the-art. For students that are less interested in
implementations, the project would be to develop a new criterion based
on connection-minimality, which overcomes some of the limitations of
the existing one. 

This project is suitable for Bachelor and Master students.

### Explaining Missing Entailments using Signature-Based Abduction

Abduction is an approach to explain missing entailments by stating
"what is missing" - namely, suggesting statements that, when added to
the ontology, would make the entailment positive. There is an
abduction tool called LETHE-abduction that computes such explanations
based on a provided signature: a vocabulary of names that are allowed
to be used in the explanation. Selecting such a vocabulary is
currently up to the user. The goal of this project is to investigate
and compare heuristics for selecting signatures for computing a nice
sequence of explanations.


This project is suitable for Bachelor and Master students.



Learning Concept Descriptions
======

The aim of this project is to implement and evaluate a new method for
learning description logic concept descriptions from examples. The
idea is that an ontology is used together with a set of positive and
negative examples. The aim is that to generate a concept that
describes all positive, but none of the negative examples. The
learning procedure will be based on logical reasoning, that is, will
use logical reasoning (with the help of existing tools) to compute the
concept. 

There is a version of this project for both Bachelor and Master students.

Extracting Subontologies
======

Existing ontologies are often very large and complex, while
applications are often only need a fragment of the information
provided by the ontology. There are different techniques (module
extraction, uniform interpolation) that can be used to extract
subontologies. The aim of this project is to investigate and evaluate
heuristics to improve the performance of these methods, leading to
simpler ontologies, and shorter computation times. 

This project is most suited for Bachelor students.

Optimizing Concept Expressions 
======

Ontologies often contain expressions that are more complex than
necessary. This is even more a problem with ontology content that is
automatically generated, which appears in many applications. The aim
of this project is to develop a method to optimize concept
expressions by replacing them by equivalent expressions that are of
minimal size. One possibility is to use ideas from concept learning.

This project is most suited for Master students.

Automated Hypothesis Generation using ABox abduction
======

This project looks at the following problem: we have an ontology, as
well as some data in the form of a knowledge graph of ABox. This
contains our background knowledge about some domain such as medicine,
or a context from robotics. We are then given a set of facts that do
not follow from what we know according to our background knowledge -
an observation that is somehow unexpected, for instance a description
of symptoms of a patient or of an unexpected situation encountered by
a robot. We then want to generate a hypothesis in the form of a set of
facts that would explain the observation if added to the background
knowledge. To avoid trivial answers, we assume that there is also a
special vocabulary for explanations provided. This means, we want to
compute a hypothesis that uses only terms from that vocabulary, but
may refer also to unknown objects. This problem is called
signature-based ABox abduction. The aim of this project is to develop
a new method for signature-based ABox abduction based on some recent
theoretical results of this problem.


This project is intended as Master project.

