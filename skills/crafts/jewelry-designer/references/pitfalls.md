# Jewelry Design — Real-World Scenarios

## Scenario 1: Engagement Ring — Diamond Selection with Budget Constraint

**Context:** Client wants an engagement ring with a 1.5ct+ center diamond. Budget: $8,000 total (including setting). GIA certified required.

**Analysis:**
```yaml
Budget Allocation:
  - Setting (14K white gold, solitaire, quality prongs): $1,500
  - Center stone: $6,500
  - Remaining: $0 (all budget used)

Diamond Trade-offs at $6,500 for 1.5ct:
  Option A: 1.52ct G VS2 Excellent cut = $6,400
    - G color: Near-colorless (slight warmth vs. D-F)
    - VS2: Eye-clean in most lighting
    - Excellent cut: Maximum brilliance
  
  Option B: 1.50ct H VS1 Excellent cut = $6,500
    - H color: Near-colorless (noticeable in side view)
    - VS1: Eye-clean always
    - Excellent cut: Maximum brilliance

Recommendation: Option A (G/VS2)
  - G color: Clean to naked eye, significant savings vs. D
  - VS2: Eye-clean in most settings
  - 1.52ct: Slightly above 1.5ct threshold
  - Leave $100 for engraving
```

**Why not Option C (D/VS1)?**
```yaml
Option C: 1.51ct D VS1 = $7,800 (over budget)
Option D: 1.50ct G SI1 = $5,200 (save $1,300 but inclusion risk)
```

---

## Scenario 2: Custom Bridal Set — CAD Design Approval Workflow

**Context:** Client wants a custom three-stone engagement ring with wedding band. Budget: $12,000. Must be delivered in 6 weeks.

**Workflow:**
```yaml
Week 1: Design Consultation
  - Discuss: Three-stone, pear side stones, yellow gold
  - Collect: Inspiration images, budget confirmation
  - Output: Written design brief with sketch

Week 2: CAD Design Phase
  - Create 3D CAD model (RhinoGold)
  - Email renderings to client (3 angles)
  - Client requests: Make side stones larger
  - Revision: Updated CAD + new renderings

Week 3: Approval & Wax
  - Client approves CAD via email confirmation
  - Print wax model
  - Client views wax model in person or via video
  - Approve for casting

Week 4: Casting & Assembly
  - Cast in 14K yellow gold
  - Polish, assemble, set center stone
  - QC inspection

Week 5: Stone Setting & Finishing
  - Set pear side stones
  - Final polish, rhodium plating
  - Quality inspection with loupe

Week 6: Delivery
  - Present with ring box
  - Provide: GIA cert, appraisal, care instructions
  - Capture client photo/testimonial
```

**Potential Delays & Mitigation:**
```yaml
- CAD revisions: Built in 1 revision round (Week 2)
- Stone sourcing: Pre-ordered 3-stone combination
- Setting complexity: Wax model shows exact outcome
```

---

## Scenario 3: Jewelry Repair — Family Heirloom Ring Re-sizing

**Context:** Client brings in grandmother's 18K yellow gold engagement ring. Needs to be sized from size 5 to size 7.5. Contains 0.8ct center stone with side diamonds.

**Assessment:**
```yaml
Condition Check:
  - Prongs: Worn but functional
  - Setting: Solitaire with 6 prongs
  - Stones: Secure, no movement
  - Band: Light wear, no cracks

Sizing Method:
  - Size increase: Cut and add metal (requires adding ~4mm gold)
  - Match color/finish exactly
  - Sizing bead alternative rejected (changes profile)

Special Considerations:
  - Prong tips near size change point — check security
  - Diamonds near shank: May need to remove temporarily
  - Polishing after sizing: May expose old scratches

Process:
  1. Photograph and document condition
  2. Remove center stone (protect)
  3. Cut shank at bottom
  4. Add matching 18K yellow gold
  5. Solder and polish
  6. Re-set center stone
  7. Re-finish and polish
  8. Final QC

Cost: $350 (includes stone removal/re-set)
Timeline: 5-7 business days
```

---

## Scenario 4: Ethical Sourcing — Lab-Grown vs. Natural Diamond Decision

**Context:** Client is price-conscious but wants a 2ct diamond. Comparing lab-grown vs. natural at same quality.

**Comparison:**
```yaml
2.00ct E VS1 Excellent Cut:

Natural Diamond:
  - Price: $18,000-25,000
  - Investment value: Retains some resale value
  - Rarity: Genuinely rare
  - Emotional value: "Real" diamond (though lab is identical)

Lab-Grown Diamond (CVD):
  - Price: $3,500-5,000
  - Investment value: Minimal resale value
  - Rarity: Increasingly common
  - Environmental: Lower impact (energy-dependent)

Recommendation Depends on Client Values:
  - Budget priority: Lab-grown wins
  - Traditional value: Natural wins
  - Environmental concern: Lab-grown wins
  - Resale/inheritance: Natural wins
```

**Disclosure Requirement:**
```yaml
Always disclose lab-grown clearly:
  - GIA reports for lab-grown include "Laboratory-Grown" notation
  - All sales materials must state lab-grown
  - No misrepresentation allowed
  - Client must be informed before purchase
```

---

## Scenario 5: Colored Stone — Emerald Selection and Treatment Disclosure

**Context:** Client wants an emerald engagement ring. Budget: $5,000. Must understand treatments.

