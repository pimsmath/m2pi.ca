---
title: "Complilogic"
subtitle:
summary: |
  The intention for this problem is to develop a digital platform to assist
  architects to develop designs that will comply with the BC Building Code.  In
  later stages, same platform will be utilized by municipalities to verify
  submitted designs comply with the building code. 

authors:
tags:
  - '2024'

weight: 7
categories: []
date: 2024-05-22

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
### Intended Product
The intention is to develop a digital platform to assist architects to develop
designs that will comply with the BC Building Code.  In later stages, same
platform will be utilized by municipalities to verify submitted designs comply
with the building code. 

### Problem Statements
We will focus on one feature of the platform which is determining the required
construction Article per Sub-section 3.2.2 of the [BC Building
Code](https://free.bcpublications.ca/civix/document/id/public/bcbc2018/bcbc_2018dbp3s32r2).

The construction Articles 3.2.2.20 to 3.2.2.90 determine the basic construction
requirements of any building.

### Main Problem

The platform should receive the 5 factors from the user and determine the
required construction articles referenced in Subsection 3.2.2 of the building
code.  The 5 factors are "building grade", "building height", "building
occupancy", "number of facing streets" and "occupancy". The platform is required
to extract the above information from the submitted architectural drawings. The
drawings will be generated in Autocad but can be changed to other formats such
as Adobe as well. 


### Subcategory of the main problem (Alternative Solutions):

The intention is to develop alternative solutions for the situations where the
design does not meet the prescriptive requirements of the code. 

If the architects do not prefer to build according to the prescriptive
requirements of the building code, the code allows alternative solutions to be
submitted. The Alternative solutions purpose is to prove the performance of the
submitted design can equally meet or exceed the objective and intention of the
building code requirements.

The alternative solutions are required to be supported by mathematical models.
For example, if the code requires a floor area to have two exit doors but the
architect prefers to have 1 exit door, it may be possible to submit an
alternative solution that will prove 1 exit door may be as safe as two exit
doors given the specific shape and other features of the building. This can be
achieved by modeling human exiting behaviour and smoke travel time using fluid
mechanics and finite element models. 
