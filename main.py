import scraper
import time
import os
import sys
print("welcome to web scraper")
query=input("enter a google search: ")
result=scraper.search(query)
print("Loading websiets with info on search.......................")
time.sleep(3)
print(result)
time.sleep(3)
print(scraping data................................")
content=scraper.scrape_data(result)
print("scraping complete")
time.sleep(3)
print("parsing data")
