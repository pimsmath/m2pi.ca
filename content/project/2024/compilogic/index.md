---
title: "Complilogic"
subtitle: Automated BC Building Codes Compliance
summary: |
  The goal of the Math to Power Industry Problem is to develop an algorithm that
  will determine the construction requirements per Sub-section 3.2.2 of the BC
  Building Code
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
### Background
The British Columbia Building Code (BCBC) is a provincial regulation that
establishes minimum requirements for safety, health, accessibility, fire and
structural protection of buildings and energy and water efficiency.  This code
governs new construction, and architects must develop designs that will comply
with the code when designing new buildings.  The code is prescriptive.  However,
a provision of the code allows for architects and builders to use building
designs which do not strictly follow the prescribed code if they are able to
prove that the design will meet minimum requirements for safety, health,
accessibility, fire and structural protection, energy and water efficiency.
These exceptional designs are called alternative solutions.  The existence of
alternative solutions which are not prescribed by the building code makes the
process of establishing that a building design is compliant with the BC Building
Code a non-trivial problem.

At CompliLogic, we are designing a digital platform to assist architects to
develop designs that will comply with the BC Building Code.   In the future, the
same platform will be utilized by municipalities to verify submitted designs
comply with the building code. 

### Goal
The goal of the Math to Power Industry Problem is to develop an algorithm that
will determine the construction requirements per Sub-section 3.2.2 of the [BC
Building
Code](https://free.bcpublications.ca/civix/document/id/public/bcbc2018/bcbc_2018dbp3s32r2)

### Main Problem
The construction requirements in Sub-section 3.2.2 are listed through
Construction Articles 3.2.2.20 to 3.2.2.90.  There are 5 factors used to
determine the Construction Articles. The 5 factors are "building grade",
"building height", "number of facing streets", "building occupancy", and
"Sprinkler".  Of the above factors, "building grade", "building height", and
"number of facing streets" must be extracted from the architectural drawings
while "building occupancy" and "Sprinkler" can be submitted by the user of the
CompliLogic digital platform. CompliLogic’s digital platform will use the
extracted information to determine the required construction article
referenced in Subsection 3.2.2 of the building code.


### Skillset

The main skillset required for progress on this problem is some familiarity with
reading architectural drawings, understanding building code and the referenced
terminology.

The program can be coded in any software program required for this type of
problem and suited to extract the information from architectural drawing.

The architectural drawings which are submitted by the user will be generated in
Autocad, but these drawing can be changed to other formats (such as Adobe) as
well.

### Support
No prior experience with architectural design or building codes will be assumed.
If the participants don’t have any building science background, CompliLogic will
be available to provide resources and assist.

A successful project will consist of an algorithm and a set of visuals answering
the questions posed above for the sandbox dataset, accompanied by any BI tool
files or notebook code used to produce them.
