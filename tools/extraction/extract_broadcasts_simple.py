#!/usr/bin/env python3
"""
Extract broadcast emails - assumes already logged in
Run this after you've manually logged into Kit in the browser
"""
import json
from playwright.sync_api import sync_playwright
import time

def extract_broadcasts():
    """Extract all broadcasts from current page"""

    with sync_playwright() as p:
        # Connect to existing browser if possible, or launch new one
        browser = p.chromium.launch(
            executable_path="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            headless=False
        )

        context = browser.new_context()
        page = context.new_page()

        # Go to campaigns page (assumes you're logged in)
        print("Navigate to https://app.kit.com/campaigns and log in if needed.")
        print("Press Enter when you're on the campaigns page and ready to extract...")
        input()

        # Current URL
        current_url = page.url
        print(f"Current URL: {current_url}")

        # Take screenshot
        page.screenshot(path='/Users/zeekfit/Documents/Z Brain/broadcasts_debug.png')
        print("Screenshot saved")

        # Get page structure
        # Look for any clickable items that might be broadcasts
        print("\nLooking for broadcast elements...")

        # Try multiple selectors
        selectors_to_try = [
            'tr',  # table rows
            'a[href*="campaigns"]',  # links with campaigns
            'button:has-text("View")',
            '[role="row"]',
            '.campaign',
            '[data-campaign]'
        ]

        for selector in selectors_to_try:
            elements = page.query_selector_all(selector)
            if elements:
                print(f"Found {len(elements)} elements with selector: {selector}")

        # Manual extraction prompt
        print("\nDo you want to:")
        print("1. Try automatic extraction")
        print("2. Get page HTML to inspect")
        choice = input("Enter choice (1 or 2): ")

        if choice == "2":
            html = page.content()
            with open('/Users/zeekfit/Documents/Z Brain/campaigns_page.html', 'w') as f:
                f.write(html)
            print("HTML saved to campaigns_page.html")
            return

        # Try automatic extraction
        # ... (will add based on what we find)

        print("\nKeeping browser open. Press Ctrl+C when done.")
        while True:
            time.sleep(1)

if __name__ == "__main__":
    extract_broadcasts()
