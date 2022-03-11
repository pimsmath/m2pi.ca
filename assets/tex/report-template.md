---
title: Practical Option Valuation with Negative Underlying Prices
author:
  - Edward Timko
  - Stephen Styles
  - Liam Wrubleski
date: "2020-08-30"
keywords:
  - Thoron
  - Radon

header-includes: |
  \usepackage[load=addn]{siunitx}

abstract:
  The detection of radon levels is important for reducing home and workplace
  exposure to ionizing radiation. For the detector under consideration, this
  detection is done by counting the number of alpha decays in any given time
  period, and a single measurement cannot distinguish between the different
  isotopes of radon that may be present. In this paper, we present a method to
  approximate the relative amounts of radon-222 and radon-220 in a particular
  sampling sequence by performing a linear regression to the theoretical
  expected count rate from each of these isotopes.
---

## Problem Statement
Residential radon (Rn) progeny exposure is “the leading cause of lung cancer in
non-smokers, and the second leading cause of lung cancer in smokers”
[@lungcancercanada].  Uranium (U) and thorium (Th) in the soil eventually decay
into radon, which can then seep into basements and low-lying areas of the house.
The two main radon isotopes are Rn-222, which is part of the U-238 decay chain,
and Rn-220, also called thoron, which is part of the Th-232 decay chain. There
is currently much interest in the Rn-220 contribution to radon progeny exposure,
which has so far been largely ignored. Though Rn-220 has a relatively short half
life and usually decays before it reaches the living areas in a house, its
radioactive progeny can still pose a problem.

Residential radon (Rn) progeny exposure is “the leading cause of lung cancer in
non-smokers, and the second leading cause of lung cancer in smokers” [1].
Uranium (U) and thorium (Th) in the soil eventually decay into radon, which can
then seep into basements and low-lying areas of the house. The two main radon
isotopes are Rn-222, which is part of the U-238 decay chain, and Rn-220, also
called thoron, which is part of the Th-232 decay chain. There is currently much
interest in the Rn-220 contribution to radon progeny exposure, which has so far
been largely ignored. Though Rn-220 has a relatively short half life and usually
decays before it reaches the living areas in a house, its radioactive progeny
can still pose a problem.  Radon is chemically inert, and is most often detected
by its decays. Environmental Instruments Canada (EIC) produces a Radon Sniffer
[2], which is used by radon mitigators and building scientists to find radon
entry points. The sniffer works by pumping air through a filter that removes all
radon progeny, after which it is passed into a detector that counts alpha
particle emissions from the decaying particles. The detector only counts the
total number of alpha decays in a given period, so it cannot distinguish between
Rn-222, Rn-220, or their progeny without further processing.  Currently, these
sniffers assume the only radon species present is Rn-222.


The problem we were presented with was to determine a sampling scheme and
algorithm that can reliably determine the approximate amounts of Rn-220 and
Rn222 in any particular radon-containing sample of air, given the existing
capabilities of the sniffer.

## Method

### Primer on Radioactive Decay.
The nuclei of some atoms can randomly and spontaneously decay. Such atoms, and
the substances they comprise, are said to be unstable, or radioactive. Nuclear
decay is accompanied by the emission of a particle

There is a variety of particles that can be emitted on decay, but here we are only
concerned with two: alpha ($\alpha$) particles and beta ($\beta$) particles. The
type of particle emitted in the decay is called the mode of that decay. Alpha or
beta decay change the nuclear species (i.e. the number of protons and neutrons)
of the given nucleus.  Another common mode of decay is gamma decay, but this
does not alter the nuclear species, and for this and other reasons it does not
play a part in the problem at hand. The nuclear species of an atom is also known
as that atom’s nuclide.


When an atom decays, the result may also be unstable. A sequence of such decays
form what is known as a decay chain, where an unstable substance $A$ decays into
another unstable substance $B$, which itself decays into substance $C$, etc.
These decay chains continue until a stable nuclide is reached. An important
quantity describing any radioactive substance is its half-life $t_{1/2}$ , which
is the amount of time over which a given particle of the substance has a $50\%$
probability of having decayed. Equivalently, it is the time by which $50\%$ of
the substance is expected to have decayed.

