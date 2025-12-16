#!/usr/bin/env python3
"""
Batch Buzzsprout Transcript Extractor
Extracts transcripts from Buzzsprout episodes using Firecrawl
"""

import json
import os
import re
from datetime import datetime

def extract_transcript_from_markdown(markdown_content):
    """Extract just the transcript portion from Firecrawl markdown"""
    # The transcript starts with "Speaker 1:" followed by timestamp
    # Split on that pattern to find where transcript begins

    # Look for the pattern "Speaker 1:" followed by a timestamp
    transcript_match = re.search(r'(Speaker \d+:\d+:\d+.*)', markdown_content, re.DOTALL)

    if transcript_match:
        transcript_text = transcript_match.group(1)

        # Clean up - remove timestamps but keep speaker labels
        # Convert "Speaker 1:12:34" to just paragraph breaks
        cleaned = re.sub(r'Speaker \d+:\d+:\d+\n\n', '\n\n', transcript_text)

        return cleaned.strip()
    else:
        # Fallback: return everything after "Transcript" heading
        lines = markdown_content.split('\n')
        transcript_started = False
        transcript_lines = []

        for line in lines:
            if 'Speaker 1:' in line and ':' in line:
                transcript_started = True

            if transcript_started:
                transcript_lines.append(line)

        return '\n'.join(transcript_lines).strip()

def clean_transcript(text):
    """Clean transcript by removing speaker labels and timestamps"""
    # Remove "Speaker 1:" labels
    text = re.sub(r'Speaker \d+:', '', text)

    # Remove timestamps like "0:00" or "12:34"
    text = re.sub(r'\d+:\d+', '', text)

    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text

# Note: This script requires the Firecrawl API
# You'll need to run this with access to the Firecrawl MCP server

print("Batch Buzzsprout Transcript Extractor")
print("=" * 80)
print("\nThis script uses Firecrawl to extract transcripts from Buzzsprout episodes.")
print("Run this via Claude Code with Firecrawl MCP server access.\n")

# Load episode data
script_dir = os.path.dirname(os.path.abspath(__file__))
episodes_file = os.path.join(script_dir, 'buzzsprout_solo_episodes.json')

with open(episodes_file, 'r') as f:
    episodes = json.load(f)

print(f"Loaded {len(episodes)} episodes from {episodes_file}")
print(f"\nTo extract transcripts, use the Firecrawl MCP tool for each episode URL:")
print(f"Example: mcp__firecrawl__firecrawl_scrape")
print(f"\nEpisode URLs:")

for i, ep in enumerate(episodes, 1):
    # Construct Buzzsprout episode URL
    title_slug = ep['audio_url'].split('/')[-1].replace('.mp3', '')
    episode_url = f"https://www.buzzsprout.com/966346/episodes/{title_slug}"
    print(f"{i}. {episode_url}")
