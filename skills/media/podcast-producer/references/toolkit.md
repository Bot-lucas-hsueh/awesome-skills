## § 6 · Professional Toolkit

### Recording & Production
- **Riverside.fm
- **Adobe Audition / Reaper
- **iZotope RX 10** — AI-powered audio restoration (noise reduction, de-reverb, de-click, dialogue isolation)
- **Auphonic** — Automated mastering and normalization to -16 LUFS broadcast standard
- **Descript** — Text-based audio/video editing; auto-transcription; filler word removal

### Distribution & Analytics
- **Transistor / Buzzsprout
- **Spotify for Podcasters (Anchor)** — Direct integration with Spotify audience
- **Chartable
- **Spotify Analytics** — Consumption rate, completion rate, audience demographics

### Monetization
- **Megaphone
- **Patreon
- **Gumroad

### Reference Standards
- **IAB Podcast Measurement Technical Guidelines v2.1** — Standardized download counting
- **Apple Podcasts Connect specs** — RSS requirements, artwork (3000×3000px, ≥72dpi, sRGB)
- **Spotify Technical Requirements** — Audio: MP3 or AAC, 96kbps minimum, 44.1 kHz
- **AES Loudness Standard** — -23 LUFS broadcast; podcast standard -16 LUFS integrated

## Phase 1: Pre-Production (1–2 weeks before recording)

**Guest Research Brief Template:**
```
GUEST: [Name, title, company]
EPISODE ANGLE: What is the specific story we're telling with this guest?
  NOT: "Let's talk about their career"
  YES: "The counterintuitive management lesson from scaling a remote team from 10 to 500"

BACKGROUND:
  - 3 most significant professional achievements (with quantification)
  - Recent news/content (articles, talks, LinkedIn posts from last 90 days)
  - Controversies or public positions that may come up
  - Previous podcast appearances: listen to 2 — what was covered? What was NOT asked?
  - Shared context with our audience: why does our listener care?

QUESTION DEVELOPMENT:
  Opening (builds rapport): Easy, gets them talking about their origin story
  Core (3–5 questions): The meat; go deeper with each question
  Insights (1–2): Counterintuitive or uncomfortable truth they're uniquely positioned to share
  Close: "What do you want our listeners to know that most people get wrong about X?"

WHAT NOT TO ASK: Questions they've answered identically in 5 other interviews
WHAT MUST BE ASKED: [The one question the audience absolutely needs answered]
```

**Recording Setup Checklist:**
```
□ Microphone: Dynamic mic (Shure SM7B, Rode PodMic) preferred for home studios; condenser for treated rooms
□ Interface: Focusrite Scarlett 2i2 (minimum); gain set to -12 to -18 dBFS speaking level
□ Headphones: Closed-back (Sony MDR-7506) — no earbuds that leak into mic
□ Acoustic treatment: Record in smallest room; closets with clothes work; avoid bathrooms/kitchens
□ Recording platform: Riverside.fm set to WAV, 48kHz, stereo — NOT Zoom (compressed audio)
□ Backup recording: Audacity or Voice Memo on separate device as redundant backup
□ Guest setup check: 15-min pre-call to test audio, video, internet; send setup guide 48h ahead
□ Do-not-disturb: Phone off; Slack/notifications off; "Recording" sign on door
□ Water: Glass (not bottle that makes noise) for host and guest
```

✓ Guest research brief completed 48 hours before recording
✓ Audio test call confirmed and issues resolved
✓ Recording backed up to cloud within 1 hour of session end
✗ Never start recording without confirming guest's local file is recording (Riverside has backup, but verify)

### Phase 2: Post-Production (2–5 days per episode)

**Editing Workflow:**
```
1. Ingest & organize (30 min) [✓] Done when: | [✗] FAIL if:
   - Download all audio tracks (host + guest separate tracks)
   - Name files: YYYY-MM-DD_GuestName_raw_host.wav
   - Create project folder structure: /raw /edit /final /assets

2. Rough cut (60–120 min) [✓] Done when: | [✗] FAIL if:
   - Remove: false starts, long silences (>3 sec), technical glitches, off-topic tangents
   - Keep: natural pauses, breathing (don't over-edit); genuine emotional moments
   - Mark chapter points with labels in DAW
   - Target: reach episode length target ±10%

3. Audio restoration (iZotope RX) (30–60 min) [✓] Done when: | [✗] FAIL if:
   - Dialogue Isolation: remove room reverb and HVAC noise
   - De-click: mouse clicks, mouth noise, plosives
   - De-noise: capture noise profile from silent section; reduce by 6–12 dB
   - De-breath (subtle — don't remove all breathing)

4. EQ & Compression (30 min) [✓] Done when: | [✗] FAIL if:
   - High-pass filter at 80–100 Hz (remove low rumble)
   - Presence boost at 2–5 kHz (voice clarity)
   - Compression: attack 10ms, release 100ms, ratio 3:1, -3 dB gain reduction in normal speech
   - Each voice separately; then bring together in mix

5. Normalization & Mastering (15 min — can use Auphonic) [✓] Done when: | [✗] FAIL if:
   - Target: -16 LUFS integrated (podcast standard)
   - Peak: -1 dBTP (true peak, not sample peak)
   - Noise floor check: < -60 dBFS in silent sections
   - Export: MP3 192 kbps

6. Quality check (15 min) [✓] Done when: | [✗] FAIL if:
   - Listen to first 5 minutes, 2 random 30-second spots, and last 2 minutes
   - Check loudness meter reads -16 LUFS
   - Verify no clipping (red on peak meter anywhere)
```

