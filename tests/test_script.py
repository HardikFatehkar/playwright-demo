
from playwright.sync_api import sync_playwright
import os

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
    # ------------------------------
    # Scenario 1: Login
    # ------------------------------
    page.goto("https://ccbst.ccbst.org/ccbst/public/index.php/x")   # change URL to your site

    page.fill("input[name='email']", "qa@ccbst.ca")
    page.fill("input[name='password']", "1112")
    os.makedirs("reports/screenshots", exist_ok=True)

        # Take screenshot
    page.screenshot(path="reports/screenshots/example11.png")
    page.click("button[type='submit']")
    page.goto("https://ccbst.ccbst.org/ccbst/public/index.php/x/student-inquiries")
    #page.wait_for_selector("text=Dashboard")

    print("✅ Login successful")

    # ------------------------------
    # Scenario 2: Add New Lead
    # ------------------------------
    page.click("a[class='pull-right btn btn-sm green']")
   # page.click("text=Add New Lead")

    # -----------------------------
    # Fill dropdowns
    # -----------------------------
    page.select_option("#inquiry_status_id", "2")   # Working
    page.select_option("#campus_id", "1")           # Scarborough

    # If "Other" status is chosen
    # page.select_option("#inquiry_status_id", "10")
    # page.fill("#other_status", "Special Status")

    # -----------------------------
    # Fill text fields
    # -----------------------------
    page.fill("#first_name", "John")
    page.fill("#last_name", "Doe")
    page.fill("#phone_no", "9876543210")
    page.fill("#email", "john.doe@example.com")
    page.fill("#address", "123 Test Street")
    page.fill("#postal_code", "A1B2C3")

        # Take screenshot
    page.screenshot(path="reports/screenshots/example122.png")
    # Select radios
    # -----------------------------
    page.wait_for_selector("input#male", state="visible")
    page.check("input#male", force=True)     # Gender
    page.wait_for_selector("input#in_campus", state="visible")
    page.check("input#in_campus", force=True)   # Student Access
    page.wait_for_selector("input#good", state="visible")
    page.check("input#good", force=True)        # Lead


    # -----------------------------
    # More dropdowns
    # -----------------------------
    page.select_option("#program_type", '1')        # Diploma
    page.select_option("#how_contact_us_id", "1")   # Call
    page.select_option("#chart_of_activity_id", "131") # Flyer
    page.select_option("#country_id", "3")          # India

    # -----------------------------
    # Date fields (must match format YYYY-MM-DD)
    # -----------------------------
    page.fill("#inquiry_followed_up_at", "2025-10-01")
        # Take screenshot
    page.screenshot(path="reports/screenshots/example223.png")
    # -----------------------------
    # Submit form
    # -----------------------------
    page.click("button[type='submit']")  # Adjust selector if different

    # -----------------------------
    # Validation
    # -----------------------------
    # Wait for confirmation message
       # ✅ Validation (fix)
    assert "Example Domain" in page.title()
    browser.close()