# Scenario Examples

## 9.1 Static Structural Analysis

**User:** "How do I analyze a steel bracket under load?"

**ANSYS Expert:**
> **Problem Setup:**
>
> ```apdl
> /prep7
> ! Element type
> et,1,solid185
>
> ! Material - Structural Steel
> mp,ex,1,200000           ! Young's modulus (MPa)
> mp,prxy,1,0.3            ! Poisson's ratio
> mp,dens,1,7.85e-9        ! Density (tonne/mm³)
>
> ! Geometry - L-bracket
> k,1,0,0,0
> k,2,100,0,0
> k,3,100,50,0
> k,4,0,50,0
> k,5,0,0,10
> k,6,100,0,10
> k,7,100,50,10
> k,8,0,50,10
>
> ! Create volume
> v,1,2,3,4,5,6,7,8
>
> ! Mesh
> esize,10
> vmesh,all
>
> ! Boundary conditions
> da,1,all,0              ! Fixed at left face
> da,5,all,0
>
> ! Load
> f,2,fy,-5000            ! Force at right edge
> f,3,fy,-5000
>
> /solu
> solve
>
> /post1
> plnsol,u,y              ! Plot Y-displacement
> plnsol,s,eqv            ! Plot equivalent stress
> ```
>
> **Validation:** Check von Mises stress at critical locations

## 9.2 Modal Analysis

**User:** "How do I find natural frequencies of a beam?"

**ANSYS Expert:**
> **Modal Analysis:**
>
> ```apdl
> /prep7
> ! Beam element
> et,1,beam188
>
> ! Material
> mp,ex,1,210000
> mp,prxy,1,0.3
> mp,dens,1,7.85e-9
>
> ! Geometry
> k,1,0,0,0
> k,2,1000,0,0
> l,1,2
>
> ! Real constants
> r,1,1000,1000000,5,0,0,0
>
> ! Mesh
> lmesh,all
>
> ! BCs
> d,1,all,0
>
> /solu
> antype,modal
> modopt,lanb,5           ! First 5 modes
> solve
>
> /post1
> set,list                ! List frequencies
> set,1,1
> pldisp,1
> ```

## 9.3 Thermal-Structural Analysis

**User:** "How do I analyze thermal stress in a pressure vessel?"

**ANSYS Expert:**
> **Coupled Field Analysis:**
>
> ```apdl
> /prep7
> ! Thermal element
> et,1,plane55
>
> ! Thermal properties
> mp,kxx,1,45             ! Conductivity
> mp,c,1,460              ! Specific heat
> mp,dens,1,7800          ! Density
>
> ! Geometry (pressure vessel cross-section)
> rectng,0,500,0,100
>
> ! Mesh
> aesize,all,20
> amesh,all
>
> ! Thermal BCs
> sf,3,conv,10,25        ! Convection at outer
> bf,4,temp,200           ! Temperature at inner
>
> /solu
> antype,static
> solve
>
> ! Get temperatures
> /post1
> etable,temp_nodal,nmisc,118
>
> ! Switch to structural
> /prep7
> et,1,plane182,1211     ! Coupled field
>
> ! Apply thermal results as load
> ldread,temp,,,,,,rth
>
> ! Structural properties
> mp,ex,1,200000
> mp,prxy,1,0.3
> mp,alpx,1,1.2e-5       ! Expansion coefficient
>
> ! Structural BCs
> da,1,all,0
> da,2,symm
>
> /solu
> solve
>
> /post1
> plnsol,s,eqv
> ```
