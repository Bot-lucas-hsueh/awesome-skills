# Scenario Examples

## 9.1 Engineering Scenarios

### Coupled Thermal-Structural

**User:** "How to simulate thermal stress in a CPU?"

**Expert:**
> **Multiphysics Setup:**
>
> 1. Add *Heat Transfer* interface
> 2. Add *Solid Mechanics* interface
> 3. Add *Multiphysics > Thermal Expansion*
> 4. Apply heat source to CPU domain
> 5. Apply convection on surfaces
> 6. Fixed displacement on PCB mount points
> 7. Run Stationary or Time Dependent

### Fluid-Structure Interaction

**User:** "How to simulate a flapping flag?"

**Expert:**
> **FSI Setup:**
>
> 1. Add *Fluid Flow > Laminar* (incompressible)
> 2. Add *Solid Mechanics* (ale)
> 3. Add *Multiphysics > Fluid-Structure Interaction*
> 4. Select moving mesh (ALE)
> 5. Use *Time Dependent* study
> 6. Consider: stability, time step, damping

### Electromagnetic Heating

**User:** "How to simulate induction heating?"

**Expert:**
> **EM + Heat Setup:**
>
> 1. Add *AC/DC > Magnetic Fields*
> 2. Add *Heat Transfer > Conduction*
> 3. Add *Multiphysics > Induction Heating*
> 4. Define coil geometry and excitation
> 5. Set material properties (electrical conductivity)
> 6. Use *Frequency-Transient* study

## 9.2 Industry Applications

| Industry | Application | Physics Coupling |
|----------|-------------|------------------|
| Electronics | PCB thermal management | Heat + Conjugate |
| Automotive | Battery thermal runaway | Heat + CFD + Chemical |
| Aerospace | Composite layup | Solid + Optimization |
| Medical | Implant design | Structural + Fluid |
| Energy | Fuel cell modeling | Electrochemical + Heat |
| Manufacturing | Induction hardening | EM + Heat + Structural |

## 9.3 Automation

### Java API Example

```java
// Create model via Java API
Model model = ModelUtil.create("Model");
model.component().create("comp1");
model.geom("comp1").create("geom1", 3);

// Add physics
model.physics().create("solid", "solid", "geom1");

// Set parameters
model.param().set("L", "10[mm]");
model.param().set("E", "200[GPa]");

// Create mesh
model.mesh("comp1").create("mesh1");
model.mesh("comp1").get("mesh1").run();

// Run study
model.study().create("std1");
model.study("std1").create("stationary", "Stationary");
model.study("std1").run();
```

### Batch Script

```bash
#!/bin/bash
# Batch parametric sweep

for param in 1 2 3 4 5; do
    comsol -batch -inputfile template.mph \
           -outputfile result_$param.mph \
           -variable L=$param
done
```