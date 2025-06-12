import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_login(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("Login successful and redirected to inventory page.")

def test_failed_login(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("wrong_password")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/")
    error_message = page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")
    print("Login was unsuccessful and wasn't redirected to inventory page.")

def test_empty_user_name(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    error_message = page.locator("[data-test=\"error\"]")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url("https://www.saucedemo.com/")
    print("Login was unsuccessful and wasn't redirected to inventory page.")

def test_empty_password(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"login-button\"]").click()
    error_message = page.locator("[data-test=\"error\"]")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Epic sadface: Password is required")
    expect(page).to_have_url("https://www.saucedemo.com/")
    print("Login was unsuccessful and wasn't redirected to inventory page.")

def test_empty_login(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"login-button\"]").click()
    error_message = page.locator("[data-test=\"error\"]")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Epic sadface: Username is required")
    expect(page).to_have_url("https://www.saucedemo.com/")
    print("Login was unsuccessful and wasn't redirected.")