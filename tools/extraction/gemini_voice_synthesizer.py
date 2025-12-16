#!/usr/bin/env python3
"""
Gemini Voice Synthesizer - Deep Brand Intake Tool
Uses Gemini 2.5 Pro's 1-2M token context window to synthesize brand voice from massive content sets

This is Step 0 of the AAA Framework - runs BEFORE Analyze, Architect, Activate

Usage:
    python gemini_voice_synthesizer.py --input-dir ./brand_content --output ./brand_voice_profile.md
    python gemini_voice_synthesizer.py --interactive

Requirements:
    pip install google-generativeai python-dotenv

Environment:
    GOOGLE_API_KEY=your_gemini_api_key (get from https://aistudio.google.com/apikey)
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

try:
    import google.generativeai as genai
except ImportError:
    print("Please install: pip install google-generativeai")
    sys.exit(1)

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Voice Synthesis Prompt - The magic happens here
VOICE_SYNTHESIS_PROMPT = """
You are a world-class brand voice analyst. Your job is to deeply analyze the provided content
and extract a comprehensive Brand Voice DNA Profile.

IMPORTANT: You have access to the COMPLETE content - not summaries or excerpts. This allows you
to identify patterns that only emerge across the full body of work.

Analyze ALL the content I'm providing and create a detailed Brand Voice Profile with these sections:

## 1. VOICE DNA SUMMARY
- Core personality in 3 adjectives
- Primary communication mode (educator/entertainer/inspirer/challenger)
- Emotional register (warm/authoritative/casual/intense)
- One-sentence voice essence

## 2. LINGUISTIC PATTERNS
- Signature phrases (exact recurring phrases, at least 10)
- Sentence structure preferences (short punchy? Complex? Mixed?)
- Opening hooks style (questions? Statements? Stories?)
- Transition patterns
- Closing patterns

## 3. TONE MARKERS
- Humor style (if present) with examples
- How they handle hard truths
- Empathy expressions
- Motivational patterns
- Vulnerability indicators

## 4. CONTENT STRUCTURE DNA
- How they typically open content
- How they build arguments
- Use of stories/anecdotes (frequency, style, purpose)
- Call-to-action patterns
- Length preferences by content type

## 5. VALUES & BELIEFS (Extracted from content)
- Core beliefs expressed repeatedly
- What they push against (anti-values)
- What success looks like to them
- Non-negotiables they mention

## 6. AUDIENCE RELATIONSHIP
- How they address the audience (you, we, guys, friend)
- Assumed audience knowledge level
- How they handle objections
- Trust-building techniques

## 7. ANTI-VOICE (What this person would NEVER say/do)
- Phrases that would feel inauthentic
- Topics they avoid
- Tones that don't fit
- Structural approaches that don't match

## 8. VOICE REPLICATION GUIDE
- 5 specific rules for writing in this voice
- Sample opening sentences in their style
- Sample transitions in their style
- Sample closes in their style

## 9. AUTHENTICITY MARKERS
- Unique quirks only visible across multiple pieces
- Contradictions or tensions in their voice
- Evolution patterns (if content spans time)
- What makes them instantly recognizable

---

Now analyze the following content:
"""


def count_tokens_estimate(text: str) -> int:
    """Rough token estimate (actual tokenization varies by model)"""
    # Gemini uses ~4 chars per token on average
    return len(text) // 4


def load_content_from_directory(directory: Path) -> tuple[str, Dict]:
    """Load all text content from a directory"""
    content_parts = []
    metadata = {
        "files_processed": [],
        "total_files": 0,
        "content_types": {},
        "total_chars": 0
    }

    # Supported file extensions
    text_extensions = {'.txt', '.md', '.json', '.html'}

    for file_path in sorted(directory.rglob('*')):
        if file_path.is_file() and file_path.suffix.lower() in text_extensions:
            try:
                content = file_path.read_text(encoding='utf-8')

                # Add file context
                file_header = f"\n\n{'='*60}\nSOURCE: {file_path.name}\nTYPE: {file_path.suffix}\n{'='*60}\n\n"
                content_parts.append(file_header + content)

                # Update metadata
                metadata["files_processed"].append(str(file_path.name))
                metadata["total_files"] += 1
                metadata["total_chars"] += len(content)

                ext = file_path.suffix.lower()
                metadata["content_types"][ext] = metadata["content_types"].get(ext, 0) + 1

            except Exception as e:
                print(f"Warning: Could not read {file_path}: {e}")

    combined_content = "\n".join(content_parts)
    return combined_content, metadata


def load_content_from_files(file_paths: List[str]) -> tuple[str, Dict]:
    """Load content from specific file paths"""
    content_parts = []
    metadata = {
        "files_processed": [],
        "total_files": 0,
        "total_chars": 0
    }

    for file_path in file_paths:
        path = Path(file_path)
        if path.exists():
            try:
                content = path.read_text(encoding='utf-8')
                file_header = f"\n\n{'='*60}\nSOURCE: {path.name}\n{'='*60}\n\n"
                content_parts.append(file_header + content)

                metadata["files_processed"].append(str(path.name))
                metadata["total_files"] += 1
                metadata["total_chars"] += len(content)
            except Exception as e:
                print(f"Warning: Could not read {file_path}: {e}")
        else:
            print(f"Warning: File not found: {file_path}")

    return "\n".join(content_parts), metadata


def synthesize_voice(
    content: str,
    brand_name: str = "Unknown Brand",
    api_key: Optional[str] = None,
    model: str = "gemini-2.5-flash"
) -> str:
    """Send content to Gemini for voice synthesis

    Models:
    - gemini-2.5-flash: Free tier, 1M context (default)
    - gemini-2.5-pro: Requires billing, 2M context, better quality
    """

    # Configure API
    api_key = api_key or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found. Set it in .env or pass directly.")

    genai.configure(api_key=api_key)

    # Initialize model
    print(f"Using model: {model}")
    if model == "gemini-2.5-pro":
        print("Note: gemini-2.5-pro requires billing. Use --model gemini-2.5-flash for free tier.")

    model_instance = genai.GenerativeModel(model)

    # Estimate tokens
    estimated_tokens = count_tokens_estimate(content)
    print(f"\nContent size: ~{estimated_tokens:,} tokens (estimated)")

    if estimated_tokens > 1_500_000:
        print("Warning: Content may exceed context window. Consider reducing input.")

    # Build the full prompt
    full_prompt = f"""
{VOICE_SYNTHESIS_PROMPT}

