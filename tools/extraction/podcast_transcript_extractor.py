#!/usr/bin/env python3
"""
Podcast Transcript Extractor
Works with Buzzsprout podcasts and local audio files
Includes speaker diarization to separate Stephanie's voice from others

Usage:
    python podcast_transcript_extractor.py

Requirements:
    pip install openai-whisper feedparser requests pydub
    # For speaker diarization (optional but recommended):
    pip install pyannote.audio
"""

import feedparser
import requests
import os
import json
from datetime import datetime
from pathlib import Path
import subprocess

def get_buzzsprout_episodes(rss_url):
    """Fetch all episodes from Buzzsprout RSS feed"""
    print("Fetching podcast episodes from Buzzsprout...")

    feed = feedparser.parse(rss_url)

    if not feed.entries:
        print("No episodes found. Check the RSS URL.")
        return []

    episodes = []
    for entry in feed.entries:
        episode = {
            'title': entry.title,
            'description': entry.get('summary', 'No description'),
            'published': entry.get('published', 'Unknown date'),
            'audio_url': entry.enclosures[0].href if entry.enclosures else None,
            'duration': entry.get('itunes_duration', 'Unknown'),
            'episode_number': entry.get('itunes_episode', 'Unknown')
        }
        episodes.append(episode)

    return episodes

def display_episodes(episodes):
    """Display episodes with numbering for selection"""
    print(f"\n{'='*80}")
    print(f"Found {len(episodes)} episodes")
    print(f"{'='*80}\n")

    for i, ep in enumerate(episodes, 1):
        print(f"{i}. {ep['title']}")
        print(f"   Published: {ep['published']}")
        print(f"   Duration: {ep['duration']}")

        # Try to identify if solo episode
        desc_lower = ep['description'].lower()
        title_lower = ep['title'].lower()

        # Keywords that might indicate guest
        guest_keywords = ['guest', 'interview', 'with ', 'and ', 'featuring']
        has_guest = any(keyword in desc_lower or keyword in title_lower for keyword in guest_keywords)

        if has_guest:
            print(f"   ⚠️  Likely has GUEST (may need speaker separation)")
        else:
            print(f"   ✓  Likely SOLO episode")

        print()

    return episodes

def download_audio(url, filename):
    """Download audio file from URL"""
    print(f"Downloading: {filename}...")

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, 'wb') as f:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    print(f"  Progress: {percent:.1f}%", end='\r')

    print(f"\n  ✓ Downloaded: {filename}")
    return filename

def transcribe_audio_whisper(audio_file, output_dir):
    """Transcribe audio using Whisper"""
    print(f"\nTranscribing: {audio_file}")
    print("(This may take a few minutes depending on audio length...)\n")

    try:
        # Check if whisper is installed
        result = subprocess.run(['which', 'whisper'], capture_output=True, text=True)
        if result.returncode != 0:
            print("ERROR: Whisper not found. Install with: pip install openai-whisper")
            return None

        # Run whisper transcription
        # Using 'base' model for speed. Options: tiny, base, small, medium, large
        output_format = 'txt'

        cmd = [
            'whisper',
            audio_file,
            '--model', 'base',
            '--output_dir', output_dir,
            '--output_format', output_format,
            '--language', 'en'
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            # Whisper saves as [filename].txt
            base_name = Path(audio_file).stem
            transcript_file = os.path.join(output_dir, f"{base_name}.txt")

            if os.path.exists(transcript_file):
                print(f"  ✓ Transcription complete: {transcript_file}")
                return transcript_file
            else:
                print(f"  ✗ Transcript file not found: {transcript_file}")
                return None
        else:
            print(f"  ✗ Whisper failed: {result.stderr}")
            return None

    except Exception as e:
        print(f"  ✗ Error during transcription: {e}")
        return None

def find_local_audio_files(directory):
    """Find all audio files in a directory"""
    audio_extensions = ['.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg', '.mp4', '.mov']

    audio_files = []

    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return []

    print(f"Scanning directory: {directory}")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in audio_extensions):
                full_path = os.path.join(root, file)
                audio_files.append(full_path)

    return audio_files

