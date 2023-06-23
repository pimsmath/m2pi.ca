---
title: IOTO
subtitle: "Tracking Involvement of Parlimentary Members on issues of
Environmental Protection and Sustainable Development"

summary: |
  This project will track and evaluate parliamentary members and their involvement
  and activities on environment protection and sustainable development. It will
  leverage public data with tools such as sentiment analysis to draw conclusions
  on these topics. The evaluation will focused on data
  from 2021 (or 2022, depending on availability) and we will start by looking at
  the activities of the [members of Standing Committee on Environment and
  Sustainable
  Development](https://www.ourcommons.ca/Committees/en/ENVI/Members?includeAssociates=True#AssociateMembers).
  
authors:
  - spat
  - pwalls
tags:
  - '2023'

categories: []
date: 2023-06-22T16:58:18-07:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
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
![](IOTOLogo.png)

### Overview
This project will track and evaluate parliamentary members and their involvement
and activities on environment protection and sustainable development. It will
leverage public data with tools such as sentiment analysis to draw conclusions
on these topics. The evaluation will focused on data
from 2021 (or 2022, depending on availability) and we will start by looking at
the activities of the [members of Standing Committee on Environment and
Sustainable
Development](https://www.ourcommons.ca/Committees/en/ENVI/Members?includeAssociates=True#AssociateMembers).

### Data Sources
#### Data from Parliament sittings and legislation bills
Data is scraped (or has already been scraped) for the specific year on the
conversations in the parliament sittings. The features in the scraped data
include Unix time, parliament member name, speech text, party, constituency,
province. The data will be processed for topics level 2 and 1, and sentiment
score.
  
#### Data from the committees regarding who is involved in which committee 
  - [committee's list](https://www.ourcommons.ca/Committees/en/List)

Committees are categorized based on sectors that can be mapped to topics.
Among committees there is Environment and Sustainable Development. The website
shows who is involved with the committee. It is suggested to start with
members of Standing Committee on Environment and Sustainable Development and
expand to other members of the parliament. Their activities such as voting and
proposing legislations in the committee is used as a measure on their
performance.

#### Expenses data for Canada
  * [Expenses
    Data](https://www150.statcan.gc.ca/n1/daily-quotidien/221125/cg-a001-eng.htm)


#### Emission data 
  * [Greenhouse gas emission by
    sector](https://www.statista.com/statistics/503526/greenhouse-gas-emissions-share-in-canada-by-economic-sector/)

  * [This
    website](https://prairieclimatecentre.ca/2018/03/where-do-canadas-greenhouse-gas-emissions-come-from/)
    is an example of demonstrating data of greenhouse gas emission in Canada. 
  * [Climate Action Tracker](https://climateactiontracker.org/countries/canada/)
    has historical data in Canada which is in MtCO2e/year and AR4 GWPs,
    excluding LULUCF (Land Use, Land-use Change and Forestry). More in depth
    study needed here.

Data sources will be added as the research proceeds.

### Skills
  - Data cleaning and wrangling
  - Machine learning
  - Visualization

