#!/usr/bin/env python3
"""
Kit Email Sequence Extractor
Extracts subject lines and full email content from Kit email sequences
"""
import json
import sys
from playwright.sync_api import sync_playwright

def extract_kit_sequence(url: str, output_file: str = None):
    """
    Extract email subjects and content from a Kit sequence

    Args:
        url: The Kit sequence URL (e.g., https://app.kit.com/sequences/2470622)
        output_file: Optional JSON output file path
    """
    with sync_playwright() as p:
        # Launch browser in non-headless mode to use existing session
        browser = p.chromium.connect_over_cdp("http://localhost:9222")

        # Get or create a page
        if len(browser.contexts) > 0:
            context = browser.contexts[0]
            if len(context.pages) > 0:
                page = context.pages[0]
            else:
                page = context.new_page()
        else:
            context = browser.new_context()
            page = context.new_page()

        # Navigate to the sequence URL
        page.goto(url)

        # Wait for the page to load
        page.wait_for_load_state('networkidle')

        emails = []

        # Try to find email elements - adjust selectors based on Kit's structure
        # This is a placeholder - we'll need to inspect the actual page
        email_items = page.query_selector_all('[data-email-item]')  # Adjust selector

        for item in email_items:
            try:
                subject = item.query_selector('[data-subject]').inner_text()  # Adjust selector

                # Click to view full email
                item.click()
                page.wait_for_timeout(500)  # Wait for email content to load

                content = page.query_selector('[data-email-content]').inner_text()  # Adjust selector

                emails.append({
                    'subject': subject,
                    'content': content
                })
            except Exception as e:
                print(f"Error extracting email: {e}")
                continue

        # Output results
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(emails, f, indent=2)
            print(f"Extracted {len(emails)} emails to {output_file}")
        else:
            print(json.dumps(emails, indent=2))

        browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python kit_email_extractor.py <sequence_url> [output_file.json]")
        sys.exit(1)

    url = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else None

    extract_kit_sequence(url, output)
