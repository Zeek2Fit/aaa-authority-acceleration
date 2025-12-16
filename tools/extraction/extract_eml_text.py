#!/usr/bin/env python3
"""
Extract text content from .eml files for Voice DNA analysis
"""

import os
import email
from email import policy
from email.parser import BytesParser
import re
from html.parser import HTMLParser

class HTMLTextExtractor(HTMLParser):
    """Extract text from HTML content"""
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def get_text(self):
        return ''.join(self.text)

def extract_text_from_html(html_content):
    """Convert HTML to plain text"""
    parser = HTMLTextExtractor()
    parser.feed(html_content)
    text = parser.get_text()

    # Clean up excessive whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r' +', ' ', text)

    return text.strip()

def extract_email_content(eml_file_path):
    """Extract text content from an .eml file"""
    with open(eml_file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    # Get subject
    subject = msg.get('Subject', 'No Subject')

    # Get body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/plain':
                body = part.get_content()
                break
            elif content_type == 'text/html' and not body:
                html_content = part.get_content()
                body = extract_text_from_html(html_content)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain':
            body = msg.get_content()
        elif content_type == 'text/html':
            html_content = msg.get_content()
            body = extract_text_from_html(html_content)

    # Format output
    output = f"Subject: {subject}\n\n{body}"

    return output, len(output.split())

def main():
    eml_dir = "/Users/zeekfit/Documents/Z Brain/projects/black-sheep-systems/vibe-marketing/eml forwards for stephanie newsletter"
    output_dir = "/Users/zeekfit/Documents/Z Brain/tools/stephanie_email_samples"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get all .eml files
    eml_files = sorted([f for f in os.listdir(eml_dir) if f.endswith('.eml')])

    total_words = 0
    extracted_count = 0

    print(f"Extracting text from {len(eml_files)} .eml files...")
    print()

    for idx, eml_file in enumerate(eml_files, 1):
        eml_path = os.path.join(eml_dir, eml_file)

        try:
            content, word_count = extract_email_content(eml_path)

            # Save as .txt file
            output_filename = f"email_{idx:02d}.txt"
            output_path = os.path.join(output_dir, output_filename)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

            total_words += word_count
            extracted_count += 1

            print(f"✓ {output_filename} - {word_count:,} words")

        except Exception as e:
            print(f"✗ Error processing {eml_file}: {e}")

    print()
    print(f"{'='*60}")
    print(f"Extraction complete!")
    print(f"Files processed: {extracted_count}/{len(eml_files)}")
    print(f"Total words: {total_words:,}")
    print(f"Output directory: {output_dir}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
