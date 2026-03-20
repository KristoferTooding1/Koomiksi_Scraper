import requests
from bs4 import BeautifulSoup
import os

def scrape_images(limit=5):
    url = 'http://books.toscrape.com/'
    folder = 'scraped_images'
    
    if not os.path.exists(folder):
        os.makedirs(folder)

    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        images = soup.find_all('img', class_='thumbnail', limit=limit)

        for i, img in enumerate(images):
            img_url = url + img.get('src').replace('../', '')
            print(f"Downloading: {img_url}")
            
            img_data = requests.get(img_url).content
            filename = os.path.join(folder, f"image_{i+1}.jpg")
            
            with open(filename, 'wb') as f:
                f.write(img_data)
            print(f"Saved: {filename}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_images(5)
