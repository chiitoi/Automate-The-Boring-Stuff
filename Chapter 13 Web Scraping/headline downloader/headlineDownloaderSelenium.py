#Chapter 13 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter13.html

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://slashdot.org/'
browser = webdriver.Firefox()
browser.get(url)

headlines = browser.find_elements(By.CSS_SELECTOR, '.story-title')

for story in headlines:
    print(story.get_property('innerText'))

browser.quit()