import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"username\"]").fill("standard_user")
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"login-button\"]").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        print("Login successful and redirected to inventory page")
        context.close()
        browser.close()


