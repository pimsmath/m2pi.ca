---
title: NRCAN
subtitle: "Detecting Swarming Mountain Pine Beetles in Weather Radar Data"

math: true

summary: |
  Long-distance dispersal of insects in fast moving air currents is increasingly
  recognized as an important driver of their dynamics at a landscape scale.
  Moreover, this type of dispersal has important implications for forest and
  agricultural crops impacted by insects.  Because the detection and tracking of
  populations of flying insects remains challenging, it is rarely possible to
  determine where insects originated after they have dispersed long distances.
  Data from weather radars designed to detect precipitation may be useful tools
  for gaining insight into insect long distance dispersal because insect bodies
  and rain drops are often similar in size. Thus, within radar scans there
  is potential to quantify the density of insects departing to start
  long-distance dispersal as well as the movement trajectories of swarms–at
  least until they pass beyond the range of the radar.  However, because
  Doppler weather radars are extremely sensitive and capable of detecting
  water vapor in clouds, it can be difficult to distinguish between
  potential insect signals and weather signals even when it is not
  ostensibly raining.

  This project has two distinct objectives. First, we will investigate
  classification of radar images, based on motion, to identify insect swarms.
  Second, we will develop a mathematical model and numerical simulations to more
  easily distinguish distinguish meteorological and biotic signals.


authors:
  - goodsman
  - nkaur
  - trofimenkoff 
  - puttipong
  - Ben Xiao

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
![](NRCANLogo.png)

### Introduction
Long-distance dispersal of insects in fast moving air currents is increasingly
recognized as an important driver of their dynamics at a landscape scale.
Moreover, this type of dispersal has important implications for forest and
agricultural crops impacted by insects.

Because the detection and tracking of populations of flying insects remains
challenging, it is rarely possible to determine where insects originated after
they have dispersed long distances. Data from weather radars designed to detect
precipitation may be useful tools for gaining insight into insect long distance
dispersal because insect bodies and rain drops are often similar in size. Thus,
within radar scans there is potential to quantify the density of insects
departing to start long-distance dispersal as well as the movement trajectories
of swarms–at least until they pass beyond the range of the radar. However,
because Doppler weather radars are extremely sensitive and capable of detecting
water vapor in clouds, it can be difficult to distinguish between potential
insect signals and weather signals even when it is not ostensibly raining.

The scientific literature contains many examples in which doppler weather radar
data have been used to quantify and track insects. Generally these studies have
either analyzed data in which there was no rainfall nor any clouds such that
a large proportion of the radar signal is likely biotic in origin, or they have
presumed that data were collected on a cloud-free day, sometimes when evidence
to the contrary exist. In reality, insects also disperse on days that are not
cloud-free. Furthermore, although most insects are unlikely to fly in rainy
conditions, small rain events and insect dispersal events may occur at the same
time albeit in different locations. Therefore, methods to distinguish the
movements of insects from the movements of clouds and weather systems are
needed.


Researchers have visually distinguished biotic and meteorological signals in
sequences of radar images. For example, biotic signals assumed to be mountain
pine beetles were distinguishable by Jackson et al. [2008] because they were
concentrated at lower altitudes near the center of radar scans and because they
did not display correlated large-scale movement typical of weather systems
[Jackson et al., 2008]. This is evidently a subjective classification.  Because
biotic signals are undesirable in meteorology, researchers have devised many
algorithmic approaches to remove them, along with other forms of noise
collectively called ground clutter. These algorithms, while also subjective
(they depend on the parameters chosen by the user), have the advantage of
producing classifications that can be repeated and optimized, unlike those
produced by a human visual observer. One example of an algorithm designed to
remove biotic signals and other ground clutter is the texture-based approach of
Gabella and Notarpietro [2002]. The al- gorithm proposed by Gabella and
Notarpietro [2002] is static in that it looks essentially for regions of high
spatial variability, and uses informed thresholds to classify regions as
clutter; regions with lower spatial variability are classified as
meteorological (this is a slight simplification but not complete
misrepresentation).