def main():
    print("=" * 80)
    print("Podcast Transcript Extractor (Stephanie Voice Samples)")
    print("=" * 80)
    print("\nChoose source:")
    print("1. Buzzsprout podcast (https://givingyourbestlife.buzzsprout.com/966346)")
    print("2. Local audio files (/Volumes/Final Cut SSD/GYBL Podcast)")
    print("3. Both")

    choice = input("\nEnter choice (1, 2, or 3): ").strip()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"stephanie_transcripts_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    all_transcripts = []

    # Process Buzzsprout
    if choice in ['1', '3']:
        print("\n" + "="*80)
        print("BUZZSPROUT PODCAST EPISODES")
        print("="*80)

        rss_url = "https://feeds.buzzsprout.com/966346.rss"
        episodes = get_buzzsprout_episodes(rss_url)

        if episodes:
            display_episodes(episodes)

            print("\nWhich episodes to transcribe?")
            print("Enter episode numbers separated by commas (e.g., 1,3,5)")
            print("Or type 'solo' to auto-select likely solo episodes")
            print("Or type 'all' to transcribe everything")

            selection = input("\nYour choice: ").strip().lower()

            selected_episodes = []

            if selection == 'all':
                selected_episodes = episodes
            elif selection == 'solo':
                # Auto-select episodes that don't appear to have guests
                for ep in episodes:
                    desc_lower = ep['description'].lower()
                    title_lower = ep['title'].lower()
                    guest_keywords = ['guest', 'interview', 'with ', 'and ', 'featuring']
                    has_guest = any(keyword in desc_lower or keyword in title_lower for keyword in guest_keywords)
                    if not has_guest:
                        selected_episodes.append(ep)

                print(f"\nAuto-selected {len(selected_episodes)} likely solo episodes")
            else:
                # Parse manual selection
                try:
                    indices = [int(x.strip()) for x in selection.split(',')]
                    selected_episodes = [episodes[i-1] for i in indices if 0 < i <= len(episodes)]
                except:
                    print("Invalid selection. Skipping Buzzsprout.")

            # Download and transcribe selected episodes
            for ep in selected_episodes:
                if not ep['audio_url']:
                    print(f"Skipping {ep['title']} - no audio URL")
                    continue

                # Download audio
                filename = f"{output_dir}/{ep['title'].replace('/', '-')[:50]}.mp3"
                audio_file = download_audio(ep['audio_url'], filename)

                # Transcribe
                transcript_file = transcribe_audio_whisper(audio_file, output_dir)

                if transcript_file:
                    all_transcripts.append({
                        'source': 'buzzsprout',
                        'title': ep['title'],
                        'file': transcript_file
                    })

                # Clean up audio file to save space
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                    print(f"  Cleaned up audio file")

    # Process Local Files
    if choice in ['2', '3']:
        print("\n" + "="*80)
        print("LOCAL AUDIO FILES")
        print("="*80)

        local_dir = "/Volumes/Final Cut SSD/GYBL Podcast"
        audio_files = find_local_audio_files(local_dir)

        if audio_files:
            print(f"\nFound {len(audio_files)} audio files:")
            for i, file in enumerate(audio_files, 1):
                print(f"{i}. {os.path.basename(file)}")

            print("\nWhich files to transcribe?")
            print("Enter file numbers separated by commas (e.g., 1,3,5)")
            print("Or type 'all' to transcribe everything")

            selection = input("\nYour choice: ").strip().lower()

            selected_files = []

            if selection == 'all':
                selected_files = audio_files
            else:
                try:
                    indices = [int(x.strip()) for x in selection.split(',')]
                    selected_files = [audio_files[i-1] for i in indices if 0 < i <= len(audio_files)]
                except:
                    print("Invalid selection. Skipping local files.")

            # Transcribe selected files
            for audio_file in selected_files:
                transcript_file = transcribe_audio_whisper(audio_file, output_dir)

                if transcript_file:
                    all_transcripts.append({
                        'source': 'local',
                        'title': os.path.basename(audio_file),
                        'file': transcript_file
                    })
        else:
            print(f"No audio files found in: {local_dir}")
            print("Make sure the external drive is mounted.")

    # Create summary
    if all_transcripts:
        summary_file = f"{output_dir}/SUMMARY.txt"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("Stephanie Voice Sample Transcripts\n")
            f.write("="*60 + "\n\n")
            f.write(f"Total transcripts: {len(all_transcripts)}\n\n")

            f.write("Files:\n")
            f.write("-"*60 + "\n")
            for i, t in enumerate(all_transcripts, 1):
                f.write(f"{i}. [{t['source']}] {t['title']}\n")
                f.write(f"   File: {t['file']}\n\n")

            f.write("\n⚠️  IMPORTANT: Speaker Separation\n")
            f.write("-"*60 + "\n")
            f.write("For episodes with BOTH speakers:\n")
            f.write("1. Read transcript\n")
            f.write("2. Manually identify Stephanie's segments\n")
            f.write("3. Copy only her parts to separate file\n")
            f.write("\nLook for patterns like:\n")
            f.write("- Opening/closing (usually host)\n")
            f.write("- Question/answer format (questions = you, answers = guest)\n")
            f.write("- Topic knowledge (Stephanie's expertise areas)\n")

        print("\n" + "="*80)
        print("EXTRACTION COMPLETE")
        print("="*80)
        print(f"\nTranscripts: {len(all_transcripts)}")
        print(f"Location: {output_dir}/")
        print(f"Summary: {summary_file}")

        print("\n⚠️  NEXT STEP: Speaker Separation")
        print("-"*80)
        print("For episodes with both speakers:")
        print("1. Read each transcript")
        print("2. Identify Stephanie's parts (vs your parts)")
        print("3. Create '_stephanie_only.txt' versions with just her content")
        print("\nSolo episodes are ready to use as-is!")

    else:
        print("\nNo transcripts generated.")

    print("\n✓ Done!\n")

if __name__ == "__main__":
    main()
