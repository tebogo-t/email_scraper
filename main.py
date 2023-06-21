import requests
import requests.exceptions
import urllib.parse
import re
from bs4 import BeautifulSoup
from collections import deque

user_url = input('[+] Enter URL to scan: ')
urls = deque([user_url])

scrapped_urls = set()
emails = set()

count = 0

try:
    while len(urls):
        count += 1
        if count == 100:
            break
        url = urls.popleft()
        scrapped_urls.add(url)

        parts = urllib.parse.urlsplit(url)
        base_url = '{0}://{1}'.format(parts.scheme, parts.netloc)

        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        print('[%d] Processing %s' % (count, url))
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        new_emails = set(re.findall(r'[a-z0-9.\-+]+@[a-z0-9.\-+_]+\.[a-z]+', response.text, re.I))
        emails.update(new_emails)

        soup = BeautifulSoup(response.text, features='lxml')

        for anchor in soup.find_all("a"):
            link = anchor.get('href', '')
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            if not link in urls and not link in scrapped_urls:
                urls.append(link)

except KeyboardInterrupt:
    print('[+] Closing!')

