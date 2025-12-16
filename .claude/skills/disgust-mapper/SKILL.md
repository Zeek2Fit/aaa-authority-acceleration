# Disgust Mapper Skill

## Purpose
Capture what someone would NEVER say to create AI guardrails. The "negative training" that prevents AI from generating content that would make the user cringe.

## The Core Concept

**Traditional AI Training:** "Here's what I DO say" (positive examples)
**Disgust Mapping:** "Here's what I'd NEVER say" (negative boundaries)

**Result:** AI that knows both inclusion AND exclusion = authentic voice with guardrails

## Why This Matters

Research basis:
- Psychology: Disgust is more persistent than attraction
- Linguistics: What you avoid defines you more than what you use
- AI: Contrastive learning with negatives outperforms positive-only

**Key insight:** One boundary violation destroys authenticity faster than 10 good patterns build it.

## Two Modes

### Quick Mode (3 Questions)
**Read:** `resources/quick-questions.md`
- 60 seconds to complete
- Captures ~80% of disgust value
- Best for demos, time-constrained situations

### Full Mode (10 Questions)
**Read:** `resources/full-questions.md`
- 5-10 minutes to complete
- Complete voice boundary mapping
- Best for high-stakes implementations

## Process

### Step 1: Choose Mode
Ask user: "Quick (3 questions, 60 sec) or Full (10 questions, 5 min)?"

### Step 2: Run Questions
Present options one at a time. For each:
- Show the options with examples
- User selects one or rates multiple
- User rates disgust level (-100 to -1000)

### Step 3: Generate Profile
**Read:** `resources/output-template.md`
Create the Disgust Profile document.

### Step 4: Integration Notes
Explain how this combines with Voice DNA for Voice Meta.

## Scoring System

**Disgust Scale:**
- -100 = Mildly annoying
- -300 = Definitely wrong
- -500 = Makes me cringe
- -750 = Kills my soul
- -1000 = Would NEVER say this

## Output Files
Save to: `/tools/[creator-name]_disgust_mapper.md`

## Important Rules
1. NEVER skip the disgust rating, the score matters
2. Record specific examples for each boundary
3. Capture reasoning when possible
4. Note any exceptions or context
5. Link to Voice DNA where relevant

## Categories Covered

**Read:** `resources/categories.md`

1. Style Archetypes (corporate, academic, Gen-Z, etc.)
2. Storytelling Styles
3. Political Boundaries
4. Profanity Levels
5. Emotional Tones
6. Earnest vs Ironic Spectrum
7. Structural Patterns
8. Formatting/Buzzword Abuse
9. Metaphor Types
10. Personal Pet Peeves

## Start

Begin with:

"# Disgust Mapper

I'll identify what you would NEVER say, so AI can avoid those patterns.

This creates **negative guardrails** for your voice.

**Two options:**

**Quick Mode** (3 questions, ~60 seconds)
- Captures 80% of voice boundaries
- Good for getting started

**Full Mode** (10 questions, ~5 minutes)
- Complete boundary mapping
- Best for production voice profiles

Which mode would you like?"

## Next Steps

After completion, suggest:
- Combine with `/voice-dna` results for complete Voice Meta Prompt
- Use for quality checking AI-generated content
- Share boundaries with team/VAs for manual writing
