#!/usr/bin/env python3
"""
YouTube Transcript Extractor
Batch download transcripts from multiple YouTube videos

Usage:
    python youtube_transcript_extractor.py

Then paste your URLs when prompted (one per line, empty line to finish)
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import re
import os
from datetime import datetime

def extract_video_id(url):
    """Extract video ID from various YouTube URL formats"""
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/)([0-9A-Za-z_-]{11})',
        r'^([0-9A-Za-z_-]{11})$'
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(video_id, video_url):
    """Fetch transcript for a single video"""
    try:
        # Try to get English transcript first
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        try:
            # Try manual English transcript first (most accurate)
            transcript = transcript_list.find_manually_created_transcript(['en'])
        except:
            # Fall back to auto-generated
            transcript = transcript_list.find_generated_transcript(['en'])

        # Get the actual transcript data
        transcript_data = transcript.fetch()

        # Combine all text segments
        full_text = ' '.join([entry['text'] for entry in transcript_data])

        # Clean up the text
        full_text = full_text.replace('\n', ' ')
        full_text = re.sub(r'\s+', ' ', full_text)

        return {
            'success': True,
            'text': full_text,
            'type': 'manual' if transcript.is_generated == False else 'auto-generated',
            'word_count': len(full_text.split())
        }

    except TranscriptsDisabled:
        return {
            'success': False,
            'error': 'Transcripts are disabled for this video'
        }
    except NoTranscriptFound:
        return {
            'success': False,
            'error': 'No English transcript found'
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def main():
    print("=" * 60)
    print("YouTube Transcript Extractor")
    print("=" * 60)
    print("\nPaste your YouTube URLs below (one per line)")
    print("Press Enter twice when done:\n")

    # Collect URLs
    urls = []
    while True:
        url = input().strip()
        if not url:
            break
        urls.append(url)

    if not urls:
        print("\nNo URLs provided. Exiting.")
        return

    print(f"\n✓ Found {len(urls)} URLs")
    print("\nProcessing transcripts...\n")

    # Create output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"youtube_transcripts_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    # Process each URL
    results = []
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] Processing: {url[:50]}...")

        video_id = extract_video_id(url)
        if not video_id:
            print(f"  ✗ Invalid URL format\n")
            results.append({
                'url': url,
                'success': False,
                'error': 'Invalid URL format'
            })
            continue

        result = get_transcript(video_id, url)
        result['url'] = url
        result['video_id'] = video_id
        results.append(result)

        if result['success']:
            # Save transcript to file
            filename = f"{output_dir}/transcript_{i}_{video_id}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"URL: {url}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write(f"Transcript Type: {result['type']}\n")
                f.write(f"Word Count: {result['word_count']}\n")
                f.write(f"\n{'=' * 60}\n\n")
                f.write(result['text'])

            print(f"  ✓ Success ({result['type']}, {result['word_count']} words)")
            print(f"    Saved to: {filename}\n")
        else:
            print(f"  ✗ Error: {result['error']}\n")

    # Create summary file
    summary_file = f"{output_dir}/SUMMARY.txt"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("YouTube Transcript Extraction Summary\n")
        f.write(f"{'=' * 60}\n\n")
        f.write(f"Total URLs processed: {len(urls)}\n")
        f.write(f"Successful: {sum(1 for r in results if r['success'])}\n")
        f.write(f"Failed: {sum(1 for r in results if not r['success'])}\n\n")

        f.write("Details:\n")
        f.write("-" * 60 + "\n\n")

        for i, result in enumerate(results, 1):
            f.write(f"{i}. {result['url']}\n")
            if result['success']:
                f.write(f"   ✓ SUCCESS ({result['type']}, {result['word_count']} words)\n")
                f.write(f"   File: transcript_{i}_{result['video_id']}.txt\n")
            else:
                f.write(f"   ✗ FAILED: {result['error']}\n")
            f.write("\n")

        # Total word count
        total_words = sum(r.get('word_count', 0) for r in results if r['success'])
        f.write(f"\nTotal words extracted: {total_words:,}\n")

    # Print summary
    print("\n" + "=" * 60)
    print("EXTRACTION COMPLETE")
    print("=" * 60)
    print(f"\nSuccessful: {sum(1 for r in results if r['success'])}/{len(urls)}")
    print(f"Total words: {sum(r.get('word_count', 0) for r in results if r['success']):,}")
    print(f"\nAll files saved to: {output_dir}/")
    print(f"Summary: {summary_file}")
    print("\n✓ Done!\n")

if __name__ == "__main__":
    main()
