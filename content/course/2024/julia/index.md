---
title: "Parallel Coding with Julia"
authors: 
  - razoumov

summary: |
  Julia is a high-level programming language well suited for scientific
  computing and data science. Just-in-time compilation, among other things,
  makes Julia really fast yet interactive. This session will introduce Julia as
  and demonstrate how it can be used to tackle problems which require parallel
  programming.

tags: ['2024']
categories: []
date: 2024-06-10T12:00:00-07:00
publishDate: 2024-04-03

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
---
### Course Description

Julia is a high-level programming language well suited for scientific computing
and data science. Just-in-time compilation, among other things, makes Julia
really fast yet interactive. For heavy computations, Julia supports
multi-threaded and multi-process parallelism, both naïvely and via a number of
external packages. It also supports memory arrays distributed across multiple
processes either on the same or different nodes. In this hands-on workshop, we
will start with a quick review of Julia’s multi-threading features but will
focus primarily on Distributed standard library and its large array of tools. We
will demo parallelization using two problems: a slowly converging series and a
Julia set. We will run examples on a multi-core laptop and an HPC cluster.
