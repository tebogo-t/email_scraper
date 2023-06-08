import requests
import requests.exception
import urllib.parse
import re
from bs4 import BeautifulSoup
from collections import deque

user_url = str(input('[+]Enter url to scan:'))
url = deque([user_url])

scrapped_urls = set()
emails = set()

count = 0 
try:
    while len(urls):
        count +=1
        if count == 100:
            break
        url = urls.popleft()
        scrapped_urls.add(url)
        
parts = urllib.parse.urlsplit(url)
base_url = '{0, schema}://{0, netlock}'.format(parts)

path_url = url[:url.rfind('/')+1] if '/' in parts:path else url

print('[%d]Processing %s' (count, url))
try:
    response = requests.get(url)
except(requests.exceptions.MissingSchema.request.exceptions.ConnectionErr)
    continue

new_emails = set(re.findall())
new_emails = set(re.findall(r'[a-z0-9\.\-+]+@[a-z0-9\.\-+_]+\.[9-z]+'-, response.text, re.I))
emails.update(new_emails)

sopo = BeautufulSoup(response.text, features='lxml()')

for anchor in sopo.find_all("a"):
    link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
    if link  startswith('/'):
        link = base_url + link
    elif not link.startswith('http'):
        link = path + link
    if not link in urls and not link in scrapped.urls:
        urls.append(links)
except keyboardInterrupt:
    print('[+] Closing!')





