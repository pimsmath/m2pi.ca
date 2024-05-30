---
title: "Nautical Crime Investigation Services - Problem 1"
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
This project aims to leverage natural language processing techniques to generate
search engine prompts that yield high-quality results. Quality indicators
include relevance, diversity, soundness, and minimizing bias.

_Note that this problem is independent of the other problem statements
submitted by NCIS._


#### Context on web -scraping
With our current algorithm, users can specify how many of the top n search
results should be scraped when a prompt is entered into the search engine. Any
site within these top n results will be scraped, meaning there are no
predetermined sites to include or exclude. However, as part of optimizing the
prompt generation system, participants may want to compare the results for
different values of n and identify any sources that are irrelevant and should
not be scraped.

_Assigned topic: underreporting/misreporting of catch_

#### Baseline Problem Statement
Develop a system to generate diverse and relevant search prompts to web scrape publicly available incident reports on the given topic. 

#### Extended Statement (time permitting)
Developing a dynamic prompt generation system that optimizes search engine prompts to web scrape publicly available incident reports on the given topic.

### Skills
##### Required
  * NLP techniques and tools for text analysis
  * Familiarity with large language models
##### Preferrable
  * Proficiency in web scraping techniques and tools


