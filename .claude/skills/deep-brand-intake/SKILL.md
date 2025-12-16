# Deep Brand Intake Skill

> **Step 0 of AAA Framework** - Capture raw content BEFORE analysis

## Purpose
Guide users through collecting 10-20+ content samples from a client's existing digital footprint. This is the essential "capture" phase that MUST happen before Voice DNA or Brand Discovery.

## When to Use
- Starting work with a new client
- User says "capture content", "gather samples", "collect writing", "digital footprint"
- BEFORE running /voice-dna or /brand-discovery
- When user doesn't know HOW to get samples for analysis

## The Problem This Solves
Users often say "I want to analyze my client's voice" but have NO IDEA how to collect the raw material. This skill bridges that gap.

## Quick Start

**Minimum viable capture: 10 samples, 10,000+ words**

Ask the client:
1. "Do you have a Kit/ConvertKit account?" → See `resources/kit-instructions.md`
2. "Do you have a YouTube channel or podcast?" → See `resources/capture-sources.md`
3. "Do you have a blog or newsletter archive?" → Use Firecrawl scraping
4. "Can you share 5-10 of your best emails?" → Request forwards/exports

## Capture Source Hierarchy

**BEST sources (most authentic, unedited voice):**
1. Podcast transcripts (unscripted natural speech)
2. YouTube video transcripts
3. Email newsletters (personal, conversational)
4. Social media threads (Twitter/X, LinkedIn)

**GOOD sources (still valuable):**
5. Blog posts (may be edited but still authentic)
6. Course content / lesson transcripts
7. Webinar recordings
8. Interview appearances

**OKAY sources (use if nothing else available):**
9. Sales pages (often more polished, less raw)
10. Book content (heavily edited but comprehensive)

## Step-by-Step Capture Process

### Step 1: Inventory Client Assets
Ask: "What content does [CLIENT] currently produce?"
- [ ] Email newsletter (Kit, ConvertKit, Mailchimp, etc.)
- [ ] Podcast (Buzzsprout, Spotify, Apple)
- [ ] YouTube channel
- [ ] Blog/website articles
- [ ] Social media (Twitter/X, LinkedIn, Instagram)
- [ ] Published book
- [ ] Courses/training materials

### Step 2: Extract Based on Sources

**If Kit/ConvertKit user:**
```bash
# See resources/kit-instructions.md for full details
python tools/extraction/kit_email_extractor.py <sequence_url>
```

**If podcaster:**
```bash
# See resources/capture-sources.md for transcript options
python tools/extraction/podcast_transcript_extractor.py <rss_feed_url>
```

**If YouTuber:**
```bash
python tools/extraction/youtube_transcript_extractor.py <channel_url>
```

**If blogger:**
Use Firecrawl MCP to scrape blog posts:
```
firecrawl_crawl: {url: "https://clientblog.com/blog", limit: 20}
```

### Step 3: Organize Content
Save all extracted content to client folder:
```
/clients/[client-name]/
├── raw-content/
│   ├── emails/           (Kit exports)
│   ├── transcripts/      (Podcast/YouTube)
│   ├── posts/            (Blog scraped content)
│   └── social/           (Twitter threads, LinkedIn posts)
└── README.md             (Source inventory)
```

### Step 4: Run Gemini Voice Synthesizer (OPTIONAL)
For massive content sets (50,000+ words), use Gemini's long context:
```bash
# See resources/gemini-instructions.md for full details
python tools/extraction/gemini_voice_synthesizer.py \
  --input-dir /clients/[client-name]/raw-content \
  --brand "[Client Name]" \
  --output /clients/[client-name]/gemini_voice_profile.md
```

### Step 5: Confirm Ready for Analysis
Use `resources/output-checklist.md` to verify:
- [ ] 10+ content pieces collected
- [ ] 10,000+ words total
- [ ] Multiple content types (at least 2 sources)
- [ ] Temporal diversity (content from different time periods)

## Output
- `/clients/[client-name]/raw-content/` - All source material
- `/clients/[client-name]/source-inventory.md` - What was collected and from where
- Ready for: `/voice-dna` and `/brand-discovery`

## Resources
- `resources/capture-sources.md` - Detailed extraction methods per source
- `resources/kit-instructions.md` - Kit email extractor usage
- `resources/gemini-instructions.md` - Gemini long-context synthesizer
- `resources/output-checklist.md` - Pre-analysis quality checklist

## Anti-Patterns (What NOT to Do)
- DON'T skip this step and go straight to Voice DNA with 2-3 samples
- DON'T only use polished/edited content (sales pages, professionally written)
- DON'T rely on client describing their voice - capture ACTUAL content
- DON'T mix multiple people's content (one voice at a time)

## Why This Matters
> "Voice DNA is only as good as the samples you feed it. Garbage in, garbage out."

10 diverse, authentic samples → 95% voice accuracy
3 polished sales pages → 60% voice accuracy (generic)

---

**Next Step After Capture:** Run `/voice-dna` with collected samples
