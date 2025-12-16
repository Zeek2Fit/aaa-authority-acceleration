# AAA Workflow - Detailed Steps

## Pre-Flight Checklist

Before starting with a new client:

- [ ] Client name and business confirmed
- [ ] Access to client's content sources identified
- [ ] Client folder created: `/clients/[client-name]/`
- [ ] Client available for interview (for brand discovery)

---

## STEP 0: CAPTURE (Deep Brand Intake)

### 0.1 Create Client Folder
```bash
mkdir -p /clients/[client-name]/raw-content/{emails,transcripts,posts,social}
```

### 0.2 Identify Content Sources

Ask client:
1. "Do you send email newsletters?" → Which platform?
2. "Do you have a podcast?" → Where hosted?
3. "Do you have a YouTube channel?" → Channel URL?
4. "Do you write blog posts?" → Website URL?
5. "Are you active on social media?" → Which platforms?

### 0.3 Extract Content

**For each YES answer, extract:**

| Source | Tool | Command |
|--------|------|---------|
| Kit emails | kit_email_extractor.py | `python tools/extraction/kit_email_extractor.py <url>` |
| Podcasts | podcast_transcript_extractor.py | `python tools/extraction/podcast_transcript_extractor.py <rss>` |
| YouTube | youtube_transcript_extractor.py | `python tools/extraction/youtube_transcript_extractor.py <url>` |
| Blog | Firecrawl MCP | `firecrawl_crawl: {url, limit: 20}` |
| Twitter | Manual/Export | Download data or copy threads |
| LinkedIn | Manual | Copy top posts to files |

### 0.4 Verify Dataset

Run checklist from `/deep-brand-intake/resources/output-checklist.md`:
- [ ] 10+ content pieces
- [ ] 10,000+ words
- [ ] 2+ content types
- [ ] Recent content (< 2 years)

### 0.5 Create Source Inventory

Save `/clients/[client-name]/source-inventory.md` documenting what was collected.

---

## STEP 1: ANALYZE (Brand Foundation)

### 1.1 Voice DNA Analysis

**Trigger:** `/voice-dna`

**Input needed:**
- 10-20 content samples from STEP 0
- Paste directly OR reference file paths

**Process:**
1. Skill analyzes samples across 5 layers
2. Identifies patterns, phrases, structure
3. Creates comprehensive voice profile

**Save output to:** `/clients/[client-name]/voice-dna-profile.md`

### 1.2 Disgust Mapper

**Trigger:** `/disgust-mapper`

**Choose mode:**
- **Quick (3 questions):** ~60 seconds, good for start
- **Full (10 questions):** ~5 minutes, comprehensive

**Process:**
1. Answer questions about what client would NEVER say
2. Skill assigns severity scores (-10 to -1000)
3. Creates boundaries list

**Save output to:** `/clients/[client-name]/disgust-profile.md`

### 1.3 Brand Discovery

**Trigger:** `/brand-discovery`

**Two modes:**
- **Interactive:** 39-question interview with client
- **Extraction:** Analyze existing content for brand elements

**Process:**
1. Phase 1: Positioning (15 questions)
2. Phase 2: Audience Deep Dive (11 questions)
3. Phase 3: Content Strategy (8 questions)
4. Phase 4: Transformation Journey (5 questions)

**Save output to:** `/clients/[client-name]/brand-profile.md`

---

## STEP 2: ARCHITECT (Topics + Authority)

### 2.1 Authority Engine

**Trigger:** `/authority-engine`

**Input needed:**
- Brand Profile from STEP 1.3

**Process:**
1. Extracts niche from brand profile
2. Runs STP analysis (Segment → Target → Position)
3. Discovers competitors via Perplexity
4. Generates perceptual map

**Output:**
- `/clients/[client-name]/authority/competitors.csv`
- `/clients/[client-name]/authority/positioning-map.md`
- `/clients/[client-name]/authority/stp-analysis.md`

