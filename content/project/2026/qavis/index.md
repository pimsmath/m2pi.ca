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
  - ffiroozi
  - mwithanachchi
  - mkaatz
  - nguyen

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
![](logo.png)

### Overview

Qavis Technologies builds **[Qoordinate](https://qordinate.tech)**, a hybrid quantum-AI optimization platform. We integrate classical solvers with quantum computing backends to solve large-scale combinatorial optimization problems for logistics and industrial operations.

Our platform serves the logistics sector with vehicle routing and delivery scheduling, achieving 240× faster planning and up to 29% fuel reduction. We are now expanding into **manufacturing and production scheduling** — and we need strong mathematical foundations to do it right.

## The Problem
### Job-Shop Scheduling at a Glance
The Job-Shop Scheduling Problem (JSSP) is one of the most important combinatorial optimization problems in manufacturing:

  * N jobs must be processed, each consisting of a sequence of operations
  * M machines are available; each operation requires a specific machine for a specific duration
  * Each machine can process only one operation at a time
  * Operations within a job must follow a prescribed order (precedence constraints)
  * Objective: minimize the makespan (total completion time)

JSSP is NP-hard. Even modest instances (15 jobs × 15 machines) challenge state-of-the-art solvers.


### Why Encoding Efficiency Matters
To solve JSSP on quantum solvers, we formulate it as a binary optimization
problem (QUBO). The standard approach uses a binary variable $x(j,m,t)$ for each
job-machine-timeslot combination. A 10×10×100 instance yields **10,000 binary
variables = 10,000 qubits.**

Recent work on the **Linear Ramp QAOA (LR-QAOA)** protocol (Montañez-Barrera &
Michielsen, npj Quantum Information, 2025) shows that quantum success
probability scales as $P(x*) \approx 2^{(–\eta(p)\cdot N_q + C)}$. **Every qubit eliminated from the
formulation exponentially improves the chance of finding the optimal solution.**

This is why we ask: **what is the most qubit-efficient way to formulate JSSP?**


### The Research Questions


**Question 1 — Formulation** How should JSSP be encoded as a binary optimization
problem with minimal variables? What are the decision variables, objective, and
how are constraints expressed as quadratic penalties?

**Question 2 — Penalties** How should penalty coefficients be chosen? Can
we derive bounds? How sensitive is solution quality to penalty weights?

**Question 3 — Decomposition** For large instances, how can the problem be split
into smaller sub-problems while preserving solution quality?


## Project Scope
### Core Deliverables
The focus is **mathematical formulation and analysis**. No quantum hardware, no
production software. The team builds the mathematical model; Qavis handles the
engineering.

| # | Core Deliverable | Description |
|---|------------------|-------------|
| C1 | JSSP Binary Formulation | One complete QUBO formulation: decision variables, objective function, all constraints as quadratic penalties. Variable count analysis as function of N, M, T. |
| C2 | Penalty Coefficient Analysis | Bounds or guidelines for choosing penalty weights. Basic sensitivity analysis on a small benchmark instance (ft06: 6×6). |
| C3 | Decomposition Strategy | A conceptual method for splitting large instances into sub-problems. Coupling analysis and one worked example showing sub-problem sizes. |
| C4 | Quantum Feasibility Note | Brief assessment: given the variable count, at what problem sizes does quantum execution become realistic? Uses published LR-QAOA scaling results (no hardware needed). |
| C5 | M2PI Final Report | Recap article for M2PI publication + 15-minute presentation.  |

### Bonus (If Time Permits)
These are extras, not expectations. The core deliverables above are what we need.

| # | Optional Extension | Description |
|---|--------------------|-------------|
| B1 | Second Encoding Variant | A second variable encoding (e.g., position-based) for comparison with the primary formulation. |
| B2 | Python QUBO Builder | Script converting a JSSP instance into the QUBO matrix.  |
| B3 | Simulated Annealing Test | Validate the formulation on small instances using classical simulated annealing. |

**No quantum hardware is needed for any part of this project.**


## Timeline & Working Style

### How We Work Together

Qavis provides a mentor who meets with the team **daily for approximately 1
hour**.  These are collaborative working sessions, not status reports. The
mentor provides domain context, answers questions, suggests directions, and
helps the team stay on track. The pace is guided: each day builds naturally on
the previous day’s work.

Think of it as a **supervised research sprint**. The team does the mathematical
heavy lifting; the mentor ensures the work stays relevant and steers around dead
ends.

| Period | Focus | Key Output |
|--------|-------|------------|
| Week 1 | M2PI Training + Background Reading | Team ready, literature reviewed |
| Week 2 | Build the formulation | Complete QUBO model with penalties |
| Week 3 | Analyze, Decompose and Write Up | Decomposition + feasibility + report |

### Week 1: M2PI Training
_No project deliverables_


Qavis preparation during this week:
 * Share a short reading list: 2–3 papers on JSSP formulations + the LR-QAOA paper for motivation
 * Brief introductory call if M2PI schedule allows (“Here’s who we are, here’s what we’re building”)

### Week 2: Build the Formulation (Project Week 1)
_The goal this week is simple: end with a complete, correct QUBO formulation of
JSSP on paper._

| Day | Focus | Details | Daily Meeting |
|-----|-------|---------|---------------|
| 1 | Onboarding & Problem Setup | Qavis presents the business context and what we need Team familiarizes with JSSP structure and benchmark instances | 90 min: onboarding presentation + Q&A Assign: review ft06 instance, sketch variable ideas |
| 2 | Define Decision Variables | Choose a variable encoding (e.g., time-indexed x(j,m,t)) Write the makespan objective function | 60 min: review variable choices, discuss trade-offs Mentor guides encoding selection |
| 3 | Precedence Constraints | Encode job operation ordering as quadratic penalty terms Document the conversion with correctness argument | 60 min: review penalty terms, check correctness together |
| 4 | Machine Constraints | Encode no-overlap constraints as penalties Complete the full QUBO formulation | 60 min: walk through complete formulation end-to-end Verify all constraints are covered |
| 5 | Penalty Analysis & Scaling | Analyze penalty coefficients: bounds, sensitivity Count variables for ft06, la01: how does Nq scale with N, M, T? | 60 min: review analysis, plan Week 3 direction CHECKPOINT: formulation complete |


### Week 3: Analyze, Decompose and Deliver (Project Week 2)
_The goal this week: understand how the formulation behaves at scale, propose a decomposition, and write it all up._
| Day | Focus | Details | Daily Meeting |
|-----|-------|---------|---------------|
| 6 | Coupling Structure Analysis | Study which variables interact through constraints Identify loosely-coupled blocks in the problem | 60 min: discuss coupling patterns, brainstorm decomposition ideas |
| 7 | Decomposition Design | Propose a decomposition strategy (machine-group, time-window, or job-cluster) Define how sub-problems communicate | 60 min: evaluate decomposition approach, refine together |
| 8 | Worked Example & Feasibility | Apply decomposition to la01 on paper Compute sub-problem Nq, check LR-QAOA scaling | 60 min: review worked example, begin outlining report |
| 9 | Write Report | Draft the M2PI final report (recap article format) Compile all formulation documents and analysis | 60 min: review draft report, give feedback |
| 10 | Finalize & Present | Polish report, prepare 15-min presentation | Final presentation to Qavis + M2PI DELIVERY: report + presentation |
## The Bigger Picture
The formulation you produce is not a standalone exercise — it is the mathematical foundation for a concrete product pipeline:

### Qavis Optimization Roadmap
  * **STEP 1 — Mathematical Formulation (this M2PI project)** Produce a qubit-efficient binary formulation of JSSP with penalty analysis and decomposition strategy.
  * **STEP 2 — Solver Integration & Validation (Qavis, post-M2PI)** Encode the formulation into solver-ready formats. Validate on classical and quantum-inspired solvers. Integrate into the Qoordinate platform.
  * **STEP 3 — Quantum Execution via LR-QAOA (Qavis, near-term)** Execute the compact encoding on quantum hardware using the LR-QAOA protocol. The team’s qubit scaling analysis directly determines feasibility.
  * **STEP 4 — Manufacturing Deployment** Deploy JSSP optimization to manufacturing clients across automotive, electronics, textiles, and food processing.

**Your work is Step 1** — everything else builds on it. The encoding quality determines quantum feasibility, the penalty analysis ensures solution quality, and the decomposition shapes how we scale.

**Interested in continuing beyond M2PI?** Steps 2–3 offer natural follow-on research — quantum hardware experiments, benchmarking papers, or ongoing consulting. We welcome that conversation.

## Intellectual Property & Publication
Fully compatible with M2PI’s public final report:
  * Published: The JSSP formulation, penalty analysis, decomposition strategy, and scaling assessment. Mathematical methodology, fully publishable.
  * Not shared: Qavis’s proprietary optimization engine, AI preprocessing, solver logic, and customer data. Not involved in this project.
  * Boundary: The team works on “what to solve” (formulation). Qavis handles “how to solve” (engineering). Zero IP conflict.


## Ideal Team Profile
We would benefit from 4-5members with backgrounds in some or all of:
  * Combinatorial / discrete optimization (integer programming, complexity theory)
  * Operations research (scheduling theory, resource allocation)
  * Linear algebra and graph theory (for coupling analysis and decomposition)
  * Scientific computing / Python (helpful, not required)

**No quantum computing experience is required**. Qavis provides all necessary quantum context through the reading list and daily meetings.


## Why This Project
* **For the team**: JSSP is a canonical NP-hard problem. Designing qubit-efficient encodings is an active research question. Your work has a path to a published paper, and you gain hands-on understanding of how formulation choices impact quantum feasibility.
* **For Qavis**: Your formulation becomes the mathematical core of our manufacturing product. It directly shapes our product roadmap and opens a new customer segment.
* **For the field**: Qubit-conscious JSSP formulations with scaling analysis are rare. This contributes to both operations research and quantum computing communities.

## Resources Provided by Qavis

| Resource | Details |
|----------|---------|
| Daily Mentor | Qavis team member meets daily (~1 hour) for guidance, Q&A, and direction. |
| Benchmark Data | Standard JSSP instances from OR-Library (ft06, ft10, la01–la40). |
| Reading List | 2–3 JSSP formulation papers + LR-QAOA paper, shared before project start. |
| Technical Context | High-level overview of optimization architecture. VRP QUBO as reference. |
| Optional: D-Wave Leap | Cloud quantum access for team members who wish to experiment. Entirely optional. |

## Key References
  * [1] Montañez-Barrera & Michielsen, "Toward a linear-ramp QAOA protocol," npj Quantum Information 11, 131 (2025). DOI: 10.1038/s41534-025-01082-1
  * [2] LR-QAOA benchmark: quantumbenchmarkzoo.org/content/application-level-benchmark/protocols/lr-qaoa
  * [3] OR-Library JSSP instances: people.brunel.ac.uk/~mastjjb/jeb/orlib/jobshopinfo.html




