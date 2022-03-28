# -*- coding: utf-8 -*
import requests
import re

def request_url(url):
   try:
       response = requests.get(url)
       if response.status_code == 200:
           return response.text
   except requests.RequestException:
       return None

def parse_result(html):
   pattern = re.compile('<li>.*?class="list_num.*?(\d+).*?class="name".*?title="(.*?)">.*?</li>',re.S)
   items = re.findall(pattern,html)
   for item in items:
       yield {
           'range': item[0],
           'title': item[1],
       }

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_url(url)
    items = parse_result(html)
    for item in items:
        print(item)

if __name__ == "__main__":
   for i in range(1,26):
       main(i)