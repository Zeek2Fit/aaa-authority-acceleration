#!/usr/bin/env python3
"""
Extract emails from Kit sequence using Brave browser
"""
import json
import sys
from playwright.sync_api import sync_playwright

def extract_kit_emails(sequence_url, email="4zjlloyd@gmail.com", password="[REDACTED]"):
    """Extract all emails from a Kit sequence"""

    with sync_playwright() as p:
        # Launch Brave browser
        browser = p.chromium.launch(
            executable_path="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            headless=False
        )

        context = browser.new_context()
        page = context.new_page()

        # Navigate to the sequence (will redirect to login if needed)
        print(f"Navigating to {sequence_url}")
        page.goto(sequence_url, wait_until='networkidle')

        # Check if we need to log in
        if "login" in page.url.lower():
            print("Logging in to Kit...")

            # Fill in email
            page.fill('input[name="user[email]"]', email)
            print("Entered email")

            # Fill in password
            page.fill('input[name="user[password]"]', password)
            print("Entered password")

            # Click login button and wait for navigation
            page.click('#user_log_in')
            print("Clicked login button")

            # Wait for navigation after login
            page.wait_for_load_state('networkidle', timeout=15000)
            print(f"After login, current URL: {page.url}")

            # Handle verification/2FA if needed
            if 'verify' in page.url.lower():
                print("Token verification required. Waiting for manual verification...")
                # Wait for user to complete verification (up to 2 minutes)
                page.wait_for_url(lambda url: 'verify' not in url.lower() and 'login' not in url.lower(), timeout=120000)
                print("Verification complete!")

            # If still on login, there might be an error
            if 'login' in page.url.lower():
                print("ERROR: Still on login page. Check credentials or handle captcha/2FA manually.")
                page.screenshot(path='/Users/zeekfit/Documents/Z Brain/login_error.png')
                return []

            # Navigate to sequence
            print(f"Navigating to sequence: {sequence_url}")
            page.goto(sequence_url, wait_until='networkidle')
            print(f"Current URL after navigation: {page.url}")

        # Wait a moment for page to fully load
        page.wait_for_timeout(2000)

        # First, let's save the HTML to inspect the structure
        html_content = page.content()
        with open('/Users/zeekfit/Documents/Z Brain/kit_page_source.html', 'w') as f:
            f.write(html_content)
        print("Saved page HTML to kit_page_source.html for inspection")

        # Take a screenshot to see what we're working with
        page.screenshot(path='/Users/zeekfit/Documents/Z Brain/kit_page.png', full_page=True)
        print("Saved screenshot to kit_page.png")

        # Extract emails data
        emails = []

        # Try to find email containers - try many different selectors
        email_elements = page.query_selector_all('.email-item, [data-email], .sequence-email')

        print(f"Found {len(email_elements)} potential email elements")

        if len(email_elements) == 0:
            # Try alternative selectors
            email_elements = page.query_selector_all('tr[data-id], .email-row, article, li, [role="row"]')
            print(f"Alternative search found {len(email_elements)} elements")

        for idx, element in enumerate(email_elements, 1):
            try:
                # Try to extract subject
                subject = None
                subject_selectors = [
                    '.email-subject',
                    '[data-subject]',
                    'h2',
                    'h3',
                    '.subject'
                ]

                for selector in subject_selectors:
                    subject_el = element.query_selector(selector)
                    if subject_el:
                        subject = subject_el.inner_text().strip()
                        break

                if not subject:
                    subject = f"Email {idx}"

                # Click to open full email
                element.click()
                page.wait_for_timeout(1000)

                # Extract full email content
                content_selectors = [
                    '.email-content',
                    '.email-body',
                    '[data-email-content]',
                    '.message-body'
                ]

                email_content = ""
                for selector in content_selectors:
                    content_el = page.query_selector(selector)
                    if content_el:
                        email_content = content_el.inner_text().strip()
                        break

                emails.append({
                    'number': idx,
                    'subject': subject,
                    'content': email_content
                })

                print(f"Extracted email {idx}: {subject}")

            except Exception as e:
                print(f"Error extracting email {idx}: {e}")
                continue

        # Save to file
        output_file = '/Users/zeekfit/Documents/Z Brain/kit_emails_extracted.json'
        with open(output_file, 'w') as f:
            json.dump(emails, f, indent=2)

        print(f"\n✓ Extracted {len(emails)} emails")
        print(f"✓ Saved to: {output_file}")

        browser.close()
        return emails

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://app.kit.com/sequences/2470622"
    extract_kit_emails(url)
