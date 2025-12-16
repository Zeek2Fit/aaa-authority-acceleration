# Kit (ConvertKit) Email Extraction Guide

## Overview
Kit (formerly ConvertKit) stores email sequences and broadcasts. This guide covers extracting that content for Voice DNA analysis.

## Prerequisites

1. **Playwright installed:**
```bash
pip install playwright
playwright install chromium
```

2. **Chrome running with debug port:**
```bash
# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# Must be logged into Kit in this browser session
```

## Method 1: kit_email_extractor.py (Automated)

**For email sequences:**
```bash
python tools/extraction/kit_email_extractor.py \
  "https://app.kit.com/sequences/[SEQUENCE_ID]" \
  output_file.json
```

**Output format:**
```json
[
  {"subject": "Email 1 Subject", "content": "Full email body..."},
  {"subject": "Email 2 Subject", "content": "Full email body..."}
]
```

**Note:** This script connects to an existing Chrome session where you're logged into Kit. Make sure Chrome is running with `--remote-debugging-port=9222`.

---

## Method 2: Kit API (Manual Setup)

**Get your API key:**
1. Kit Dashboard → Settings → Developer
2. Copy API Secret

**Export broadcasts via API:**
```bash
curl -X GET "https://api.kit.com/v4/broadcasts" \
  -H "Authorization: Bearer $KIT_API_KEY" \
  -H "Content-Type: application/json" > broadcasts.json
```

**Export sequences via API:**
```bash
curl -X GET "https://api.kit.com/v4/sequences" \
  -H "Authorization: Bearer $KIT_API_KEY" \
  -H "Content-Type: application/json" > sequences.json
```

---

## Method 3: Manual Export (Fallback)

If automation fails:

1. **Go to Kit Dashboard → Broadcasts**
2. **Click on each broadcast → Copy content**
3. **Paste into individual .txt files**
4. **Name format:** `YYYY-MM-DD_email-subject.txt`

**For Sequences:**
1. **Go to Sequences → Select sequence**
2. **Click each email in sequence**
3. **Copy subject + content**
4. **Save to files**

---

## Organizing Extracted Content

```
/clients/[client-name]/raw-content/emails/
├── broadcasts/
│   ├── 2024-01-15_welcome-email.txt
│   ├── 2024-02-01_launch-announcement.txt
│   └── ...
├── sequences/
│   ├── welcome-sequence/
│   │   ├── 01_day1-email.txt
│   │   ├── 02_day3-email.txt
│   │   └── ...
│   └── sales-sequence/
│       └── ...
└── kit_export_manifest.md
```

---

## Manifest Template

Create `/clients/[client-name]/raw-content/emails/kit_export_manifest.md`:

```markdown
# Kit Export Manifest

**Client:** [Name]
**Export Date:** [Date]
**Account:** [Kit account email/URL]

## Broadcasts Extracted
- [ ] Broadcast 1: [Subject] (Date)
- [ ] Broadcast 2: [Subject] (Date)
...

## Sequences Extracted
- [ ] Sequence: [Name] (X emails)
  - Email 1: [Subject]
  - Email 2: [Subject]
  ...

## Stats
- Total broadcasts: X
- Total sequences: X
- Total emails: X
- Estimated words: X
```

---

## Troubleshooting

**"Browser not found" error:**
Make sure Chrome is running with debug port BEFORE running the script.

**"Not logged in" error:**
Navigate to Kit in the Chrome debug instance and log in first.

**Empty results:**
Kit may have updated their DOM structure. Inspect the page and update selectors in `kit_email_extractor.py`.

**Rate limiting:**
Add delays between requests if extracting large volumes:
```python
page.wait_for_timeout(1000)  # 1 second delay
```