This project has two distinct objectives that require two distinct skill-sets.
Therefore, depending on interest, the project may have two groups of
participants that work on each of the two objectives. The first objective is to
create a new method or customize an existing motion segmentation method such
that it can be applied to sequences of radar images to classify regions based
on movement without supervision. The concept behind this objective is that
swarming animals move differently from weather systems as observed by [Jackson
et al., 2008]. Classification based on motion segmentation, can then be
compared to classification based on the static texture-based approach
referenced above.

The second objective of this project is to develop theory that could allow researchers to
more easily distinguish meteorological and biotic signals based on simple mathematical
models. Ideally, the theory developed will facilitate tests of whether the dynamics in
regions classified by the motion segmentation algorithm as part of the first objective
are consistent with swarming insects. A preliminary partial differential equation model
based on Newtonian physics has been developed by the industrial mentor on the project
(see following section for a brief overview). The participants focused on the second
objective will conduct numerical simulations, mathematical analyses, and may improve
or generalize this model to maximize its utility in the context described above.

### A simple mathematical model of swarming insects
We consider insects moving in one spatial dimension. Insects in our model will
have a natural attraction to a home range at the center of the spatial domain
(x = 0). There is a diffusive force, which pushes insects away from the center
of the domain, but this is opposed by directed acceleration back towards the
center. Acceleration, back towards the center is limited by air resistance. A
system of equations that embodies these traits can be written as

$$
\frac{dv}{dt} = -\text{sgn}(v)\frac{q}{m}v^2 - \frac{\eta}{m}x,
$$

$$
\frac{\partial u}{\partial t} = -\frac{\partial}{\partial x}(vu) + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial{x^2}}
$$

wherein $v$ represents velocity; $x$, is the spatial domain; $u$ is insect
density as a function of space and time $(u(x, t))$; $m$ represents the
insect’s mass (assumed constant); $q$ is a product of several parameters that
control air resistance, and $\eta$ governs how the net force acting on the
insect changes as a function of location along $x$. A full explanation of the
derivation that led to this system will be provided to participants.

Some possible avenues for analysis include

1. What are the overall (transient and steady-state) dynamics of a group of
individuals governed by these physics and do they correspond to observations
made of swarming insects?
2. What are the spatial spectra (obtained from Fourier transform) of the steady
state solution (for velocity and population density) of the PDE system? Do the
spatial spectra of the non-steady state solutions resemble those of the steady
state solutions?
3. At what spatial scales are we likely to observe the system’s spatial spectra
and how do they differ from those of classical diffusion?
4. Consider the problem on a finite domain with absorbing boundary conditions:
For a given level of diffusion, is there a threshold size of the spatial domain
such that persistence of the swarm becomes impossible (eg: critical domain size
problem).


### Team prerequisites
This project has two different objectives: Objective one is likely to depend
more heavily on machine learning approaches than objective two; Objective two
will rely on analysis of partial differential equation models. Therefore,
participants may divide into two sub- groups depending on their interests but
they should have interest in at least one of the topics below:

1. Machine learning or clustering algorithms applied to moving data or interest in
learning about ML for unsupervised learning (objective one)

2. Applied PDE modeling (objective two and possibly also for objective one
depending on the direction the team takes)

3. Mathematical biology (objective two)

Participants need not be interested in both machine learning and modeling using
partial differential equations to participate. However, some overlap in
interests may facilitate cross-talk between the two sub-groups.


### Doppler weather radar data

The Doppler radar data available for this project come from Environment and
Cli- mate Change Canada (ECCC). Specifically, the data are from the Prince
George (Baldy Hughes) radar in British Columbia on July 11 and July 26, 2005.
The data for these dates are provided because on July 11 2005, Prince George
received a measurable amount of rain and there was relatively little mountain
pine beetle activity; conversely on July 26, no rain was measured but mountain
pine beetles flying high above the forest canopy were observed and quantified
at the radar site using a small aircraft with a drogue net [Jackson et al.,
2008].


