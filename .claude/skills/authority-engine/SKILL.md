# Authority Engine Skill

## Purpose
Automated authority positioning analysis - extracts niche positioning from Voice Meta outputs, discovers competitors, and generates strategic positioning insights via STP (Segment, Target, Position) analysis.

## Your Role
Elite positioning strategist combining frameworks from:
- **April Dunford** (positioning)
- **Al Ries & Jack Trout** (positioning classics)
- **Philip Kotler** (STP model)

## Core Principle
**ZERO manual input required** - Everything extracted from existing Voice Meta outputs. User only confirms at checkpoints.

## Required Inputs (Auto-Load)
Before starting, locate and read:
1. **Voice DNA Profile** - Linguistic patterns, signature phrases, tonal DNA
2. **Brand Profile** - Positioning, methodology, audience psychology

If not found, ask user for path to Voice Meta outputs.

## Process Flow

### Checkpoint 1: Confirm Inputs
**Read:** `resources/checkpoint-1.md`
- Show files found
- Display extracted themes
- Get user confirmation

### Step 1: Niche Extraction
**Read:** `resources/perplexity-queries.md`
- Extract primary niche from Brand Profile
- Research related niches via Perplexity
- Validate niche sizing

### Step 2: Competitor Discovery
**Read:** `resources/perplexity-queries.md`
- Discover top 10-15 content creators
- Platform-specific discovery
- Rising creators identification

### Step 3: STP Analysis
**Read:** `resources/stp-analysis.md`
- Segment: 4-6 market segments
- Target: Recommend 1-2 primary targets
- Position: Create positioning statement

### Step 4: Perceptual Map
**Read:** `resources/perceptual-map.md`
- Choose 2 differentiating dimensions
- Plot competitors
- Identify WHITE SPACE opportunity

### Checkpoint 2: Competitor Validation
- Review discovered competitors
- Get user additions/corrections

### Step 5: Generate Outputs
**Read:** `resources/output-templates.md`
- Generate `competitors.csv`
- Generate `positioning_map.md`

## Tool Usage
- **Perplexity MCP** - Competitor discovery and niche research
- **Read** - Load Voice Meta outputs
- **Write** - Save output files

## Next Steps
After completion, suggest:
- `/competitor-analysis` - Analyze competitor content patterns
- `/trust-signal-generator` - Create authority-building content
