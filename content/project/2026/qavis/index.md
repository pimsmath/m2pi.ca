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
![](logo.png)

### Overview

Qavis Technologies builds Qoordinate, a hybrid quantum-AI optimization platform.
We integrate classical solvers (Gurobi, OR-Tools) with quantum computing
backends to solve large- scale combinatorial optimization problems for logistics
and industrial operations.

Our platform currently serves the logistics sector (vehicle routing, delivery
scheduling) with demonstrated results: 15 to 400× faster planning and up to 23%
fuel reduction versus classical- only systems. We are now expanding into
manufacturing and production scheduling, and we need strong mathematical
foundations to do it right.

## The Problem
### Job-Shop Scheduling at a Glance
The Job-Shop Scheduling Problem (JSSP) is one of the most important
combinatorial optimization problems in manufacturing:

  * There are N jobs to be processed, each consisting of a sequence of
operations
  * There are M machines; each operation requires a specific machine for a
specific duration
  * Each machine can process only one operation at a time (no overlap)
  * Operations within a job must follow a prescribed order (precedence
constraints)
  * The objective is to minimize the makespan: the total time until all jobs
are complete

JSSP is NP-hard. Even modest instances (15 jobs × 15 machines) challenge
state-of-the-art solvers. Every manufacturing facility - automotive,
electronics, textiles, food processing - faces variants of this problem daily.

### Why We Need Your Help
Qavis has a working QUBO formulation for vehicle routing (logistics). But
scheduling is a fundamentally different problem structure: the constraints
involve temporal precedence (operation A must finish before B starts) and
resource exclusivity (machine can only do one thing at a time), rather than
spatial relationships.

We need a rigorous, well-analyzed mathematical formulation of JSSP that can
later be encoded into quantum-compatible formats (QUBO, CQM, or QAOA). The key
challenge is not just writing down a formulation - it is understanding its
structure: how the constraints interact, how penalty coefficients should be
chosen, and how large instances can be decomposed into manageable sub-problems.

### The Core Mathematical Questions
We propose the team focus on three interconnected questions:

**Question 1 — Formulation** How should JSSP be mathematically formulated as a
binary optimization problem?  What are the decision variables, the objective
function, and how are the precedence and machine constraints best expressed as
quadratic penalty terms? Are there alternative variable encodings
(time-indexed, position-based, order-based) that yield tighter or sparser
formulations?

**Question 2 — Penalty Analysis** How should penalty coefficients be chosen to ensure
constraint satisfaction without overwhelming the objective? Can we derive theoretical bounds?
How sensitive is solution quality to penalty weights?

**Question 3 — Decomposition** For large instances (hundreds of jobs, dozens of
machines), the variable count makes direct solving impractical. How can the
problem be decomposed into smaller, loosely-coupled sub-problems? What are
natural decomposition boundaries — by machine group, by job cluster, by time
window? How do we coordinate solutions across sub- problems?

## Project Scope
### Core Scope (Mathematical)
The primary focus of this project is mathematical. We are asking the team to
produce a rigorous formulation and analysis, not a software product.
Specifically:

| # | Core Deliverable | Description |
|---|------------------|-------------|
| C1 | JSSP Binary Formulation | Complete mathematical model: decision variables, objective function, all constraints written as quadratic penalty terms. LaTeX document. |
| C2 | Penalty Coefficient Analysis | Theoretical bounds or systematic guidelines for choosing penalty weights. Sensitivity analysis showing impact of penalty choices on feasibility and solution quality. |
| C3 | Decomposition Strategy | A proposed method for splitting large JSSP instances into sub-problems. Analysis of coupling structure, natural decomposition boundaries, and a coordination mechanism between sub-problems. |
| C4 | Complex & Variable Count Analysis | For each formulation variant, document the number of variables and quadratic terms as a function of N (jobs), M (machines), T (time horizon). Compare encodings. |
| C5 | M2PI Final Report | Recap article for the M2PI publication summarizing the team's approach, analysis and findings. | 