### 2.2 Competitor Analysis (OPTIONAL)

**Only if learning from competitors is valuable:**

| Skill | Purpose | Output |
|-------|---------|--------|
| `/competitor-hooks` | Viral openers | Hook patterns library |
| `/competitor-structures` | Content formats | Structure templates |
| `/competitor-topics` | Engagement topics | Topic ideas |
| `/competitor-gaps` | White space | Opportunity list |

### 2.3 Topic Generation

**Trigger:** `/generate-topics`

**Input needed:**
- Brand Profile
- Authority Engine output (optional)

**Process:**
1. Generates 50-100 topics from brand profile
2. Maps to ERISE buckets
3. Scores by impact + uniqueness + urgency
4. Organizes by theme

**Save output to:** `/clients/[client-name]/topic-library.md`

---

## STEP 3: ACTIVATE (Content Generation)

### 3.1 Topic to Matrix

**Trigger:** `/topic-to-matrix`

**Input needed:**
- ONE topic from topic library
- Brand Profile (referenced)
- Voice Meta prompt (from Voice DNA + Disgust)

**Process:**
1. Analyzes topic for best ERISE bucket
2. Identifies core message and emotional hook
3. Generates 19 pieces:
   - 1 primary long-form asset
   - 18 atomized social/email pieces

**Save output to:** `/clients/[client-name]/content/[topic-slug]/`

### 3.2 Trust Signals (OPTIONAL)

**Only use when client HAS DATA:**

| Skill | Requires | Creates |
|-------|----------|---------|
| `/trust-case-studies` | Real client results | Case study content |
| `/trust-frameworks` | Named methodology | Framework content |
| `/trust-contrarian` | Defensible hot take | Thought leadership |
| `/trust-metrics` | Real numbers | Transparency content |
| `/trust-deep-dives` | Deep expertise | Ultimate guide |
| `/trust-provenance` | Behind-scenes process | Authenticity content |

**Anti-hallucination rule:** Never use trust skills to FABRICATE - only to MAGNIFY existing data.

---

## Client Folder Structure

After complete workflow:

```
/clients/[client-name]/
├── README.md                    (client overview)
├── source-inventory.md          (STEP 0)
├── raw-content/                 (STEP 0)
│   ├── emails/
│   ├── transcripts/
│   ├── posts/
│   └── social/
├── voice-dna-profile.md         (STEP 1.1)
├── disgust-profile.md           (STEP 1.2)
├── brand-profile.md             (STEP 1.3)
├── authority/                   (STEP 2)
│   ├── competitors.csv
│   ├── positioning-map.md
│   └── stp-analysis.md
├── topic-library.md             (STEP 2.3)
└── content/                     (STEP 3)
    ├── [topic-1-slug]/
    │   ├── primary-asset.md
    │   ├── twitter-threads.md
    │   ├── social-posts.md
    │   └── emails.md
    ├── [topic-2-slug]/
    └── ...
```

---

## Timing Estimates

| Step | First Client | Repeat Clients |
|------|--------------|----------------|
| STEP 0: Capture | 30-60 min | 15-30 min |
| STEP 1: Analyze | 60-90 min | 45-60 min |
| STEP 2: Architect | 30-60 min | 20-30 min |
| STEP 3: Activate | Ongoing | Ongoing |
| **TOTAL SETUP** | **2-3.5 hours** | **1.5-2 hours** |

Content generation (STEP 3) is ongoing - typically 1-3 topics per week.

---

## Troubleshooting

**"I don't have enough content samples"**
→ Work with client to identify more sources
→ Consider interviewing client to generate content

**"Voice DNA seems generic"**
→ Need more diverse samples
→ Include more unscripted content (podcasts, lives)

**"Topics don't feel unique"**
→ Run /authority-engine for positioning
→ Use /competitor-gaps to find white space

**"Content still sounds like AI"**
→ Check Disgust Mapper boundaries are applied
→ Review Voice DNA for missing patterns
→ Have client edit and note what they change
