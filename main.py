from config import config
from scraper import get_wi_news

wi_urls = { "wi_news_india" : config['wi_india_url'],
      "wi_news_world" : config['wi_world_url'],
      "wi_news_science" : config['wi_science_url']
      }

for key, url in wi_urls.items():
    get_wi_news(key, url)