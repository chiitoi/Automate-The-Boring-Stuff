#Chapter 13 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter13.html

from playwright.sync_api import sync_playwright

url = 'https://slashdot.org/'

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=True, slow_mo=50)

page = browser.new_page()
page.goto(url)

locator = page.locator('.story-title')

for i in range(locator.count()):
    print(locator.nth(i).inner_text())

browser.close()
playwright.stop()