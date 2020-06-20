# Level 2: Using the OpenFOAM adapter

---

## Overview

- Function object that calls the preCICE API
- Writes boundary values to preCICE buffers
- Reads boundary values from preCICE buffers
- Adjusts the time step size
- Stores and reloads checkpoints

---

## Dependencies

- [preCICE](https://www.precice.org/) v2
- Recent OpenFOAM (e.g. v1706-v1912 or 4-7)
- [preCICE OpenFOAM adapter](https://github.com/precice/openfoam-adapter) (latest master)

---

## Building

- Run Allwmake

---

## Tutorial: Flow over a heated plate

(image)

---

## Configuration: overview

(overview picture)

---

## Configuration: preciceDict

- preciceDict example

---

## Configuration: OpenFOAM

- boundary condition types
- load function object

---

## Configuration: preCICE

- serial-explicit coupling
- nearest-projection (?) mapping

---

## Configuration: preCICE

(visualized)

---

## Running

- normal OpenFOAM execution
- two terminals
- look at the output
- execute the commands one-by-one

---

## Let's try again: Implicit Coupling

- Figure

---

## Configuration: Implicit coupling

- Comparison to previous

---

## Visualization

- Show the results on ParaView