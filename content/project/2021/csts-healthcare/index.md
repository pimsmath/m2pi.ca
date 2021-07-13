---

title: "CSTS Healthcare"
subtitle: Therapy Similarity Measures
summary: |
  Cancer is a disease that affects 14M people each year. While we have had some
  success with specific cancers, many patients are put on a roller coaster of
  emotion through cycles of remission and relapse. There is abundant scientific
  evidence which tells us cancer is driven by multiple genes working in concert.
  CSTS Healthcare has developed a computational system which identifies
  personalized cancer therapy for every cancer patient given their unique set of
  DNA and RNA. In practice, the therapy a patient actually receives may not
  exactly match what our system has identified as the best therapy.  In this
  project we will develop therapy similarity measures to allow us to compare our
  therapies with those actually given by to a patient by their oncologists.


authors: []
tags: ["2021"]
categories: []
date: 2021-07-12T12:54:49-07:00

# Optional external URL for project (replaces project detail page).
external_link: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:

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

math: true

#final_report: 'Aerium-final.pdf'
---

## Background
Cancer is a disease that affects 14M people each year. While we have had some
success with specific cancers, many other patients are put on a rollercoaster of
emotion through cycles of remission and relapse. At this point, there is
abundant scientific evidence that tells us cancer is driven by multiple genes
working in concert.

Traditionally in medicine, drugs are designed and approved by testing on large
populations. This type of results in only a portion of the population actually
responding to a given therapy. However, different patients respond differently
to the same drugs. Typically, on a large double-blind clinical trial with
thousands of patients and two arms, everyone on one arm receives the same
therapy A, while everyone else on the other arm receives exactly the same
therapy B.

In the past several decades, we have learned that cancer is a highly
heterogenous disease with multiple genes involved in cancer progression, and
therefore requires combination therapies tailored to each individual’s life
history and genomic profile. Based on multiomic profiles one can model the
cancer biology: which genes are driving the cancer, and which of the 10
hallmarks of cancer are active.

This allows the design of personalized therapies that are unique to every individual. However, this also presents a novel statistical problem, called the N-of-One problem, where it is difficult to achieve statistical power. Because each patient in a trial is receiving a differing, unique therapy, these therapies are not obviously comparable. One recent study, the I-PREDICT trial attempted to provide a comparison of personalized combination therapies when the therapy was only partially adopted. They did not directly evaluate personalized therapies, but simply determined that when a given therapy targeted more mutations, it was correlated with better outcomes.


## Problem Statement
We have developed a computational system that identifies a personalized cancer
therapy for every cancer patient, given their unique set of DNA and RNA. For
each patient, our system identifies the best of set of target genes and active
hallmarks, each of which have sets of available therapies associated with them.
In a clinical setting however, a clinician prescribes the therapy they believe
is most appropriate for a given patient. In this context, if there are 100
patients, there are 100 unique therapies. Moreover, the therapy a patient
receives may not match what our system identified as the best therapy. This
problem then breaks down into the following sub-problems:

  * We would like to construct a set of similarity measures that allow us to
    compare our Aiomic therapies with those actually given by oncologists.
  * Given the entire set of patients, can we quantify adoption rates of Aiomic
    therapies 
  * Can we measure outcomes for Aiomic therapies as to whether they succeeded,
    partially succeeded or failed?

In contrast to the I-PREDICT approach, for our problem, we are interested in not
just matching gene targets, but evaluating the success of Aiomic therapies when
the given therapies are not an exact match. The problem can be stated as follows:

  * A trial consists of N patients.
  * Each patient receives a therapy T, that consists of a set of drugs D
    that target zero or more Genes, and zero or more Hallmarks.
  * A therapy can be viewed as set of drugs, T = Drugs = $\left\\{d_1, \ldots, d_n \right\\}$
  * Each drug can be related to zero more targets, where a target is either a
    gene or a hallmark.
  * Each therapy is associated with one of three Outcome = {succeeds, partially
    succeed, or fails}
  * Aiomic identifies the best therapy Aiomic-Therapy for each patient
  * A clinician administers a given therapy Given-Therapy for each patient

### Questions

  * How can we compare Aiomic-Therapies to Given-Therapies? For example, would
    it simply be the % intersection between the set of targets and hallmarks
    that are covered by the drugs in each therapy?
  * Across all patients, given the set of Aiomic-Therapies and Given-Therapies,
    can we say how often Aiomic therapies were adopted? To what degree? 
  * Across all patients, given outcomes, when a Given-Therapy is not exactly the
    same as a Aiomic- Therapy, and has non-zero overlap, can we assign an
    outcome to the corresponding Aiomic- Therapy?
  * How much of a Given-Therapy outcome can we allocate to the Aiomic-Therapy in
    cases where there is partial overlap between the recommended therapy and the
    given therapy? 
  * If the adoption rate was 30%, is 30% of the outcome due to the
    recommendation? That is to say, if only one of the drugs from the
    recommendation were used in the given therapy, what % is attributable to the
    recommendation. 
  * Can we create a predictive model for partial adoption of our therapies?


### References
See: [^1][^2][^3][^4][^5][^6]
[^1]: Klement et al. Future Paradigms for Precision Oncology. Oncotarget (2016). 7:46813-46831. https://doi.org/10.18632/oncotarget.9488
[^2]: Hanahan, Douglas et al. Hallmarks of Cancer: The Next Generation. Cell, Volume 144, Issue 5, 646 – 674. https://doi.org/10.1016/j.cell.2011.02.013 
[^3]: Lillie EO, Patay B, Diamant J, Issell B, Topol EJ, Schork NJ. The n-of-1 clinical trial: the ultimate strategy for individualizing medicine? Per Med. (2011) 8:161–73. 10.2217/pme.11.7 
[^4]: N-Of-One Trial- https://en.wikipedia.org/wiki/N_of_1_trial 
[^5]: Offord, Catherine. N-of-1 Trials Take on Challenges in Health Care– The Scientist. (2019) July/August. https://www.the-scientist.com/features/n-of-1-trials-take-on-challenges-in- health-car-66071 
[^6]: Sicklick JK, et al. Molecular profiling of cancer patients enables personalized combination therapy: the I-PREDICT study. Nat Med. 2019 May;25(5):744-750. doi: 10.1038/s41591-019- 0407-5. Epub2019 Apr 22. PMID: 31011206; PMCID: PMC6553618. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6553618/

