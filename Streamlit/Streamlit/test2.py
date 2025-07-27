# test_script.py

from flask import Flask
import pyautogui
import asyncio
from playwright.async_api import async_playwright

# Flask Test
app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is working!"

# PyAutoGUI Test
def test_pyautogui():
    screen_width, screen_height = pyautogui.size()
    print(f"Screen resolution is: {screen_width}x{screen_height}")

# Playwright Test
async def test_playwright():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://example.com")
        title = await page.title()
        print(f"Page title from Playwright: {title}")
        await browser.close()

if __name__ == "__main__":
    print("✅ Starting test...")

    # Test Flask (run only once using flask run)
    print("✅ Flask route available at: http://127.0.0.1:5000")

    # Test PyAutoGUI
    test_pyautogui()

    # Test Playwright
    asyncio.run(test_playwright())

    print("✅ All components tested successfully.")
