#!/usr/bin/env python3
"""
Extract all Stephanie podcast transcripts from Buzzsprout
Uses episode list from buzzsprout_solo_episodes.json
Saves clean transcripts to stephanie_podcast_transcripts/
"""

import json
import os
import re

def extract_episode_slug(audio_url):
    """Extract episode slug from audio URL for constructing web URL"""
    # From: https://www.buzzsprout.com/966346/episodes/16776008-episode-124-living-the-only-god-mindset.mp3
    # Get: 16776008-episode-124-living-the-only-god-mindset
    slug = audio_url.split('/')[-1].replace('.mp3', '')
    return slug

def construct_buzzsprout_url(audio_url):
    """Construct Buzzsprout web page URL from audio URL"""
    slug = extract_episode_slug(audio_url)
    # Buzzsprout show ID is 966346
    return f"https://www.buzzsprout.com/966346/episodes/{slug}"

# Load episode data
script_dir = os.path.dirname(os.path.abspath(__file__))
episodes_file = os.path.join(script_dir, 'buzzsprout_solo_episodes.json')

with open(episodes_file, 'r') as f:
    episodes = json.load(f)

print("Buzzsprout Transcript Extractor")
print("=" * 80)
print(f"\nFound {len(episodes)} solo episodes to extract\n")

# Create output directory
output_dir = os.path.join(script_dir, 'stephanie_podcast_transcripts')
os.makedirs(output_dir, exist_ok=True)

print("Episode URLs to scrape with Firecrawl MCP:")
print("-" * 80)

for i, episode in enumerate(episodes, 1):
    episode_url = construct_buzzsprout_url(episode['audio_url'])
    duration_min = int(episode['duration']) // 60

    print(f"\n{i}. Episode {episode['number']}: {episode['title']}")
    print(f"   Duration: {duration_min} minutes")
    print(f"   URL: {episode_url}")

print("\n" + "=" * 80)
print("\nNext Step: Use Claude's Firecrawl MCP to scrape each URL above")
print("Then extract 'Speaker 1:' transcript content and save to individual files")
