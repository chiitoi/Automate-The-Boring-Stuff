#Chapter 13 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter13.html

from playwright.sync_api import sync_playwright
import time

url = 'https://play2048.co/'

with sync_playwright() as playwright:
    print(f'Opening {url} ...')
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto(url)

    page.click("body")
    moves = ["ArrowUp", "ArrowRight", "ArrowDown", "ArrowLeft"]
    for i in range(200):
        move = moves[i % 4]
        page.keyboard.press(move)
        time.sleep(0.1)
    browser.close()
        