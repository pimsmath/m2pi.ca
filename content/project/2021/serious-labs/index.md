---

title: "Serious Labs"
summary: |
  Realtime simulators in virtual reality are a leading-edge technology to
  provide standardized training and evaluation that contribute to
  heavy-equipment operator safety. They aim to reduce accidents due to operator
  inexperience by training an operator in scenarios before they are expected to
  perform these same tasks in reality. To satisfy the high frame-rate
  requirements of real-time simulation, algorithms to solve these models must be
  extremely efficient and yield predictable and reproducible results.

  The simulation of heavy equipment involves simulating both physical bodies in
  motion and hydraulic pressures. The goal of this project is to develop an
  approach to the simulation of fluid pressure volumes that can be interfaced
  with a position-based dynamics (PBD) simulation, improving performance and
  providing a more realistic experience.


authors: []
tags: ["2021"]
categories: []
date: 2021-07-12T12:54:49-07:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:

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

#final_report: 'Aerium-final.pdf'
---

# Problem Statement

Realtime simulators in virtual reality are a leading-edge technology to provide
standardized training and evaluation that contribute to operator safety. They
aim to reduce accidents due to operator inexperience by training an operator in
scenarios before they are expected to perform these same tasks in reality. To
satisfy the high frame-rate requirements of real-time simulation, algorithms to
solve these models must be extremely efficient and yield predictable and
reproducible results.

The simulation of heavy equipment involves simulating both physical bodies in
motion and hydraulic pressures. For example, one might wish to simulate a system
involving a combustion engine coupled to several hydraulic pumps,motors, and
cylinders that drive mechanical components. Over the past decades, numerous
models and algorithms have been developed for these applications. Recently,
position-based dynamics (PBD) has emerged as a strong contender for realtime
simulation. Focusing on updating positional constraints, rather than the more
traditional force or impulse based methods, allows it to be simple, stable,
performant, while still converging to the same solution as the traditional
methods [^1]. This approach has been shown to be easily applicable to the
simulation of rigid bodies [^2]. Similarly in the hydraulic domain, many methods
are too computationally expensive to be viable for a real time simulation. For
example, [^3] provides a thorough review of lumped-parameter hydraulic
simulation; however, due to the relative incompressibility of fluids, the
equations in their provided form are computationally expensive to solve.

The goal of this project is to develop an approach to the simulation of fluid
pressure volumes that can be interfaced with a PBD simulation. This approach can
then be applied to the simulation of many types of heavy equipment. At a
high-level, PBD involves 3 steps: position prediction, application of
constraints, and velocity calculation. For hydraulics, it should be possible to
develop a collection of constraints that affect the pressures and flows of
hydraulic volumes. Specifically, models for the following components should be
defined:

  * Hydraulic cylinder, which couples two fluid volumes (input/output) and two
    rigid bodies (both ends of the cylinder)
  * Hydraulic pump/motor, which couples two fluid volumes (input/output) and a
    single rigid body
  * Orifice, which connects two fluid volume

### Skills
  * Programming in a language geared toward scientific-computing, e.g. Python,
    MATLAB, Fortran.
  * Strong background in applied mathematics.

### References
[^1]: MACKLIN M., MÜLLER M., CHENTANEZ N.: Xpbd: Position-based simulation of
compliant constrained dynamics. In Proceedings of the 9th International
Conference on Motion in Games (2016)
[^2]: MÜLLER M., MACKLIN M., CHENTANEZ N., JESCHKE S., KIM T.: Detailed Rigid
Body Simulation with Extended Position Based Dynamics. Eurographics Symposium on
Computer Animation (2020)
[^3]: Modelon AB, Modeling of Hydraulic Systems. Hydraulics Library Manual and
Tutorial (2013)