**Show Notes Template:**
```markdown
# [Episode Title — 60 chars max for SEO]

[2–3 sentence episode summary with primary keywords in first sentence]

## In This Episode
- [Timestamp] Key topic 1 (what listener will learn)
- [Timestamp] Key topic 2
- [Timestamp] Key topic 3

## Guest Bio
[1 paragraph; professional accomplishments + why they're on this show]

## Resources Mentioned
- [Guest's book/project with link]
- [Tool mentioned with link]
- [Study or article referenced with source]

## Connect With [Guest]
- LinkedIn: [URL]
- Twitter: [URL]
- Website: [URL]

## Transcript
[Searchable transcript — helps SEO and accessibility]
```

✓ Episode passes -16 LUFS
✓ Show notes include timestamps, guest bio, resources
✓ Transcript uploaded for accessibility and SEO
✗ Never publish without listening to full final export (catch metadata errors, silent sections)

### Phase 3: Distribution & Growth

**Platform Submission Checklist:**
```
□ RSS feed validated (Podbase.fm, Cast Feed Validator)
□ Episode artwork: 3000×3000 px, JPG/PNG, < 1MB, sRGB color space
□ Episode title: includes guest name and core topic keyword
□ Episode description: SEO-optimized, 200-500 words, includes key timestamps
□ Tags/categories: IAB content taxonomy (correct category for Apple/Spotify)
□ Explicit content rating set correctly
□ Publication date/time: Tuesday–Thursday 6 AM local time (peak discovery window)
□ Cross-promotion: social clips (60-sec audiogram via Headliner), email newsletter, LinkedIn
```

**Growth Analytics Framework:**
```python
PODCAST_KPIs = {
    'Downloads': {
        '7-day downloads': 'Primary industry benchmark; compare month-over-month',
        'IAB-certified': 'Use IAB v2.1 certified host; reject vanity metrics',
        'benchmark': '1,000 downloads/episode = top 20% of all podcasts (per Spotify/Apple data)',
    },
    'Completion Rate': {
        'target': '≥ 65% mean completion rate',
        'alarm': '< 50% → content issue or episode too long for audience',
        'tool': 'Spotify for Podcasters → Episode Performance → Completion Rate'
    },
    'Subscriber Growth': {
        'follow_rate': 'New followers per episode (Spotify = follows; Apple = subscriptions)',
        'target': '2–5% of listeners follow on first listen for new shows',
    },
    'Audience Retention Curve': {
        'drop_point_1': 'First 2 minutes: high drop if intro too long/no hook',
        'drop_point_2': 'Mid-episode sag (20-30 min): needs re-engagement moment',
        'action': 'If completion < 65%: tighten intro (≤90 sec to first main content), add chapter hooks'
    },
}
```

## 🔬 Scenario Examples

### 🚫 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Long Cold Intros ("Welcome to Episode 247 of...")
**Wrong:** "Hey everyone, welcome back to the show! I'm your host [Name], and on today's episode we're going to be talking about... but first a word from our sponsors... and if you're new here, make sure to subscribe... and we're so grateful to have reached 500 reviews..."
**Why it fails:** Listeners who clicked an episode did so for the content, not the intro ritual. 30+ seconds of house-keeping causes ~15% listener drop before the content begins.
**Correct:** Open with a hook — the most compelling thing the guest says, played as a cold open. Start main conversation within 90 seconds. Move sponsor reads to post-intro (minute 10–15 performs better than pre-roll for completion).

### Anti-Pattern 2: Recording on Zoom (Compressed Audio)
**Wrong:** Schedule guest interview as regular Zoom call; record cloud recording.
**Why it fails:** Zoom compresses audio dynamically (Opus codec, variable bitrate). Background noise, internet dropouts, and compression artifacts survive editing. Final audio sounds "Zoom-y" — a credibility signal to quality-conscious listeners.
**Correct:** Use Riverside.fm or SquadCast — record local .wav files on each participant's device; platform uploads in background. Results in broadcast-quality independent tracks even with bad internet.

### Anti-Pattern 3: Publishing Without Audio Mastering
**Wrong:** Export raw recording, normalize to -3 dBFS peak, upload to host.
**Why it fails:** -3 dBFS peak normalization ≠ -16 LUFS loudness. Result sounds much quieter or louder than other podcasts. Spotify auto-levels, but Apple and other platforms don't — listener has to manually adjust volume constantly.
**Correct:** Use Auphonic (free tier: 2 hours/month) or manual LUFS meter to target -16 LUFS integrated, -1 dBTP peak. Every episode at the same loudness level.

### Anti-Pattern 4: Asking Closed Questions
**Wrong:** "Did that experience change how you think about leadership?" (yes/no possible)
**Why it fails:** Guest can answer "yes" or "no" and stop. Interview stalls; host scrambles for follow-up; audio has dead air or awkward transitions.
**Correct:** Open questions: "How did that experience change your thinking about leadership?" or "Walk me through what you were feeling when that happened." "How," "What," "Walk me through," "Tell me about" — always open.

### Anti-Pattern 5: Treating Downloads as the Only Metric
**Wrong:** Optimize exclusively for download volume; judge all content decisions by downloads/episode.
**Why it fails:** Downloads are a vanity metric without context. 10,000 downloads with 30% completion rate = 3,000 episodes actually heard. 2,000 downloads with 75% completion rate = 1,500 fully heard episodes and likely far higher conversion to subscriber or customer.
**Correct:** Track the full funnel: Downloads × Completion Rate × Follow/Subscribe Rate × Conversion (email/trial/purchase). A smaller, highly engaged audience is worth 5× a large, shallow one for business outcomes.

