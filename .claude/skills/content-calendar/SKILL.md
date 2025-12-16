# Content Calendar Skill

> **Bulk Generator** - Generate and schedule weeks/months of content from multiple topics

## Purpose
Generate a complete content calendar by processing multiple topics through `/topic-to-matrix` logic and automatically scheduling them in Airtable with intelligent date spacing.

## When to Use
- User wants "a month of content" or "6 months of content"
- User says "fill my content calendar", "bulk generate", "schedule content"
- After `/generate-topics` when user wants to produce content at scale
- User needs a complete content queue, not just one topic

## The Math
```
/content-calendar --weeks 4 --topics-per-week 3

4 weeks × 3 topics = 12 topics processed
12 topics × 19 pieces per topic = 228 content pieces
228 pieces scheduled across 28 days
= 8+ pieces per day, balanced across platforms
```

## Process

### Step 1: Get Calendar Parameters
Ask for:
1. **Duration**: How many weeks? (default: 4)
2. **Topics per week**: How many topics to process per week? (default: 3)
3. **Start date**: When should the calendar start? (default: tomorrow)
4. **Client name**: Which client is this for?
5. **Platform priorities**: Which platforms to prioritize? (default: all)

### Step 2: Load Topic Library
**Option A:** From Airtable
```
mcp__airtable__list_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Topics
  filterByFormula: AND({Client}='[client]', {Status}='Pending')
  sort: [{field: 'Priority Score', direction: 'desc'}]
```

**Option B:** From file
Read topic library from: `/clients/[name]/topic-library.md`

### Step 3: Select Top Topics
Based on:
- Priority Score (highest first)
- ERISE bucket balance (distribute across Education, Relevance, Inspiration, Story, Engagement)
- Not already "In Production" or "Complete"

Select: `weeks × topics_per_week` topics

### Step 4: Generate Content for Each Topic
For each selected topic, generate using `/topic-to-matrix` logic:

**Per Topic Output (19 pieces):**
- 1 Primary asset (blog/newsletter)
- 3 Twitter threads
- 5 Single tweets
- 2 LinkedIn posts
- 3 Instagram posts
- 1 Instagram carousel
- 1 YouTube Short
- 2 Email follow-ups

**Read:** `resources/content-templates.md` for platform-specific generation

### Step 5: Intelligent Scheduling
Distribute content across the calendar period:

**Scheduling Rules:**
```
Daily Posting Cadence:
- Twitter: 2-3 posts/day (morning, afternoon, evening)
- LinkedIn: 1 post/day (business hours)
- Instagram: 1-2 posts/day (morning, evening)
- Email: 2-3 per week (Tues, Thurs, Sat)
- Blog: 1-2 per week
- YouTube: 1-2 per week
```

**Date Assignment Algorithm:**
1. Calculate total pieces per platform
2. Distribute evenly across calendar days
3. Assign optimal posting times per platform
4. Avoid weekend posting for LinkedIn
5. Balance ERISE buckets across each week

### Step 6: Push to Airtable
For each generated piece, create record:
```
mcp__airtable__create_record
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Content Pieces
  fields:
    Content Title: "[Topic] - [Platform] [Type]"
    Platform: [platform]
    Content Type: [type]
    Content: [generated content]
    Hook: [opening line]
    CTA: [call to action]
    Status: Draft
    Scheduled Date: [calculated date]
    Voice Match Score: [score]
    Topic: [topic record ID]
    Client: [client record ID]
```

### Step 7: Update Topic Status
Mark processed topics as "In Production":
```
mcp__airtable__update_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Topics
  records: [{id: [topic_id], fields: {Status: 'In Production'}}]
```

### Step 8: Generate Calendar Summary
Output:
```markdown
## Content Calendar Summary

**Period:** [start date] to [end date]
**Topics Processed:** [count]
**Total Content Pieces:** [count]

### By Platform:
| Platform | Pieces | Posts/Week |
|----------|--------|------------|
| Twitter | 96 | 24 |
| LinkedIn | 24 | 6 |
| Instagram | 48 | 12 |
| Email | 24 | 6 |
| Blog | 12 | 3 |
| YouTube | 12 | 3 |

### By Week:
| Week | Topics | Pieces | ERISE Balance |
|------|--------|--------|---------------|
| Week 1 | 3 | 57 | E:2, R:1, I:0, S:0, E:0 |
| ... | ... | ... | ... |

### Next Steps:
1. Run /content-review to approve content
2. Check Airtable Calendar view
3. Connect n8n/Blotato for auto-posting
```

## Example Usage

**User:** "Generate a month of content for Stephanie"

**Process:**
1. Duration: 4 weeks (default)
2. Topics/week: 3 (default)
3. Load Stephanie's topic library
4. Select top 12 topics by priority
5. Generate 228 pieces (12 × 19)
6. Schedule across 28 days
7. Push all to Airtable
8. Output calendar summary

**Result:** 228 draft content pieces in Airtable, scheduled and ready for review

## Configuration Options

### Quick Presets
```
/content-calendar --preset quick    # 2 weeks, 2 topics/week = 76 pieces
/content-calendar --preset month    # 4 weeks, 3 topics/week = 228 pieces
/content-calendar --preset quarter  # 12 weeks, 3 topics/week = 684 pieces
```

### Platform Focus
```
/content-calendar --platforms twitter,linkedin  # Only these platforms
/content-calendar --skip email,blog            # Exclude these platforms
```

### ERISE Balance
```
/content-calendar --erise-focus education      # Prioritize educational content
/content-calendar --erise-balanced             # Equal distribution (default)
```

## Important Rules
1. Never schedule on past dates
2. Respect platform-specific posting windows
3. Balance ERISE buckets across each week
4. All content starts as "Draft" status
5. Generate Voice Match Score for each piece
6. Update topic status after processing
7. Provide clear summary with actionable next steps

## Next Steps After Generation
- "Run /content-review to approve draft content"
- "Open Airtable Calendar view to see schedule"
- "Run /content-to-airtable if you need to add more content"
