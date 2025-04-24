---
title: "Type One Energy"
subtitle: "Efficient computation of Taylor relaxed equilibria in stellarators"
summary: |
  The purpose of this project is to compute numerical solutions to Beltrami's
  equation in three-dimensional toroidal geometries. Magnetic fields in
  so-called Taylor relaxed states satisfy Beltrami's equation and can be good
  models of magnetic fields in confined plasma equilibria.

authors:
  - acerfon

keywords: 
 - Finite Element Method
 - Plasma Equilibrium
 - Taylor State
 - Beltrami Field
 - Automated solutions to partial differential equations
tags:
  - '2025'

categories: []
date: 2024-05-05

weight: 5

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
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
![](TypeOneEnergy.png)
The purpose of this project is to compute numerical solutions to [Beltrami's
equation](https://en.wikipedia.org/wiki/Beltrami_equation) in three-dimensional
toroidal geometries. Magnetic fields in so-called Taylor relaxed states satisfy
Beltrami's equation and can be good models of magnetic fields in confined plasma
equilibria.

To make this project tractable, we will rely on Python-based automated
frameworks for solving partial differential equations, such as
[Firedrake](https://www.firedrakeproject.org/) or
[FEniCS](https://fenicsproject.org/).
