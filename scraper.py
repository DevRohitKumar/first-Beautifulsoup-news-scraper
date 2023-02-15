import requests
from bs4 import BeautifulSoup
from config import config

wion_main_response = requests.get(config['wion_main_url'], headers = config['headers'])
wion_india_response = requests.get(config['wion_india_url'], headers = config['headers'])
wion_world_response = requests.get(config['wion_world_url'], headers = config['headers'])
wion_science_response = requests.get(config['wion_science_url'], headers = config['headers'])

wion_main_soup = BeautifulSoup(wion_main_response.text, 'lxml')
wion_india_soup = BeautifulSoup(wion_india_response.text, 'lxml')
wion_world_soup = BeautifulSoup(wion_world_response.text, 'lxml')
wion_science_soup = BeautifulSoup(wion_science_response.text, 'lxml')

wion_india_news, wion_world_news, wion_science_news = []

wion_india_headline = wion_india_soup.find("div", class_="thumb-txt")
wion_india_headline_title = wion_india_headline.find("h2").text
wion_world_headline = wion_world_soup.find("div", class_="thumb-txt")
wion_world_headline_title = wion_world_headline.find("h2").text
wion_science_headline = wion_science_soup.find("div", class_="thumb-txt")
wion_science_headline_title = wion_science_headline.find("h2").text

wion_india_news.append(wion_india_headline_title)
wion_world_news.append(wion_world_headline_title)
wion_science_news.append(wion_world_headline_title)

for item in wion_world_soup.find_all("div", class_="article-list-txt"):
    title = item.find("h2").text
    time = item.find("div", class_="date-author-loc").text
    wion_world_news.append([title , time])

for item in wion_india_soup.find_all("div", class_="article-list-txt"):
    title = item.find("h2").text
    time = item.find("div", class_="date-author-loc").text
    wion_india_news.append([title , time])

for item in wion_science_soup.find_all("div", class_="article-list-txt"):
    title = item.find("h2").text
    time = item.find("div", class_="date-author-loc").text
    wion_science_news.append([title , time])






'''
Author 👨‍🔬: Rohit Kumar
Email ✉️: contactdevrk@gmail.com
Created 📆: 14-02-2023
'''