---
title: Quantum Advantage Partners
subtitle: 

summary: |
  In real organizations, each role (CEO, CFO, VP Sales…) sees different
  information and applies different decision criteria - yet every multi-agent
  simulation framework today gives all agents the same shared context. This
  project seeks to mathematically test whether modeling information
  compartmentalization and role-specific decision processes produces measurably
  better collective outcomes than the standard shared-context approach.
authors:
 - bozzorey
 - mxiao
 - pparida
 - sghosh
 - tkargin
 - rsadoughian
tags:
  - '2026'

weight: 6
categories: []
date: 2026-03-24

keywords:
  - agent-based modeling
  - information asymmetry
  - organization simulation
  - Monte Carlo methods
  - experimental design
  - decision theory
  - multi-agent systems


# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

final_report:

---
![](IOTOLogo.png)

### Overview

In real organizations, each role (CEO, CFO, VP Sales…) sees different
information and applies different decision criteria — yet every multi-agent
simulation framework today gives all agents the same shared context. We want to
mathematically test whether modeling information compartmentalization and
role-specific decision processes produces measurably better collective outcomes
than the standard shared-context approach.

## Problem Statement
Multi-agent simulation frameworks ([CrewAI](https://crewai.com),
[TinyTroupe](https://github.com/microsoft/tinytroupe),
[Concordia](https://github.com/google-deepmind/concordia)) model organizations by
assigning role labels to agents that all share the same information. This
ignores two fundamental features of real organizations:

1. information is compartmentalized — a CFO doesn't know everything the VP Sales
   knows, and vice versa;
1. each role processes information differently — applying distinct criteria,
   thresholds, and filters when making decisions.

We propose a rule-based (no LLM, no API costs) agent-based simulation of a
simplified company with 5-7 roles operating in a stochastic market environment.

Three configurations are tested against identical market scenarios:

<style type="text/css">
    ol.upperalpha { list-style-type: upper-alpha; }
</style>
<ol class="upperalpha">
<li> <strong>Baseline</strong>: shared context, simple role labels only.
<li> <strong>Decision process modeling</strong>: shared context, but each role applies role-specific decision functions
(different weights, thresholds, filters).
<li> <strong>Full compartmentalization</strong>: role-specific information subsets AND
role-specific decision functions. Each configuration is run M times across N
simulated quarters using Monte Carlo methods.
</ol>

Primary metric: **cumulative simulated revenue.**

Secondary metrics:
  - **decision speed** (cycles to consensus)
  - **decision reversal rate** (coherence proxy), and information request patterns between agents.

The mathematical work involves:
 - formalizing agent decision functions and information partition matrices,
 - designing the stochastic market environment, specifying the experimental design
(factorial or fractional factorial),
 - running simulations in Python, and performing statistical hypothesis testing to compare outcome distributions
across configurations A/B/C.

A sensitivity analysis identifies which compartmentalization parameters have the
largest effect on outcomes, including boundary conditions where
compartmentalization may hurt rather than help performance.

### Expected background

 - probability
 - stochastic processes
 - statistical inference
 - Python (NumPy/SciPy).

Game theory or mechanism design is a plus but not required. The industry mentor
([Mehdi Bozzo-Rey, QAP](/authors/bozzorey)) will provide will
provide the initial conceptual model of role-specific decision processes,
informed by applied work in deeptech commercialization advisory.

The team will collaboratively formalize this model into mathematical
specifications during week 1, then implement and test it in weeks 2-3.

