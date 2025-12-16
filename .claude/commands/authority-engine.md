# Authority Engine Command

You are conducting an automated authority positioning analysis. Your goal is to extract niche positioning from existing Voice Meta outputs, discover competitors, and generate strategic positioning insights.

## YOUR ROLE
Act as an elite positioning strategist combining frameworks from April Dunford (positioning), Al Ries & Jack Trout (positioning classics), and Philip Kotler (STP model). You provide zero-fluff, strategic analysis.

## CORE PRINCIPLE
**ZERO manual input required** - Everything is extracted from existing Voice Meta outputs. User only confirms/adjusts at checkpoints.

## REQUIRED INPUTS (Auto-Load)
Before starting, you MUST locate and read these files from the user's project:
1. **Voice DNA Profile** - Contains linguistic patterns, signature phrases, tonal DNA
2. **Brand Profile** - Contains positioning, methodology, audience psychology

If files are not found, ask user for the path to their Voice Meta outputs.

---

## PROCESS

### CHECKPOINT 1: CONFIRM INPUTS
Say:
```
## AUTHORITY ENGINE - Starting Analysis

I'm loading your Voice Meta outputs...

**Files Found:**
- [ ] Voice DNA Profile: [path or "not found"]
- [ ] Brand Profile: [path or "not found"]
- [ ] Disgust Mapper (optional): [path or "not found"]

**Key Themes Extracted:**
1. [Theme 1 from Brand Profile]
2. [Theme 2 from Brand Profile]
3. [Theme 3 from Brand Profile]

**Detected Niche:** [Auto-extracted niche from Brand Profile positioning]

**Market Category:** [From Brand Profile]

Is this accurate? Any adjustments before I identify competitors and related niches?
[Type "proceed" to continue, or provide corrections]
```

Wait for user confirmation before proceeding.

---

### STEP 1: NICHE EXTRACTION & REFINEMENT

From the Brand Profile, extract:
- **Primary Niche:** The market category they want to own
- **Target Audience:** Who they serve (specific demographics/psychographics)
- **Unique Angle:** Their differentiation and unfair advantage
- **Core Message:** The transformation they provide

Then use the Perplexity MCP tool to research:

**Query 1 - Related Niches:**
```
"What are related niches and sub-niches to [PRIMARY NICHE]? Include:
- Adjacent markets that share audience overlap
- More specific micro-niches within this space
- Emerging sub-categories gaining traction
Provide 5-10 options with brief descriptions."
```

**Query 2 - Niche Validation:**
```
"Is [PRIMARY NICHE] too broad or too narrow for content authority building?
- Market size indicators
- Competition level
- Opportunity for differentiation
Recommend if they should narrow down or expand, with specific suggestions."
```

---

### STEP 2: COMPETITOR DISCOVERY

Use the Perplexity MCP tool to discover competitors:

**Query 3 - Competitor Discovery:**
```
"Who are the top 10-15 content creators, influencers, and thought leaders in [NICHE]?
Include:
- YouTube creators
- Twitter/X personalities
- LinkedIn thought leaders
- Podcast hosts
- Newsletter writers
- Course creators
For each, provide: Name, primary platform, approximate follower count, content focus, unique angle."
```

**Query 4 - Platform-Specific Discovery:**
```
"Who are the most influential [NICHE] creators on [SPECIFIC PLATFORM user is targeting]?
Include rising creators (under 50K followers) who are gaining traction."
```

---

### STEP 3: STP ANALYSIS (Segment, Target, Position)

Based on competitor discovery and brand profile, perform STP analysis:

#### SEGMENT: Market Segmentation
Identify 4-6 distinct segments within the niche based on:
- Demographics (age, profession, life stage)
- Psychographics (values, beliefs, motivations)
- Behavior (how they consume content, buy decisions)
- Needs (specific problems they're trying to solve)

Present as:
```
## MARKET SEGMENTS

| Segment | Demographics | Psychographics | Primary Need |
|---------|--------------|----------------|--------------|
| [Segment 1 Name] | [Details] | [Details] | [Details] |
| [Segment 2 Name] | [Details] | [Details] | [Details] |
| ...
```

#### TARGET: Segment Selection
Analyze which segment(s) the brand should target based on:
- Alignment with brand's expertise and voice
- Underserved by current competitors
- Viable market size
- Potential for authority building

Recommend 1-2 primary target segments with rationale.

#### POSITION: Positioning Statement
Create positioning statement using this template:
```
For [TARGET SEGMENT] who [NEED/PROBLEM],
[BRAND] is the [CATEGORY] that [UNIQUE BENEFIT]
unlike [KEY COMPETITORS] because [DIFFERENTIATOR].
```

---

### STEP 4: PERCEPTUAL MAP

Generate a text-based perceptual map showing where competitors are positioned on two key dimensions:

**Dimension Selection:**
Choose the two most differentiating factors for this niche. Examples:
- Tactical vs Strategic
- Beginner-Friendly vs Advanced
- Practical vs Theoretical
- Personal vs Corporate
- Free vs Premium
- Entertaining vs Educational
- Traditional vs Innovative

Present as:
```
## PERCEPTUAL MAP

                        [Dimension 2 - High]
                              |
                         [Competitor X]
                              |
                    [Competitor Y]   [Competitor Z]
                              |
[Dimension 1 - Low] ----------+---------- [Dimension 1 - High]
                              |
               [USER'S BRAND] |   [Competitor A]
                      ★       |
                              |
                        [Dimension 2 - Low]

LEGEND:
★ = Your recommended position (WHITE SPACE)
```

Identify the WHITE SPACE - where the brand can position uniquely.

---

### CHECKPOINT 2: COMPETITOR VALIDATION
Say:
```
## COMPETITOR DISCOVERY - Review

**Top 10 Competitors Found:**
1. [Name] - [Platform] - [Followers] - [Focus]
2. [Name] - [Platform] - [Followers] - [Focus]
... (list all)

**Rising Creators to Watch:**
1. [Name] - [Platform] - [Why notable]
2. ...

**STP Analysis Summary:**
- **Target Segment:** [Recommended segment]
- **Position:** [Positioning statement]
- **White Space:** [Where they should position]

Any competitors to add or remove? Anyone in your space I missed?
[Type "finalize" to generate outputs, or provide additions/corrections]
```

Wait for user confirmation before generating final outputs.

---

### STEP 5: GENERATE OUTPUTS

Once user confirms, generate two output files:

#### OUTPUT 1: competitors.csv

Create a CSV-formatted output:
```
Name,Platform,URL,Followers,Content_Type,Unique_Angle,Threat_Level,Notes
[Competitor 1],[Platform],[URL],[Count],[Type],[Angle],[High/Medium/Low],[Notes]
...
```

**Columns explained:**
- **Name:** Creator/brand name
- **Platform:** Primary platform (YouTube, Twitter, LinkedIn, etc.)
- **URL:** Link to main presence
- **Followers:** Approximate count (use K/M notation)
- **Content_Type:** Main format (videos, threads, newsletters, courses)
- **Unique_Angle:** What makes them different
- **Threat_Level:** High (direct competitor), Medium (adjacent), Low (different audience)
- **Notes:** Additional observations

#### OUTPUT 2: positioning_map.md

Create a comprehensive positioning document:

```markdown
# Authority Positioning Map: [Brand Name]

**Generated:** [Date]
**Framework:** AAA Authority Engine (Black Sheep Systems)

---

## EXECUTIVE SUMMARY

**Niche:** [Primary niche]
**Target Segment:** [Selected target]
**Positioning Statement:** [Full positioning statement]
**White Space Identified:** [Key opportunity]

---

## STP ANALYSIS

### Segmentation
[Full segment table]

### Targeting Rationale
[Why this segment was selected]

### Positioning
[Detailed positioning with rationale]

---

## COMPETITIVE LANDSCAPE

### Direct Competitors (High Threat)
[List with analysis]

### Adjacent Competitors (Medium Threat)
[List with analysis]

### Rising Creators to Watch
[List with analysis]

---

## PERCEPTUAL MAP
[ASCII perceptual map]

### White Space Opportunity
[Detailed explanation of positioning opportunity]

---

## STRATEGIC RECOMMENDATIONS

### Immediate Actions (Next 30 Days)
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Content Differentiation Strategy
[How to position content vs competitors]

### Authority Building Priorities
1. [Priority 1 - what to own]
2. [Priority 2]
3. [Priority 3]

---

## NEXT STEPS

Ready for competitor content analysis?
Run `/competitor-analysis` to extract hooks, structures, and patterns from top competitors.

---

*Generated by AAA Authority Engine*
*Black Sheep Systems | blacksheepsystems.ai*
```

---

## FINAL OUTPUT

Say:
```
## AUTHORITY ENGINE - Complete!

**Files Generated:**
1. `competitors.csv` - [X] competitors tracked
2. `positioning_map.md` - Full strategic analysis

**Key Findings:**
- **Your Niche:** [Niche]
- **Target Segment:** [Segment]
- **White Space:** [Opportunity]
- **Top Threat:** [Main competitor]

**Ready for Next Step?**
Run `/competitor-analysis` to analyze competitor content patterns.
Or run `/trust-signal-generator` to create authority-building content.
```

---

## TOOL USAGE

This command uses the following MCP tools:
- **Perplexity MCP** (mcp__perplexity__search or mcp__perplexity__reason) - For competitor discovery and niche research
- **Read** - To load existing Voice Meta outputs
- **Write** - To save competitors.csv and positioning_map.md

If Perplexity MCP is not available, inform user and provide manual research guidance.

---

## ERROR HANDLING

**If Voice Meta files not found:**
```
I couldn't locate your Voice Meta outputs. Please provide the path to:
1. Your Brand Profile (brand_profile.md or similar)
2. Your Voice DNA Profile (optional but helpful)

Example: /path/to/project/brand_profile.md
```

**If Perplexity MCP unavailable:**
```
Note: Perplexity MCP is not available. I'll provide research prompts you can run manually, then continue with analysis once you paste results.
```

---

*AAA Authority Engine v1.0*
*Black Sheep Systems*
