---
title: "Complilogic"
subtitle: Automated BC Building Codes Compliance
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
## Problem Statement
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
The goal of the Math to Power Industry Problem is to investigate and incorporate
mathematical models which can be used to prove that the performance of the
submitted design can equally meet or exceed the objective and intention of the
building code requirements.

More specifically, the goal of this project will be to model human exiting
behaviour and smoke travel time using fluid mechanic and finite element models.

### Details
In this project, we will focus on one feature of the digital platform:
determining the required construction per Sub-section 3.2.2 of the [BC Building
Code](https://free.bcpublications.ca/civix/document/id/public/bcbc2018/bcbc_2018dbp3s32r2)

The construction Articles 3.2.2.20 to 3.2.2.90 determine the basic construction
requirements of any building.  There are 5 factors used to determine whether or
not a building is compliant with the building code.  CompliLogic’s digital
platform should receive these 5 factors from the user, and determine the
required construction articles referenced in Subsection 3.2.2 of the building
code.

The 5 factors are "building grade", "building height", "building occupancy",
"number of facing streets" and "occupancy". The platform is required to extract
the required information about these factors from architectural drawings
submitted by the user.

### Main Problem

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
mechanic and finite element models.

### Skillset
The main skillset required for progress on this problem is some familiarity with
mathematical modelling.  Specific experience with fluid mechanics and finite
element models would be beneficial to solving this problem.

The architectural drawings which are submitted by the user will be generated in
Autocad, but these drawing can be changed to other formats (such as Adobe) as
well.

No prior experience with architectural design or building codes will be assumed.
