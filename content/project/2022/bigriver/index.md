---
title: Big River Analytics
subtitle: Labour Market Information Modeling

summary: |
  Local labour market information (LMI), including employment, unemployment, and
  participation rates, are important for planning activities conducted by
  municipal and First Nation governments, service providers, and many more
  organizations. Census of Population (Census) data, published by Statistics
  Canada (StatCan), provides LMI at the Census Division (CD) and Census
  Subdivision (CSD) levels. However, the Census is only conducted every five
  years. This project asks participants to build a model which estimates
  intercensal LMI at the CD and CSD levels.

  LMI are not publicly available at the CD and CSD levels of geography for years
  when the Census is not conducted. StatCan’s Labour Force Survey provides data on
  a monthly basis. However, StatCan does not publish Labour Force Survey data at
  the CD or CSD levels. As such, LMI at the Economic Region level are often used
  in the place of intercensal data on CDs or CSDs. Figure 1 shows the CSD of the
  District of Kitimat, as well as the larger CD and Economic Region it is within,
  as an example illustrating how Economic Regions may not serve as good proxies
  for CSDs.

authors:
  - edinger
  - reiltetrault
  - kevinhalasz
  - spencerbritten
  - mxiao
  - pbains
  - fatinboyo
  - antwi

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
![](BigRiverLogo.png)

## Introduction
Local labour market information (LMI), including employment, unemployment, and
participation rates, are important for planning activities conducted by
municipal and First Nation governments, service providers, and many more
organizations. Census of Population (Census) data, published by Statistics
Canada (StatCan), provides LMI at the Census Division (CD) and Census
Subdivision (CSD) levels. However, the Census is only conducted every five
years. This project asks participants to build a model which estimates
intercensal LMI at the CD and CSD levels.


## Problem Description
LMI are not publicly available at the CD and CSD levels of geography for years
when the Census is not conducted. StatCan’s Labour Force Survey provides data on
a monthly basis. However, StatCan does not publish Labour Force Survey data at
the CD or CSD levels. As such, LMI at the Economic Region level are often used
in the place of intercensal data on CDs or CSDs. Figure 1 shows the CSD of the
District of Kitimat, as well as the larger CD and Economic Region it is within,
as an example illustrating how Economic Regions may not serve as good proxies
for CSDs.

{{< figure src="./featured.png" title="Standard Levels of Geography for Kitimat, BC" >}}

In this project, participants will build a model that can produce estimates of
intercensal LMI statistics at the CD and CSD levels. This model should be able
to produce estimates only using data available at the time the estimate is made.
For instance, estimates for the 2020 unemployment rate in the District of
Kitimat should not rely on the 2021 Census.

## Use Cases
Big River Analytics frequently works with municipal and First Nations
governments seeking to inform their decision-making with LMI. Here are a few
examples of projects Big River Analytics have conducted that would have
benefited from intercensal LMI estimates at the CD or CSD levels:

  * Kitimat & Kitimaat Village Child Care Supply & Demand Study: Big River
    Analytics and Stantec estimated the supply and demand for child care
    services, in order to anticipate and address unmet demand. This analysis
    involved modeling population changes, which used LMI to inform migration
    projections.

  * Bi-Annual LNG Monitoring Reports: Big River Analytics produces regular
    reports to measure whether the employment opportunities from Liquified
    Natural Gas (LNG) projects benefit women, Indigenous people, and local
    residents. These reports often rely on LMI at the Economic Region level, or
    Census data that may be years old.

## Extensions
The Problem Description provides a summary of this project at a basic level.
There are a variety of ways in which this project can be extended. Participants
taking on this project can address some or all of these extensions, or propose
their own.

  * Testing the Model: participants should develop a method for testing their
    model. This testing method will be important in the model development, as
    participants will need to measure the effects of changes they make while
    developing the model. A testing method will also be important for the
    application of the model, as the model will be used to produce LMI estimates
    for various different regions. A testing method will allow Big River
    Analytics to confirm that the model produces reliable estimates for each
    new CD and CSD the model is applied to.
  * Incorporating More Data: the model developed in this project does not only
    have to rely on StatCan data. Other publicly available data may also be
    utilized, such as population projections from provincial governments,
    Natural Resource Canada’s Major Projects Inventory, and online job postings.
  * Calculating Necessary Sample Sizes: StatCan’s Labour Force Survey sample
    size varies across Economic Regions. The small samples can pose an issue for
    data quality. If participants are able to calculate the minimum sample size
    needed to produce reliable intercensal estimates at the CD and CSD levels,
    Big River Analytics will take their findings to StatCan, and use it to
    demonstrate the need for larger sample sizes.

## Links

  * Statistics Canada. (2019). Census Profile, 2016 Census.
https://www12.statcan.gc.ca/census-recensement/2016/dp-pd/prof/index.cfm?Lang=E
  * Statistics Canada. (2022). Labour Force Survey.
https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=3701
