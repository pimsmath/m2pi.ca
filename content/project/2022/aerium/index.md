---
title: Aerium Analytics
subtitle: Locating Man-Made Objects in Vegetation from Aerial Multispectral Imagery

summary: |
  The ability to detect man-made objects in vegetation would aid many fields of
  industry including -- but not limited to -- search and rescue as well as
  agriculture. The ability to locate man-made objects such as damaged modes of
  transportation, camping or hiking equipment, parachutes, etc. in said vegetation
  aids the chances of locating missing individuals involved in these cases. While
  much imagery of these objects exists, imagery of them in varying degrees of
  repair within vegetation is limited at best making standard machine learning
  detection methods difficult. In such cases, focusing on the vegetation may
  enable the detection of such objects through machine learning methods where
  imagery is limited. In agriculture, farming equipment may require repair while
  in the field where it is easily possible to misplace equipment in vegetation.
  This lost equipment could damage other farming equipment while work is being
  done. Locating lost equipment will help limit further damage of farming
  equipment saving not only money, but time and production as well.

  For this project, the team will be given access to aerial multispectral imagery
  containing a variety of man-made objects located in vegetation. The goal of this
  project is to develop a method which can detect these random man-made objects
  using machine learning and computer vision techniques while investigating the
  benefits of multispectral data to solving this problem. The machine learning
  field of focus for this problem is that of anomaly detection.

authors:
  - hardeman
  - bjoshi
  - hkohut
  - verberne
  - Hiva Gheisari
tags:
  - '2022'

categories: []
date: 2022-07-01T16:58:18-07:00

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

![](AeriumLogo.png)

## Preparatory material
_Calculus, image processing, numerical methods, knowledge of machine learning and
computer vision methods. Knowledge of Python is important. Knowledge of Fourier
analysis would be beneficial._

## Introduction

Vegetation mapping often utilizes the benefits of multispectral data as it
enables us to highlight specific aspects of imagery which are lacking in RGB
imagery. Since we see most vegetation as green, vegetation appears more
prominently in the green multiband. Combining specific bands can further
emphasize aspects of an image. For instance, the Green-Red-Infrared multiband
combination highlights vegetation.

Much research regarding vegetation mapping and classification occurs through the
help of multispectral imagery with machine learning and computer vision methods
providing many of these answers. With the abundance of such research, we propose
taking the advantages of multispectral data in vegetation mapping and
classification and utilizing it to find non- vegetation objects located in
vegetation. Specifically, can this research help improve the detection of
objects which are difficult to highlight with multispectral data such as
man-made objects?

The ability to detect man-made objects in vegetation would aid many fields of
industry including -- but not limited to -- search and rescue as well as
agriculture. The ability to locate man-made objects such as damaged modes of
transportation, camping or hiking equipment, parachutes, etc. in said vegetation
aids the chances of locating missing individuals involved in these cases. While
much imagery of these objects exists, imagery of them in varying degrees of
repair within vegetation is limited at best making standard machine learning
detection methods difficult. In such cases, focusing on the vegetation may
enable the detection of such objects through machine learning methods where
imagery is limited. In agriculture, farming equipment may require repair while
in the field where it is easily possible to misplace equipment in vegetation.
This lost equipment could damage other farming equipment while work is being
done. Locating lost equipment will help limit further damage of farming
equipment saving not only money, but time and production as well.

## Problem Description
For this project, the team will be given access to aerial multispectral imagery
containing a variety of man-made objects located in vegetation. The goal of this
project is to develop a method which can detect these random man-made objects
using machine learning and computer vision techniques while investigating the
benefits of multispectral data to solving this problem. The machine learning
field of focus for this problem is that of anomaly detection.

{{< figure src="featured.png" title="Figure 1: An image of vegetation taken with a rgb camera (left) and the rgb-bands from a multispectral camera." >}}

## References

1. Van Deventer, Heidi & Cho, Moses & Lück-Vogel, Melanie & Van Niekerk, Lara.
   (2016). Using multi-spectral sensors for vegetation mapping. PositionIT
   Magazine. July. 26-29.
1. Yichun Xie, Zongyao Sha, Mei Yu, Remote sensing imagery in vegetation
   mapping: a review, Journal of Plant Ecology, Volume 1, Issue 1, March 2008,
   Pages 9–23, https://doi.org/10.1093/jpe/rtm005
1. Oumer S. Ahmed, Adam Shemrock, Dominique Chabot, Chris Dillon, Griffin
   Williams, Rachel Wasson & Steven E. Franklin(2017)Hierarchical land cover and
   vegetation classification using multispectral data acquired from an unmanned
   aerial vehicle, International Journal of Remote Sensing, 38:8-10, 2037- 2052,
   DOI: 10.1080/01431161.2017.1294781
1. Samantha Yeo, Virginie Lafon, Didier Alard, Cécile Curti, Aurélie Dehouck,
   Marie-Lise Benot, Classification and mapping of saltmarsh vegetation
   combining multispectral images with field data, Estuarine, Coastal and Shelf
   Science, Volume 236, 2020, 106643, ISSN 0272-7714,
   https://doi.org/10.1016/j.ecss.2020.106643.
