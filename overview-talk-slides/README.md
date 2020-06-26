# My 15th OpenFOAM Workshop contributed talk slides

- Title: A flexible and preCICE solver coupling ecosystem
- Speaker: Gerasimos Chourdakis, Technical University of Munich
- Authors: Gerasimos Chourdakis, Benjamin Uekermann, + [more](https://www.precice.org/about/)
- Event: [15th OpenFOAM Workshop](http://www.cpe.vt.edu/ofw15/), Arlington, VA, USA (switched to online)
- Date: June 22, 2020

[Get the PDF](https://github.com/MakisH/ofw15-slides/blob/master/pdf-export/slides_overview_talk.pdf)

Find also the slides of my training talk "Multiphysics Modeling with the preCICE Coupling Library" in the [parent directory / on GitHub](https://github.com/MakisH/ofw15-slides).

## Abstract

In the world of OpenFOAM, many advanced solutions already exist for fluid-structure interaction, conjugate heat transfer, or other multiphysics problems. These solutions are often the result of long and dedicated research, being optimized for a specific application field, and (most commonly) OpenFOAM-only. In several cases, users opt for different computational frameworks and libraries for each single-physics domain, as domain-specific software often offers features that are difficult to find in general-purpose tools. Partitioned coupling tools are in this case a sustainable alternative.

The coupling library preCICE (www.precice.org, LGPL3) is an established and actively developed project, offering advanced coupling algorithms, mapping techniques, and communication channels. A minimally-invasive, high-level API in C++, C, Fortran, Python, and Matlab allows to exchange coupling participants arbitrarily, treating the numerics of each participant as a black box.

Ready-to-use adapters for OpenFOAM and other free and proprietary solvers comprise a flexible coupling ecosystem, now including OpenFOAM, FEniCS, deal.ii, Nutils, SU2, CalculiX, and more. The OpenFOAM adapter is a function object that passes data from/to the preCICE library, manages checkpoints, and adapts the time step size. It can be used with a variety of OpenFOAM solvers and for different applications, while it can easily be extended for different types of coupling data. The growing preCICE community has now tried the OpenFOAM adapter in conjugate heat transfer, fluid-structure interaction, and fluid-fluid coupling scenarios, while recent contributions extended its capabilities to further directions.

This talk will present the current state of preCICE and the OpenFOAM adapter, with an emphasis on recently added and upcoming features.

## Build

Follow the instructions on [reveal.js](https://revealjs.com/installation/), or just install Node.js 10.0.0 or later and do:

```bash
npm install
npm start
```

and go to [localhost:8000](http://localhost:8000/) to see the slides.

## Convert to PDF

See section "[Export to PDF](https://revealjs.com/pdf-export/)" in the reveal.js documentation.

[Decktape](https://github.com/astefanutti/decktape) does a marvelous job converting this presentation to PDF. Get the Docker image (see Decktape README) and run (for localhost):

```bash
docker run --rm -t --net=host -v "$(pwd)":/slides astefanutti/decktape generic --key=" " -p 2000 -s 1920x1440 http://localhost:8000 slides.pdf
```

## License & more

- License: [CreativeCommons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)
- Based on [reveal.js](https://github.com/hakimel/reveal.js). Template based on the "White" template by Hakim El Hattab.
- The TUM and the TU/e logos are part of the corporate identity of the Technical University of Munich and the Eindhoven University of Technology.
