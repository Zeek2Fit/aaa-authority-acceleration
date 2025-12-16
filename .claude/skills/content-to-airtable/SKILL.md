# Content to Airtable Skill

> **Pipeline Connector** - Push generated content directly into Airtable Content Engine

## Purpose
After `/topic-to-matrix` generates content, this skill pushes it directly to the Airtable "AAA Content Engine" base, creating proper records with relationships.

## When to Use
- After running `/topic-to-matrix` and generating content
- User says "push to airtable", "save to airtable", "add to content queue"
- User wants to store generated content for scheduling/review
- After any content generation that should be tracked

## Prerequisites
- Airtable MCP server connected
- AAA Content Engine base exists (ID: apptbYRdtuqrSGXJb)
- Client record exists in AAA Clients table
- Topic record exists in AAA Topics table (or will be created)

## Process

### Step 1: Identify Content Source
Ask: "What content should I push to Airtable?"

Options:
1. **From conversation** - Content just generated in this session
2. **From file** - Read from a specific file path
3. **Manual input** - User pastes content directly

### Step 2: Parse Content Structure
For each content piece, extract:
- **Platform**: Twitter, Email, Instagram, LinkedIn, YouTube, Blog
- **Content Type**: Thread, Single Post, Newsletter, Carousel, Short Video, Article
- **Content**: Main body text
- **Hook**: Opening line (first sentence or explicit hook)
- **CTA**: Call to action (last sentence or explicit CTA)
- **Hashtags**: Any tags mentioned
- **Voice Match Score**: If provided (default: 90.0)

### Step 3: Verify/Create Client Record
Check if client exists in AAA Clients table:
```
mcp__airtable__search_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Clients
  searchTerm: [client name]
```

If not found, create:
```
mcp__airtable__create_record
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Clients
  fields:
    Client Name: [name]
    Status: Active
```

### Step 4: Verify/Create Topic Record
Check if topic exists in AAA Topics table:
```
mcp__airtable__search_records
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Topics
  searchTerm: [topic name]
```

If not found, create:
```
mcp__airtable__create_record
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Topics
  fields:
    Topic Name: [topic]
    ERISE Bucket: [bucket if known]
    Priority Score: [score if known]
    Status: In Production
    Client: [client record ID]
    Client Tag: [client short name - matches Content Pieces mapping]
```

### Step 5: Create Content Piece Records
For EACH content piece:
```
mcp__airtable__create_record
  baseId: apptbYRdtuqrSGXJb
  tableId: AAA Content Pieces
  fields:
    Content Title: "[Topic] - [Platform] [Type]"
    Platform: [platform]
    Content Type: [type]
    Content: [full content]
    Hook: [opening line]
    CTA: [call to action]
    Status: Draft
    Voice Match Score: [score]
    Hashtags: [tags]
    Topic: [topic record ID]
    Client: [client record ID]
    Client Tag: [client short name - e.g., "Zach Lloyd" or "Stephanie Jones"]
```

**Client Tag Mapping:**
| Client Name | Client Tag Value |
|-------------|------------------|
| Zach Lloyd Coaching | Zach Lloyd |
| Stephanie Jones | Stephanie Jones |
| [New Client] | [Add to AAA Content Pieces field options first] |

> **Important:** When adding a new client, first add their name as a new option to the "Client Tag" single-select field in both AAA Content Pieces and AAA Topics tables.

### Step 6: Confirm Success
Report:
- Number of records created
- Link to Airtable base
- Next steps (review in Airtable, run /content-review)

## Airtable Schema Reference

**Base ID:** `apptbYRdtuqrSGXJb`

**Tables:**
| Table | ID | Purpose |
|-------|-----|---------|
| AAA Clients | tbldySumfGgo1nHs1 | Client profiles |
| AAA Topics | tbl9EBQO0Swy8O9IY | Topic library |
| AAA Content Pieces | tblZoCZeYRMzMS0ld | Content queue |

**Platform Options:** Twitter, Email, Instagram, LinkedIn, YouTube, Blog

**Content Type Options:** Thread, Single Post, Newsletter, Carousel, Short Video, Article

**Status Options:** Draft, Review, Approved, Scheduled, Published

**Client Tag Options:** Zach Lloyd (green), Stephanie Jones (purple), [Add new clients as needed]

## Example Usage

**User:** "Push the Digital Sabbath content we just generated to Airtable for Stephanie"

**Process:**
1. Identify client: Stephanie Jones
2. Identify topic: Digital Sabbath
3. Parse generated content (thread, newsletter, carousel, etc.)
4. Create/verify client record
5. Create/verify topic record
6. Create 19 content piece records (one per generated piece)
7. Report: "Created 19 content pieces in AAA Content Engine"

## Important Rules
1. Always verify client/topic exist before creating content pieces
2. Set initial status to "Draft" (never auto-approve)
3. Include Voice Match Score if available
4. Extract Hook from first sentence if not explicit
5. Extract CTA from last sentence if not explicit
6. Use descriptive Content Title: "[Topic] - [Platform] [Type]"
7. **Always set Client Tag** for visual differentiation in Airtable views
8. **New clients:** Add their name as a Client Tag option in Airtable before first content push

## Next Steps
After pushing content:
- "Run /content-review to review draft content"
- "Open Airtable to see your content queue"
- "Run /content-calendar to schedule content"
