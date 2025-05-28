---
title: "Parallel Coding with Python"
authors: 
  - razoumov

summary: |
  Python has become the dominant language in scientific computing thanks to its
  high-level syntax, extensive ecosystem, and ease of use. However, its
  performance often lags behind traditional compiled languages like C, C++, and
  Fortran, as well as newer contenders like Julia and Chapel. This course is
  designed to help you speed up your Python workflows using a variety of tools
  and techniques.

tags: ['2025']
categories: []
date: 2025-05-09T10:00:00-08:00
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
Python has become the dominant language in scientific computing thanks to its
high-level syntax, extensive ecosystem, and ease of use. However, its
performance often lags behind traditional compiled languages like C, C++, and
Fortran, as well as newer contenders like Julia and Chapel. This course is
designed to help you speed up your Python workflows using a variety of tools and
techniques.

We'll begin with classic optimization methods such as NumPy-based vectorization,
and explore just-in-time compilation using Numba, along with performance
profiling techniques. From there, we'll delve into parallelization – starting
with multithreading using external libraries like NumExpr and Python 3.13's new
free-threading capabilities – but placing greater emphasis on multiprocessing.

We will also look into into Ray, a powerful and flexible framework for scaling
Python applications. While Ray is widely used in AI, our focus will be on its
core capabilities for distributed computing. We'll also explore combining Ray
with Numba and will discuss coding tightly coupled parallel problems.

