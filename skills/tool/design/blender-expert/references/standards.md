# Standards & Reference

## 7.1 Official Documentation

- [Blender Manual](https://docs.blender.org/manual/en/latest/)
- [Blender API Documentation](https://docs.blender.org/api/current/)
- [Blender Cloud](https://cloud.blender.org)
- [Blender Studio](https://studio.blender.org)
- [Blender Developers Documentation](https://developer.blender.org)
- [Blender Guru Tutorials](https://www.blenderguru.com)

## 7.2 Keyboard Shortcuts & Configuration

### Essential Keyboard Shortcuts

| Action | Default Key |
|--------|-------------|
| Select Object | Right-click |
| Box Select | B |
| Circle Select | C |
| Lasso Select | Ctrl+Left-click |
| Select All | A |
| Deselect | Alt+A |
| Invert Selection | Ctrl+I |
| Move | G |
| Rotate | R |
| Scale | S |
| Grab/Move (X-axis) | G then X |
| Grab/Move (Y-axis) | G then Y |
| Grab/Move (Z-axis) | G then Z |
| Confirm Transform | Left-click or Enter |
| Cancel Transform | Right-click or Escape |
| Delete | X or Delete |
| Duplicate | Shift+D |
| Duplicate Linked | Alt+D |
| Add Object | Shift+A |
| Parent | Ctrl+P |
| Unparent | Alt+P |
| Join Objects | Ctrl+J |
| Separate | P |
| Set Origin | Ctrl+Shift+Alt+O |
| Search | F3 |
| Toolbar | T |
| Sidebar | N |
| Properties Panel | N (when in right panel) |
| Outliner | Shift+F9 |
| Properties | Shift+F7 |
| 3D Viewport | Shift+F5 |
| UV Editor | Shift+F10 |
| Shader Editor | Shift+F3 |
| Compositor | Shift+F11 |
| Render | F12 |
| Render Animation | Ctrl+F12 |
| Play Animation | Spacebar |
| Frame Step | Alt+Right/Left arrows |
| Jump to Keyframe | Up/Down arrows |
| Insert Keyframe | I |
| Clear Keyframe | Alt+I |
| Shade Smooth | Ctrl+F |
| Shade Flat | Ctrl+Shift+F |
| Loop Cut | Ctrl+R |
| Inset Faces | I |
| Extrude | E |
| Knife Tool | K |
| Bisect | B (in knife mode) |
| Bevel | Ctrl+B |
| Spin | Alt+R |
| Screw | (modifier) |
| Smooth Vertex | Ctrl+V |
| Decimate | (modifier) |
| Add Subdivision | Ctrl+1, 2, 3, 4 |
| Toggle Wireframe | Z (pie menu) |
| Toggle X-Ray | Alt+Z |
| Focus Selected | Numpad . |
| View All | Home |
| View Selected | Numpad . |
| Front View | Numpad 1 |
| Right View | Numpad 3 |
| Top View | Numpad 7 |
| Camera View | Numpad 0 |
| Orthographic View | Numpad 5 |
| Local/Global View | Numpad / |
| Toggle Quad View | Ctrl+Alt+Q |

### Workspace Configuration

#### Layout Workspaces
| Workspace | Purpose | Default Panels |
|-----------|---------|----------------|
| Layout | General 3D editing | 3D Viewport, Outliner, Properties |
| Modeling | Sculpt mode and hard surface | 3D Viewport, Tool Settings, Properties |
| Sculpting | Organic modeling | 3D Viewport, Brushes, Tool Settings |
| UV Editing | UV unwrapping | 3D Viewport, UV Editor |
| Texture Paint | 2D painting on 3D | 3D Viewport, Image Editor |
| Shading | Node-based materials | 3D Viewport, Shader Editor, Properties |
| Animation | Keyframing and rigging | 3D Viewport, Dope Sheet, Graph Editor |
| Rendering | Cycles/Eevee rendering | 3D Viewport, Compositor |
| Compositing | Post-processing | Node Editor (Compositor) |

#### Performance Settings
| Setting | Low-end | Mid-range | High-end |
|---------|---------|----------|----------|
| Viewport Samples | 16-32 | 64-128 | 256-512 |
| Render Samples | 128-256 | 512-1024 | 2048+ |
| Use GPU | Compute Off | Compute On | Compute On + RTX |
| Shadow Quality | Medium | High | Ultra |
| SSS | Off | On | On |

## 7.3 Common Tasks & Workflows

### Mesh Modeling
- **Primitives**: Shift+A > Mesh (Cube, Sphere, Cylinder, etc.)
- **Boolean**: Ctrl+Shift+Alt+C (Fast Carve add-on) or intersect/union/difference
- **Mirror Modifier**: Essential for symmetric modeling
- **Subsurface**: Ctrl+1-4 for subdivision levels
- **Bevel**: Ctrl+B for edge softening, customize segments

### Sculpting
- **Brushes**: Draw, Clay, Clay Strips, Grab, Snake Hook, Smooth, Fill/Deepen
- **Masks**: Ctrl+M to mask areas, Shift+X to smooth mask
- **Dyntopo**: Enable for dynamic topology during sculpting
- **Multiresolution**: For high-poly static meshes
- **Remesh**: After sculpting for cleaner topology

### UV Unwrapping
1. **Mark Seams**: Ctrl+E > Mark Seam, select edges
2. **Unwrap**: U > Unwrap or Smart UV Project
3. **Pack**: Ctrl+Shift+Alt+M to pack UV islands
4. **Check**: View > Toggle Sibling or checker pattern
5. **Export**: UV > Export UV Layout

### Materials & Shaders
- **Principled BSDF**: PBR base shader for most materials
- **Node Editor**: Shift+A to add nodes
- **Texture Coordinate**: Foundation for all texture mapping
- **Mapping**: Control scale and offset
- **Bump/Normal**: Add surface detail
- **Displacement**: For actual geometry displacement

### Rendering
| Engine | Use Case | Settings |
|--------|----------|----------|
| Eevee | Real-time, fast preview | Bloom, SSAO, ambient occlusion |
| Cycles | Photorealistic | Samples, denoising, light paths |
| Workbench | Modeling, baking | Color, matcap |

### Export Formats

| Format | Use Case | Key Settings |
|--------|----------|---------------|
| FBX | Game engines, Unity, Unreal | Selected Objects, Apply Scalings |
| glTF/GLB | Web, AR/VR | Include > Selected Objects, Apply Transform |
| OBJ | Universal compatibility | Wavefront OBJ settings |
| STL | 3D printing | ASCII/Binary, Scale |
| Alembic | Animation cache | Single Object, Frame Range |
| USD | Film pipeline | Primitives, Attributes |

## 7.4 Version Compatibility

| Version | Release | Key Features |
|---------|---------|--------------|
| 4.x | 2024 | Geometry Nodes improvements, EEVEE Next, Python 3.11 |
| 3.6 LTS | 2023 | Long-term support, stable API |
| 3.5 | 2023 | Geometry Nodes 2.0, shader improvements |
| 3.4 | 2022 | Asset Browser, improved shadows |
| 3.0 | 2022 | Overhaul, new nodes, Grease Pencil 3D |
| 2.93 LTS | 2021 | Final 2.x LTS release |

**Compatibility Notes:**
- 4.x files work with 3.6+ with minor conversion
- Older 2.7x files need manual migration
- Add-ons may require updates between major versions
- Always backup before upgrading

## 7.5 Performance Tips

### Viewport Performance
- **Reduce viewport samples**: 32-64 for modeling
- **Enable overlap**: Limit draw distance
- **Use X-Ray sparingly**: Only when needed
- **Hide objects**: H to hide, Alt+H to reveal
- **Simplify**: Scene > Simplify for lower poly view

### Render Optimization
- **Denoising**: Enable Denoise for fewer samples
- **Adaptive Sampling**: Stop when noise threshold reached
- **Light Linking**: Only illuminate what needs it
- **Instancing**: Use instanced geometry for repeated objects
- **Bake**: Bake shadows and normals when possible

### Tips
- Save incremental versions (file_v01.blend, v02.blend)
- Use append/link instead of duplicating scenes
- Pack external data for portable files
- Clear unused data (Outliner > Orphan Data)
- Use local collections to reduce scene complexity
