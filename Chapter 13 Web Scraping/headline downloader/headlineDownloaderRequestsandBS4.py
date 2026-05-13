#Chapter 13 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter13.html

import requests, bs4

url = 'https://slashdot.org/'

response = requests.get(url)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser')

headlines = soup.select('.story-title')
for story in headlines:
    inner_text = story.get_text()
    print(inner_text)