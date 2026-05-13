#Chapter 13 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter13.html

from playwright.sync_api import sync_playwright
from urllib.parse import urljoin

url = 'https://autbor.com/breadcrumbs/'
page = 'index.html'

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=True, slow_mo=50)
    tab = browser.new_page()
    while True:
        tab.goto(urljoin(url, page))

        locator = tab.locator('#hello')
        text = locator.first.inner_text()
        print(text)
        
        if "Go to" in text:
            next_link = text.split()
            page = next_link[-1]
        else:
            break
    browser.close()