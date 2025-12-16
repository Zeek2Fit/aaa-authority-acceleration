# Content Capture Sources Guide

## Source Extraction Methods

### 1. Podcast Transcripts
**Quality: BEST** (natural, unscripted speech)

**Tools:**
```bash
# Buzzsprout (direct transcript access)
python tools/extraction/batch_buzzsprout_extractor.py <feed_url>

# General podcast transcription
python tools/extraction/podcast_transcript_extractor.py <rss_feed_url>
```

**Manual options:**
- Buzzsprout: Export from dashboard → Transcripts
- Spotify for Podcasters: Download transcript files
- Apple Podcasts Connect: Copy from episode details
- Descript: Upload audio → auto-transcribe

**Tip:** Aim for 10-15 recent episodes (6-12 months) for temporal diversity.

---

### 2. YouTube Transcripts
**Quality: BEST** (visual personality + speech patterns)

**Tools:**
```bash
python tools/extraction/youtube_transcript_extractor.py <channel_url>
```

**Manual options:**
- Click "..." under video → "Show transcript" → Copy all
- Use [YouTubeTranscript.com](https://youtubetranscript.com) for bulk export
- Download via `yt-dlp --write-auto-sub`

**Tip:** Include both long-form content AND shorts/clips for range.

---

### 3. Email Newsletters
**Quality: BEST** (personal, conversational, unfiltered)

**If Kit/ConvertKit:**
See `kit-instructions.md` for detailed extraction.

**If Mailchimp:**
1. Campaigns → All campaigns → Export
2. Download HTML or plain text versions

**If Beehiiv:**
1. Content → Posts → Export
2. Or request data export from settings

**If other ESP:**
Ask client to forward 10-15 best-performing emails.

**If .eml files:**
```bash
python tools/extraction/extract_eml_text.py <directory_of_emls>
```

---

### 4. Blog Posts / Website Articles
**Quality: GOOD** (may be edited but still authentic)

**Using Firecrawl MCP:**
```
firecrawl_crawl: {
  url: "https://example.com/blog",
  limit: 20,
  maxDiscoveryDepth: 2
}
```

**Using Firecrawl scrape (single pages):**
```
firecrawl_scrape: {
  url: "https://example.com/specific-post",
  formats: ["markdown"]
}
```

**Manual:** Use browser extension to "save as markdown" for key posts.

---

### 5. Social Media Content
**Quality: GOOD** (short-form voice, hooks, punchy style)

**Twitter/X:**
- Use TweetDeck to export
- Use [ThreadReaderApp](https://threadreaderapp.com) for threads
- Request "Your Twitter data" export from Settings

**LinkedIn:**
- Request data download from Settings
- Copy/paste key posts manually
- Use [Phantom Buster](https://phantombuster.com) for automation

**Instagram:**
- Request data download
- Copy captions from saved posts
- Screenshot → OCR for archived content

---

### 6. Books / Long-Form Content
**Quality: OKAY** (heavily edited but comprehensive worldview)

**If available:**
- Request manuscript/Word doc from client
- Use Kindle Highlights export
- PDF → text extraction:
```bash
pdftotext book.pdf book.txt
```

**Note:** Books are valuable for VALUES and BELIEFS but may not capture natural voice cadence.

---

### 7. Course Content / Webinars
**Quality: GOOD** (teaching voice, authority tone)

**Options:**
- Request transcript from course platform
- Download video → transcribe via Descript
- Use [AssemblyAI](https://assemblyai.com) for batch transcription

---

## Minimum Viable Dataset

| Source Type | Ideal Count | Minimum | Words Est. |
|------------|-------------|---------|------------|
| Podcasts | 10-15 episodes | 5 | 30,000+ |
| YouTube | 5-10 videos | 3 | 15,000+ |
| Emails | 15-20 newsletters | 10 | 10,000+ |
| Blog posts | 10-15 articles | 5 | 7,500+ |
| Social | 20-30 posts/threads | 10 | 3,000+ |

**Target: 10,000+ words minimum, 50,000+ for best results**

---

## Source Quality Ranking

1. **Unscripted audio** (podcasts, interviews) - RAW authenticity
2. **Personal writing** (emails, social) - Direct voice
3. **Semi-scripted** (YouTube with outline) - Natural + structured
4. **Edited content** (blog posts) - Polished but authentic
5. **Highly produced** (books, sales pages) - Values but not voice cadence

---

## Red Flags (Sources to Avoid)

- Ghost-written content (not their voice)
- Content from 5+ years ago (voice evolves)
- Collaborative pieces (multiple authors)
- Heavily templated content (using formulas)
- Legal/compliance-reviewed content (sanitized)
