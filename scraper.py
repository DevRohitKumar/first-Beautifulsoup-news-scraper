import time
from datetime import datetime
from bs4 import BeautifulSoup
from config import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from db_connection import my_database

wi_urls = [config['wi_india_url'],
             config['wi_world_url'],
             config['wi_science_url']]

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

my_db_conn = my_database(config['DB'])

def scroll_height(driver, scroll_times=1 ):
    for i in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll to end of the browser window
        time.sleep(5) # sleep for 5 seconds to allow page content to load

def get_wi_news(url, pages_to_load=3):
    global time    
    wi_browser = webdriver.Chrome(service= Service( config['MY_PATH_TO_CHROME'] ), options = chrome_options)
    wi_browser.get(url)
    time.sleep(10) # sleep for first time to load page properly
    scroll_height(scroll_times= pages_to_load, driver= wi_browser)
    wi_response = wi_browser.page_source
    wi_soup = BeautifulSoup(wi_response, 'lxml')
    wi_news = []

    wi_headline = wi_soup.find("div", class_="thumb-txt")
    wi_headline_title = wi_headline.find("h2").text
    
    #extract headline link from the first sharer link
    wi_headline_sharer = wi_soup.find("div", class_="social-icon")
    headline_sharer_link = wi_headline_sharer.find("a").get("href")
    wi_headline_link = headline_sharer_link.split("u=", 1)
    date_time = str( datetime.now().replace(microsecond=0)).split()
    
    wi_news.append((wi_headline_title, date_time[0], date_time[1] , wi_headline_link[1]))
    
    for item in wi_soup.find_all("div", class_="article-list-txt"):
        title = item.find("h2").text
        str_time = item.find("div", class_="date-author-loc").text
        link = item.find("a", class_="list-more").get("href")
        date_time = str_time.split()
        
        if title == my_db_conn.get_last_db_headline():
            break
        wi_news.append((title , date_time[0], date_time[1], config['wi_main_url']+link))

    wi_browser.quit()
    # reverse collected data list for easy access and usability later.
    wi_news.reverse()     
    my_db_conn.save_to_india_db(wi_news) #save collected data to database




'''
Author 👨‍🔬: Rohit Kumar
Email ✉️: contactdevrk@gmail.com
Created 📆: 14-02-2023
'''