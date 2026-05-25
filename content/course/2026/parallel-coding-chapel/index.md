---
title: "Parallel Coding with Chapel"
authors: 
  - razoumov

summary: |
  Chapel is a modern programming language designed for both shared and
  distributed memory systems, offering high-level, easy-to-use abstractions for
  task and data parallelism. This session will introduce you to chapel and show
  you how to leverage the power of parallel computing.

tags: ['2026']
categories: []
date: 2026-05-28T13:00:00-08:00
publishDate: 2025-05-03

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

Chapel is a modern programming language designed for both shared and distributed
memory systems, offering high-level, easy-to-use abstractions for task and data
parallelism. Its intuitive syntax makes it an excellent choice for novice HPC
users learning parallel programming. Chapel supports a wide range of parallel
hardware – from multicore processors and multi-node clusters to GPUs – using
consistent syntax and concepts across all levels of hardware parallelism.

Chapel dramatically reduces the complexity of parallel coding by combining the
simplicity of Python-style programming with the performance of compiled
languages like C and Fortran. Parallel operations that might require dozens of
lines in MPI can often be written in just a few lines of Chapel. As an
open-source language, it runs on most Unix-like operating systems and scales
from laptops to large HPC systems.

This course begins with Chapel fundamentals, then focuses on data parallelism
through two numerical examples: one embarrassingly parallel and one tightly
coupled. We’ll also briefly explore task parallelism (a more complex topic, and
not the primary focus in this course). Finally, we’ll introduce GPU programming
with Chapel.

More information and links available at
https://folio.vastcloud.org/chapel-compact.html

_Participant preparation: Alex will prepare a training cluster with guest
accounts, so all the participants need is a computer with an SSH client to log
into the training cluster. Participants who are not familiar with using SSH to
access a remote system, can read https://mint.westdri.ca/login before the course
begins._

