---
title: Qavis Inc.
subtitle: 

summary: |
  Qavis Technologies seeks a rigorous mathematical formulation of the Job-Shop
  Scheduling Problem (JSSP) as a binary quadratic optimization model
  (QUBO/CQM-compatible), including penalty coefficient analysis and a
  decomposition strategy for large-scale instances, to extend our hybrid
  quantum-AI optimization platform from logistics into manufacturing.
authors:
  - uke
tags:
  - '2026'

weight: 6
categories: []
date: 2026-03-24

keywords:
  - Job-Shop Scheduling
  - Combinatorial Optimization
  - QUBO Formulation
  - Binary Quadratic Programming
  - Decomposition Methods
  - Penalty Coefficient Analysis
  - Manufacturing Scheduling
  - Quantum-Ready Optimization
  - NP-Hard Problems
  - Operations Research


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

Qavis builds a hybrid quantum-AI optimization platform currently serving
logistics (vehicle routing, delivery scheduling). We are expanding into
manufacturing, where Job-Shop Scheduling (JSSP) is a core challenge: N jobs must
be processed across M machines, each operation requiring a specific machine for
a specific duration, with precedence and no-overlap constraints, minimizing
makespan.  We need a complete mathematical formulation of JSSP as a binary
quadratic optimization problem suitable for quantum and hybrid solvers.

## Problem Statement

The key research questions are:

  1. How should decision variables, objective, and constraints be encoded as
     quadratic penalty terms, and which variable encoding (time-indexed,
     position-based, order-based) yields the best structure?
  2. How should penalty coefficients be chosen — can we derive theoretical
     bounds and sensitivity guidelines?
  3. How can large instances be decomposed into smaller sub-problems while
     preserving solution quality? The project is purely mathematical - no
     quantum hardware or production software is required.

Deliverables are a formal formulation document, penalty analysis, decomposition
strategy, and an M2PI final report. Qavis provides benchmark datasets, domain
context, and optional IBM simulator access for interested team members.