In raw format, the radar data are in polar coordinates because the radar
antenna does a rotational sweep at preset angular elevations relative to
horizontal. At each elevation, the radar sends and receives radar signals along
rays at 720 azimuths (every 0.5 degrees around a full circle). Along each of
the 720 rays in a sweep, data are organized by discrete bins that are 0.5 km in
length such that the radar resolution is 0.5 degrees × 0.5 km.  The Doppler
radar data comprise three data types. The first data type is reflectivity,
which is measured in dBZ (decibel relative to Z), a logarithmic dimensionless
unit that when properly transformed, can provide information regarding the
density of drops (or insects) per unit volume. The second type of data are
Doppler velocities in $ms^{−1}$ . These are the average velocities of objects
in the radar beam projected onto the ray in each bin. Negative velocities
indicate movement towards the radar antenna along the ray and positive
velocities indicate movement away from it along the ray. The third data type is
referred to by meteorologists as spectrum width. It is the standard deviation
of Doppler velocities in each bin along each ray.


The raw radar data have been processed to remove artifacts created by static
objects that intercept the radar beam (referred to as beam blockage). Then, the
data were classified using a texture-based clutter detection algorithm [Gabella
and Notarpietro, 2002] to create two subsets: regions classified as clutter,
and regions classified as meteorological. The reflectivity (dBZ) data were
then transformed ($Z = \exp(dBZ))$ such that they are proportional to the
density of rain drops or insects per volume ($m^3$). These data will serve as a
benchmark against which the results of this project will be compared.

A version of the data with beam blockage artifacts removed, but which was not
preprocessed using the texture-based algorithm is the data-set that will be the
focus of this project. Similar to the segmented data-set described above,
reflectivity (dBZ) data for the unclassified data-set were transformed $(Z =
\exp(dBZ))$ such that they are proportional to the density of rain drops or
beetles per volume ($m^3$).  All data (classified and unclassified) have been
geo-referenced, converted to rasters using regular square grids (with
interpolation) and written to geotiffs, which are a standard format of
georeferenced rasters that can readily be read using any of the most common
scientific computing languages. The time resolution of the data is 10
minutes. Thus there is a separate raster for every 10 minutes from 8:00 to
18:00 local standard time. These data will be made available to team members in
a Google Drive folder along with detailed meta-data.


### Some potential motion segmentation approaches

The ideas below are meant to inspire creativity rather than to be a definitive
list. Obviously, the team could choose to apply an approach that is not
listed here.

1. Motion segmentation algorithm: several such algorithms are available on Github
(https://github.com/topics/motion-segmentation).
2. Combined PDE and ML approach: In an inverse approach, one might assume that
dynamics can be represented by a simple convection-diffusion model with diffusion
and advection coefficients that vary in space. One potential approach to solving
the inverse problem is to use a numerical PDE solving scheme that is fused with a
machine learning model [Long et al., 2018]. If the inverse problem can be solved
and estimates of the coefficients as well as model error can be obtained, then the
presence of swarming might be detectable by analysis of the model error because
the convection-diffusion model should be a poor representation of dynamics when
swarming is present.

### Bibliography

* M Gabella and R Notarpietro. Ground clutter characterization and elimination
in moun- tainous terrain. In Proceedings of ERAD, volume 305, 2002.
* Peter L Jackson, Dennis Straussfogel, B Staffan Lindgren, Selina Mitchell,
and Brendan Murphy. Radar observation and aerial capture of mountain pine
beetle, dendroctonus ponderosae hopk.(coleoptera: Scolytidae) in flight above
the forest canopy. Canadian Journal of Forest Research, 38(8):2313–2327, 2008.
* Zichao Long, Yiping Lu, Xianzhong Ma, and Bin Dong. Pde-net: Learning pdes
from data. In International Conference on Machine Learning, pages 3208–3216.
PMLR, 2018.

