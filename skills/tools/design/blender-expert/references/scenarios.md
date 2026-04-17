# Scenario Examples

## 9.1 Project Scenarios

### Scenario 1: Low-Poly Game Asset

**User:** "I need to create a low-poly tree for a mobile game. What poly count and workflow should I use?"

**Expert:**
> **Solution:**
> 
> **Poly Budget:**
> - Trunk: 100-200 triangles
> - Foliage: 300-500 triangles
> - Total: 500-800 triangles
> 
> **Workflow:**
> 1. **Trunk**
>    - Use cylinder with 6-8 vertices
>    - Apply displacement or vertex sculpting
>    - Export as separate mesh if used multiple times
> 
> 2. **Foliage**
>    - Create 3-4 planes with tree silhouette
>    - Assign to vertex group for wind animation
>    - Use alpha texture for soft edges
>    - Consider instancing multiple small planes
> 
> 3. **Material Setup**
>    - Use Principled BSDF
>    - Set Base Color from texture
>    - Enable Alpha Clip for foliage
>    - Keep shader simple for mobile performance
> 
> 4. **Export**
>    - FBX format for game engines
>    - Apply modifiers before export
>    - Include materials/textures
>    - Test in engine
> 
> **Key Tips:**
> - Mobile GPUs prefer fewer draw calls
> - Combine foliage planes into one mesh
> - Use LOD groups if supported
> - Test on target device early

---

### Scenario 2: Animated Product Turntable

**User:** "I need to create a 360° turntable animation of a product for our website."

**Expert:**
> **Solution:**
> 
> **Setup:**
> 1. Position product at origin
> 2. Create camera at eye level
> 3. Add empty at product center
> 4. Parent camera to empty (or use object offset)
> 
> **Animation Method 1: Object Rotation**
> ```
> - Rotate product 360° over 250 frames
> - Ease in/out for smooth acceleration
> - Camera stays stationary
> ```
> 
> **Animation Method 2: Camera Orbit**
> ```
> - Keep product stationary
> - Animate camera in circle
> - Use empty as orbit pivot
> - Better for showing all angles
> ```
> 
> **Render Settings:**
> - Output: PNG sequence (for flexibility)
> - Resolution: 1920x1920 (square for turntable)
> - Samples: 64-128 (Eevee) or 256 (Cycles)
> - Enable denoising
> - Output: PNG RGBA (transparent background)
> 
> **Post-Processing:**
> - Import into compositor
> - Add subtle vignette
> - Color correct
> - Export as GIF (looping) or MP4 (longer)
> 
> **Key Tips:**
> - Use 72 frames for smooth GIF (5 seconds at 15fps)
> - Pre-render preview in viewport first
> - Render passes for flexibility
> - Consider WebM for web (good compression)

---

### Scenario 3: Stylized Character for Animation

**User:** "I'm creating a stylized character for a short film. How should I approach the modeling and texturing?"

**Expert:**
> **Solution:**
> 
> **Modeling Approach:**
> 1. **Base Mesh**
>    - Start from sphere, block out proportions
>    - Use subdivision levels for smooth base
>    - Reference concept art with background images
> 
> 2. **Proportions**
>    - Exaggerate features (large eyes, small hands)
>    - Use squash and stretch principles
>    - Keep topology clean for animation
> 
> 3. **Details**
>    - Sculpt in Sculpt mode
>    - Use Dynamic Topology for organic shapes
>    - Add clothing as separate meshes
> 
> **Texturing Pipeline:**
> 1. **Hand-Painted Look**
>    - Use Texture Paint mode
>    - Paint colors directly in Blender
>    - Use brush with texture for painterly effect
> 
> 2. **Stylized PBR**
>    - Create clean texture bakes
>    - Use soft shadows and gradients
>    - Keep colors vibrant and saturated
> 
> 3. **Toon Shading**
>    - Use Shader to RGB node
>    - Add color ramp for hard edges
>    - Combine with rim lighting
> 
> **Rigging Tips:**
> - Keep limb joints simple
> - Add secondary rig for face
> - Use correct bone roll angles
> - Test with basic walk cycle

## 9.2 Client Deliverables

### Game Asset Package

| Item | Format | Specs |
|------|--------|-------|
| 3D Model | FBX, GLTF | Applied modifiers, Triangulated |
| Textures | PNG (TGA) | 1024x1024 to 4096x4096 |
| Normal Map | PNG | Tangent space |
| PBR Maps | PNG | Albedo, Roughness, Metallic |
| Animation | FBX | Baked keyframes |
| Documentation | PDF | Texture names, material settings |

### Print/Animation Package

| Item | Format | Specs |
|------|--------|-------|
| 3D Model | FBX, OBJ | High-poly or production mesh |
| Turntable | MP4, GIF | 1080x1080, 72-120 frames |
| Renders | PNG, TIFF | 4K+, transparent option |
| Wireframes | PNG | White background |
| Clay Render | PNG | Matte white material |
| Motion Background | MP4 | 4K, transparent |

### Archviz Package

| Item | Format | Specs |
|------|--------|-------|
| Scene File | BLEND | With packed textures |
| Exported Mesh | FBX | Full scene |
| Textures | PNG, EXR | 2K-4K |
| HDRI | EXR | For lighting reference |
| Final Renders | PNG | 4K per frame |
| Animation | MP4 | 30fps, h.264 |
| Turntable | MP4 | Multiple angles |

## 9.3 Automation

### Python Scripting Basics

**Batch Rename Objects:**
```python
import bpy

# Rename selected objects
for i, obj in enumerate(bpy.context.selected_objects):
    obj.name = f"Prop_{i:03d}"
```

**Batch Apply Modifiers:**
```python
import bpy

for obj in bpy.context.selected_objects:
    bpy.context.view_layer.objects.active = obj
    for mod in obj.modifiers:
        bpy.ops.object.modifier_apply(modifier=mod.name)
```

**Batch Export:**
```python
import bpy
import os

output_dir = "/path/to/export/"

for obj in bpy.context.selected_objects:
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.ops.export_scene.fbx(
        filepath=os.path.join(output_dir, f"{obj.name}.fbx"),
        use_selection=True
    )
```

### Geometry Nodes Automation

**Scatter Objects on Surface:**
```
1. Add Geometry Nodes modifier to ground plane
2. Add Distribute Points on Faces node
3. Add Instance on Points node
4. Connect collection of props
5. Adjust density with Random Value
6. Use Rotation and Scale for variation
```

**Procedural Building Generator:**
```
Nodes:
- Grid > Extrude Mesh > Set Material
- Random Value for floor heights
- Instance for windows/doors
- Combine with boolean operations
```

### Animation Automation

**Auto Keyframe Every 10 Frames:**
```python
import bpy

def auto_keyframe():
    scene = bpy.context.scene
    if scene.frame_current % 10 == 0:
        for obj in bpy.context.selected_objects:
            obj.keyframe_insert(data_path="location")
            obj.keyframe_insert(data_path="rotation_euler")

# Register in frame change handler
bpy.app.handlers.frame_change_pre.append(auto_keyframe)
```

### Render Farm Integration

**Command Line Rendering:**
```bash
# Render single frame
blender -b scene.blend -o //render/ -f 1

# Render animation
blender -b scene.blend -o //render/ -a

# Render range
blender -b scene.blend -s 1 -e 250 -a

# Use特定的 GPU
blender -b scene.blend --cycles-device CUDA -a
```

**Distributed Rendering:**
- Use Fan Thrasher for Cycles
- Configure worker nodes
- Set up network share for files
- Use EXR for float render passes
