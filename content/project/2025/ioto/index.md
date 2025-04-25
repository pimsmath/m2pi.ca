---
title: IOTO
subtitle: "Tracking Involvement of Parlimentary Members on issues of
Environmental Protection and Sustainable Development"

summary: |
  This project aims to create new tools to extract insights with predictive or
  decision making value from the output of legislative bodies. It will
  investigate whether techniques from [signal
  analysis](https://invention.si.edu/invention-stories/sports-analytics-moneyball)
  or related mathematical fields can be used to help construct these tools. The
  goal is to leverage public data from legislative bodies to reveal what in the
  legislative activity is deserving if attention from a policy point of view,
  either by connecting with a known policy ontology (such as the [comparative agendas
  codebook](https://www.comparativeagendas.net/pages/master-codebook)), or by
  surfacing issues that _should_ be connected to a known ontology.


authors:
  - spat
tags:
  - '2025'

weight: 6
categories: []
date: 2025-04-05

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
This project aims to create new tools to extract insights with predictive or
decision making value from the output of legislative bodies. It will
investigate whether techniques from [signal
analysis](https://invention.si.edu/invention-stories/sports-analytics-moneyball)
or related mathematical fields can be used to help construct these tools. The
goal is to leverage public data from legislative bodies to reveal what in the
legislative activity is deserving if attention from a policy point of view,
either by connecting with a known policy ontology (such as the [comparative agendas
codebook](https://www.comparativeagendas.net/pages/master-codebook)), or by
surfacing issues that _should_ be connected to a known ontology.


### Background

Goverlytics<sup>&reg;</sup> seeks to produce low-dimensional representations of
legislative activity to: 1) make politics accessible to a broader public; and to
2) increase focus on policy goals. The model for Goverlytics<sup>&reg;</sup> is
sports analytics, which has transformed the way in which sports are understood
and consumed.  Goverlytics<sup>&reg;</sup> analyzes data generated during
legislative sessions: attendance, documents, transcripts, vote tallies, audio
and video recordings.

Analytics in sports first [began with measurement of what could be easily
measured](https://invention.si.edu/invention-stories/sports-analytics-moneyball)
– goals (of course!), strokes, hits, etc. By distilling all that goes on during
the activity into a few dimensions that allow for quantification and comparison,
analytics helps to explain and so increase comprehension and engagement.
Increasingly complex measurements are being engineered from ever larger datasets
to enhance predictions and decision-making. Both short-term outcomes and
strategies that may be decided in game, and for long-term considerations such as
player health are at stake.

### Challenge
Challenge. In some cases, Goverlytics<sup>&reg;</sup> has to start creating statistics for
legislative sessions from simple audio tracks.  Audio is transcribed into words
of a language. Then the language words (and concatenations of them) are binned
into topic discourse, by means language models and [topic
classifications](https://www.comparativeagendas.net/datasets_codebooks).
Finally, topic classifications are used to index parts of the legislative
activity that are likely to be interesting for a broader public.  This process
is akin to the distillation of a sporting match into a highlights reel or
abbreviated match summary e.g. What topics were discussed the most? Who talked
about those topics? Were there any significant new topics, or was voting and
discussion about previously known topics? Were there significant outliers? Smash
hits?


Because legislative sessions can go on for hours with very little information of
predictive or decision-making value, it can be costly to process raw data to
reach insight. The challenge is to find shorter paths to interesting bits of
discourse. Can methods from [signal
analysis](https://www.mdpi.com/journal/mathematics/special_issues/Mathematical_Methods_Signal_Analysis)
or related mathematical fields be used to more efficiently signpost insight into
legislative data? Unsupervised learning techniques may provide some guidance.
However, a successful solution will reveal what in the legislative activity is
deserving of attention from a policy point of view, ether by connecting with a
known policy ontology (such as [comparative agendas
codebook](https://www.comparativeagendas.net/pages/master-codebook), or by
surfacing issues that should be connected to a known ontology.


### Data
At a minimum, APIs covering topic data for various legislative leagues (Canada,
BC, Alberta, etc.) will be made available to the M2PI team. These APIs reliably
serve data concerning legislative 'players' and their topic-related interventions
over a number of legislative sessions. Corresponding audio will also be supplied.

Further datasets concerning elections, voting, and financial data may be made
available – depending time available, which legislative leagues the M2PI team
elects to study, and how they choose to analyse.

* Finance data are available from
  [OECD](https://data.oecd.org/gga/general-government-spending.htm), [Statistics
  Canada](https://www150.statcan.gc.ca/n1/en/type/data), and [legislative
  'leagues'
  themselves](https://www2.gov.bc.ca/gov/content/data/statistics/economy/bc-economic-accounts-gdp).
* Topics are standardized along [Comparative Agendas Project (CAP)
  lines](https://www.comparativeagendas.net/pages/master-codebook)
* Charts of
  [accounts](https://www.tpsgc-pwgsc.gc.ca/recgen/pceaf-gwcoa/2324/tdm-toc-eng.html)
  for
      [finance](https://www.oecd-ilibrary.org/sites/df28fbde-en/index.html?itemId=/content/component/df28fbde-en#:~:text=Governments'%20expenditures%20by%20function%20reveal,and%20public%20order%20and%20safety)
      overlap topic categories, but do not correspond exactly.
* Voting data for bills and motions may be available for [certain
  legislatures](https://www.ourcommons.ca/members/en/votes).
* Audio files are available for whatever legislative level is chosen for study
  by the M2PI team.
