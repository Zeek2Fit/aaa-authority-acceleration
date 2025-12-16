# AAA Authority Acceleration System

> **Authentic AI-Assisted Authorship:** Turn one brand interview into 12+ months of content that's 90-95% indistinguishable from the original creator.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Created by Zach Lloyd** | [Black Sheep Systems](https://blacksheepsystems.ai) | [@blacksheepsystems](https://youtube.com/@blacksheepsystems)

---

## Overview

The AAA System solves the #1 problem in AI content creation: **authenticity**.

Most AI content fails because:
- Everyone uses the same prompts from the same YouTube videos
- They skip the strategic work (brand discovery, voice analysis)
- They treat AI like a microwave: "Make me content"
- Result: 40-50% authenticity. Your audience can tell.

**The AAA System is different:**
- **23 modular skills** for the complete content lifecycle
- **Voice Meta v2.0** captures what you say AND what you'd NEVER say
- **Validated at 90-95% authenticity** in blind tests
- **Complete pipeline** from generation to publishing

## The Math

```
1 Brand Interview → 100 Topics
1 Topic → 19 Content Pieces
100 × 19 = 1,900 Pieces
= 12+ MONTHS of content from ONE session
```

## Quick Start

### 1. Install Skills

Copy the `.claude/skills/` folder to your Claude Code environment:

```bash
cp -r .claude/skills/ ~/.claude/skills/
```

### 2. Verify Installation

```bash
ls ~/.claude/skills/
# Should show 23 skill directories + skill-rules.json
```

### 3. Run Your First Workflow

```
/aaa-workflow
```

You'll be guided through the complete journey:
- **STEP 0:** CAPTURE - Gather content samples
- **STEP 1:** ANALYZE - Voice DNA + Disgust Mapper + Brand Discovery
- **STEP 2:** ARCHITECT - Authority positioning + Topics
- **STEP 3:** ACTIVATE - Multi-platform content generation

## System Architecture

```
Natural Language Input → Skill Auto-Activation → Content Generation
        ↓                       ↓                       ↓
"New client Sarah"     /aaa-workflow suggested    Voice DNA extracted
                                                         ↓
                                              /content-to-airtable
                                                         ↓
                                                  Airtable Queue
                                                         ↓
                                        curl webhook → n8n → Kit Draft
```

### The 3 Layers

| Layer | Purpose | Output |
|-------|---------|--------|
| **Layer 0: Brand Discovery** | Strategic positioning (125 ERISE variables) | Complete Brand Profile |
| **Layer 1: Voice Meta** | Voice DNA + Disgust Mapper (negative boundaries) | Voice Meta Profile |
| **Layer 2: Topic Generation** | Combinatorial creativity | 50-100 strategic topics |

## Skills Inventory (23 Total)

### Core Workflow
- `/aaa-workflow` - Master orchestrator
- `/deep-brand-intake` - Content capture
- `/brand-discovery` - 39-question strategic interview
- `/voice-dna` - 5-layer voice extraction
- `/disgust-mapper` - Negative boundary mapping
- `/generate-topics` - Combinatorial topic generation
- `/topic-to-matrix` - 1 topic → 19 pieces

### Authority Engine
- `/authority-engine` - STP analysis + competitor discovery
- `/competitor-analysis` - Full content analysis
- `/competitor-hooks` - Viral hook extraction
- `/competitor-structures` - Format analysis
- `/competitor-topics` - High-engagement topics
- `/competitor-gaps` - White space opportunities

### Trust Signals (E-E-A-T)
- `/trust-signal-generator` - Orchestrator
- `/trust-case-studies` - Client transformation stories
- `/trust-frameworks` - Proprietary methodologies
- `/trust-contrarian` - Thought leadership takes
- `/trust-metrics` - Transparency content
- `/trust-deep-dives` - Long-form authority
- `/trust-provenance` - Behind-the-scenes

### Pipeline & Utilities
- `/content-to-airtable` - Push to content queue
- `/content-calendar` - Bulk scheduling
- `/content-review` - Human-in-the-loop approval
- `/session-handoff` - Context management

## Why NOT RAG?

We rejected RAG (Retrieval Augmented Generation) in favor of **complete context loading**:

| RAG (What Others Do) | AAA System |
|---------------------|------------|
| Chunks content into snippets | Loads COMPLETE digital footprint |
| Searches for "relevant" pieces | 500k-800k tokens in one shot |
| Stitches together fragments | Uses Gemini's 1-2M context window |
| **40-50% authenticity** | **90-95% authenticity** |

**RAG can't see that you always open with a question. RAG can't detect your signature three-beat rhythm. We load everything.**

## Airtable Integration

The system integrates with Airtable for content management:

**Base ID:** See SETUP.md for configuration

| Table | Purpose |
|-------|---------|
| AAA Clients | Client profiles |
| AAA Topics | Topic library |
| AAA Content Pieces | Content queue |

## n8n Pipeline

The included n8n workflow automates publishing:

```
Airtable (Status: Approved) → Webhook → n8n → Kit Draft → Airtable (Published)
```

**Currently Supported:**
- Email → Kit (ConvertKit)
- Twitter → X API (bring your key)
- WordPress → WP REST API (bring credentials)
- LinkedIn → LinkedIn API (bring token)

## Extraction Tools

The `tools/extraction/` folder contains Python scripts for gathering content:

| Tool | Purpose |
|------|---------|
| `youtube_transcript_extractor.py` | Download YouTube video transcripts |
| `kit_email_extractor.py` | Extract Kit (ConvertKit) email broadcasts |
| `podcast_transcript_extractor.py` | Get podcast transcripts from Buzzsprout |
| `gemini_voice_synthesizer.py` | Analyze 500k+ tokens with Gemini 2.5 |

**For Twitter/X:** See `tools/extraction/README.md` for alternatives (API is paid).

**Quick start:**
```bash
pip install youtube-transcript-api requests beautifulsoup4
python tools/extraction/youtube_transcript_extractor.py
```

See `tools/extraction/README.md` for complete AI-friendly usage instructions.

## Requirements

- **Claude Code** - This system runs in Claude Code
- **Airtable MCP** - For content queue integration
- **Kit Account** - For email draft creation
- **n8n Instance** - For automation (optional)
- **Python 3.9+** - For extraction scripts

## Credits

### Created By

**Zach Lloyd** - Founder of [Black Sheep Systems](https://blacksheepsystems.ai)

Black Sheep Systems helps small business owners implement AI automation that actually works. The AAA System was built to solve the authentic content problem once and for all.

### Built With

- [Claude Code](https://claude.ai/claude-code)
- Anthropic's Skills architecture
- Gemini 2.5 for voice synthesis

---

**License:** MIT - Use freely, attribution appreciated.
