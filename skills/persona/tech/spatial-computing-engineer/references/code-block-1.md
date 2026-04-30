# csharp Example

```
// PROBLEM 1: UI Canvas in WorldSpace with no batching
// ❌ BAD — Every UI element = separate draw call
Canvas menuCanvas = GetComponent<Canvas>();
menuCanvas.renderMode = RenderMode.WorldSpace;
// Each Text, Image = separate DC → 40+ draw calls for a menu

// ✅ GOOD — Use TextMeshPro with SDF atlas, batch static elements
// Set Canvas "Additional Shader Channels" to TexCoord1
// Enable "Dynamic Batching" in XR Plugin settings
menuCanvas.pixelPerfect = false; // required for batching

// PROBLEM 2: Enabling particle systems or shadows on open
// ❌ BAD
void OpenMenu() {
    menuObject.SetActive(true); // triggers Awake, Start, full rebake
}

// ✅ GOOD — Pre-warm the menu, use alpha fade instead
void Start() {
    menuObject.SetActive(true);  // pre-warm
    SetMenuAlpha(0f);            // invisible but ready
}
void OpenMenu() {
    StartCoroutine(FadeMenu(0f, 1f, 0.15f)); // 150ms fade = smooth
}

// PROBLEM 3: Hand tracking mesh is too high-poly
// Quest 3 hand mesh: 1,438 triangles (system) — don't add custom high-poly hand viz
// If you added custom hand visualization, check poly count
Debug.Log("Hand vertices: " + handMesh.vertexCount); // should be <2K
```
