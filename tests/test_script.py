from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, expect
import os

def run(playwright):
    # Launch browser (set headless=False to see browser actions)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ------------------------------
    # Scenario 1: Login
    # ------------------------------
    page.goto("https://ccbst.ccbst.org/ccbst/public/index.php/x")   # change URL to your site

    page.fill("input[name='email']", "qa@ccbst.ca")
    page.fill("input[name='password']", "1112")
    os.makedirs("reports/screenshots/Ccbst", exist_ok=True)

        # Take screenshot
    page.screenshot(path="reports/screenshots/Ccbst/example.png")
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
    page.screenshot(path="reports/screenshots/Ccbst/example1.png")
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
    page.screenshot(path="reports/screenshots/Ccbst/example2.png")
    # -----------------------------
    # Submit form
    # -----------------------------
    page.click("button[type='submit']")  # Adjust selector if different

    # -----------------------------
    # Validation
    # -----------------------------
    # Wait for confirmation message
       # ✅ Validation (fix)
    try:
        expect(page.locator("text=Lead created successfully")).to_be_visible(timeout=5000)
        print("✅ Lead form submitted successfully")
                # Take screenshot
        page.screenshot(path="reports/screenshots/Ccbst/example3.png")
    except:
        page.screenshot(path="error.png")
        print("❌ Success message not found. Screenshot saved as error.png")

    # ------------------------------
    # Cleanup
    # ------------------------------
    context.close()
    #browser.close()


with sync_playwright() as playwright:
    run(playwright)
