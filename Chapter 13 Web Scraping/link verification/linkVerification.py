#Chapter 13 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter13.html

#from playwright.sync_api import sync_playwright
from pathlib import Path
import requests, bs4

current_directory = Path.cwd()
file_path = current_directory / 'example.html'

#url = file_path.resolve().as_uri()

#read the page off the current directory
html = file_path.read_text(encoding='utf-8')
soup = bs4.BeautifulSoup(html, 'html.parser')

#find all the anchor elements in the page
link_elements = soup.select('a')

for link in link_elements:
    href = link.get('href')
    #print(link.attrs)
    inner_text = link.get_text(strip=True) or '[No Text]'
    if not href:
        continue

    try:
        response = requests.get(href, timeout=5)

        if response.status_code == 404:
            
            print(f'Broken link: {inner_text} ({href})\n')
    except requests.RequestException as exc:
        print(f'Something went wrong accessing: {inner_text} ({href})')
        print(f'Error: {exc}\n')

"""
with sync_playwright() as playwright:
    print(f'Opening {url} ...\n')
    browser = playwright.firefox.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto(url)

    links = page.locator('a').all()

    for link in links:
        print(link.get_attribute('href'))
    browser.close()
"""