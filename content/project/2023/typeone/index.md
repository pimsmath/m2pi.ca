---
title: "Type One Energy"
draft: true
subtitle: "Magnetic coils for stellarator fusion reactors"
summary: |
  In a stellarator reactor, the hot fusion fuel is maintained inside the reactor
  chamber by strong magnetic fields. These magnetic fields are produced by
  running electric currents in metallic wires, called electromagnetic coils. The
  purpose of this project is to compute the shape of coils and the magnitude of
  the currents running in them to confine the hot fusion fuel in a desired
  volume.  Mathematically, this is a high dimensional optimization problem. The
  unknowns are the shape parameters of the coils and the current values, and the
  objective is to minimize the mismatch between the magnetic field produced by
  the coils and the reactor volume. More precisely, this is a constrained
  optimization problem, since the shapes of the coils are constrained by
  engineering requirements, and coils cannot support electric currents beyond a
  certain maximum value. In this project, we would explore a variety of
  geometric constraints on the coils, from relatively simple ones to more
  realistic ones, which make the optimization landscape more complicated.  This
  is mostly a numerical project.  We would develop efficient methods for
  evaluating the Biot-Savart integrals for the magnetic field along the reactor
  surface, and design gradient-based algorithms for finding optimal coil
  configurations. We would also explore different geometric representations for
  the coils (Fourier, splines, etc.), enabling different coil topologies.
authors:
  - spiteri
tags:
  - '2023'

categories: []
date: 2023-06-22T08:58:18-07:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: "Center"
  preview_only: true

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
![](TypeOneLogo.png)

In a stellarator reactor, the hot fusion fuel is maintained inside the reactor
chamber by strong magnetic fields. These magnetic fields are produced by running
electric currents in metallic wires, called electromagnetic coils. The purpose
of this project is to compute the shape of coils and the magnitude of the
currents running in them to confine the hot fusion fuel in a desired volume.
Mathematically, this is a high dimensional optimization problem. The unknowns
are the shape parameters of the coils and the current values, and the objective
is to minimize the mismatch between the magnetic field produced by the coils and
the reactor volume. More precisely, this is a constrained optimization problem,
since the shapes of the coils are constrained by engineering requirements, and
coils cannot support electric currents beyond a certain maximum value. In this
project, we would explore a variety of geometric constraints on the coils, from
relatively simple ones to more realistic ones, which make the optimization
landscape more complicated.  This is mostly a numerical project. We would
develop efficient methods for evaluating the Biot-Savart integrals for the
magnetic field along the reactor surface, and design gradient-based algorithms
for finding optimal coil configurations. We would also explore different
geometric representations for the coils (Fourier, splines, etc.), enabling
different coil topologies.
