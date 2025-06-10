import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_empty_user_name():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()
        error_message = page.locator("[data-test=\"error\"]")
        expect(error_message).to_be_visible()
        expect(error_message).to_have_text("Epic sadface: Username is required")
        expect(page).to_have_url("https://www.saucedemo.com/")
        print("Login was unsuccessful and wasn't redirected to inventory page")
        context.close()
        browser.close()
