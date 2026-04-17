# Scenario Examples

## 9.1 Game Project Scenarios

### FPS (First Person Shooter)
**User:** "How do I create an FPS controller in Godot?"

**Expert:**
> **FPS Controller Setup:**
>
> 1. Player scene structure:
>     ```
>     CharacterBody3D (Player)
>     ├── CollisionShape3D (Capsule)
>     ├── Camera3D (at head height)
>     │   └── GunModel (MeshInstance3D)
>     └── RayCast3D (for shooting)
>     ```
> 2. Movement script:
>     ```gdscript
>     extends CharacterBody3D
>     
>     const SPEED = 5.0
>     const JUMP_VELOCITY = 4.5
>     var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")
>     
>     func _physics_process(delta):
>         if not is_on_floor():
>             velocity.y -= gravity * delta
>         if Input.is_action_just_pressed("ui_accept") and is_on_floor():
>             velocity.y = JUMP_VELOCITY
>         var input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
>         velocity.x = input_dir.x * SPEED
>         velocity.z = input_dir.y * SPEED
>         move_and_slide()
>     ```
> 3. Mouse look:
>     ```gdscript
>     func _input(event):
>         if event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
>             rotation.y -= event.relative.x * sensitivity
>             $Camera3D.rotation.x -= event.relative.y * sensitivity
>             $Camera3D.rotation.x = clamp($Camera3D.rotation.x, -PI/2, PI/2)
>     ```

### RPG (Role Playing Game)
**User:** "How do I create a dialogue system?"

**Expert:**
> **Dialogue System Setup:**
>
> 1. Dialogue resource (CustomResource):
>     ```gdscript
>     # dialogue_resource.gd
>     class_name DialogueResource extends Resource
>     @export var lines: Array[DialogueLine]
>     
>     @export_class DialogueLine
>     @export var speaker: String
>     @export var text: String
>     @export var choices: Array[DialogueChoice]
>     @export var next_id: String
>     ```
> 2. Dialogue Manager (Autoload):
>     ```gdscript
>     # dialogue_manager.gd
>     extends Node
>     
>     var current_dialogue: DialogueResource
>     var current_line_index: int = 0
>     
>     func start_dialogue(resource: DialogueResource):
>         current_dialogue = resource
>         current_line_index = 0
>         show_current_line()
>     ```
> 3. UI integration:
>     - Label for speaker name
>     - Label for dialogue text
>     - VBoxContainer for choice buttons

### Platformer
**User:** "How do I create wall jumping and coyote time?"

**Expert:**
> **Platformer Setup:**
>
> 1. Coyote time:
>     ```gdscript
>     var coyote_timer: float = 0.0
>     const COYOTE_TIME = 0.15
>     
>     func _physics_process(delta):
>         if is_on_floor():
>             coyote_timer = COYOTE_TIME
>         else:
>             coyote_timer -= delta
>         
>         if Input.is_action_just_pressed("jump") and coyote_timer > 0:
>             velocity.y = jump_velocity
>             coyote_timer = 0
>     ```
> 2. Wall jump:
>     ```gdscript
>     var is_on_wall: bool = is_on_wall()
>     
>     if is_on_wall and not is_on_floor():
>         if Input.is_action_just_pressed("jump"):
>             velocity = Vector2(-sign(get_wall_normal().x), 1.0) * wall_jump_force
>     ```
> 3. Variable jump height:
>     ```gdscript
>     if Input.is_action_just_released("jump") and velocity.y < 0:
>         velocity.y *= 0.5  # Cut velocity for short jump
>     ```

## 9.2 Optimization Scenarios

### Draw Call Optimization
**User:** "How do I optimize rendering for mobile?"

**Expert:**
> **Mobile Rendering Optimization:**
>
> 1. Use Compatibility renderer:
>     - Project Settings -> Rendering -> Renderer -> Rendering Method = gl_compatibility
> 2. Reduce draw calls:
>     - Use MultiMeshInstance3D for repeated objects
>     - Use GPU particles instead of CPU particles
>     - Bake lighting (not real-time)
> 3. Texture optimization:
>     - Max texture size: 1024x1024
>     - Use compressed formats (VRAM compressed)
>     - Enable mipmaps for 3D
> 4. Reduce overdraw:
>     - Limit transparency layers
>     - Use simple geometry
>     - Disable MSAA on mobile

### LOD Implementation
**User:** "How do I implement LOD?"

**Expert:**
> **LOD Setup:**
>
> 1. Use VisibilityNotifier3D:
>     ```gdscript
>     extends MeshInstance3D
>     
>     var high_detail_mesh: Mesh
>     var low_detail_mesh: Mesh
>     
>     func _ready():
>         $VisibilityNotifier3D.connect("screen_exited", _on_screen_exited)
>         $VisibilityNotifier3D.connect("screen_entered", _on_screen_entered)
>     
>     func _on_screen_exited():
>         mesh = low_detail_mesh  # Replace with simpler mesh
>     
>     func _on_screen_entered():
>         mesh = high_detail_mesh
>     ```
> 2. Distance-based switching in _process:
>     ```gdscript
>     var dist = global_position.distance_to(get_viewport().get_camera_3d().global_position)
>     if dist < 20:
>         mesh = high_poly_mesh
>     elif dist < 50:
>         mesh = mid_poly_mesh
>     else:
>         mesh = low_poly_mesh
>     ```

### Memory Management
**User:** "How do I manage memory efficiently?"

**Expert:**
> **Memory Optimization:**
>
> 1. Resource preloading:
>     ```gdscript
>     # Preload commonly used resources
>     const BULLET = preload("res://scenes/bullet.tscn")
>     
>     func shoot():
>         var b = BULLET.instantiate()
>     ```
> 2. Unload unused resources:
>     ```gdscript
>     ResourceLoader.load(path)  # Don't use full path, use cached
>     # For unloading:
>     ResourceLoader.free_invalidation()
>     ```
> 3. Use Signal for loose coupling:
>     - Don't use get_node() for everything
>     - Emit signals for state changes

## 9.3 Multi-Platform Deployment

### HTML5/Web Export
**User:** "How do I export for web?"

**Expert:**
> **Web Export:**
>
> 1. Install export templates:
>     - Editor -> Manage Export Templates
>     - Download Web templates
> 2. Export settings:
>     - Project -> Export -> Add Web
>     - Export path: index.html
> 3. Web-specific settings:
>     - Extensions support (ETC2/ASTC)
>     - VRAM Texture Compression
> 4. Hosting:
>     - Itch.io: zip HTML5 export
>     - GitHub Pages: enable Git LFS
>     - Simmer.io: direct upload
> 5. Limitations:
>     - No threads in WebGL 1
>     - Limited memory (~2GB)
>     - No file system access

### Mobile Deployment
**User:** "How do I build for Android and iOS?"

**Expert:**
> **Mobile Export:**
>
> 1. Android:
>     - Install Android SDK (Java required)
>     - Configure keystore in export preset
>     - Use "Export With Debug" for testing
> 2. iOS:
>     - macOS required
>     - Configure signing identity
>     - Use Xcode to deploy to device
> 3. Touch input:
>     ```gdscript
>     func _input(event):
>         if event is InputEventScreenTouch:
>             handle_touch(event.position)
>         if event is InputEventScreenDrag:
>             handle_drag(event.position)
>     ```
> 4. Device profiling:
>     - Connect device via USB
>     - Use remote debug in Godot