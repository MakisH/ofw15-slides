# My 15th OpenFOAM Workshop training session slides

- Title: Multiphysics Modeling with the preCICE Coupling Library
- Speaker: Gerasimos Chourdakis, Technical University of Munich
- Authors: Gerasimos Chourdakis, Benjamin Uekermann, + [more](https://www.precice.org/about/)
- Event: [15th OpenFOAM Workshop](http://www.cpe.vt.edu/ofw15/), Arlington, VA, USA (switched to online)
- Date: June 24, 2020

[Start the presentation](https://makish.github.io/ofw15-slides/training/)

## Abstract

The coupling library preCICE (www.precice.org, LGPL3) is an established and actively developed project, offering advanced coupling algorithms, mapping techniques, and communication channels. A minimally-invasive, high-level API in C++, C, Fortran, Python, and Matlab allows to exchange coupling participants arbitrarily, treating the numerics of each participant as a black box.

This tutorial will introduce the participants to the basic concepts of preCICE, guiding them to couple two toy solvers in Python. It will then show how the same concepts are applied in the ready-to-use OpenFOAM adapter and demonstrate example cases for FSI or CHT with OpenFOAM and, depending on the interest, CalculiX or deal.II.

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
docker run --rm -t --net=host -v `pwd`:/slides astefanutti/decktape -s 1024x768 http://localhost:8000 slides.pdf
```

## License & more

- License: [CreativeCommons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)
- Based on [reveal.js](https://github.com/hakimel/reveal.js). Template based on the "White" template by Hakim El Hattab.
- The TUM and the TU/e logos are part of the corporate identity of the Technical University of Munich and the Eindhoven University of Technology.
