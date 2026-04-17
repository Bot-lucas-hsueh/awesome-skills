# Scenario Examples

## 9.1 Game Project Scenarios

### FPS (First Person Shooter)
**User:** "How do I set up a basic FPS game with weapon switching?"

**Expert:**
> **FPS Setup:**
>
> 1. Use "First Person" template as starting point
> 2. Character setup:
>    - Skeletal mesh with FPS arms (hidden body)
>    - Camera component at eye height (170cm)
>    - Add weapon socket on WeaponHolder bone
> 3. Weapon system:
>    - Create Weapon Blueprint (Actor)
>    - Implement Fire() function with Trace queries
>    - Use AnimNotify for muzzle flash/sound
>    - Use Montages for reload animations
> 4. Weapon switching:
>    - Store weapons in array on Character
>    - Use Equip() function with Blend poses by enum
>    - Attach to weapon socket with AttachToComponent
>
> ```cpp
> // C++ weapon spawning
> FActorSpawnParameters SpawnParams;
> SpawnParams.Owner = this;
> AWeapon* NewWeapon = GetWorld()->SpawnActor<AWeapon>(WeaponClass, SpawnParams);
> NewWeapon->AttachToComponent(GetMesh(), FAttachmentTransformRules::SnapToTargetIncludingScale, "WeaponSocket");
> ```

### RPG (Role Playing Game)
**User:** "How do I implement an inventory system with item pickup?"

**Expert:**
> **RPG Inventory Setup:**
>
> 1. Data Asset for items:
>    - Create UDataAsset subclass (UItemData)
>    - Properties: Name, Description, Icon, ItemType, StackSize, Stats
> 2. Inventory component:
>    - Add UActorComponent (UInventoryComponent)
>    - Use TArray<FInventorySlot> for storage
>    - Implement AddItem(), RemoveItem(), FindItem()
> 3. Item pickup:
>    - Create pickup actor (APickupItem)
>    - On overlap -> Call InventoryComponent->AddItem()
>    - Destroy actor on pickup
> 4. UI integration:
>    - Create UMG Widget for inventory
>    - Bind to InventoryComponent OnInventoryUpdated delegate

### Platformer
**User:** "How do I create a character movement system with double jump?"

**Expert:**
> **Platformer Setup:**
>
> 1. Character movement component:
>    - Set DefaultGravityScale: 2.0
>    - Set JumpZVelocity: 1000
>    - Enable CanJump override
> 2. Double jump implementation:
>    - Track jump count with int32 JumpCount
>    - MaxJumps = 2
>    - On Jump() check: if (JumpCount < MaxJumps)
>    - Reset JumpCount on Landed() callback
> 3. Wall jump (optional):
>    - Detect wall in CheckJump()
>    - Apply launch velocity away from wall
>    - Disable input briefly during wall jump

## 9.2 Optimization Scenarios

### LOD (Level of Detail)
**User:** "How do I set up LOD for my character models?"

**Expert:**
> **LOD Setup:**
>
> 1. Import model with LODs or create in DCC:
>    - LOD0: High poly (10k+ tris)
>    - LOD1: Medium (5k tris)
>    - LOD2: Low (2k tris)
>    - LOD3: Ultra low (500 tris)
> 2. Configure in Mesh Editor:
>    - Select LOD Settings tab
>    - Set Auto Compute LOD Distances
>    - Percent of Screen Size: 100%, 50%, 25%, 12.5%
> 3. Materials:
>    - Reduce complexity on lower LODs
>    - Disable expensive effects on LOD1+

### Occlusion Culling
**User:** "What's the best approach for occlusion in open-world games?"

**Expert:**
> **Occlusion Strategies:**
>
> 1. Built-in occlusion:
>    - Hierarchical View Frustum (HVF) culling
>    - Distance culling per actor
>    - Precomputed visibility volumes
> 2. For open worlds:
>    - Use World Partition with streaming
>    - Implement custom occlusion with occlusion queries
>    - Use Chaos physics for complex scenes
> 3. Enable in Project Settings:
>    - Rendering -> Occlusion Culling
>    - Pixel Cost threshold: 0.5
>    - Single Point Occlusion: True
> 4. Debug:
>    - `stat unit` to see draw call breakdown
>    - `vis` console command for visibility

### Draw Call Batching
**User:** "How do I reduce draw calls for mobile?"

**Expert:**
> **Mobile Draw Call Optimization:**
>
> 1. Static batching:
>    - Mark static meshes as "Static" not "Movable"
>    - Use "Enable Static Lighting" for batching
> 2. Material consolidation:
>    - Use Material Instances with parameter overrides
>    - Share materials across similar objects
>    - Enable "Instanced Stereo" for VR
> 3. Mesh merging:
>    - Use "Merge Actors" tool
>    - Combine related props into single mesh
> 4. Project Settings:
>    - Mobile -> Support Hardware Ray Tracing: Off
>    - Mobile -> Multi-view rendering: On
>    - Mobile -> HDR: Off (for older devices)

## 9.3 Multi-Platform Deployment

### Mobile Deployment
**User:** "How do I build for iOS and Android from one project?"

**Expert:**
> **Mobile Multi-Platform:**
>
> 1. Platform-specific settings:
>    - iOS: Configure signing certificate + provisioning
>    - Android: Configure keystore + package name
> 2. Adaptive quality:
>    - Detect device capability at runtime
>    - Adjust scalability groups
>    - Quality settings: Low/Medium/High presets
> 3. Input handling:
>    - Use Enhanced Input System
>    - Create Input Actions (Touch, Gesture, Gyro)
>    - Map to same Input Triggers for all platforms
> 4. Platform-specific code:
>    - Use `#if PLATFORM_IOS` and `#if PLATFORM_ANDROID`
>    - Use `ISensorInterface` for touch/input abstraction

### Console Deployment
**User:** "What's required for PlayStation and Xbox?"

**Expert:**
> **Console Development:**
>
> 1. Requirements:
>    - Registered developer with Sony/Microsoft
>    - DevKit hardware
>    - Platform SDK installed
> 2. Project configuration:
>    - Target hardware: PlayStation 5 / Xbox Series X
>    - Memory budget: ~8GB for game
>    - Frame rate: 30fps or 60fps target
> 3. Optimization:
>    - GPU scarcity is primary constraint
>    - Use State Cache for shader precompilation
>    - Memory: Use pool allocators
> 4. Certification:
>    - Both platforms require cert testing
>    - Follow Sony's "Technical Requirements Checklist"
>    - Follow Microsoft's "Xbox Requirements Document"