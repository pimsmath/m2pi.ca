---
title: "Nautical Crime Investigation Services - Problem 3"
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
This project aims to develop a strategy for leveraging large language models
(LLMs) to identify relevant incidents from web-scraped content and extract key
information.

_Note that this problem is independent of the other problem statements submitted
by NCIS._

#### Context for LLM utilization
For a given topic, NCIS will have 100+ search engine prompts to yield relevant
results on incident reports, which will be web-scraped. For the scope of this
problem, assume the top 20 results returned will be scraped, with no
predetermined sites to be excluded. With thousands of sources scraped, an LLM
model will be used to identify whether a source contains an incident related to
the assigned topic. If so, specific details from the incident reports should be
extracted. Examples of details that can be extracted include vessel name, flag,
company, etc. 

To achieve this, it is necessary to determine the best approach for employing
LLMs in these tasks. The effectiveness of different LLMs in identifying and
extracting relevant information from diverse and potentially noisy data sources
should be assessed.

_Assigned topic: underreporting/misreporting of catch_

#### Baseline Problem Statement
Develop a strategy for employing large language models to accurately identify relevant incidents and extract key information from scraped sources.

### Skills
  * NLP techniques and tools for text analysis
  * Proficiency in working with training and finetuning large language models
  * Experience with textual data pre and post-processing

