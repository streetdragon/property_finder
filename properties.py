#!/usr/bin/env python3

import urllib.request
import re
from bs4 import BeautifulSoup

def get_urls(url):
    urls = list()
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        urls.append(link.get('href'))
    return urls

def get_properties_trademe(price_start, price_end, keywords):
    url = 'http://www.trademe.co.nz/Browse/CategoryAttributeSearchResults.aspx?search=1&cid=5748&sidebar=1&rptpath=350-5748-4233-&132=FLAT&selected135=7&selected136=89&134=1&135=7&136=89&216=0&216=0&217=0&217=0&153=' + keywords + '&122=0&122=1&59=' + price_start + '00' + '&59=' + price_end + '00' + '&178=0&178=0&sidebarSearch_keypresses=0&sidebarSearch_suggested=0'

    urls = get_urls(url)
    properties = list()
    for u in urls:
        if u is not None and 'auction' in u:
            properties.append(u)

    properties.sort()
    properties = list(set(properties))

    return properties

if __name__ == '__main__':
    urls = get_properties_trademe('250', '400', 'unfurnished')
    print(urls)
