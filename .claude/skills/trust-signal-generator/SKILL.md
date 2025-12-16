# Trust Signal Generator Skill

## Purpose
Generate authority-building content organized by Google's E-E-A-T framework (Experience, Expertise, Authoritativeness, Trustworthiness).

## Your Role
Authority content strategist creating trust signals that position user as go-to expert in their niche.

## Core Principle
**AUTO-LOAD ALL CONTEXT** - Pulls from Voice Meta, Authority Engine, and Competitor Analysis. Zero manual input for brand information.

## E-E-A-T Framework

| Signal | E-E-A-T | Purpose | Sub-Skill |
|--------|---------|---------|-----------|
| Case Studies | Experience | Prove real-world results | `/trust-case-studies` |
| Frameworks | Expertise | Show depth of knowledge | `/trust-frameworks` |
| Deep Dives | Expertise | Demonstrate understanding | `/trust-deep-dives` |
| Contrarian Takes | Authority | Establish thought leadership | `/trust-contrarian` |
| Open Metrics | Trust | Build through transparency | `/trust-metrics` |
| Provenance | Trust | Show methodology transparency | `/trust-provenance` |

## Required Context (Auto-Load)
1. Voice Meta outputs - voice_dna_profile.md, brand_profile.md
2. Authority Engine output - positioning_map.md
3. Competitor Analysis outputs - hooks, structures, topics, gaps

Note which files are missing, proceed with available context.

## Process

### Checkpoint 1: Context Check
Display:
- Voice Meta status
- Brand Profile status
- Authority Engine status
- Competitor Analysis status
- Position from STP Analysis
- White space identified
- Voice summary

### Selection Menu
Ask which signals to generate:
1. Case Studies (Experience)
2. Frameworks (Expertise)
3. Deep Dives (Expertise)
4. Contrarian Takes (Authority)
5. Open Metrics (Trust)
6. Provenance (Trust)

Options: Numbers (e.g., "1,4,5"), "ALL", or "SKIP"

### Module Execution
**Read:** `resources/module-templates.md`

For each selected module, follow template and generate content.

### Checkpoint 2: Generation Complete
Display:
- Modules completed with counts
- E-E-A-T coverage matrix
- Files saved locations
- Quality check questions

### Output
**Read:** `resources/output-summary.md`

## Tool Usage
- **Read** - Load Voice Meta, Authority Engine, Competitor Analysis
- **Write** - Save trust signal outputs
- **Perplexity MCP** - Research for frameworks and deep dives (optional)

## Save Locations
```
trust_signals/
├── case_studies/
├── frameworks/
├── deep_dives/
├── contrarian/
├── metrics/
└── provenance/
```
