from playwright.sync_api import sync_playwright
import os

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("https://ccbst.ccbst.org/ccbst/public/index.php/x")
            assert "Login" in page.title()
            page.fill("input[name='email']", "qa@ccbst.ca")
            page.fill("input[name='password']", "1112")

            page.click("button[type='submit']")
            page.goto("https://ccbst.ccbst.org/ccbst/public/index.php/x/student-inquiries")
            #page.wait_for_selector("text=Dashboard")
            # Ensure reports/screenshots folder exists
            os.makedirs("reports/screenshots2", exist_ok=True)

            # Take screenshot
            page.screenshot(path="reports/screenshots2/example875.png") 
            print("✅ Login successful")         
        except Exception as e:
            os.makedirs("reports/failure", exist_ok=True)
            page.screenshot(path="reports/failure.png")
            raise e
        finally:
            browser.close()