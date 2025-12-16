# AAA Workflow Skill

> **Orchestrator** - The complete "new client" journey through the AAA Framework

## Purpose
When a user says "I have a new client" or "run the AAA framework", this skill guides them through the complete Authority Acceleration journey.

## When to Use
- User says "new client", "start AAA", "run AAA", "begin AAA"
- User asks "where do I start with a new client?"
- User wants the FULL workflow overview
- User seems lost in which skill to use next

## The AAA Framework Overview

**AAA = Authority Acceleration Agency**

The framework has 4 phases:

```
STEP 0: CAPTURE (Deep Brand Intake)
    ↓
STEP 1: ANALYZE (Brand Foundation)
    ↓
STEP 2: ARCHITECT (Topics + Authority Positioning)
    ↓
STEP 3: ACTIVATE (Content Generation)
```

---

## Complete Workflow

### STEP 0: CAPTURE (Deep Brand Intake)
**Skill:** `/deep-brand-intake`
**Time:** 30-60 minutes
**Purpose:** Collect raw content samples BEFORE any analysis

**Process:**
1. Identify client's content sources:
   - Kit/ConvertKit emails? → `kit_email_extractor.py`
   - Podcast? → `podcast_transcript_extractor.py`
   - YouTube? → `youtube_transcript_extractor.py`
   - Blog? → Firecrawl scraping
   - Social media? → Export/manual collection

2. Extract content to `/clients/[name]/raw-content/`

3. Verify minimum viable dataset:
   - 10+ content pieces
   - 10,000+ words
   - 2+ content types

4. (Optional) Run Gemini Voice Synthesizer for large datasets:
   ```bash
   python tools/extraction/gemini_voice_synthesizer.py \
     --input-dir /clients/[name]/raw-content \
     --brand "[Client Name]"
   ```

**Output:**
- `/clients/[name]/raw-content/` - All collected content
- `/clients/[name]/source-inventory.md` - What was collected

**Next:** Move to STEP 1 when you have enough samples

---

### STEP 1: ANALYZE (Brand Foundation)
**Skills:** `/voice-dna`, `/disgust-mapper`, `/brand-discovery`
**Time:** 45-90 minutes total
**Purpose:** Create complete brand profile with voice patterns and boundaries

**Process:**

**1A. Voice DNA Analysis** (20-30 min)
- Skill: `/voice-dna`
- Input: 10-20 content samples from STEP 0
- Output: 5-layer Voice DNA Profile
  - Layer 1: Structural (sentence patterns)
  - Layer 2: Linguistic (word choices, phrases)
  - Layer 3: Tonal (emotional register)
  - Layer 4: Narrative (story patterns)
  - Layer 5: Ideological (beliefs, values)

**1B. Disgust Mapper** (10-15 min)
- Skill: `/disgust-mapper`
- Input: Quick mode (3 questions) or Full mode (10 questions)
- Output: Disgust boundaries with severity scores
  - What they would NEVER say
  - Topics to avoid
  - Tones that don't fit

**1C. Brand Discovery** (30-45 min)
- Skill: `/brand-discovery`
- Input: 39-question interactive interview OR extract from existing content
- Output: Complete Brand Profile Document
  - Positioning (who, what, how, why)
  - Audience deep dive
  - Content strategy foundations
  - Transformation journey

**Output:**
- `/clients/[name]/voice-dna-profile.md`
- `/clients/[name]/disgust-profile.md`
- `/clients/[name]/brand-profile.md`

**Next:** Move to STEP 2 with complete foundation

---

### STEP 2: ARCHITECT (Topics + Authority Positioning)
**Skills:** `/generate-topics`, `/authority-engine`, `/competitor-*`
**Time:** 30-60 minutes
**Purpose:** Create strategic topic library and competitive positioning

**Process:**

**2A. Authority Engine** (15-20 min)
- Skill: `/authority-engine`
- Input: Brand Profile from STEP 1
- Process:
  - Auto-extract niche from brand profile
  - STP Analysis (Segment → Target → Position)
  - Discover competitors via Perplexity
  - Generate perceptual map
