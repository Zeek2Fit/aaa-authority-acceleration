#!/usr/bin/env python3
"""
Save all 14 newly scraped podcast transcripts
Episode 124 is already saved, so this handles episodes:
123, 122, 121, 120, 119, 116, 115, 113, 112, 111, 110, 105, 102, 100
"""

import os
import re

output_dir = "/Users/zeekfit/Documents/Z Brain/tools/stephanie_podcast_transcripts"
os.makedirs(output_dir, exist_ok=True)

def save_episode(num, title, content):
    """Save episode transcript to file"""
    # Extract transcript portion (everything after "Speaker")
    transcript_match = re.search(r'(Speaker \d+:\d+:\d+.*)', content, re.DOTALL)
    if transcript_match:
        transcript = transcript_match.group(1)
        # Remove excessive newlines
        transcript = re.sub(r'\n{3,}', '\n\n', transcript)

        filename = f"episode_{num:03d}.txt"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"{title}\n")
            f.write("="*80 + "\n\n")
            f.write(transcript.strip())

        words = len(transcript.split())
        print(f"✓ Episode {num}: {words:,} words")
        return words
    return 0

# Episode data with full markdown content from Firecrawl
episodes = {
    123: ("Episode 123: What Happens When You Trust God?", """[Content from episode 123 scrape]"""),
    # ... I'll need to pass the actual content from the scrapes
}

print("Saving podcast transcripts...")
print("="*80)

total_words = 0

# I'll save each individually using the scraped content
# This is a template - the actual saving will happen via bash with the full content

print("\nReady to save all episodes...")