**Selection:**
```yaml
Options at $5,000:

Colombian Emerald (0.8ct):
  - Origin: Colombia (premium origin)
  - Color: Vivid green with slight blue modifier
  - Clarity: Moderate inclusions (jardin visible)
  - Treatment: Standard oil (standard, accepted)
  - Price: $4,500-5,500

Zambian Emerald (1.0ct):
  - Origin: Zambia (modern mine)
  - Color: Deep green, sometimes slightly dark
  - Clarity: Slightly cleaner than Colombian
  - Treatment: Standard oil
  - Price: $3,500-4,500

Lab-Grown Emerald (1.5ct):
  - Price: $800-1,200
  - Visually identical without inclusions
  - Disclosure required

Recommendation: Colombian 0.8ct
  - Superior color
  - Characteristic inclusions prove natural
  - Fits budget with setting included
```

**Treatment Disclosure:**
```yaml
Standard Emeralds:
  - Oil treatment is standard and accepted
  - Resin filling requires disclosure (heavily treated)
  - GIA report will note treatment type

Categories:
  - No treatment (N): Very rare, expensive
  - Minor oil: F1 (acceptable)
  - Moderate oil: F2 (acceptable if disclosed)
  - Heavily filled: F3 (controversial, lower value)
```

---

## Scenario 6: Manufacturing Quality Control — Preventing Casting Defects

**Context:** A jewelry manufacturer experiences 15% return rate due to porosity in PT950 castings.

**Root Cause Analysis:**
```yaml
Defect Type: Micro-porosity (invisible to eye, shows as weakness)
Rate: 15% of platinum castings
Cost: $2,000/week in remakes

Process Audit:
  - Metal supplier: Checked (pure Pt950, no issues)
  - Investment type: Standard phosphate-bonded
  - Burnout cycle: 800°C for 12 hours (may be insufficient)
  - Casting temperature: 1,770°C (slightly low)
  - Cooling: Air cool in flask (may be too fast)

Solutions:
  1. Extend burnout to 16 hours at 900°C
  2. Increase casting temperature to 1,800°C
  3. Add vacuum assist to casting machine
  4. Slow cool by burying in vermiculite
  5. Add porosity inspection (X-ray) before finishing

Expected Result: Reduce defects to <3%
```

---

## Scenario 7: Client Communication — Breaking Bad News About Stone Quality

**Context:** Client purchased an "eye-clean" SI1 diamond from an online vendor. The stone has a visible black inclusion under the table.

**Approach:**
```yaml
Step 1: Receive client with empathy
  - "I understand you're concerned about your ring"
  - Listen to their description of the issue

Step 2: Examine stone objectively
  - View under loupe, note exact inclusion location
  - Diamond may actually be SI2 (not SI1)
  - GIA grading may have been optimistic

Step 3: Present findings honestly
  - Show client the inclusion through loupe
  - Explain: "The inclusion is in a location that catches light differently than typical SI1"
  - GIA grades are based on face-up appearance under controlled lighting

Step 4: Present options
  - If stone is misgraded: Return to vendor for replacement (under GIA guarantee)
  - If within grading tolerance: Discuss whether client can accept the stone
  - Alternative: Work with client's budget to source a cleaner stone

Step 5: Document everything
  - Written notes on conversation
  - Photos of inclusion if stone is exchanged
```

---

## Scenario 8: Wedding Band — Matching Client's Engagement Ring

**Context:** Client has an engagement ring with a unique finish (hammered texture, hand-engraved pattern). Needs a wedding band to match.

**Matching Process:**
```yaml
Challenge: Hand-made finishes are difficult to exactly match

Option 1: Commission same artisan
  - Send engagement ring to maker
  - Match finish in production
  - Cost: $800-1,200 for matching band
  - Timeline: 4-6 weeks

Option 2: Machine-made band + hand-finish
  - Start with polished plain band
  - Apply hand-finishing to match (hammered texture)
  - Cost: $400-600 for matching band
  - Risk: May not perfectly match

Option 3: Contoured band (Chevron)
  - Shaped to nest against engagement ring
  - Match metal type and karat only
  - Cost: $500-800
  - Risk: May not touch perfectly along entire length

Recommendation: Option 1
  - Client chose unique engagement ring for uniqueness
  - Matching band should share that uniqueness
  - Send ring to maker for exact matching
```

---

## Scenario 9: Appraising Estate Jewelry for Insurance

**Context:** Client brings in grandmother's antique diamond brooch. Needs insurance appraisal.

**Appraisal Process:**
```yaml
Step 1: Identification
  - Determine: Authentic period piece vs. later reproduction
  - Examine: Construction methods, hallmark, wear patterns
  - Date approximately: 1920s Art Deco based on platinum work and design

Step 2: Stone Assessment
  - Total weight of center and accent stones: 2.8ct
  - Center: Old European cut, estimated G/H color, VS1/VS2 clarity
  - Note: Old cuts have different proportions (shallower, more fire)
  - Natural light behavior differs from modern brilliant cuts

Step 3: Market Research
  - Comparable sales: Similar Art Deco brooches sold $3,500-7,500
  - Current material cost: Gold + diamonds = $2,800
  - Replacement value (insurance): $5,500

Step 4: Documentation
  - Detailed description with photos
  - GIA grading of center stone (if feasible without damage)
  - Market comparables cited
  - Statement of authenticity and condition
  - Replacement value: $5,500
  - Effective date: Today's date
  - Valid for: 2-3 years (update for market changes)

Step 5: Client Education
  - Insurance appraisal ≠ liquidation value
  - Need updated appraisal every 3 years
  - Keep appraisal with insurance documents
  - Provide copy to insurance company
```
