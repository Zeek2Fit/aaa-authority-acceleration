# Gemini Voice Synthesizer Guide

## Overview
The Gemini Voice Synthesizer uses Google's Gemini 2.5 Pro/Flash models with 1-2M token context windows to analyze massive content sets in a SINGLE pass - no chunking, no RAG, no information loss.

**Why Gemini for Voice Synthesis:**
- 1M-2M token context = 750K-1.5M words in ONE call
- Sees EVERYTHING at once → finds patterns humans miss
- No chunking artifacts or lost connections
- Perfect for "voice DNA" that spans entire body of work

## Prerequisites

```bash
# Install required packages
pip install google-generativeai python-dotenv

# Get API key from https://aistudio.google.com/apikey
# Add to .env file:
echo "GOOGLE_API_KEY=your_key_here" >> .env
```

## Basic Usage

**Single directory:**
```bash
python tools/extraction/gemini_voice_synthesizer.py \
  --input-dir /clients/sarah/raw-content \
  --brand "Sarah Smith" \
  --output /clients/sarah/gemini_voice_profile.md
```

**Specific files:**
```bash
python tools/extraction/gemini_voice_synthesizer.py \
  --files podcast1.txt podcast2.txt email1.txt email2.txt \
  --brand "Sarah Smith" \
  --output /clients/sarah/gemini_voice_profile.md
```

**Interactive mode:**
```bash
python tools/extraction/gemini_voice_synthesizer.py --interactive
```

## Model Options

| Model | Context | Cost | Quality |
|-------|---------|------|---------|
| `gemini-2.5-flash` | 1M tokens | FREE | Good |
| `gemini-2.5-pro` | 2M tokens | Pay-per-use | Best |

**Default:** `gemini-2.5-flash` (free tier)

To use Pro:
```bash
python tools/extraction/gemini_voice_synthesizer.py \
  --model gemini-2.5-pro \
  --input-dir /clients/sarah/raw-content \
  --brand "Sarah Smith"
```

## What It Analyzes

The synthesizer extracts:

1. **Voice DNA Summary** - Core personality, communication mode, emotional register
2. **Linguistic Patterns** - Signature phrases, sentence structure, hooks
3. **Tone Markers** - Humor style, hard truths, empathy, motivation
4. **Content Structure DNA** - Openings, arguments, stories, CTAs
5. **Values & Beliefs** - Core beliefs, anti-values, non-negotiables
6. **Audience Relationship** - How they address readers, trust-building
7. **Anti-Voice** - What they would NEVER say (disgust mapping)
8. **Voice Replication Guide** - Rules for writing in their voice
9. **Authenticity Markers** - Unique quirks, recognizable elements

## Output Example

```markdown
---
title: Brand Voice DNA Profile - Sarah Smith
generated: 2025-12-14T10:30:00
files_analyzed: 47
total_characters: 285,000
estimated_tokens: 71,250
model: gemini-2.5-flash
---

# Brand Voice DNA Profile: Sarah Smith

> Generated from 47 content pieces (~71,250 tokens)

## 1. VOICE DNA SUMMARY
- Core personality: Warm, Direct, Encouraging
- Primary communication mode: Educator-Inspirer hybrid
- Emotional register: Optimistic with grounded honesty
- Voice essence: "A wise friend who tells you the truth with love"

## 2. LINGUISTIC PATTERNS
- Signature phrases: "Here's the thing...", "Friends, listen..."
...
```

## When to Use vs. Voice DNA Skill

| Scenario | Use This | Why |
|----------|----------|-----|
| 50,000+ words | Gemini Synthesizer | Long context advantage |
| 10-30 samples | Voice DNA Skill | More structured analysis |
| Need quick profile | Gemini Synthesizer | Single API call |
| Need interactive Q&A | Voice DNA Skill | Iterative refinement |
| Initial exploration | Gemini Synthesizer | Fast overview |
| Deep analysis | Voice DNA Skill | 5-layer methodology |

**Best practice:** Run Gemini FIRST for overview, then Voice DNA skill for structured profile.

## Integration with AAA Framework

```
STEP 0: CAPTURE (deep-brand-intake)
    ↓
GEMINI VOICE SYNTHESIZER (optional, for large datasets)
    ↓
    Creates: gemini_voice_profile.md
    ↓
STEP 1: ANALYZE
    ├── /voice-dna → Uses Gemini output as input
    └── /brand-discovery → References voice findings
```

## Troubleshooting

**"GOOGLE_API_KEY not found":**
```bash
# Make sure .env exists in working directory
cat .env  # Should show GOOGLE_API_KEY=...
```

**"Content may exceed context window":**
- Reduce input files
- Use `gemini-2.5-pro` (2M context) instead of flash (1M)

**Rate limiting:**
- Free tier has usage limits
- Wait a few minutes and retry
- Or upgrade to paid tier

**Poor quality output:**
- Ensure content is ACTUALLY from one person
- Remove headers/footers/boilerplate
- Include more diverse content types
