# Scenario Examples

## 9.1 Game Project Scenarios

### FPS (First Person Shooter)
**User:** "How do I create an FPS controller with aiming?"

**Expert:**
> **FPS Controller Setup:**
>
> 1. Player object structure:
>    - Capsule collider (height 2m)
>    - Camera at Y: 1.6 (eye level)
>    - CharacterController component
> 2. Movement script:
>    ```csharp
>     float x = Input.GetAxis("Horizontal");
>     float z = Input.GetAxis("Vertical");
>     Vector3 move = transform.right * x + transform.forward * z;
>     controller.Move(move * speed * Time.deltaTime);
>     ```
> 3. Camera look:
>     ```csharp
>     float mouseX = Input.GetAxis("Mouse X") * sensitivity;
>     float mouseY = Input.GetAxis("Mouse Y") * sensitivity;
>     xRotation -= mouseY;
>     xRotation = Mathf.Clamp(-90f, 90f);
>     camera.localRotation = Quaternion.Euler(xRotation, 0, 0);
>     transform.Rotate(Vector3.up * mouseX);
>     ```
> 4. Aiming:
>     - Use Cinemachine Virtual Camera
>     - Adjust FOV (60 -> 40 on aim)
>     - Animate weapon position

### RPG (Role Playing Game)
**User:** "How do I implement a dialogue system?"

**Expert:**
> **Dialogue System Setup:**
>
> 1. Data structure:
>     ```csharp
>     [System.Serializable]
>     public class DialogueNode {
>         public string id;
>         public string text;
>         public string speakerName;
>         public List<DialogueChoice> choices;
>         public string nextNodeId;
>     }
>     ```
> 2. Dialogue Manager (singleton):
>     - Display current node text
>     - Generate choice buttons
>     - Handle node transitions
> 3. Integration with inventory:
>     - Check conditions: `if (inventory.HasItem("key"))`
>     - Use ScriptableObject for quest flags

### Platformer
**User:** "How do I create a double jump system?"

**Expert:**
> **Platformer Setup:**
>
> 1. CharacterController setup:
>     - Center (0, 1, 0), Height 2
>     - Slope limit: 45
>     - Step offset: 0.3
> 2. Jump logic:
>     ```csharp
>     bool canDoubleJump = false;
>     int jumpCount = 0;
>     
>     void Update() {
>         if (isGrounded) jumpCount = 0;
>         if (Input.GetButtonDown("Jump")) {
>             if (isGrounded) {
>                 velocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);
>             } else if (jumpCount < maxJumps) {
>                 velocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);
>                 jumpCount++;
>             }
>         }
>     }
>     ```
> 3. Ground check:
>     - Physics.CheckSphere at feet
>     - Use LayerMask for ground detection

## 9.2 Optimization Scenarios

### Draw Call Batching
**User:** "How do I reduce draw calls for mobile?"

**Expert:**
> **Draw Call Optimization:**
>
> 1. Static batching:
>     - Mark non-moving objects as "Static"
>     - Use Batching static on MeshRenderer
> 2. GPU instancing:
>     - Enable "Enable GPU Instancing" on materials
>     - Works for identical meshes with different transforms
> 3. Texture atlases:
>     - Use Sprite Atlas (Window -> 2D -> Sprite Atlas)
>     - Pack all UI sprites into one atlas
>     - Enable "Allow Rotation", "Tight Packing"
> 4. Material consolidation:
>     - Share materials between similar objects
>     - Use material property blocks for variations
> 5. UI optimization:
>     - Use RectTransform2D elements sparingly
>     - Canvas "Screen Space - Overlay" is fastest

### Memory Management
**User:** "How do I handle memory efficiently?"

**Expert:**
> **Memory Optimization:**
>
> 1. Object pooling:
>     ```csharp
>     public class ObjectPool : MonoBehaviour {
>         public GameObject prefab;
>         public int poolSize = 20;
>         private Queue<GameObject> pool;
>         
>         void Start() {
>             pool = new Queue<GameObject>();
>             for (int i = 0; i < poolSize; i++) {
>                 GameObject obj = Instantiate(prefab);
>                 obj.SetActive(false);
>                 pool.Enqueue(obj);
>             }
>         }
>         
>         public GameObject Get() {
>             GameObject obj = pool.Dequeue();
>             obj.SetActive(true);
>             pool.Enqueue(obj);
>             return obj;
>         }
>     }
>     ```
> 2. Addressables:
>     - Use Addressables.LoadAssetAsync
>     - Release with Addressables.Release()
> 3. Texture streaming:
>     - Enable "Streaming Mip Maps"
>     - Set max loading for budget

### LOD (Level of Detail)
**User:** "How do I implement LOD for performance?"

**Expert:**
> **LOD Setup:**
>
> 1. Create LOD Group:
>     - Right-click in Hierarchy -> LOD Group
>     - Add LOD levels (0-3 typically)
> 2. Configure:
>     - LOD 0: Distance 0-15 (High quality)
>     - LOD 1: Distance 15-30 (Medium)
>     - LOD 2: Distance 30-60 (Low)
>     - LOD 3: Distance 60+ (Very low)
> 3. For character meshes:
>     - Use 3D modeling software to create lower poly versions
>     - Import all LODs in single FBX

## 9.3 Multi-Platform Deployment

### Mobile Multi-Platform
**User:** "How do I handle input across devices?"

**Expert:**
> **Cross-Platform Input:**
>
> 1. New Input System (recommended):
>     - Package Manager -> Input System
>     - Create Input Actions (keyboard, touch, gamepad)
>     - Use "PlayerInput" component
> 2. Touch handling:
>     ```csharp
>     if (Input.touchCount > 0) {
>         Touch touch = Input.GetTouch(0);
>         // Handle touch phase
>     }
>     ```
> 3. Platform detection:
>     ```csharp
>     #if UNITY_ANDROID
>     #elif UNITY_IOS
>     #elif UNITY_STANDALONE
>     #endif
>     ```
> 4. Resolution handling:
>     - Camera.main.rect for split-screen
>     - Screen.SetResolution for custom resolutions

### Console Development
**User:** "What's required for PlayStation and Xbox?"

**Expert:**
> **Console Development:**
>
> 1. Requirements:
>     - Unity Pro license
>     - Platform-specific SDK
>     - Developer membership (Sony, Microsoft)
> 2. Project setup:
>     - Install platform module from Unity Hub
>     - Configure target platform in Build Settings
> 3. Optimization:
>     - Use IL2CPP (required for consoles)
>     - Set API Compatibility Level: .NET Framework
>     - Optimize for memory constraints
> 4. Certification:
>     - Follow platform-specific requirements
>     - Use Tracked Performance Marker API
>     - Test on dev kit before submission