# Disgust Mapper Output Template

Use this structure for the final output document.

```markdown
# DISGUST PROFILE: [Name/Brand]

**Analysis Date:** [Date]
**Mode:** [Quick 3-Question | Full 10-Question]
**Total Disgust Score:** [Sum of all scores]

---

## TOP 3 CRITICAL BOUNDARIES

### Boundary #1: [Type]
**Category:** [Category name]
**Score:** [Number]
**ABSOLUTE NEVER:**
- [Example 1]
- [Example 2]
- [Example 3]

### Boundary #2: [Type]
**Category:** [Category name]
**Score:** [Number]
**ABSOLUTE NEVER:**
- [Example 1]
- [Example 2]
- [Example 3]

### Boundary #3: [Type]
**Category:** [Category name]
**Score:** [Number]
**ABSOLUTE NEVER:**
- [Example 1]
- [Example 2]
- [Example 3]

---

## COMPLETE BOUNDARY LIST

### Style Archetypes
| Type | Score | Status |
|------|-------|--------|
| Corporate Jargon | [score] | [BLOCK/WARN/OK] |
| Academic Speak | [score] | [BLOCK/WARN/OK] |
| Gen-Z Slang | [score] | [BLOCK/WARN/OK] |
| [etc.] | | |

### Taboo Topics
| Type | Score | Status |
|------|-------|--------|
| Political Content | [score] | [NEVER/CONTEXT/OK] |
| Profanity | [score] | [level description] |

### Emotional Tones
| Type | Score | Status |
|------|-------|--------|
| Toxic Positivity | [score] | [BLOCK/WARN/OK] |
| Cynical Snark | [score] | [BLOCK/WARN/OK] |
| Preachy Moralizing | [score] | [BLOCK/WARN/OK] |
| Victim Mentality | [score] | [BLOCK/WARN/OK] |

### Structural Patterns
| Type | Score | Status |
|------|-------|--------|
| Passive Voice | [score] | [BLOCK/WARN/OK] |
| Emoji Overload | [score] | [BLOCK/WARN/OK] |
| CAPS LOCK | [score] | [BLOCK/WARN/OK] |
| [etc.] | | |

### Personal Quirks
| Type | Score | Status |
|------|-------|--------|
| [Metaphor type] | [score] | [AVOID/OK] |
| [Pet peeve] | [score] | [AVOID/OK] |

---

## VOICE META INTEGRATION

### Priority 1: DISGUST GUARDRAILS (NEVER VIOLATE)

These boundaries override Voice DNA patterns:

```
CRITICAL DISGUST GUARDRAILS:
- [Boundary #1] (Score: [X]) - ABSOLUTE NEVER
- [Boundary #2] (Score: [X]) - ABSOLUTE NEVER
- [Boundary #3] (Score: [X]) - ABSOLUTE NEVER
```

### Priority 2: Voice DNA Patterns (Match these)

[Reference Voice DNA profile when available]

### Conflict Resolution

If Voice DNA suggests something that triggers a Disgust boundary:
1. Disgust boundary WINS
2. Find alternative phrasing
3. The negative is MORE important than the positive

---

## QUALITY CHECK PROMPT

Use this to verify AI-generated content:

```
Before publishing, check for these violations:

[ ] Does it contain [Boundary #1]?
[ ] Does it contain [Boundary #2]?
[ ] Does it contain [Boundary #3]?
[ ] Does it use forbidden metaphor types?
[ ] Does it have personal pet peeve patterns?

If ANY box is checked, REWRITE before publishing.
```

---

## QUICK REFERENCE CARD

### 10 Things [Name] Would NEVER Say:
1. [Example]
2. [Example]
3. [Example]
4. [Example]
5. [Example]
6. [Example]
7. [Example]
8. [Example]
9. [Example]
10. [Example]

### Emergency Guardrails:
- NEVER: [Top violation]
- NEVER: [Second violation]
- NEVER: [Third violation]

---

## RECOMMENDED NEXT STEPS

1. Combine with Voice DNA for complete Voice Meta Prompt
2. Share Quick Reference Card with team/VAs
3. Use Quality Check Prompt before publishing
4. Review boundaries quarterly for evolution
```