### Optional Extensions (If Time & Interest Permit)
The following are not expected but welcome if the team has the interest and
capacity. Think of these as bonus explorations:

| # | Optional Extension | Description |
|---|--------------------|-------------|
| E1 | Python QUBO Builder | A script that takes a JSSP instance file and outputs the QUBO matrix based on the team’s formulation. Useful for validation but not required. |
| E2 | Simulated Annealing Test | Test the QUBO formulation using classical simulated annealing (no quantum hardware needed) on small benchmark instances like ft06 (6×6). Validates that the formulation works.
| E3 | Classical Solver Comparison | Solve benchmark instances with Gurobi or OR-Tools (MILP) to establish a baseline. Compare variable counts and solution quality with the QUBO formulation.

**Note on quantum hardware**: No quantum computer access is needed for this
project. The formulation work is purely mathematical. If any team member wishes
to experiment with quantum simulation, Qavis can provide gate-based quantum
hardware access or help set up a local simulated annealing environment - but
this is entirely optional.

###  Out of Scope
* Building or modifying Qavis’s solver engine or platform
* Running experiments on actual quantum hardware
* Production-grade software development
* Multi-objective optimization (energy, cost) — focus is on makespan only

## Three Week Timeline
This timeline is designed around mathematical work. There is no pressure to
write production code. The deliverables are formulations, proofs, analysis, and
a written report.

### Week 1: Understand and Formulate
Theme: Build the mathematical model from scratch

| Days | Activity | Milestone |
|------|----------|-----------|
| 1-2  | Onboarding & Problem Familiarization Qavis presents a high-level overview of the platform and the business context (no proprietary details).  Team reviews JSSP literature, standard benchmark instances (OR-Library), and existing binary/quadratic formulation approaches. | Team has shared understanding of the problem and relevant literature | 
| 3-4 | Variable Design & Objective Function Define binary decision variables. Explore at least two encoding options (e.g., time-indexed x(j,m,t) vs.  position-based).  Write the makespan objective function in quadratic form.  Analyze variable count growth: how does N×M×T scale? | Draft formulation with variables and objective defined | 
| 5   | Constraint Encoding Translate precedence constraints (operation order within jobs) into quadratic penalty terms.  Translate machine capacity constraints (no two operations overlap on a machine) into penalty terms. Document all constraint-to-penalty conversions with proofs of equivalence. | WEEK 1 CHECKPOINT: Complete formulation on paper (variables + objective + all penalties) |

### Week 2 Analyze & Stress Test
Theme: Theme: Interrogate the formulation. Find its strengths, weaknesses, and boundaries.

| Days | Activity | Milestone |
|------|----------|-----------|
| 6-7  | Penalty Coefficient Analysis Derive theoretical bounds on penalty weights: what is the minimum penalty that guarantees constraint satisfaction?  Analyze sensitivity: how does solution quality change as penalties vary?  Compare penalty behavior across small instances (ft06: 6 jobs × 6 machines, la01: 10 jobs × 5 machines). | Penalty analysis document with bounds and sensitivity results |
| 8-9  | Formulation Comparison Compare the variable encodings explored in Week 1: which gives fewer variables? Sparser quadratic matrix? Better penalty structure?  For each encoding, compute exact variable/quadratic term counts on benchmark instances.  Identify which encoding is most promising for decomposition. | Encoding comparison table with quantitative analysis | 
| 10   | Structure Analysis for Decomposition Study the interaction graph: which variables are coupled through constraints?  Identify natural partition boundaries (e.g., machine groups with minimal inter-group coupling, job families, temporal windows).  Prepare the groundwork for Week 3’s decomposition design. | WEEK 2 CHECKPOINT: Penalty analysis complete. Encoding comparison documented. Coupling structure mapped. | 

Qavis involvement: 30-60 minute check-in everyday (Day 8). Available for domain questions
(e.g., what real manufacturing constraints look like).

