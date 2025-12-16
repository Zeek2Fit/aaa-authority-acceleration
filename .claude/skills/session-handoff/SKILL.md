# Session Handoff Skill

> **Context Reset Helper** - Update progress files and generate resume prompt for next session

## Purpose
When the user needs to reset context (context window full, switching tasks, ending session), this skill:
1. Updates PROGRESS.md with what was accomplished
2. Updates NEXT_STEPS.md with current status and next actions
3. Generates a comprehensive resume prompt for the next context window

## Trigger Keywords
- "session handoff"
- "context reset"
- "prepare handoff"
- "end session"
- "progress next" (shorthand)

## Process

### Step 1: Gather Session Summary
Ask or infer:
- What project are we working on?
- What was accomplished this session?
- What's the current status?
- What are the immediate next steps?
- Any critical context the next session needs?

### Step 2: Update PROGRESS.md
Find the project's PROGRESS.md file and append:

```markdown
---

### [DATE] - [Session Description]
**Session Duration:** ~X minutes
**Status:** [Current status]

**Completed:**
- [x] Task 1
- [x] Task 2
- [x] Task 3

**Key Decisions/Discoveries:**
- [Important finding 1]
- [Important finding 2]

**Files Created/Modified:**
- `path/to/file1` (description)
- `path/to/file2` (description)

---

## CURRENT STATUS ([Date])

**What's Built:**
- [Summary of what exists]

**What's Next:**
- [Immediate next steps]

---

*Last updated: [Date] ([Session description])*
```

### Step 3: Update NEXT_STEPS.md
Update the header and current status section:

```markdown
# [Project] - Next Steps

**Updated:** [Date] ([Session description])
**Current Phase:** [Phase name]
**Status:** [One-line status]
**[Key deadline if any]**

---

## SESSION STATUS - [Status Header]

### Completed ([Date]):
1. [x] Task 1
2. [x] Task 2

### Next Actions:
1. [ ] Immediate task 1
2. [ ] Immediate task 2

---

## [Rest of existing content...]
```

### Step 4: Generate Resume Prompt
Create a comprehensive prompt the user can copy for the next session:

```
[PROJECT NAME] - RESUME SESSION

WORKING DIRECTORY: [path]

OBJECTIVE: [Clear statement of what needs to happen next]

WHAT WAS JUST COMPLETED:
- [Completed item 1]
- [Completed item 2]
- [Completed item 3]

CURRENT STATUS:
- [Key status point 1]
- [Key status point 2]

KEY DATA/IDs (if applicable):
- [Important IDs, paths, or values needed]

NEXT STEPS:
1. [Step 1]
2. [Step 2]
3. [Step 3]

READ FIRST:
- [Path to NEXT_STEPS.md]
- [Path to PROGRESS.md]
- [Any other critical files]

[DEADLINE/CONTEXT if applicable]

WHAT TO DO:
[Clear instruction for what Claude should do first]
```

## Output Format

Present the resume prompt in a code block so the user can easily copy it:

```
---

## COPY THIS PROMPT FOR NEXT SESSION:

```
[The full resume prompt here]
```

---

Files updated:
- [path/to/PROGRESS.md] - Added session summary
- [path/to/NEXT_STEPS.md] - Updated status

Ready to reset context.
```

## Important Rules

1. **Always update both files** - PROGRESS.md and NEXT_STEPS.md
2. **Include specific IDs/paths** - The next session needs concrete data, not abstractions
3. **Be comprehensive but concise** - Include everything needed, nothing extra
4. **Use the project's existing format** - Match the style already in the files
5. **Include READ FIRST section** - Tell next session exactly what to read
6. **Make it copy-pasteable** - The resume prompt should work as-is

## Example Usage

**User:** "progress next"

**Claude:**
1. Summarizes what was done this session
2. Updates PROGRESS.md with session log
3. Updates NEXT_STEPS.md with current status
4. Generates resume prompt in code block
5. Confirms files updated and ready for reset

## Quick Reference

For Black Sheep Systems project:
- PROGRESS.md: `/Users/zeekfit/Documents/Z Brain/projects/black-sheep-systems/PROGRESS.md`
- NEXT_STEPS.md: `/Users/zeekfit/Documents/Z Brain/projects/black-sheep-systems/NEXT_STEPS.md`
- Working Dir: `/Users/zeekfit/Documents/Z Brain`
