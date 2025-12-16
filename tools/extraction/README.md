# AAA Extraction Tools

> **For AI Assistants:** These tools help gather content for the CAPTURE phase of the AAA Framework. Read this file to understand how to use each tool.

---

## Overview

These Python scripts extract content from various platforms to build a client's "digital footprint" for voice analysis.

**Minimum viable dataset:**
- 10+ content pieces
- 10,000+ words
- 2+ content types (mix of email, video, social, etc.)

---

## Quick Reference for AI

| Source | Tool | Command |
|--------|------|---------|
| YouTube | `youtube_transcript_extractor.py` | `python youtube_transcript_extractor.py` |
| Kit/ConvertKit | `kit_email_extractor.py` | `python kit_email_extractor.py` |
| Podcasts (Buzzsprout) | `podcast_transcript_extractor.py` | `python podcast_transcript_extractor.py` |
| Twitter/X | See "Twitter Extraction" section below | Manual or browser automation |
| Blog/Website | Use Firecrawl MCP | `mcp__firecrawl__firecrawl_scrape` |
| Large datasets | `gemini_voice_synthesizer.py` | For 500k+ token analysis |

---

## Tool Details

### 1. YouTube Transcript Extractor

**File:** `youtube_transcript_extractor.py`

**What it does:** Downloads transcripts from YouTube videos (auto-generated or manual captions).

**Requirements:**
```bash
pip install youtube-transcript-api
```

**Usage:**
```bash
python youtube_transcript_extractor.py
# Then paste YouTube URLs, one per line
# Press Enter twice when done
```

**For AI to use:**
```
Tell the user to run this command in their terminal:
python tools/extraction/youtube_transcript_extractor.py

Then paste these YouTube URLs:
[list the URLs]

The tool will create a folder with all transcripts.
```

**Output:** `youtube_transcripts_TIMESTAMP/` folder with `.txt` files

---

### 2. Kit (ConvertKit) Email Extractor

**File:** `kit_email_extractor.py`

**What it does:** Extracts email broadcasts from Kit (ConvertKit) using their API.

**Requirements:**
- Kit API key (v4)
- Set environment variable: `KIT_API_KEY`

**Usage:**
```bash
export KIT_API_KEY="your_api_key_here"
python kit_email_extractor.py
```

**For AI to use:**
```
Ask the user for their Kit API key, then run:
export KIT_API_KEY="[their_key]"
python tools/extraction/kit_email_extractor.py

This extracts all their email broadcasts.
```

**Output:** `kit_broadcasts_TIMESTAMP/` folder with email content

---

### 3. Podcast Transcript Extractor (Buzzsprout)

**File:** `podcast_transcript_extractor.py`

**What it does:** Extracts transcripts from Buzzsprout-hosted podcasts.

**Requirements:**
- Buzzsprout API credentials

**Usage:**
```bash
python podcast_transcript_extractor.py --podcast-id YOUR_ID
```

**For AI to use:**
```
Ask the user for their Buzzsprout podcast ID, then run:
python tools/extraction/podcast_transcript_extractor.py --podcast-id [ID]
```

---

### 4. Twitter/X Content Extraction

**IMPORTANT:** Twitter/X API is now paid ($100/month minimum). Here are the alternatives:

#### Option A: Manual Export (Recommended)
1. Go to twitter.com/settings/download_your_data
2. Request your data archive
3. Extract the `tweets.js` file
4. Use it as source content

**For AI to use:**
```
Twitter API is paid. Ask the user to:
1. Export their Twitter archive from twitter.com/settings/download_your_data
2. Wait for the download link (can take 24-48 hours)
3. Share the tweets.js file for analysis
```

#### Option B: Browser Automation (Playwright)
Use the Playwright MCP server to scrape a Twitter profile:

```
mcp__playwright__browser_navigate to https://x.com/[username]
mcp__playwright__browser_snapshot to capture tweets
```

**Limitations:** Rate limited, may require login

#### Option C: Firecrawl (Currently Blocked)
Twitter/X is blocked on Firecrawl free tier. Enterprise customers can request access.

#### Option D: Third-Party Services
- **Apify:** twitter.com scraper actors (paid)
- **Phantombuster:** Twitter export (paid)
- **TweetDeck export:** For owned accounts

---

### 5. Gemini Voice Synthesizer

**File:** `gemini_voice_synthesizer.py`

**What it does:** Sends large content datasets (500k-800k tokens) to Gemini 2.5 for complete voice analysis.

**Requirements:**
- Google AI API key
- Set environment variable: `GOOGLE_AI_API_KEY`

**Usage:**
```bash
export GOOGLE_AI_API_KEY="your_key"
python gemini_voice_synthesizer.py \
  --input-dir /path/to/raw-content \
  --brand "Client Name"
```

**For AI to use:**
```
After gathering all content samples, run:
python tools/extraction/gemini_voice_synthesizer.py \
  --input-dir clients/[name]/raw-content \
  --brand "[Client Name]"

This performs the complete voice analysis using Gemini's 1-2M token context.
Cost: ~$0.15-0.50 one-time.
```

**Output:** Comprehensive voice profile with 5-layer analysis

---

### 6. Blog/Website Extraction

**No Python script needed.** Use Firecrawl MCP directly:

**For AI to use:**
```
Use the Firecrawl MCP tool to scrape website content:

mcp__firecrawl__firecrawl_scrape with URL = "https://example.com/blog"

For multiple pages, use:
mcp__firecrawl__firecrawl_map to discover URLs
mcp__firecrawl__firecrawl_crawl for batch extraction
```

---

## Recommended Extraction Order

For a new client, gather content in this order:

1. **Email newsletters** (Kit) - Highest quality voice samples
2. **Podcast/YouTube** - Long-form, natural speech
3. **Blog posts** - Written voice samples
4. **Social media** - Short-form patterns
5. **Run Gemini synthesizer** - After 10k+ words collected

---

## Output Structure

All extractors save to timestamped folders:

```
clients/
└── [client-name]/
    └── raw-content/
        ├── kit_broadcasts_20251216/
        │   ├── broadcast_1.txt
        │   └── SUMMARY.txt
        ├── youtube_transcripts_20251216/
        │   ├── transcript_1_videoId.txt
        │   └── SUMMARY.txt
        └── source-inventory.md
```

---

## Troubleshooting

**"Module not found" errors:**
```bash
pip install youtube-transcript-api requests beautifulsoup4
```

**Twitter/X scraping fails:**
Use manual export or browser automation. API is paid.

**YouTube "Transcripts disabled":**
Some videos don't have captions. Skip them.

**Rate limiting:**
Add delays between requests. Most tools handle this automatically.

---

## For AI Assistants

When a user says "gather content for [client]", follow this workflow:

1. **Ask what platforms they use:** Email, YouTube, podcast, blog, Twitter?
2. **For each platform:**
   - YouTube → Run `youtube_transcript_extractor.py`
   - Kit → Run `kit_email_extractor.py` (needs API key)
   - Blog → Use Firecrawl MCP
   - Twitter → Recommend manual export
3. **Verify minimum dataset:** 10+ pieces, 10k+ words
4. **Run Gemini synthesizer** if dataset is large (50k+ words)
5. **Proceed to ANALYZE phase** with `/voice-dna`
