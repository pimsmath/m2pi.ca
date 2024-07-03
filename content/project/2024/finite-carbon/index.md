---
title: "Finite Carbon"
subtitle: "Building a Platform for Digital Energy"
summary: |
  This project aims to improve machine learning models for image classification
  of areas affected by deforestation. It will involve techniques such
  as feature engineering, binary classifier design and the use of 
  evaulation metrics to design models which maximize precision while minimizing
  false positives.
authors:
  - jgolinkoff
  - byekkehkhany
  - yshahhosseini
  - bluna
  - ajahangiri
  - iasamoah
  - pcoulibaly
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
![](./finite-carbon.jpg)

Imagine you’re working on a machine learning model to identify areas affected
by deforestation. The dataset contains satellite images, and your task is to
classify image patches into two categories: “Deforested” (Class A) and
“Non-Deforested” (Class B). However, deforested patches are significantly rarer
than non-deforested ones.
 
### Data Description:

 * **Class A (Deforested; at most 5% of the dataset)**: Represents the rare
instances of deforested patches (e.g., cleared land, logging areas).
 * **Class B (Non-Deforested)**: Dominates the dataset and includes natural forest
cover, agricultural land, and other non-deforested regions.

### Classifier Performance Metrics:

 * **Accuracy**: While overall accuracy is commonly used, it can be misleading due
to class imbalance. In this case, achieving high accuracy might not reflect the
model’s true performance.
 * **Precision**: Precision measures the proportion of correctly predicted
deforested instances (Class A) out of all predicted positive instances.
Minimizing false positives is crucial to avoid misclassifying non-deforested
areas.
 * **Recall (Sensitivity)**: Recall calculates the proportion of true deforested
instances (Class A) correctly identified out of all actual deforested
instances. High recall ensures we don’t miss deforested areas.
 * **Specificity**: Specificity represents the proportion of true non-deforested
instances (Class B) correctly identified out of all actual non-deforested
instances. Avoiding false alarms for natural forest cover is essential.
 * **F1 Score**: The F1 Score balances precision and recall, considering both false
positives and false negatives. It’s particularly useful for imbalanced data.

### Challenge:

 * How would you design a binary classifier that optimizes both precision
(minimizing false positives) and recall (minimizing false negatives) for
detecting deforested areas?
 * Consider techniques like oversampling deforested patches, using weighted
loss functions, or leveraging synthetic data generation.
 * Which evaluation metric(s) would you prioritize when evaluating your model’s
performance on deforestation detection?

Remember, in rare-case binary classification, thoughtful model selection, feature engineering, and robust evaluation are critical to achieving reliable results, especially when dealing with imbalanced data.
