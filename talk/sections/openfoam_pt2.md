## New: `system/preciceDict`

```c++
preciceConfig "precice-config.xml";

participant Fluid;

modules (FSI);

interfaces
{
  Interface1
  {
    mesh              Fluid-Mesh-Faces;
    patches           (flap);
    locations         faceCenters;
    
    readData
    (
    );
    
    writeData
    (
      Forces0
    );
  };
  
  Interface2
  {
    mesh              Fluid-Mesh-Nodes;
    patches           (flap);
    locations         faceNodes;
    
    readData
    (
      Displacements0
    );
    
    writeData
    (
    );
  };
};

FSI
{
  rho rho [1 -3 0 0 0 0 0] 1;
}
```

<small>No need for yaml-cpp anymore!</small>

vvv

## `preciceDict` - implementation

```c++
IOdictionary preciceDict
(
    IOobject
    (
        "preciceDict",
        runTime_.system(),
        mesh_,
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE
    )
);

// lookupType&lt;T&gt;("name") is deprecated in openfoam.com since v1812,
// which recommends get&lt;T&gt;("name") instead.
preciceConfigFilename_ = preciceDict.lookupType&lt;fileName&gt;("preciceConfig");

// ...

// Every interface is a subdictionary of "interfaces",
// each with an arbitrary name. Read all of them and create
// a list (here: pointer) of dictionaries.
const dictionary * interfaceDictPtr = preciceDict.subDictPtr("interfaces");

// Check if we found any interfaces
// and get the details of each interface
if (!interfaceDictPtr)
{
  adapterInfo("  Empty list of interfaces", "warning");
  return false;
}
else
{
  for (const entry& interfaceDictEntry : *interfaceDictPtr)
  {
    if(interfaceDictEntry.isDict())
    {
      dictionary interfaceDict = interfaceDictEntry.dict();
      struct InterfaceConfig interfaceConfig;
      
      interfaceConfig.meshName = interfaceDict.lookupType&lt;word&gt;("mesh");
      // ...
    }
  }
}
```
<small>Many thanks to Mark Olesen (ESI) for the hints</small>

---

## Before: Special cases in branches

<img src="images/openfoam/branches.png" style="height:150px"/>

<small>Multiple Git branches, differing in small details</small>

---

## New: One source to rule them all

```c++
// Adapter.C

// Version-specific code with possible variants:
// - const_cast&lt;Time&&gt;(runTime_).setDeltaT(timestepSolver_, false);
// - const_cast&lt;Time&&gt;(runTime_).setDeltaTNoAdjust(timestepSolver_);
#include "version-specific/setDeltaT.H"
```

```bash
# Make/options

EXE_INC = \
    # ...
    -Ivariants/$(WM_PROJECT_VERSION) \
    # e.g. -Ivariants/v1912
```

vvv

## New: One source to rule them all

```
variants/
├── 4.0
│   └── version-specific
│       └── setDeltaT.H
├── 4.1 -> 4.0
├── 5.0
│   └── version-specific
│       └── setDeltaT.H -> ../../4.0/version-specific/setDeltaT.H
├── 6
│   └── version-specific
│       └── setDeltaT.H
├── 7
│   └── version-specific
│       └── setDeltaT.H -> ../../6/version-specific/setDeltaT.H
├── v1712
│   └── version-specific
│       └── setDeltaT.H -> ../../4.0/version-specific/setDeltaT.H
├── v1806 -> v1712/
├── v1812 -> v1806
├── v1906 -> v1812
└── v1912 -> v1906
```

vvv

## New: One source to rule them all

```
variants/
├── 4.0
│   └── version-specific
│       ├── directory_type.H
│       ├── init.H
│       └── setDeltaT.H
├── 4.1 -> 4.0
├── 5.0
│   └── version-specific
│       ├── directory_type.H -> ../../4.0/version-specific/directory_type.H
│       ├── init.H
│       └── setDeltaT.H -> ../../4.0/version-specific/setDeltaT.H
├── 6
│   └── version-specific
│       ├── directory_type.H -> ../../5.0/version-specific/directory_type.H
│       ├── init.H
│       └── setDeltaT.H
├── 7
│   └── version-specific
│       ├── directory_type.H
│       ├── init.H
│       └── setDeltaT.H -> ../../6/version-specific/setDeltaT.H
├── default -> 5.0
├── dev -> 7
├── v1712
│   └── version-specific
│       ├── directory_type.H -> ../../4.0/version-specific/directory_type.H
│       ├── init.H
│       └── setDeltaT.H -> ../../4.0/version-specific/setDeltaT.H
├── v1806 -> v1712/
├── v1812 -> v1806
├── v1906 -> v1812
└── v1912 -> v1906
```

---

## New: Pressure-based solver type selection

```c++
dimensionSet pressureDimensionsCompressible(1, -1, -2, 0, 0, 0, 0);
dimensionSet pressureDimensionsIncompressible(0, 2, -2, 0, 0, 0, 0);

if (mesh_.foundObject&lt;volScalarField&gt;("p"))
{
  volScalarField p_ = mesh_.lookupObject&lt;volScalarField&gt;("p");

  if (p_.dimensions() == pressureDimensionsCompressible)
    solverType = "compressible";
  else if (p_.dimensions() == pressureDimensionsIncompressible)
    solverType = "incompressible";
}
```

<small>Thanks to David Schneider (TUM) for <a href="https://github.com/precice/openfoam-adapter/pull/124">adding this</a>.</small>

---

## New: Write stresses (FSI)

- Before: write forces, read displacements
- Now: write forces **or stresses**, read displacements
    - No need for conservative mapping!

<small>Thanks to David Schneider (TUM) for <a href="https://github.com/precice/openfoam-adapter/pull/125">adding this</a>.</small>

---

## Upcoming: Unit & integration tests

- Already CI with system tests
- Wish: Test specific parts of the adapter
    - Unit tests with [Catch2](https://github.com/catchorg/Catch2)
    - Integration tests with [Google Test](https://github.com/google/googletest)
    - Other ideas?

<small>Prototype <a href="https://github.com/precice/openfoam-adapter/pull/122">contributed</a> by Qunsheng Huang (TUM).</small>