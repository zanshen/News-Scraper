"""
program: news_scrape.py
author: Brandon

Uses the Beautiful Soup web scraper to pull rss data from a news feed url.

"""

from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen

news_url = "http://si.com/rss/si_ncaab.rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = Soup(xml_page, "xml")
news_list = soup_page.findAll("item")

for news in news_list:
	print(news.title.text)
	print(news.link.text)
	print(news.pubDate.text)
	print("-" * 60)