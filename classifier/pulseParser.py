from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import os
from lxml import html
import re
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

linkRegexp = r'/(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])/igm'



def prepareString(string):
    withOutLinks = re.sub(linkRegexp,' ',string)
    withOutTicker = re.sub(r'\$\w+',' ',withOutLinks)
    withOutSmile = re.sub(r'[^A-z0-9А-я $]',' ',withOutTicker)
    withOutMultipleSpaces = re.sub(r'  ',' ',withOutSmile)
    withOutTags = re.sub(r'ИСПРАВЛЕНО ', '',withOutMultipleSpaces)
    return withOutTags

def notTable(post):
        return not('ТАБЛИЦА' in post)

def get_time_text(element):
       return element.findChildren("div" , recursive=False)[0].text


driver = webdriver.Chrome(ChromeDriverManager().install())
tickers = ['YNDX', 'LKOH', 'MAIL', 'AFLT', 'QIWI', 'VTBR', 'DSKY', 'LNTA', 'MSFT', 'TSLA', 'SBUX','OZON']



for ticker in tickers:
        pulseURL = f'https://www.tinkoff.ru/invest/stocks/{ticker}/pulse/'
        newsURL = f'https://www.tinkoff.ru/invest/stocks/{ticker}/news/'
        driver.get(newsURL)
        news_button_get_news_class = 'Button-module__button_theme_secondary_2pyTJ' 
        # page_length = driver.execute_script("return document.body.scrollHeight")
        
        i = 0
        while (i < 200):
                try:
                    button = driver.find_elements_by_class_name()[0]
                    button.click()
                except: print(123)
                print(i)
                i += 1
                sleep(3)

        source_data = driver.page_source
        soup = bs(source_data, 'lxml')
                # NewsItem__title_36OwX
                # PulsePostCollapsed__text_3nQ1n

        date_footer_class = 'NewsItem__footer_33aPL'
        posts = soup.find_all('div', {'class':'NewsItem__title_36OwX'})
        
        
        dates = soup.find_all('div',{'class' : date_footer_class})
        news_dates = [get_time_text(element) for element in dates]
        posts = [post.text for post in posts]
        

        df_posts = pd.DataFrame()
        df_posts['post'] = posts
        df_posts['time'] = news_dates
        df_posts.to_csv(f'newsdata/{ticker}.csv', index=False)
                
        print(f'SAVED {ticker}')