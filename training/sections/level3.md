# Level 3: Coupling OpenFOAM with other solvers

---

## Other tutorials

```text [|1-4|10,19-20,24-25]
tutorials
├── CHT
│   ├── flow-over-plate
│   │   ├── buoyantPimpleFoam-buoyantPimpleFoam
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
│   ├── cylinderFlap_2D
│   │   └── OpenFOAM-deal.II
│   ├── flap_perp
│   │   ├── OpenFOAM-CalculiX
│   │   ├── OpenFOAM-deal.II
│   │   ├── OpenFOAM-FEniCS
│   │   └── SU2-CalculiX
│   └── flap_perp_2D
│       └── OpenFOAM-deal.II
|
├── HT
│   └── partitioned-heat
│       └── fenics-fenics
|
└── SSI
    └── loaded_beam
        └── CalculiX-CalculiX
```

---

## Tutorial: Channel with a perpendicular flap

<img src="images/level3/flap_perp.png" style="max-height:400px;"/>

---

## Dependencies

- [preCICE](https://www.precice.org/) v2
- Recent OpenFOAM (e.g. v1706-v1912, 4-7)
- [preCICE OpenFOAM adapter](https://github.com/precice/openfoam-adapter) (latest master)
- [deal.ii](https://www.dealii.org/) 9.2
- [preCICE deal.ii adapter/example](https://github.com/precice/dealii-adapter)

---

## Configuration: overview

(todo: overview picture)

---

## Configuration: preciceDict

(todo: quick, more of the same)

---

## Configuration: OpenFOAM

(todo: quick, more of the same)

---

## Configuration: deal.ii

(todo)

- The deal.ii solver is only an example implementation
- show the parameters file

---

## Configuration: preCICE

(todo)

- RBF mapping
- parallel execution
- watchpoint

---

## Running

(todo)

- Use the run scripts

---

## Results

(todo)

- Watchpoint
- ParaView