#!/usr/bin/env python3
"""
Extract all broadcast emails from Kit campaigns
"""
import json
import os
from playwright.sync_api import sync_playwright

def extract_kit_broadcasts(campaigns_url="https://app.kit.com/campaigns", email=None, password=None):
    """Extract all broadcast emails with subjects and content

    Credentials should be passed as arguments or set as environment variables:
    - KIT_EMAIL
    - KIT_PASSWORD
    """
    email = email or os.environ.get("KIT_EMAIL")
    password = password or os.environ.get("KIT_PASSWORD")

    if not email or not password:
        raise ValueError("Kit credentials required. Set KIT_EMAIL and KIT_PASSWORD environment variables.")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            headless=False
        )

        context = browser.new_context()
        page = context.new_page()

        # Navigate and login
        print(f"Navigating to {campaigns_url}")
        page.goto(campaigns_url, wait_until='networkidle')

        if "login" in page.url.lower():
            print("Logging in...")
            page.fill('input[name="user[email]"]', email)
            page.fill('input[name="user[password]"]', password)
            page.click('#user_log_in')
            page.wait_for_load_state('networkidle', timeout=15000)

            if 'verify' in page.url.lower():
                print("✋ Waiting for 2FA verification (complete on your phone)...")
                page.wait_for_url(lambda url: 'verify' not in url.lower(), timeout=120000)
                print("✓ Verified!")

            page.goto(campaigns_url, wait_until='networkidle')

        # Wait for page to load
        page.wait_for_timeout(3000)

        # Take screenshot to inspect page
        page.screenshot(path='/Users/zeekfit/Documents/Z Brain/kit_broadcasts_page.png', full_page=True)
        print("Saved screenshot to kit_broadcasts_page.png")

        # Save HTML for inspection
        with open('/Users/zeekfit/Documents/Z Brain/kit_broadcasts_page.html', 'w') as f:
            f.write(page.content())
        print("Saved HTML to kit_broadcasts_page.html")

        broadcasts = []

        # Get all broadcast items
        # Try to find broadcast rows/items
        broadcast_items = page.query_selector_all('[data-testid="campaign-row"], tr[data-id], .campaign-row, a[href*="/campaigns/"]')

        if not broadcast_items:
            # Alternative: find all links that contain "campaigns"
            all_links = page.query_selector_all('a')
            broadcast_items = [link for link in all_links if '/campaigns/' in link.get_attribute('href') or '']

        print(f"Found {len(broadcast_items)} broadcast items")

        # Extract broadcast data
        for idx, item in enumerate(broadcast_items, 1):
            try:
                # Try to get subject from the item text
                item_text = item.inner_text().strip()
                subject = item_text.split('\n')[0] if '\n' in item_text else item_text

                # Click to view the broadcast
                item.click()
                page.wait_for_timeout(1000)

                # Try to get better subject from subject line input/field
                subject_selectors = [
                    'input[name="broadcast[subject]"]',
                    'input[id*="subject"]',
                    '[data-testid="subject-line"]',
                    '.subject-line'
                ]

                for selector in subject_selectors:
                    subject_el = page.query_selector(selector)
                    if subject_el:
                        subject_value = subject_el.get_attribute('value') or subject_el.inner_text()
                        if subject_value:
                            subject = subject_value
                            break

                # Extract email content
                content_selectors = [
                    '[contenteditable="true"]',
                    '.ql-editor',
                    '[data-testid="email-content"]',
                    '.email-content'
                ]

                content = ""
                for selector in content_selectors:
                    content_el = page.query_selector(selector)
                    if content_el:
                        content = content_el.inner_text().strip()
                        break

                broadcasts.append({
                    'number': idx,
                    'subject': subject,
                    'content': content
                })

                print(f"✓ {idx}. {subject[:70]}...")

                # Go back to campaigns list
                page.go_back(wait_until='networkidle')

            except Exception as e:
                print(f"✗ Error extracting broadcast {idx}: {str(e)[:100]}")
                # Try to go back to list
                try:
                    page.go_back(wait_until='networkidle')
                except:
                    page.goto(campaigns_url, wait_until='networkidle')
                continue

        # Save results
        output_json = '/Users/zeekfit/Documents/Z Brain/kit_broadcasts.json'
        output_md = '/Users/zeekfit/Documents/Z Brain/kit_broadcasts.md'

        # Save JSON
        with open(output_json, 'w') as f:
            json.dump(broadcasts, f, indent=2)

        # Save Markdown
        md_content = f'# Kit Broadcast Emails\n\n**Total Broadcasts:** {len(broadcasts)}\n\n---\n\n'
        for broadcast in broadcasts:
            md_content += f'## Broadcast {broadcast["number"]}\n\n'
            md_content += f'### Subject Line\n{broadcast["subject"]}\n\n'
            md_content += f'### Email Content\n\n{broadcast["content"]}\n\n'
            md_content += '---\n\n'

        with open(output_md, 'w') as f:
            f.write(md_content)

        print(f"\n✓ Extracted {len(broadcasts)} broadcasts")
        print(f"✓ Saved to: {output_json}")
        print(f"✓ Saved to: {output_md}")

        browser.close()
        return broadcasts

if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://app.kit.com/campaigns"
    extract_kit_broadcasts(url)
