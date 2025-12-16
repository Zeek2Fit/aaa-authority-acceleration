#!/usr/bin/env python3
"""
Save podcast transcripts from Firecrawl scrapes
Extracts transcript content and saves to individual files
"""

import os
import re

def extract_transcript_from_markdown(markdown_text):
    """Extract just the transcript portion from Firecrawl markdown"""
    # Find the start of the transcript (Speaker 1:)
    match = re.search(r'(Speaker \d+:\d+:\d+.*)', markdown_text, re.DOTALL)

    if match:
        return match.group(1).strip()
    return None

def clean_transcript(text):
    """Clean up transcript text"""
    # Keep speaker labels for now
    # Just clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def save_transcript(episode_num, title, transcript_text, output_dir):
    """Save transcript to file"""
    # Create safe filename
    safe_title = re.sub(r'[^\w\s-]', '', title).strip()
    safe_title = re.sub(r'[-\s]+', '_', safe_title)

    filename = f"episode_{episode_num:03d}_{safe_title[:50]}.txt"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"{title}\n")
        f.write("="*80 + "\n\n")
        f.write(transcript_text)

    word_count = len(transcript_text.split())
    print(f"✓ Saved: {filename}")
    print(f"  Words: {word_count:,}")

    return word_count

# Output directory
output_dir = "/Users/zeekfit/Documents/Z Brain/tools/stephanie_podcast_transcripts"
os.makedirs(output_dir, exist_ok=True)

print("Saving podcast transcripts...")
print("="*80)

# Manually paste transcript content here for each episode
# (I'll do this via direct file writes since I have the content)
