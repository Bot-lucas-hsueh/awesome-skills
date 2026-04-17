## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Uncanny Valley** | 🔴 High | Halfway-realistic characters appear eerie; avoid "almost human" unless intentional horror | Use stylized proportions or go fully realistic |
| **Motion Blur Artifacts** | 🔴 High | Incorrect motion blur settings create flickering or ghosting in render | Verify motion blur samples match frame rate |
| **Broken Silhouette** | 🔴 High | Joints invisible in certain poses → animation reads poorly at distance | Test silhouettes at multiple angles; adjust rig |
| **Sync Errors** | 🟡 Medium | Lip sync misaligned with audio → breaks immersion, especially in dialogue | Use correct phoneme set; test with audio playback |
| **Frame Rate Mismatch** | 🟡 Medium | Animation created at wrong frame rate looks wrong on delivery | Confirm delivery frame rate early; test playback |
| **Rendering Too Slow** | 🟡 Medium | Overly complex effects or high-res renders miss deadlines | Plan render times early; use preview/test renders |

**⚠️ IMPORTANT
- Animation techniques vary by software (Maya, Blender, After Effects, Toon Boom). Recommendations should be adapted to the available tools.

- Always back up work and use version control. Animation is labor-intensive and losses are catastrophic.

---
