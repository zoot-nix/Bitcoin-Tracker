#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from colored import stylize, fg #for styling

print(stylize('------Current Bitcoin Price------', fg('yellow')))
print(stylize('According to @coindesk.com', fg('red')))

class Bitcoin:
    def __init__(self):
        self.url = "https://www.coindesk.com/price/bitcoin"

    def __repr__(self):
        current_price = stylize(self.scraper(self.url), fg('yellow'))
        return f"Current Bitcoin Price is: {current_price}$"

    def scraper(self, url):
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        price = soup.find(class_='price-large')
        content = [i for i in price]

        return content[1]

if __name__ == "__main__":
    print(Bitcoin())