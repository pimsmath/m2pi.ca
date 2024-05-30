---
title: "Nautical Crime Investigation Services - Problem 2"
subtitle:
summary: |
authors:
  - sghattan
tags:
  - '2024'

categories: []
date: 2024-05-22T08:58:18-07:00

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
![](NCISLogo.svg)

### Overview
NCIS is developing software to identify, track, and build profiles for vessels
involved in incidents at sea. This software intends to use a large language
model to collect and analyze publicly available web data. With a predefined
list of incident categories, the algorithm will gather relevant information
about vessels and their reported incidents. It will filter this data to focus
solely on incident reports, extracting key details such as vessel name, flag
state, and company for any vessel involved in the report. This information will
be used to create comprehensive profiles of the reported vessels.

### Proposed Problem
Note that this problem is independent of the other problem statements submitted
by NCIS.

This project aims to develop a strategy for determining performance indicators
to compare different search engines for yielding high-quality results from web
scraping.

#### Context for quality indicators
For each assigned topic, NCIS will have 100+ search engine prompts to yield
relevant results on incident reports, which will be web-scraped. For the scope
of this problem, assume the top 20 results returned will be scraped, with no
predetermined sites to be excluded. The challenge is determining which search
engine yields the best results. 

To define the quality of search engine results, several factors must be
considered. Some suggestions include topical bias and clustering, the novelty
of the returned sources, relevance to the assigned topic, and search engine
volatility. 

_Assigned topic: underreporting/misreporting of catch_

#### Baseline Problem Statement
Develop a strategy for evaluating different search engines on the quality of
the yielded results. 

#### Extended Problem Statement (time permitting)
Develop a method to manage search engine volatility and evaluate the
performance of search engine results for a given prompt over time, ensuring
consistent and high-quality data collection.

### Skills
#### Required
 * NLP techniques and tools for text analysis
 * Proficiency in web scraping techniques and tools
#### Preferrable
 * Familiarity with search engine optimization (SEO) principles
