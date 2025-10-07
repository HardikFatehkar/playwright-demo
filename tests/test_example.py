from playwright.sync_api import sync_playwright
import os

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
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
            # ------------------------------
            # Scenario 2: Add New Lead
            # ------------------------------
            page.click("a[class='pull-right btn btn-sm green']")
            # Ensure reports/screenshots folder exists
            os.makedirs("reports/screenshots", exist_ok=True)

            page.wait_for_selector("input#good", state="visible")
        
            page.click("input#good", force=True)
            page.wait_for_timeout(500)
            assert page.locator("input#good").is_checked(), "Radio button did not stay checked"
        except Exception as e:
            page.screenshot(path="reports/failure1.png")
            raise e
        finally:
           # browser.close()
            page.screenshot(path="reports/failure11.png")