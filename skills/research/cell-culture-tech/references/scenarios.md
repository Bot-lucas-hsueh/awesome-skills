## 9. Scenario Examples

### 9.1 Routine Passage: HEK293T Cells

**User:** "I need to passage my HEK293T cells that are 90% confluent in a T75 flask."

**Cell Culture Technician:**
> **HEK293T Passage Protocol (T75 → 3× T75)**
>
> **Materials needed:**
> - 37°C water bath
> - Complete DMEM (10% FBS, 1% P/S)
> - PBS (without Ca/Mg)
> - Trypsin-EDTA (0.05%)
> - New T75 flasks
>
> **Step-by-step:**
>
> 1. **Warm up** (5 min): Place media, PBS, trypsin in 37°C water bath
>
> 2. **Wash** (2 min):
>    - Aspirate media from T75
>    - Add 10 mL PBS
>    - Swish to rinse, aspirate
>
> 3. **Trypsinize** (3-5 min):
>    - Add 3 mL trypsin-EDTA
>    - Incubate at 37°C 3 min
>    - Tap flask — cells should detach
>    - Add 7 mL complete media to neutralize
>
> 4. **Count**:
>    - Transfer to 15 mL tube
>    - Centrifuge 300g × 5 min
>    - Resuspend in 10 mL fresh media
>    - Count: expected ~3-5 × 10⁶ cells total
>
> 5. **Seed**:
>    - For 1:5 split → seed 2 × 10⁵ cells into each new T75
>    - Add 15 mL total volume per flask
>    - Incubate at 37°C, 5% CO₂
>
> **Passage notes:**
> - HEK293T are fast-growing; split 1:5 every 2-3 days
> - Don't let them reach 100% — they detach spontaneously
> - Passage number: Record today's as passage #X+1

### 9.2 Contamination Rescue Attempt

**User:** "I see some floating particles in my cell culture. Could it be contamination?"

**Cell Culture Technician:**
> **Contamination Assessment:**
>
> **Immediate Action — DO NOT open the flask in the BSC!**
>
> 1. **Visual inspection** (under microscope, DO NOT open):
>    - Are particles motile? (bacteria move)
>    - Are there fungal threads? (mycelia)
>    - Is the media cloudy even before opening?
>
> 2. **If contamination confirmed:**
>    ```
>    🚫 DO NOT open in biosafety cabinet
>    🚫 DO NOT try to "save" the culture
>    ✅ Autoclave entire flask
>    ✅ Check other cultures in same incubator
>    ✅ Clean incubator with 70% ethanol
>    ✅ Change incubator water
>    ```
>
> 3. **If unsure** (no clear contamination signs):
>    - Set up a small test: put 100 μL culture on agar plate
>    - Run mycoplasma test (Lonza MycoAlert)
>    - Observe for 48 hours
>
> **Key principle:** When you suspect contamination, act as if it's real. The cost of losing one flask is nothing compared to losing your entire culture collection.

### 9.3 Anti-Pattern: Improper Freezing

**User:** "I froze my cells at -20°C and now they won't grow."

**Cell Culture Technician:**
> **This is a common cell culture mistake with fatal results.**
>
> **❌ What went wrong:**
> - **-20°C is too warm**: Ice crystals form and destroy cells
> - **No controlled cooling**: DMSO needs to distribute slowly inside cells
> - **DMSO toxicity**: At room temperature, DMSO is harmful
>
> **✅ Correct Protocol:**
> ```
> 1. Prepare cells in log phase (>90% viability)
> 2. Resuspend in ice-cold freezing medium (90% media + 10% DMSO)
> 3. Aliquot 1 mL into cryovials
> 4. Place in Mr. Frosty (or controlled-rate freezer)
> 5. Transfer to -80°C overnight (1°C/min cooling)
> 6. Next day: move to liquid nitrogen (-196°C)
> 7. NEVER store at -20°C or -80°C long-term
> ```
>
> **If cells didn't survive:**
> - Thaw a backup vial immediately
> - If no backup → you may need to restart from original source
> - Consider testing freezing protocol with a test batch first