The last point to make is that the probability of decay for each atom in any
interval of time depends only on the length of that interval (i.e. the decay
process is memoryless). It does not depend on how long that atom has existed
overall, nor does it depend on the atoms around it. As such, mixing different
radioactive substances does not change their individual behaviour. From the
memoryless property of the process, it follows that the time it takes for a
given atom to decay follows an exponential distribution, while the number of
decays in a given period from a large amount of a pure radioactive substance
approximately follows a Poisson distribution.


### Modelling Expected Values
Modelling Expected Values. Suppose at time 0 you have a collection of $N(0)$
radioactive atoms, all of a single nuclide. On average, the number $N(t)$ of
atoms you expect to find remaining at time $t$ is given by

$$
N(t) = N(0)e^{-\lambda t}
$$

Where $\lambda$, called the _decay constant_ of the nuclide, is related to the
half-life $t_{1/2}$ by $\lambda = \ln(2)/t_{1/2}$. The decay rate of this
collection of atoms at time t is $\lambda N(t)$.

Before we proceed, a word about units. Radioactive quantities are frequently
described not by mass or number of particles but in terms of activity, which in
the equation above is the quantity $\lambda N(t)$. Activity carries units of
decays per unit time. The most common units of activity in the applications
being considered are becquerels ($\si{\becquerel}$) and picocuries
($\si{\pico\curie}$). By definition, $1\si{\becquerel}$ is $1$ decay per second,
and $1\si{\pico\curie}$ is equivalent to $0.037\si{\becquerel}$. In the context
of radon mitigation, quantities are usually described in activity per volume,
and the units are becquerels per cubic metre ($\si[per=slash]{\becquerel\per\cubic\meter}$)
and picocuries per litre ($\si{\pico\curie\per\liter}$).  One finds that
$1\si[per=slash]{\pico\curie\per\liter}$ is equal to $37\si[per=slash]{\becquerel\per\cubic\meter}$.

As mentioned before, the progeny of a radionuclide can also be radioactive,
resulting in so-called decay chains. The word “chain” may be somewhat
misleading, as some radionuclides can decay in more than one way. For example,
Bi-212 decays by alpha emission into Tl-208 with a probability of 33.7%, and
decays by beta emission into Po-212 with a probability of 66.3%. The decay
series which are relevant to this project are those of U-238 and Th-232, the
relevant portions of which are illustrated in [Figure \ref{rn222} and \ref{rn220}].

![Rn-222 Decay chain. Based on [@Leighton1959 chapter 15]. Effective linear
chains are indicated in bold.\label{rn222}](images/rn-222.png){width=300px}

![Rn-220 Decay chain. Based on [@Leighton1959 chapter 15]. Effective linear
chains are indicated in bold.\label{rn220}](images/rn-220.png){width=300px}

Consider a (linearly ordered) decay chain $X_0 \to X_1 \to\ldots\to X$ in which
the decay constant of $X_j$ is $\lambda_j$ for $j = 0, 1,\ldots, l - 1$, and $X$
is stable. We assume throughout that $\lambda_0, \lambda_1, \ldots,
\lambda_{l-1}$ are distinct and positive. Starting at time $0$ with a collection
$N_0(0)$ atoms of $X_0$, $N_1(0)$ atoms of $X_1$, etc., let $N_0(t), N_1(t),
\ldots, $N_{l-1}(t)$ denote the expected number of atoms of the respective type
in the given decay chain remaining at time $t$. When $.0 < j < l$, the number
$N_j(t)$ can change over time either by the decay of an atom of type $X_j$ into
one of type $X_{j+1}$ (decreasing $N_j(t)$ in the process) or by an atom of
$X_{j-1}$ decaying into an atom of $X_j$ (thereby increasing $N_j (t)$). The
time evolution of the ensemble is thus described by the following system of
ordinary differential equations:

$$
\frac{dN_0}{dt} = -\lambda_0 N_0, \qquad
\frac{dN_j}{dt} = -\lambda_jN_j + \lambda_{j-1}N_{j-1} \qquad
(0 < j < l)
$$

# References

