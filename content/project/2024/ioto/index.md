---
title: IOTO
subtitle: "Tracking Involvement of Parlimentary Members on issues of
Environmental Protection and Sustainable Development"

summary: |
  This project aims to use [feature
  engineering](https://en.wikipedia.org/wiki/Feature_engineering) to help track
  and evaluate parliamentary and legislative members. We will leverage public data
  and attempt to engineer new features which may enhance engagement and/or
  predictive and decision making analytics of legislative bodies.

authors:
  - spat
  - csong
  - amane
  - ghaffari
  - syadegarzadeh
  - hghadjari
tags:
  - '2024'

weight: 6
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
This project aims to use [feature
engineering](https://en.wikipedia.org/wiki/Feature_engineering) to help track
and evaluate parliamentary and legislative members. We will leverage public data
and attempt to engineer new features which may enhance engagement and/or
predictive and decision making analytics of legislative bodies.


### Background
Expected Goals ($xG$) is an example of a number used to [compare
performance](https://statsbomb.com/soccer-metrics/expected-goals-xg-explained/)
in the complex team activity of playing soccer. $xG$ indicates the probability
of a soccer player's shot [resulting in a
goal](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0282295).
$xG$ is used to rank players and their teams on ability to capitalize on chances
(do they score more than $xG$ expected, or less?). $xG$ is an example of
[feature engineering](https://en.wikipedia.org/wiki/Feature_engineering) a
technique used to enhance predictive and decision-making in analytics. Analytics
helps to explain, understand, and increase engagement in complex phenomena such
as [baseball](https://en.wikipedia.org/wiki/Sabermetrics) and a broad range of
other activities.

### Challenge
Given data for one or more 'leagues' of legislative player, derive at least one
number like $xG$ that allows legislative players to be compared in a fair and
transparent way that may enhance engagement and/or predictive and
decision-making analytics of legislative 'play.' Numbers could be comparative –
about legislative players and their topics. They could be about situating topics
in some kind of spectrum or space in which players can be located and compared.
Examine the data and discover what might work – you may be uncovering a
dimensionless quantity that is implicitly defined!

### Data
At a minimum, APIs covering topic data for various legislative leagues (Canada,
BC, Alberta, etc.) will be made available to the M2PI team. These APIs reliably
serve data concerning legislative 'players' and their topic-related
interventions over a number of legislative sessions.  Further datasets
concerning elections (how many voted for the legislative player?), voting (what
bills and their topics did a legislative player vote for/against) and financial
data (what spending did the legislature approve and how is revenue generated?)
may be made available – depending time available, which legislative leagues the
M2PI team elects to study, and how they choose to analyse.

  * Finance data are available from
    [OECD](https://data.oecd.org/gga/general-government-spending.htm),
    [Statistics Canada](https://www150.statcan.gc.ca/n1/en/type/data), and
    [legislative 'leagues'
    themselves.](http://www2.gov.bc.ca/gov/content/data/statistics/economy/bc-economic-accounts-gdp)
  * Topics are standardized along [Comparative Agendas Project (CAP)
    lines](https://www.comparativeagendas.net/pages/master-codebook)
  * Charts of
    [accounts](https://www.tpsgc-pwgsc.gc.ca/recgen/pceaf-gwcoa/2324/tdm-toc-eng.html)
    for
        [finance](https://www.oecd-ilibrary.org/sites/df28fbde-en/index.html?itemId=/content/component/df28fbde-en#:~:text=Governments'%20expenditures%20by%20function%20reveal,and%20public%20order%20and%20safety)
        overlap topic categories, but do not correspond exactly.
  * [Elections
    data](https://www.elections.ca/content.aspx?section=res&dir=rep/off/44gedata&document=index&lang=e) are available for all elected officials.

  * [Voting data](https://www.ourcommons.ca/members/en/votes) for bills and motions may be available for certain legislatures.

