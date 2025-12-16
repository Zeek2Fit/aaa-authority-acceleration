#!/usr/bin/env python3
"""
Save all scraped podcast transcripts to individual files
Extracts clean transcript text from Firecrawl markdown
"""

import os
import re

# Output directory
output_dir = "/Users/zeekfit/Documents/Z Brain/tools/stephanie_podcast_transcripts"
os.makedirs(output_dir, exist_ok=True)

def extract_transcript(markdown_text):
    """Extract just the Speaker 1: transcript portion"""
    # Find the start of the transcript (Speaker 1:)
    match = re.search(r'(Speaker \d+:\d+:\d+.*)', markdown_text, re.DOTALL | re.IGNORECASE)

    if match:
        transcript = match.group(1).strip()
        # Clean up excessive newlines
        transcript = re.sub(r'\n{3,}', '\n\n', transcript)
        return transcript
    return None

def save_transcript(episode_num, title, transcript_text):
    """Save transcript to individual file"""
    filename = f"episode_{episode_num:03d}.txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"{title}\n")
        f.write("="*80 + "\n\n")
        f.write(transcript_text)

    word_count = len(transcript_text.split())
    print(f"✓ Saved {filename}: {word_count:,} words")
    return word_count

# This script will be called with transcript data from Claude
# The actual saving will happen through Python execution with the scraped data

print("Ready to save scraped transcripts...")
print("="*80)
