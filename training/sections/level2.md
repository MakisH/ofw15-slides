# Level 2: Using the OpenFOAM adapter

---

## What does the adapter do?

<img src="images/level2/openfoam_adapter_overview_linking.svg" />

vvv

## What does the adapter do?

<img src="images/level2/openfoam_adapter_overview_data.svg" />

vvv

## What does the adapter do?

<img src="images/level2/openfoam_adapter_overview_checkpointing.svg" />

vvv

## What does the adapter do?

<img src="images/level2/openfoam_adapter_overview_timestep.svg" />

---

## Dependencies

- [preCICE](https://www.precice.org/) v2
- Recent OpenFOAM (e.g. v1706-v1912 or 4-7)
- [preCICE OpenFOAM adapter](https://github.com/precice/openfoam-adapter) (latest master)

---

## Building

```bash
openfoam-adapter/ $ ./Allwmake

# Debugging output in Allwmake.log, wmake.log, ldd.log
```

vvv

## Building

[![asciicast](https://asciinema.org/a/341978.svg)](https://asciinema.org/a/341978)

---

## Tutorial: Flow over a heated plate

![](images/level2/openfoam-openfoam_flat_plate_surface_T_RBG_ruler.png)

---

## Configuration: overview

![](images/level2/config.svg)

vvv

## Configuration: files

<pre><code class="language-bash" data-trim data-line-numbers="|13,22,26,28,34,40,44">
.
├── Allclean
├── Allrun
├── Allrun_parallel
├── Fluid
│   ├── 0
│   │   ├── alphat
│   │   ├── epsilon
│   │   ├── k
│   │   ├── nut
│   │   ├── p
│   │   ├── p_rgh
│   │   ├── T
│   │   └── U
│   ├── constant
│   │   ├── g
│   │   ├── thermophysicalProperties
│   │   └── turbulenceProperties
│   ├── Fluid.foam
│   └── system
│       ├── blockMeshDict
│       ├── controlDict
│       ├── decomposeParDict
│       ├── fvSchemes
│       ├── fvSolution
│       └── preciceDict
├── overview.png
├── precice-config.xml
├── README.md
├── runFluid
├── runSolid
└── Solid
    ├── 0
    │   └── T
    ├── constant
    │   └── transportProperties
    ├── Solid.foam
    └── system
        ├── blockMeshDict
        ├── controlDict
        ├── decomposeParDict
        ├── fvSchemes
        ├── fvSolution
        └── preciceDict

8 directories, 35 files
</code></pre>

<!-- Continuing in index.html -->