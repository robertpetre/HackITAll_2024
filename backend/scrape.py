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
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    accept_button = driver.find_element(By.XPATH, "//button[text()='Acceptați tot']")
    accept_button.click()
    time.sleep(1)
    html_page = driver.page_source
    supa =  BeautifulSoup(html_page, 'html.parser')
    articol = supa.find('div', class_ = 'body-wrap')
    a_tags = supa.find_all('a', attrs={'data-testid' : "ticker-container"})
    values = {}
    values["description"] = articol.text if articol else "No article found"
    values["tags"] = [
        tag.get('title') for tag in a_tags
    ]
    driver.quit()
    
    return values
  
      
def main(): 
    news = loadRSS("https://finance.yahoo.com/news/rssindex") 
    news_data = []
    for item in news.findall('.//channel/item'):
        entry = {}
        for child in item:
           if child.tag in ["title", "link", "pubDate"]:
               entry[child.tag] = child.text
        if not entry["link"].startswith("https://finance.yahoo.com/"):
            continue
        entry = {**entry, **get_article(entry["link"])}
        print(entry)
        news_data.append(entry)
    with open("yahoo_news.json", "w") as f:
        f.write(json.dumps(news_data))
      
if __name__ == "__main__": 
    main() 