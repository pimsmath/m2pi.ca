---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Aerium Analytics"
summary: |
  Roads are a vital component of today’s society. They not only connect us to
  different cities, towns, provinces, and countries, but they also provide of a
  means of transporting goods and services. Typically, roads are constructed
  using materials such as concrete, or asphalt. Between the cold winter
  temperatures and hot summer temperatures, as well as settling earth, cracks
  and potholes are bound to occur on roads.

  Alberta spent over 1.6 billion dollars in transportation related needs in
  2020-21. Over 26% of this money went towards road construction and maintenance
  related expenditures. Roads undergo regular inspection; a detailed Surface
  Condition Rating occurs every two years in Alberta. This helps determine the
  priority in which maintenance should occur on roads in the province. One
  method of conducting these inspections could be done via aerial imagery. While
  an individual could go through these images to inspect the roads for cracks
  and potholes, is there a way that machine learning and computer vision could
  not only detect cracks but also classify their severity? 

authors: []
tags: ["2021"]
categories: []
date: 2021-07-10T16:57:49-07:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: |
    (Left) An aerial image of a road containing different deformations to the
    pavement. (Right) The aerial image of the road with red bounding boxes
    designating the defects perpendicular to the road and yellow bounding boxes
    designating the defects parallel with the road. Such distinction is not a
    requirement of the project but could be of interest for judging severity. 
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

final_report: 
---

## Introduction
Roads are a vital component of today’s society. They not only connect us to
different cities, towns, provinces, and countries, but they also provide of a
means of transporting goods and services. Typically, roads are constructed using
materials such as concrete, or asphalt. Between the cold winter temperatures and
hot summer temperatures as well as settling earth, cracks and potholes are bound
to occur on roads. These result in further wear and tear on roads but also
vehicles which transport goods and services as well as us to different parts of
the world.

Alberta alone spent over 1.6 billion dollars in transportation related needs in
2020-21 [^1]. Over 26% of this money went towards road construction and
maintenance related expenditures. Roads undergo regular inspection; a detailed
Surface Condition Rating occurs every two years in Alberta [^2]. This helps
determine the priority in which maintenance should occur on roads in the
province. One method of conducting these inspections could be done via aerial
imagery. While an individual could go through these images to inspect the roads
for cracks and potholes, is there a way that machine learning and computer
vision could not only detect cracks but also classify their severity? 

## Problem Statement

Several techniques for road surveillance exist, from manual detection to machine
detection methods. The use of an individual to inspect pavement takes a
significant amount of work hours [^3]. The use of various machines such as
microwave, ultrasound, etc. still require some form of analysis once the data
has been collected. The analysis of such large data sets can also be time
consuming for a single or even group of individuals and result in human error or
even bias.

Using machine learning and computer vision to analyze this data enables a
smaller likelihood of bias and error. While various types of data could be used
to solve this problem, aerial RGB imagery can be collected quickly with minimal
additional costs as well as decreased interruptions to standard operations. The
use of RGB images will also allow for the interpretation of the severity of the
deformations in the pavement.

For this project, the team will be given access to aerial RGB images of
pavements with various defects including cracks and potholes. The goal is to
develop a method which can detect defects in the payment using machine learning
and computer vision techniques. Producing a system to adequately relay the
severity of a detected defect will also be a goal of the project. We plan to
focus on unsupervised machine learning techniques for this problem, as data in
industry is often limited. Methods for addressing this problem may involve edge
detection and cluster analysis for detection purposes and for classification,
geometry may be useful. The overall goal is to find a method which requires
limited user input for detecting and classifying defects found in pavement.

### References
[^1]: Government of Alberta. “Annual Report Transportation 2020-2021.” 2021. URL
https://open.alberta.ca/dataset/d24ecf3f-d15a-4e41-b090-9e1a4c85949a/resource/d46ff3e4-
9180-48f1-94dc-1eda8d9b5771/download/trans-annual-report-2020-2021.pdf
[^2]: Transportation Alberta. “Highway Maintenance Guidelines and Level of Service Manual.” 2000
[^3]: Yang C, Chen J, Li Z, Huang Y. Structural Crack Detection and Recognition
Based on Deep Learning. Applied Sciences. 2021; 11(6):2868.
https://doi.org/10.3390/app11062868 


