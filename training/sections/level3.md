# Level 3: Coupling OpenFOAM with other solvers

---

## Other tutorials

```text [|1-4|10,19-20,24-25]
tutorials
├── CHT
│   ├── flow-over-plate
│   │   ├── buoyantPimpleFoam-laplacianFoam
│   │   ├── buoyantPimpleFoam-fenics
│   │   └── buoyantPimpleFoam-nutils
│   └── heat_exchanger
│       └── buoyantSimpleFoam-CalculiX
|
├── FSI
│   ├── 3D_Tube
│   │   └── OpenFOAM-CalculiX
│   ├── cylinderFlap
│   │   ├── OpenFOAM-CalculiX
│   │   ├── OpenFOAM-deal.II
│   │   └── OpenFOAM-FEniCS
│   ├── flap_perp
│   │   ├── OpenFOAM-CalculiX
│   │   ├── OpenFOAM-deal.II
│   │   ├── OpenFOAM-FEniCS
│   │   └── SU2-CalculiX
|
├── HT
│   └── partitioned-heat
│       └── fenics-fenics
|
└── SSI
    └── loaded_beam
        └── CalculiX-CalculiX
```

<small>See <a href="https://github.com/precice/tutorials">github.com/precice/tutorials</a>.</small>

---

## Tutorial: Channel with a perpendicular flap

<img src="images/level3/flap_perp.png" style="max-height:400px;"/>

<small>Find the case in <a href="https://github.com/precice/tutorials/tree/master/FSI/flap_perp_2D/OpenFOAM-deal.II">github.com/precice/tutorials/FSI/flap_perp_2D/OpenFOAM-deal.II</a>.</small>

---

## Dependencies

- [preCICE](https://github.com/precice/precice/wiki/Get-preCICE) v2 (e.g. [packages for Ubuntu](https://github.com/precice/precice/releases))
    - Build with PETSc (only for parallel && RBF)
- Recent OpenFOAM (e.g. v1706-v1912, 4-7)
- [preCICE OpenFOAM adapter](https://github.com/precice/openfoam-adapter) (latest master)
- [deal.II](https://www.dealii.org/) 9.2
- [preCICE deal.II adapter/example](https://github.com/precice/dealii-adapter)

