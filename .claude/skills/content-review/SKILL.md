# Content Review Skill

> **Human-in-the-Loop** - Review, edit, and approve content before scheduling

## Purpose
Provides a structured review workflow for content in Airtable. Fetches "Review" status content, presents it for human approval, captures edits, and updates status to "Approved" or back to "Draft".

## When to Use
- User says "review content", "approve content", "check my queue"
- After running `/content-to-airtable` to push content
- When content needs human approval before scheduling
- To batch-review multiple content pieces

## Prerequisites
- Airtable MCP server connected
- AAA Content Engine base exists (ID: apptbYRdtuqrSGXJb)
- Content pieces exist with Status = "Review" or "Draft"

## Process

### Step 1: Fetch Content for Review
Ask: "Should I review content marked for Review, or include Drafts too?"

**Review only (default):**
```
mcp__airtable__list_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Content Pieces
  filterByFormula: {Status} = 'Review'
  maxRecords: 10
```

**Include Drafts:**
```
mcp__airtable__list_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Content Pieces
  filterByFormula: OR({Status} = 'Review', {Status} = 'Draft')
  maxRecords: 10
```

### Step 2: Present Content for Review
For each content piece, display:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTENT REVIEW: [Content Title]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Platform: [Platform]
Type: [Content Type]
Status: [Current Status]
Voice Match: [Score]%

HOOK:
[Hook text]

CONTENT:
[Full content body]

CTA:
[Call to action]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Actions:
  [A] Approve - Move to Approved status
  [E] Edit - Make changes before approving
  [R] Reject - Move back to Draft with notes
  [S] Skip - Review later
  [Q] Quit - End review session
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 3: Handle User Actions

**Approve (A):**
```
mcp__airtable__update_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Content Pieces
  records: [
    {
      id: [record_id],
      fields: {
        Status: "Approved"
      }
    }
  ]
```

**Edit (E):**
1. Ask: "What would you like to change?"
2. Accept edits to: Content, Hook, CTA, or Hashtags
3. Update record with changes:
```
mcp__airtable__update_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Content Pieces
  records: [
    {
      id: [record_id],
      fields: {
        Content: [updated content],
        Hook: [updated hook],
        CTA: [updated cta],
        Hashtags: [updated hashtags],
        Status: "Approved"
      }
    }
  ]
```

**Reject (R):**
1. Ask: "What notes should I add for revision?"
2. Update status back to Draft with notes:
```
mcp__airtable__update_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Content Pieces
  records: [
    {
      id: [record_id],
      fields: {
        Status: "Draft",
        Notes: [rejection reason]
      }
    }
  ]
```

**Skip (S):**
- Move to next content piece
- Don't change status

**Quit (Q):**
- End review session
- Show summary of actions taken

### Step 4: Review Summary
After completing review (or quitting), show:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REVIEW SESSION COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Reviewed: [X] pieces
Approved: [X] pieces
Edited & Approved: [X] pieces
Rejected: [X] pieces
Skipped: [X] pieces

Remaining in queue: [X] pieces

Next steps:
- Open Airtable to see approved content
- Run /content-calendar to schedule approved content
- Re-run /content-review for remaining pieces
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Batch Review Mode

For faster review, offer batch mode:

**Command:** "batch review" or "quick review"

Show condensed view:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BATCH REVIEW: 10 pieces
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. [Twitter] Digital Sabbath - Thread (92%)
   "Your phone isn't the enemy..."

2. [Email] Digital Sabbath - Newsletter (91%)
   "When was the last time you..."

3. [Instagram] Digital Sabbath - Carousel (90%)
   "5 Signs You Need a Digital Sabbath..."

...

Actions:
  [AA] Approve All
  [1,3,5] Approve specific (comma-separated)
  [V1] View full content for #1
  [Q] Quit
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Airtable Schema Reference

**Base ID:** `apptbYRdtuqrSGXJb`

**Table:** AAA Content Pieces (tblZoCZeYRMzMS0ld)

**Fields Used:**
| Field | Type | Purpose |
|-------|------|---------|
| Content Title | Text | Display name |
| Platform | Select | Twitter, Email, etc. |
| Content Type | Select | Thread, Newsletter, etc. |
| Content | Long Text | Main body |
| Hook | Text | Opening line |
| CTA | Text | Call to action |
| Status | Select | Draft, Review, Approved, Scheduled, Published |
| Voice Match Score | Number | Authenticity percentage |
| Hashtags | Text | Tags |
| Notes | Long Text | Review notes |

**Status Flow:**
```
Draft → Review → Approved → Scheduled → Published
  ↑                │
  └────(reject)────┘
```

## Example Usage

**User:** "Review my content queue"

**Process:**
1. Fetch content with Status = "Review"
2. Found 5 pieces
3. Present first piece for review
4. User approves → Update status to "Approved"
5. Present next piece
6. User edits hook → Update content + status to "Approved"
7. Continue until done or user quits
8. Show summary

**User:** "Quick review my Stephanie content"

**Process:**
1. Fetch content with client = "Stephanie" and Status = "Review"
2. Show batch view with condensed list
3. User types "AA" to approve all
4. Update all records to "Approved"
5. Show summary

## Important Rules

1. **Never auto-approve** - Always require human action
2. **Preserve original** - Keep unedited fields unchanged
3. **Track edits** - Note when content was edited in review
4. **Show context** - Display Voice Match Score to build trust
5. **Easy escape** - Always allow skip/quit options
6. **Clear feedback** - Confirm each action taken

## Next Steps
After review:
- "Open Airtable to see your content calendar"
- "Run /content-calendar to schedule approved content"
- "Content is ready for n8n automation"