BRAND/PERSON: {brand_name}
CONTENT COUNT: Analyzing complete content below

---BEGIN CONTENT---

{content}

---END CONTENT---

Now provide the comprehensive Brand Voice DNA Profile for {brand_name}:
"""

    print(f"\nSending to Gemini {model}...")
    print("This may take 1-3 minutes for large content sets...")

    try:
        response = model_instance.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=8192,
            )
        )
        return response.text
    except Exception as e:
        raise RuntimeError(f"Gemini API error: {e}")


def save_profile(
    profile: str,
    output_path: Path,
    metadata: Dict,
    brand_name: str
):
    """Save the voice profile with metadata"""

    header = f"""---
title: Brand Voice DNA Profile - {brand_name}
generated: {datetime.now().isoformat()}
files_analyzed: {metadata['total_files']}
total_characters: {metadata['total_chars']:,}
estimated_tokens: {metadata['total_chars'] // 4:,}
model: gemini-2.5-pro
---

# Brand Voice DNA Profile: {brand_name}

> Generated from {metadata['total_files']} content pieces (~{metadata['total_chars'] // 4:,} tokens)
> This profile was synthesized using Gemini 2.5 Pro's full context window - not RAG chunks.

---

"""

    full_output = header + profile
    output_path.write_text(full_output, encoding='utf-8')
    print(f"\nProfile saved to: {output_path}")


def interactive_mode():
    """Interactive CLI for content input"""
    print("\n" + "="*60)
    print("GEMINI VOICE SYNTHESIZER - Deep Brand Intake")
    print("="*60)

    brand_name = input("\nBrand/Person name: ").strip()

    print("\nHow would you like to provide content?")
    print("1. Directory path (scans all .txt, .md, .json files)")
    print("2. List of file paths")
    print("3. Paste content directly")

    choice = input("\nChoice (1/2/3): ").strip()

    if choice == "1":
        dir_path = input("Directory path: ").strip()
        content, metadata = load_content_from_directory(Path(dir_path))
    elif choice == "2":
        print("Enter file paths (one per line, empty line to finish):")
        files = []
        while True:
            file = input().strip()
            if not file:
                break
            files.append(file)
        content, metadata = load_content_from_files(files)
    else:
        print("Paste content (enter 'END' on a new line when done):")
        lines = []
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        content = "\n".join(lines)
        metadata = {"files_processed": ["pasted_content"], "total_files": 1, "total_chars": len(content)}

    if not content.strip():
        print("Error: No content provided.")
        return

    print(f"\nLoaded {metadata['total_files']} files, ~{metadata['total_chars']:,} characters")

    # Synthesize
    try:
        profile = synthesize_voice(content, brand_name)
    except Exception as e:
        print(f"Error: {e}")
        return

    # Output
    output_path = Path(f"{brand_name.lower().replace(' ', '_')}_voice_profile.md")
    save_profile(profile, output_path, metadata, brand_name)

    print("\n" + "="*60)
    print("SYNTHESIS COMPLETE")
    print("="*60)
    print(f"\nProfile saved to: {output_path}")
    print("\nNext steps:")
    print("1. Review the profile for accuracy")
    print("2. Use this profile as input for AAA Framework agents")
    print("3. Reference this profile in all brand content generation")


def main():
    parser = argparse.ArgumentParser(
        description="Synthesize brand voice using Gemini's long context"
    )
    parser.add_argument(
        "--input-dir", "-i",
        type=Path,
        help="Directory containing content files"
    )
    parser.add_argument(
        "--files", "-f",
        nargs="+",
        help="Specific files to analyze"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("brand_voice_profile.md"),
        help="Output file path"
    )
    parser.add_argument(
        "--brand", "-b",
        default="Unknown Brand",
        help="Brand/person name"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )
    parser.add_argument(
        "--model",
        default="gemini-2.5-flash",
        help="Gemini model (gemini-2.5-flash=free, gemini-2.5-pro=billing required)"
    )

    args = parser.parse_args()

    if args.interactive or (not args.input_dir and not args.files):
        interactive_mode()
        return

    # Load content
    if args.input_dir:
        content, metadata = load_content_from_directory(args.input_dir)
    else:
        content, metadata = load_content_from_files(args.files)

    if not content.strip():
        print("Error: No content found.")
        sys.exit(1)

    # Synthesize
    try:
        profile = synthesize_voice(content, args.brand, model=args.model)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Save
    save_profile(profile, args.output, metadata, args.brand)


if __name__ == "__main__":
    main()
