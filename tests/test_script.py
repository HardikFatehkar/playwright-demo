from playwright.sync_api import sync_playwright
import os

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("https://ccbst.ccbst.org/ccbst/public/index.php/x")
            assert "Login" in page.title()
        except Exception as e:
            page.screenshot(path="reports/failure.png")
            raise e
        finally:
            browser.close()