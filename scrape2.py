import requests 
import time
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def loadRSS(url): 
    resp = requests.get(url) 
    return ET.fromstring(resp.content)

def get_article(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(1)
        html_page = driver.page_source
        supa = BeautifulSoup(html_page, 'html.parser')
        articol = supa.find('div', id='article')
        text = articol.text if articol else "No article found"
        tags_div = supa.find('div', class_="ArticleRelatedInstrumentsView_hideScrollbar__df3hk")
        divs = tags_div.find_all("div") if tags_div else []
        tags = []
        for tag in divs:
            span = tag.find("span")
            if span:
                tags.append(span.text)

        return {"description": text, "tags": list(set(tags))}
    except Exception as _:
        return {"description": "No article found", "tags": []}
    finally:
        driver.quit()

def main(): 
    rss_urls = [
        "https://www.investing.com/rss/news_25.rss",
        "https://www.investing.com/rss/news_301.rss",
        "https://investing.com/rss/news_356.rss"
    ]

    news_data = []
    
    for url in rss_urls:
        news = loadRSS(url) 
        for item in news.findall('.//channel/item'):
            entry = {}
            for child in item:
                if child.tag in ["title", "link", "pubDate"]:
                    entry[child.tag] = child.text
            print(entry)
            if not entry["link"].startswith("https://www.investing.com/news/"):
                continue
            entry = {**entry, **get_article(entry["link"])}
            news_data.append(entry)
            print(entry)

    with open("investing_news.json", "w") as f:
        f.write(json.dumps(news_data))

if __name__ == "__main__": 
    main()
