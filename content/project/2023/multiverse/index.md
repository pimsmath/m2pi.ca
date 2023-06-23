---
title: "Multiverse Computing"
subtitle: "Analyzing deforestation in the Amazon Basin with machine learning"
summary: |
authors:
  - mbrs
  - rayan
  - bauerk
  - lixing
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
![](MultiverseLogo.png)

## Overview

This project uses machine learning techniques to analyze data regarding
deforestation in the Amazon basin.  In a [recent blog
post](https://vitalflux.com/machine-learning-use-cases-climate-change/#Forest_degradation),
Ajitesh Kumar wrote:

> Forest degradation is a major problem that contributes to
climate change.  It occurs when forests are damaged or destroyed, typically as a
result of human activity.  Deforestation, forest fires, pests, and poor forest
management are all major causes of forest degradation.  The loss of trees and
other vegetation can have a significant impact on the local climate.  In
addition to absorbing carbon dioxide, trees, and plants help to regulate
temperature and precipitation levels.  When forests are degraded, these
important functions are compromised, contributing to climate change…. In
addition, forest degradation can also cause soil erosion, which can lead to
desertification and loss of biodiversity.  Therefore, it is essential to address
the problem of forest degradation in order to protect our environment.

In principle, deforestation can be monitored automatically using high-resolution
satellite imagery.  At a Kaggle competition in 2016, the project “Planet:
Understanding the Amazon from Space” evaluated Machine Learning algorithms for
tracking human footprint in the Amazon rainforest (Luis Di Martino posted
solutions to [Part
1](https://medium.com/digital-sense-ai/monitoring-deforestation-with-open-data-and-machine-learning-part-1-24d29c346752)
and [Part
2](https://medium.com/digital-sense-ai/monitoring-deforestation-with-open-data-and-machine-learning-part-2-c1be298c574b)
of this problem; also see Nick Condo’s work on this project summarized
[here](https://towardsdatascience.com/understanding-the-amazon-rainforest-with-deep-learning-732bfb2eca6e)
and [repo here](https://github.com/ncondo/amazon-from-space)).  This year’s M2PI
project aims to update this solution to make a machine-learning algorithm using
tensor network techniques inspired by quantum many-body physics.

## Proposal
The solutions explained in the above links employ standard off-the-shell
convolutional neural networks (CNNs) such as ResNet. We propose to (hopefully)
improve the solution by replacing vanilla CNNs with "Tensorized" CNNs (TCNNs),
or at least develop a detailed benchmarking of the performance and accuracy of
TCNNs vs. CNNs for this problem. The basic ideas underlying TCNNs are explained
[here](https://arxiv.org/abs/2107.03436).

## Skills
##### Required
  * Deep learning techniques, especially CNNs
##### Preferrable
  * Familiarity with low rank tensor factorization and tensor networks

The best skill match would be familiarity with [this
paper](https://arxiv.org/pdf/2302.09019.pdf)'s general ideas,
particularly some of the references cited under the subcategory CNNs in Table 1. 

### Resources
In addition to the links above, the data set from the original Kaggle
competition is available
[here](https://www.kaggle.com/competitions/planet-understanding-the-amazon-from-space/data).