- Output: Competitor list + positioning strategy

**2B. Competitor Analysis** (20-30 min, OPTIONAL)
Run if you want to learn from competitors:
- `/competitor-hooks` - Extract viral opening patterns
- `/competitor-structures` - Identify content formats that work
- `/competitor-topics` - Find high-engagement topic angles
- `/competitor-gaps` - Discover white space opportunities

**2C. Topic Generation** (10-15 min)
- Skill: `/generate-topics`
- Input: Brand Profile + Authority Engine output
- Output: 50-100 strategically positioned topics
  - Scored by impact + uniqueness + urgency
  - Mapped to ERISE buckets
  - Organized by theme

**Output:**
- `/clients/[name]/authority/competitors.csv`
- `/clients/[name]/authority/positioning-map.md`
- `/clients/[name]/topic-library.md`

**Next:** Move to STEP 3 to generate content

---

### STEP 3: ACTIVATE (Content Generation)
**Skills:** `/topic-to-matrix`, `/trust-*`
**Time:** Ongoing (per topic)
**Purpose:** Generate authentic, multi-platform content

**Process:**

**3A. Topic to Matrix** (5-10 min per topic)
- Skill: `/topic-to-matrix`
- Input: ONE topic from library + Brand Profile + Voice Meta
- Output: 1 topic → 19 pieces of content
  - 1 primary asset (long-form)
  - 3 Twitter threads
  - 5 single tweets
  - 2 LinkedIn posts
  - 3 Instagram posts
  - 1 Instagram carousel
  - 1 YouTube Short / TikTok
  - 2 email follow-ups

**3B. Trust Signals** (OPTIONAL - when data exists)
- Skill: `/trust-signal-generator`
- Purpose: Build E-E-A-T authority content
- ONLY USE IF CLIENT HAS DATA:
  - `/trust-case-studies` - IF real client results exist
  - `/trust-frameworks` - IF named methodology exists
  - `/trust-contrarian` - IF defensible unique POV exists
  - `/trust-metrics` - IF real data/numbers exist
  - `/trust-deep-dives` - IF deep expertise to expand
  - `/trust-provenance` - IF process to show behind-scenes

**Output:**
- `/clients/[name]/content/[topic-slug]/` - Generated content
- Content ready for editing and publishing

---

## Quick Reference Card

```
NEW CLIENT → CAPTURE → ANALYZE → ARCHITECT → ACTIVATE

STEP 0: CAPTURE
└── /deep-brand-intake (30-60 min)
    └── Output: raw-content/

STEP 1: ANALYZE
├── /voice-dna (20-30 min)
├── /disgust-mapper (10-15 min)
└── /brand-discovery (30-45 min)
    └── Output: voice + disgust + brand profiles

STEP 2: ARCHITECT
├── /authority-engine (15-20 min)
├── /competitor-* (optional)
└── /generate-topics (10-15 min)
    └── Output: topic library + positioning

STEP 3: ACTIVATE
├── /topic-to-matrix (per topic)
└── /trust-* (when data exists)
    └── Output: multi-platform content
```

---

## Decision Tree

```
"I have a new client [NAME]"
    │
    ├── Do you have content samples?
    │   ├── NO → Start with /deep-brand-intake
    │   └── YES → How many?
    │       ├── < 10 samples → /deep-brand-intake to collect more
    │       └── 10+ samples → Move to /voice-dna
    │
    ├── Do you have a brand profile?
    │   ├── NO → Run /brand-discovery
    │   └── YES → Move to /generate-topics
    │
    └── Do you need topics?
        ├── NO (have topics) → /topic-to-matrix
        └── YES → /generate-topics first
```

---

## The Math

Starting with ONE brand discovery session:
- 1 interview → 1 brand profile
- 1 brand profile → 100 topics
- 1 topic → 19 pieces of content
- **100 topics × 19 pieces = 1,900 pieces of content**

At 3 topics/week = **12+ months of content** from one session.

---

## Resources
- `resources/workflow-steps.md` - Detailed step-by-step guide
