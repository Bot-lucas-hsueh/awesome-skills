## § 9 · Scenario Examples

### Scenario 1: Walk Cycle Feedback

**Context:**
Animator requests feedback on a character run cycle that feels "too floaty."

**User Input:**
"Review my character's run cycle — the body feels too floaty and lacks weight."

**Expert Response:**
**Key Observations:**

1. **Anticipation phase too short** → Add 2-3 frames of wind-up before forward motion; currently only 1 frame
2. **Vertical bounce insufficient** → Passing poses need more vertical displacement; aim for 1.5x current amplitude
3. **Arms not opposing** → Add counter-swing to match leg motion; left arm forward when right leg contacts
4. **Contact pose lacks "strike"** → Push silhouette further; extreme poses read better at distance
5. **Recovery too smooth** → Add settle/dampen after contact; real runs have impact absorption

**Frame-by-Frame Notes:**
- Frame 8: Anticipation peak — add more crouch
- Frame 12: Contact — push chest forward, snap pose
- Frame 24: Passing — highest point, show weight shift

---

### Scenario 2: Lip Sync Correction

**Context:**
Dialogue animation has timing misalignment with audio.

**User Input:**
"The character's mouth movements don't match the audio — some phonemes are late."

**Expert Response:**
**Diagnosis:**

| Issue | Frame Offset | Fix |
|-------|--------------|-----|
| /B/ /P/ onset | +3 frames | Move key earlier |
| /S/ /SH/ duration | +6 frames | Extend hold |
| /AO/ peak | +2 frames | Align with audio wave |

**Solution Steps:**
1. Use phoneme reference chart (23 shapes minimum)
2. Sync "closed" frames to audio silence/breathe points
3. Overlap adjacent phonemes by 1-2 frames for fluidity
4. Test with audio playing at 0.5x speed for precision

---

### Scenario 3: Action Blocking Approval

**Context:**
Director needs to approve animation blocking before spline phase.

**User Input:**
"Review the fight scene blocking — is the timing right before we proceed to spline?"

**Expert Response:**
**Blocking Assessment:**

| Pose | Timing | Clarity | Approval |
|------|--------|---------|----------|
| Punch wind-up | 12 frames | Clear wind-up | ✓ |
| Contact | 4 frames (too fast) | Too quick to read | Revise |
| Recovery | 8 frames | Good weight | ✓ |
| Dodge | 6 frames | Clear anticipation | ✓ |

**Recommendation:**
- Slow contact pose to 8 frames minimum
- Add 2-frame breakdown between wind-up and contact
- Approved for spline with noted revisions

---

### Scenario 4: Motion Graphics Style Frame Selection

**Context:**
Client needs to choose between style frame options for explainer video.

**User Input:**
"We have 3 style frames — which direction best fits our tech startup brand?"

**Expert Response:**
**Style Frame Analysis:**

| Frame | Strengths | Weaknesses | Best For |
|-------|-----------|------------|----------|
| A: Geometric | Modern, clean | Too minimal | B2B |
| B: Illustrated | Warm, friendly | Less scalable | Consumer |
| C: 3D Product | Premium, showcase | Higher render cost | Product demo |

**Recommendation:** Frame B — illustrated style aligns with "friendly innovation" brand positioning. Can evolve to include subtle 3D elements in Phase 2.

---
