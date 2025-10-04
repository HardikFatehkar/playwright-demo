# tests/test_example.py

import os
from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        # Ensure reports/screenshots folder exists
        os.makedirs("reports/screenshots", exist_ok=True)

        # Take screenshot
        page.screenshot(path="reports/screenshots/example.png")

        assert "Example Domain" in page.title()
        browser.close()
