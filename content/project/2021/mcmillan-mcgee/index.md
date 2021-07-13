---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Mcmillan Mcgee"
summary: |
  McMillan-McGee have developed induction heating technology for in-situ soil
  remediation.  As such, we have developed heater casings, work coils, and
  inverters which generate high frequency alternating current.  We have also
  developed a great amount of the analytical work for engineering this
  equipment.

  An important aspect of our inverter design (or for that matter any high
  frequency inverter in general) is to have a good understanding of the
  electrical properties (resistance and inductive reactance) of the DC bus bar
  that supplies current to the high speed switching devices (IGBTs and SiC
  Mosfets).  Knowing this would allow us to design a suitable bus bar system
  that can absorb energy caused by switching transients from these semiconductor
  devices as a result of commuting current through the work coil.  The problems
  in this project centre on solving certain boundary value problems involving
  Maxwell's equations and linking these to the laws of thermodynamics.

authors: [reid]
tags: ['2021']
categories: []
date: 2021-07-10T16:58:18-07:00

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

## Problem Statement

My mathematical problems are centered on solving certain boundary value problems
involving Maxwell's equations and linking these to the laws of thermodynamics.
As you may recall, my team and I at McMillan-McGee have developed induction
heating technology for in situ soil remediation.  As such, we have developed
heater casings, work coils, and inverters which generates high frequency
alternating current.  We have also developed a great amount of the analytical
work for engineering this equipment.

An important aspect of our inverter design (or for that matter any high
frequency inverter in general) is to have a good understanding of the electrical
properties (resistance and inductive reactance) of the DC bus bar that supplies
current to the high speed switching devices (IGBTs[^1] and SiC Mosfets[^2]).
Knowing this would allow us to design a suitable bus bar system[^3] that can
absorb energy caused by switching transients from these semiconductor devices as
a result of commuting current through the work coil.  The bus bar is an
electrically conducting (copper) rod of a certain length with rectangular
cross-section.  We would like to be able to compute in closed form[^4] the bus
high frequency effective resistance[^5] and inductance.  An approach that I am
presently using is a technique that I have learned from Norman McLauchlan^6
where he approximates the rectangular cross-section of a bus bar with an ellipse
having suitable dimensions.  In McLauchlan's textbook he only computes the
effective resistance of a long straight conductor of elliptical cross-section to
high frequency alternating current.  This spring, I extended his work to compute
the inductance too.  The big problem with McLauchlan's work is that he is
working in the Gaussian system of electromagnetic units; not, the MKS as most
electrical engineers are familiar with including myself.   I immediately became
aware of this when I found that McLauchlan uses unity for the permeability of
copper (same as that for free-space).  So, I place some doubt on the my
interpretation of his result as well as my extension for computing inductance.
It should be noted that when passing sufficiently high frequency alternating
current on a bus bar of rectangular (approximated to elliptical) cross section
the current is confined mainly to a surface layer of the conductor, and the
current density is negligible within the body of the bus bar.  Thus the
component of the magnetic field normal to the bar's surface tends to rapidly
diminish immediately above it.  Therefore, the magnetic field can be assumed
tangential to the bus bar.  It then follows that on the surface the vector
magnetic potential, A, is constant and satisfies the same conditions as the
scalar electrostatic potential, "phi".  Consequently, McLauchlan draws the
conclusion that the surface distribution of current density is identical to that
of a bar holding an electric charge.  Hence, the total current flowing axially
on the bus bar corresponds to the total surface charge.  With these assumptions,
McLauchlan developed formulas involving a certain elliptic integral for
computing current density, power loss, and the high frequency resistance.

To tackle this problem requires a team familiar with electrostatics and
electrodynamics.  Certain individuals within the team should possess a working
knowledge on curvilinear coordinates, with special attention to the system of
orthogonal elliptic-hyperbolic coordinates.  Also, team members should be
familiar with elliptic integrals.  Fortunately, McLauchlan's solution to the
problem side-steps the task of solve a boundary value problem using Mathieu
functions.

#### References

[^1]:  IGBT stands for Insulated Gate Bipolar Transistor -- a high power switching device often used in the induction heating industry
[^2]:  SiC stands for Silicon Carbide  -- this is a new semiconductor switching device which is becoming popular with electric vehicles
[^3]:  bus bar system includes the bus bar and by pass capacitors which are in close proximity to the switching semiconductors.
[^4]:  closed form -- using certain analytical expressions to compute a desired result; not numerical simulation.  In my case I use Matlab as the computational engine.
[^5]:  effective resistance -- here we account for the skin-effect.
[^6]:  Norman W. McLauchlan, "Theory and Applications of Mathieu Functions",  Oxford University Press, 1947.
