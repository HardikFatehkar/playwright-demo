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
 
            # Select radios
            # -----------------------------
            page.wait_for_selector("input#male", state="visible")
            page.check("input#male", force=True)     # Gender
            page.wait_for_selector("input#in_campus", state="visible")
            page.check("input#in_campus", force=True)   # Student Access
            # Wait until element exists
            #page.wait_for_selector("input#good", state="visible")
           # assert page.is_checked("input#good")  # Works for checkbox, may fail for radio


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

            # -----------------------------
            # Submit form
            # -----------------------------
            page.click("button[type='submit']")  # Adjust selector if different

            # -----------------------------
            # Validation
            # -----------------------------
            # Wait for confirmation message
            # ✅ Validation (fix)         
        except Exception as e:
            os.makedirs("reports/failure", exist_ok=True)
            page.screenshot(path="reports/failure.png")
            raise e
        finally:
            browser.close()