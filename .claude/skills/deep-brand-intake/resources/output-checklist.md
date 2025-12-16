# Pre-Analysis Output Checklist

## Before Running Voice DNA or Brand Discovery

Use this checklist to verify you have enough quality content for accurate voice analysis.

---

## Quantity Check

| Metric | Minimum | Ideal | Status |
|--------|---------|-------|--------|
| Total content pieces | 10 | 20+ | [ ] |
| Total word count | 10,000 | 50,000+ | [ ] |
| Unique content types | 2 | 4+ | [ ] |
| Time span covered | 3 months | 12+ months | [ ] |

---

## Source Diversity Check

**Have you collected from at least 2 of these categories?**

- [ ] **Spoken content** (podcasts, YouTube, webinars)
- [ ] **Written-personal** (emails, social posts, DMs)
- [ ] **Written-formal** (blog posts, articles, books)
- [ ] **Unscripted** (interviews, Q&As, live streams)

**Why diversity matters:**
- Spoken shows natural cadence
- Written shows editing preferences
- Personal shows authentic voice
- Formal shows public persona
- Combining reveals TRUE voice patterns

---

## Quality Check

Answer YES to all before proceeding:

- [ ] All content is from ONE person (not collaborations)
- [ ] Content is recent (within last 2-3 years)
- [ ] No ghost-written or heavily edited content
- [ ] Minimal template/formulaic content
- [ ] Content includes personal opinions (not just facts)
- [ ] Mix of topics/contexts (not all about same thing)

---

## File Organization Check

```
/clients/[client-name]/
├── raw-content/
│   ├── emails/           [ ] Contains files
│   ├── transcripts/      [ ] Contains files
│   ├── posts/            [ ] Contains files
│   └── social/           [ ] Contains files
├── source-inventory.md   [ ] Created
└── README.md             [ ] Optional but recommended
```

---

## Source Inventory Template

Create `/clients/[client-name]/source-inventory.md`:

```markdown
# Content Source Inventory

**Client:** [Name]
**Collection Date:** [Date]
**Collected By:** [Your name]

## Summary
- Total pieces: [X]
- Estimated words: [X]
- Date range: [Start] to [End]

## Sources Collected

### Emails ([X] pieces, ~[X] words)
- Source: [Kit/Mailchimp/etc.]
- Extraction method: [Tool used]
- Files: emails/

### Podcasts ([X] episodes, ~[X] words)
- Source: [Podcast name]
- Extraction method: [Tool used]
- Files: transcripts/

### Blog Posts ([X] articles, ~[X] words)
- Source: [Website URL]
- Extraction method: [Firecrawl/manual]
- Files: posts/

### Social Media ([X] posts, ~[X] words)
- Source: [Twitter/LinkedIn/etc.]
- Extraction method: [Export/manual]
- Files: social/

## Notes
- [Any observations about content quality]
- [Missing sources we couldn't access]
- [Recommendations for future collection]

## Ready for Analysis
- [ ] Minimum quantity met
- [ ] Diversity requirement met
- [ ] Quality check passed
- [ ] Files organized
- [ ] Inventory complete

**Next Step:** Run /voice-dna with this content
```

---

## Red Flags - DO NOT Proceed If:

1. **Only marketing content** - Sales pages and ads don't capture authentic voice
2. **All same topic** - Need variety to see full voice range
3. **Heavily templated** - Fill-in-the-blank content won't reveal patterns
4. **Multiple authors** - Will muddy the voice profile
5. **Very old content** - Voice evolves; 5+ year old content may not represent current voice
6. **Under 5,000 words** - Not enough data for reliable patterns

---

## Quick Assessment

**Score your collection:**

| Factor | Points |
|--------|--------|
| 10,000+ words | +2 |
| 50,000+ words | +3 |
| 4+ content types | +2 |
| 12+ month span | +2 |
| Includes unscripted | +2 |
| All from one person | +2 |
| Recent (< 2 years) | +1 |

**Total: __/14**

- **12-14:** Excellent - proceed with high confidence
- **8-11:** Good - proceed, may need refinement
- **5-7:** Marginal - consider collecting more
- **< 5:** Insufficient - collect more before proceeding

---

## Next Steps

Once checklist is complete:

1. **Run Gemini Synthesizer** (if 50K+ words):
   ```bash
   python tools/extraction/gemini_voice_synthesizer.py --input-dir /clients/[name]/raw-content
   ```

2. **Run Voice DNA Skill:**
   ```
   /voice-dna
   ```

3. **Run Brand Discovery:**
   ```
   /brand-discovery
   ```
