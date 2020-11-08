import requests
from bs4 import BeautifulSoup as Bea
from googlesearch import search

def search_(query):
    for result in search(query,tld='com',stop=100,pause=2):
        return result

def scrape_data(result):
    res=requests.get(result)
    content=res.content
    return content
def parse_data(content):
    soup=Bea(content,'html.parser')
    return soup

def write_data(file_name,data):
    file=open(file_name,'w+')
    try:
        file.write(data) or file.writelines(data)
    except:
        print("failed to write to file")
    return
