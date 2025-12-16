# AAA System Setup Guide

## Prerequisites

Before installing the AAA system, ensure you have:

1. **Claude Code** installed and running
2. **Airtable account** (free tier works)
3. **Kit (ConvertKit) account** for email automation
4. **Python 3.9+** for extraction scripts

## Installation

### Step 1: Copy Skills to Claude Code

```bash
# Clone or download this repository
git clone https://github.com/blacksheepsystems/aaa-authority-acceleration.git
cd aaa-authority-acceleration

# Copy skills to your Claude Code environment
cp -r .claude/skills/* ~/.claude/skills/
cp -r .claude/commands/* ~/.claude/commands/
```

### Step 2: Verify Installation

Open Claude Code and run:

```bash
ls ~/.claude/skills/
```

You should see 23 skill directories plus `skill-rules.json`.

### Step 3: Configure Airtable

#### Create a Personal Access Token

1. Go to [https://airtable.com/create/tokens](https://airtable.com/create/tokens)
2. Create token with scopes:
   - `data.records:read`
   - `data.records:write`
   - `schema.bases:read`
3. Save the token securely

#### Create AAA Content Engine Base

In Airtable, create a new base with these tables:

**Table 1: AAA Clients**
| Field | Type |
|-------|------|
| Client Name | Single line text |
| Status | Single select (Active, Inactive) |
| Voice DNA Profile | Long text |
| Disgust Profile | Long text |
| Brand Profile | Long text |

**Table 2: AAA Topics**
| Field | Type |
|-------|------|
| Topic Name | Single line text |
| ERISE Bucket | Single select |
| Priority Score | Number |
| Status | Single select |
| Client | Link to AAA Clients |

**Table 3: AAA Content Pieces**
| Field | Type |
|-------|------|
| Content Title | Single line text |
| Platform | Single select (Twitter, Email, Instagram, LinkedIn, YouTube, Blog) |
| Content Type | Single select (Thread, Single Post, Newsletter, Carousel, Short Video, Article) |
| Content | Long text |
| Hook | Single line text |
| CTA | Single line text |
| Status | Single select (Draft, Review, Approved, Scheduled, Published) |
| Scheduled Date | Date |
| Voice Match Score | Number |
| Hashtags | Single line text |
| Topic | Link to AAA Topics |
| Client | Link to AAA Clients |

#### Get Your Base ID

Your base ID is in the URL when viewing your base:
```
https://airtable.com/appXXXXXXXXXXXXXX/...
                     ^^^^^^^^^^^^^^^^^
                     This is your Base ID
```

### Step 4: Configure n8n (Optional)

If you want automated publishing:

1. Import `n8n/aaa-publish-workflow.json` into your n8n instance
2. Update these credentials in the workflow:
   - Airtable API key
   - Kit API key
   - (Optional) Twitter, WordPress, LinkedIn API keys
3. Activate the workflow

### Step 5: Install Python Dependencies

```bash
pip install openai anthropic google-generativeai requests
```

## First Run

### Test Auto-Activation

Type this in Claude Code:
```
I have a new client named Test Company
```

You should see the skill suggestion:
```
🎯 AAA SKILL AUTO-ACTIVATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚨 CRITICAL (REQUIRED):
   /aaa-workflow - Complete AAA Framework journey

→ Use slash command to activate skill
```

### Run the Orchestrator

```
/aaa-workflow
```

The system will guide you through the complete process.

## Extraction Tools

### Kit Email Extractor

Extract emails from your Kit account:

```bash
python tools/extraction/kit_email_extractor.py \
  --api-key YOUR_KIT_API_KEY \
  --output clients/[name]/raw-content/emails/
```

### YouTube Transcript Extractor

Extract transcripts from YouTube:

```bash
python tools/extraction/youtube_transcript_extractor.py \
  --channel @ChannelName \
  --output clients/[name]/raw-content/youtube/
```

### Gemini Voice Synthesizer

Run complete voice analysis (500k+ tokens):

```bash
python tools/extraction/gemini_voice_synthesizer.py \
  --input-dir clients/[name]/raw-content/ \
  --brand "Client Name" \
  --output clients/[name]/voice-synthesis.md
```

## Troubleshooting

### Skills Not Loading

1. Check file permissions: `chmod -R 755 ~/.claude/skills/`
2. Verify `skill-rules.json` exists in `~/.claude/skills/`
3. Restart Claude Code

### Airtable Connection Issues

1. Verify API token has correct scopes
2. Check Base ID matches your base
3. Ensure table names match exactly

### n8n Webhook Not Working

1. Verify n8n workflow is activated
2. Check webhook URL is correct
3. Verify Airtable filter matches Status="Approved"

## Support

For issues or questions:
- GitHub Issues: [Link to your repo]
- Email: zach@blacksheepsystems.ai
