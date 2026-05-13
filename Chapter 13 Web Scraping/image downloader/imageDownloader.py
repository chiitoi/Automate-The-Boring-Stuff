#Chapter 13 of Automate the Boring Stuff by Al Sweigart
#https://automatetheboringstuff.com/3e/chapter13.html

import requests, bs4, os
from urllib.parse import urljoin
import time

def download_images_from(website):
    #make an "images" folder in the current working directory
    os.makedirs('images', exist_ok=True)

    #download the website data to parse the html and look for img elements
    response = requests.get(website)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    images = soup.select('img')

    
    for image in images:
        #get the source for each image
        src = image.get('src')

        if not src:
             continue
        
        image_url = urljoin(website, src)

        print(image_url)
        
        #establish the file name that the image will be named
        file_name = os.path.basename(image_url)

        if os.path.exists(os.path.join('images', file_name)):
            continue

        #download the image and save it within the images folder
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        with open(os.path.join('images', file_name), 'wb') as f:
                for chunk in response.iter_content(10000):
                     f.write(chunk)
        time.sleep(1)
        
url = 'https://inventwithpython.com/index.html'

download_images_from(url)