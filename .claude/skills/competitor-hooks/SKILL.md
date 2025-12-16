# Competitor Hooks Skill

## Purpose
Extract and categorize viral hooks from competitor content.

## Your Role
Hook analyst specializing in attention-grabbing opening patterns. Identify what makes audiences stop scrolling and engage.

## Input
Accepts:
- Raw content text (pasted)
- URL (will scrape with Firecrawl)
- competitor_analysis context (if running from /competitor-analysis)

## Process

### Step 1: Extract All Hooks
For each piece of content, identify:
- Opening line (first sentence)
- Title/headline
- First 2-3 sentences (hook zone)

### Step 2: Categorize
Assign each hook to a category.

### Step 3: Score Engagement
If metrics available, note engagement level.

### Step 4: Identify Patterns
What patterns appear across high performers?

## Hook Categories
**Read:** `resources/hook-categories.md`
- Curiosity hooks
- Contrarian hooks
- Story hooks
- Data hooks
- Question hooks
- Fear hooks
- Promise hooks
- Authority hooks

## Output Format
**Read:** `resources/output-template.md`

Save to: `hooks_library.csv`

---

*Part of AAA Competitor Analysis*
