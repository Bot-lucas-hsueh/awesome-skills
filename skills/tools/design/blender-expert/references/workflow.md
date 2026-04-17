# Standard Workflow

## 8.1 Getting Started

### Character Modeling Workflow

```
Phase 1: Reference Setup
├── Import reference images (front, side, top)
├── Set as background images in 3D Viewport
├── Adjust opacity for sketching comfort
└── Enable X-Ray to see through mesh

Phase 2: Base Mesh
├── Create low-poly base from primitives
├── Block out major forms (head, torso, limbs)
├── Use mirror modifier for symmetry
├── Maintain clean edge flow
└── Target polygon count for game (5-20K)

Phase 3: Detail Refinement
├── Sculpt major muscle groups
├── Add anatomical details
├── Refine proportions
├── Create clothing forms if applicable
└── Use Multiresolution for detail pass

Phase 4: Topology
├── Retopologize with proper edge flow
├── Use Retopo tools, shrinkwrap, or poly build
├── Ensure proper subdivision levels
├── Check for poles and Ngons
└── Clean up geometry

Phase 5: UV and Texturing
├── UV unwrap with proper seams
├── Pack UV islands efficiently
├── Create texture maps (diffuse, normal, roughness)
├── Paint details in Substance or Blender
└── Set up material in Shader Editor

Phase 6: Rigging (if needed)
├── Create armature
├── Weight paint character
├── Test deformation
└── Create control rig
```

### Product Visualization Workflow

```
Phase 1: Model Preparation
├── Import CAD data or start from primitives
├── Fix any mesh issues (non-manifold, holes)
├── Apply all modifiers
├── Check scale (1 Blender unit = 1 meter)
└── Organize in collections

Phase 2: Materials Setup
├── Create PBR materials (Principled BSDF)
├── Add roughness/metalness maps
├── Set up environment HDRI
├── Configure render engine (Cycles/Eevee)
└── Test material on object

Phase 3: Lighting
├── Set up three-point lighting
├── Add area lights for soft shadows
├── Position environment lighting
├── Adjust exposure and temperature
└── Add fill lights if needed

Phase 4: Scene Composition
├── Place camera with framing in mind
├── Set up camera depth of field
├── Add secondary props
├── Configure background/hdri
└── Fine-tune camera angle

Phase 5: Rendering
├── Set render samples (256-1024)
├── Enable denoising
├── Add post-processing (bloom, chromatic aberration)
├── Render to resolution (4K for stills)
└── Review and adjust

Phase 6: Compositing
├── Import render layers
├── Color grade
├── Add vignettes
├── Composite in passes
└── Export final image
```

### Architectural Visualization Workflow

```
Phase 1: Scene Setup
├── Import CAD model or create in Blender
├── Check scale and proportions
├── Set up scene units (meters)
├── Organize by floors/collections
└── Enable world background or HDRI

Phase 2: Materials
├── Create architectural materials
├── Use image textures for surfaces
├── Set up procedural materials (concrete, wood)
├── Configure glass and mirrors
└── Test materials in scene lighting

Phase 3: Lighting Setup
├── Sun light with proper angle
├── Ambient occlusion
├── Interior lights (area, point)
├── Light portals for interior
└── Adjust exposure

Phase 4: Camera Animation
├── Set up camera path
├── Define key frames
├── Add camera cuts
├── Configure focal length changes
└── Test animation timing

Phase 5: Final Render
├── Set high sample count (512-2048)
├── Enable ambient occlusion
├── Configure denoiser
├── Set output format (PNG sequence)
└── Render animation

Phase 6: Post-Production
├── Import into compositor
├── Add sky replacement
├── Color correct
├── Add people/trees (optional)
└── Export final video
```

## 8.2 Asset Production Workflow

### 3D Asset Pipeline

```
Step 1: Concept
├── Create concept art or reference
├── Define style (stylized, realistic)
├── Determine LOD requirements
├── Set target poly count
└── Plan texture resolution

Step 2: Modeling
├── Create low-poly base mesh
├── Maintain clean topology
├── UV unwrap early
├── Add edge loops for deformation
└── Test in game engine or viewer

Step 3: Baking
├── Duplicate mesh for high-poly
├── Sculpt detailed geometry
├── Transfer details with Normal Map
├── Bake ambient occlusion
├── Bake curvature map
└── Bake ID masks

Step 4: Texturing
├── Create albedo/diffuse map
├── Paint detail textures
├── Export texture sets
├── Configure PBR workflow
└── Test in viewport

Step 5: Export
├── FBX export with correct settings
├── Include materials (embedded or separate)
├── Apply transforms
├── Set up LODs
└── Package for delivery
```

### Animation Production Workflow

1. **Blocking**
   - Rough key poses
   - Blocking splines
   - Test timing
   - Get approval

2. **Splining**
   - Smooth keyframe curves
   - Refine timing
   - Add breakdowns
   - Polish motion

3. **Fine-tuning**
   - Finalize easing
   - Add secondary motion
   - Polish contacts
   - Check footwork

4. **Rendering**
   - Set up render engine
   - Configure output settings
   - Render passes
   - Batch render

## 8.3 Collaboration Workflow

### Team Project Structure

```
Project/
├── 01_Assets/
│   ├── Characters/
│   ├── Props/
│   └── Environments/
├── 02_Models/
│   ├── WIP/
│   └── Approved/
├── 03_Textures/
├── 04_Animations/
├── 05_Renders/
├── 06_References/
└── README.txt
```

### File Management Best Practices

1. **Naming Convention**
   - `asset_type_variant_version.blend`
   - `chair_wood_v01.blend`
   - `character_hero_v02.blend`

2. **Version Control**
   - Increment version on major changes
   - Keep last 3-5 versions
   - Archive approved versions separately
   - Use cloud storage (Blender Cloud, Google Drive)

3. **Linking vs Appending**
   - Link: Keep master library editable
   - Append: Make local copy for project
   - Use collections for organization

4. **Asset Library**
   - Set up Asset Browser library
   - Tag assets with metadata
   - Use consistent categorization
   - Enable auto-save for assets

### Review Workflow

```
Step 1: Render for Review
├── Set up render settings for review
├── Use lower samples for speed
├── Export as PNG or MP4
├── Add frame markers if needed
└── Export with filename including version

Step 2: Feedback Collection
├── Share via cloud link or file share
├── Collect written feedback
├── Mark specific frames/objects
├── Track revision notes
└── Prioritize changes

Step 3: Implementation
├── Duplicate file for new version
├── Make approved changes
├── Review internally first
├── Re-render for approval
└── Update version number
```
