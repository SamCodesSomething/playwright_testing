import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_item_to_cart(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_be_visible()
    expect(cart_badge).to_have_text("1")
    check_out_button = page.locator("[data-test=\"checkout\"]")
    expect(check_out_button).to_be_visible()
    print("add item to cart was successful")

