---
title: University of Victoria
subtitle: "Quantum computing for climate modeling"

summary: |
  The goal of the project is to develop an interface between quantum and
  classical- binary computing devices for the purpose of climate modelling.
authors:
  - khouider
tags:
  - '2026'

weight: 6
categories: []
date: 2026-03-24

keywords:
 - graphs
 - lattices
 - categories
 - topology
 - linear algebra
 - geometry

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
### Overview
The goal of this project is to develop an interface between quantum and classical (binary) computing systems for climate modeling.

Climate models are large, complex computer programs made up of multiple components that represent different parts of the Earth system, such as the atmosphere, oceans, cryosphere, and vegetation. Each component is typically developed as a separate code, and many of these are further divided into sub-modules.

For example, atmospheric models usually include a dynamics module—often called the dynamical core—and one or more physics modules. The dynamical core is based on systematic discretization methods (such as finite differences, finite volumes, or spectral methods) to solve the equations of motion. In contrast, the physics modules represent processes that are not explicitly resolved by the dynamical core. These processes occur at spatial or temporal scales smaller than the model’s grid resolution and include phenomena such as radiation, phase changes of water and associated latent heat transfer, turbulence, and convection.

Because resolving these small-scale processes directly is computationally expensive, they are typically approximated using heuristic models based on ad hoc closure assumptions.

Although quantum computing is advancing rapidly, it is not yet practical to implement all components of climate models on quantum systems. Moreover, existing classical codes for dynamical cores are well established and highly reliable. However, if a quantum algorithm can be developed for specific sub-grid processes that is both efficient and accurate, it could be integrated with a classical dynamical core to create a hybrid quantum–classical modeling framework.

As a proof of concept, this project proposes to couple a simple convection model with a toy climate model developed by Khouider et al. (2010). The convection model, known as the Stochastic Multicloud Model (SMCM), is a Markov model that describes the area fractions of three cloud types.

In [Khouider et al. (2010)](#ref2), the SMCM is coupled with a set of ordinary differential equations (ODEs) that describe the vertical profiles of temperature and moisture, assuming horizontal homogeneity (i.e., no spatial derivatives). More recently, Ueno and Miura (2025) developed a quantum implementation of the SMCM component alone.

This project aims to integrate the quantum SMCM code of [Ueno and Miura (2025)](#ref1) with the ODE-based system used in Khouider et al. (2010), which serves as a simplified dynamical core. This integration will act as a demonstration of a hybrid quantum–classical climate modeling approach.

As a possible extension, the quantum SMCM code could also be applied to machine learning tasks. For example, it could be used to generate sample paths for a synthetic likelihood algorithm to calibrate the SMCM using radar data (Sevilla and Khouider, unpublished work).

## References
1. <a name="ref1"></a>Kazumasa Ueno, Hiroaki Miura, Quantum Algorithm for a Stochastic
Multicloud Model, SOLA, 2025, Vol. 21, pp. 43-50, Publication Date
2025/01/22, [Early Release] Publication Date 2024/12/11, Online ISSN
1349-6476, https://doi.org/10.2151/sola.2025-006.
1. <a name="ref2"></a> Khouider, B., J. Biello, and A. J. Majda, 2010: [A stochastic multicloud
model for tropical
convection](https://projecteuclid.org/journals/communications-in-mathematical-sciences/volume-8/issue-1/A-stochastic-multicloud-model-for-tropical-convection/cms/1266935019.full). Commun. Math. Sci., 8, 187–216.