### Week 3: Decompose and Deliver
Theme: Design the decomposition strategy and write everything up.

| Days | Activity | Milestone |
|------|----------|-----------|
| 11-12 | Decomposition Strategy Design Propose one or more decomposition approaches based on Week 2’s coupling analysis.  Define: how to partition, what information passes between sub-problems, how to coordinate/iterate. Analyze theoretical properties: does the decomposition preserve feasibility? What is the expected quality loss? | Decomposition design document |
| 13    | Worked Example Apply the decomposition to a concrete benchmark instance (e.g., la01 or la06) on paper or with basic scripting.  Show the sub-problems, their sizes, and how the coordinated solution compares to the monolithic formulation. | Worked example with analysis | 
| 14-15 | Report & Presentation Write the M2PI final report (academic recap article format).  Prepare a 15-minute presentation for the M2PI closing event.  Optional: clean up any scripts/notebooks for sharing. | FINAL DELIVERY: Report + presentation + all analysis documents | 

Qavis involvement: 30-60 minute check-ins (Day 13). Review of draft report (Day 14).
Attendance at final presentation.

## Future Directions: Quantum and Beyond
This project intentionally focuses on the mathematical foundations. But the
long-term vision is exciting, and we want the team to know where their work
leads:

 * Quantum execution: The formulation produced by the team will be encoded into
QUBO/CQM format and run on D-Wave quantum annealers and IBM Q gate-based
machines through Qavis’s Hybrid Quantum Optimization Engine.
 * QAOA pathway: Qavis is actively exploring QAOA (Quantum Approximate
Optimization Algorithm) formulations for gate-based quantum hardware. A clean
binary formulation of JSSP is the prerequisite for QAOA encoding.
 * Hybrid integration: The decomposition strategy directly feeds into Qavis’s
hybrid architecture, where sub-problems can be allocated to different solver
backends (quantum for hard sub-problems, classical for easier ones).
 * Market expansion: The formulation opens the door to an entirely new customer
segment: manufacturing companies with scheduling challenges.

**For team members interested in continued collaboration**: Qavis is open to
extending the partnership beyond M2PI. If team members wish to continue this
work, including quantum hardware experimentation, paper co-authorship, or
consulting, we would welcome that conversation.

## Intellectual Property & Publication
This project is designed for full compatibility with M2PI’s public final report requirement:

  * **What will be published**: The JSSP formulation, penalty analysis, and
    decomposition strategy are mathematical methodology and fully publishable
    and academically valuable.
  * **Clear boundary**: The team works on “what to solve” (mathematical
    formulation). Qavis handles “how to solve” (engineering integration). This
    clean separation ensures zero IP conflict.
 
## Ideal Team Profile
We would benefit from 4-5members with backgrounds in some or all of:
  * Combinatorial / discrete optimization (integer programming, complexity theory)
  * Operations research (scheduling theory, resource allocation)
  * Linear algebra and graph theory (for coupling analysis and decomposition)
  * Scientific computing (Python, for optional extensions)

**No quantum computing experience is required**. The entire project can be
completed with classical optimization knowledge. Quantum context will be
provided during onboarding for those interested.

## Why This Project
**For the mathematicians**: JSSP is a canonical NP-hard problem with deep connections to
complexity theory, approximation algorithms, and polyhedral analysis. Formulating it for
quantum-compatible solvers is an active research frontier with genuine open questions. Your
work can lead to a publishable paper, and you get exposure to how quantum optimization works
in industry — without needing to become a quantum physicist.

**For Qavis**: Your formulation becomes the mathematical foundation for our entry into
manufacturing. Every factory with scheduling challenges becomes a potential customer. This is
not a theoretical exercise, but it directly shapes a product roadmap.

**For the field**: Rigorous, well-analyzed formulations of industrial scheduling problems in
quantum-ready formats are still rare. A clean JSSP formulation with decomposition analysis,
produced and published through M2PI, contributes to both the OR and quantum computing
communities.
