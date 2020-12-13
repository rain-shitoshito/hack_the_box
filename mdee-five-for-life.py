#!/usr/bin/env python3

import requests, hashlib
from bs4 import BeautifulSoup

target_url = 'http://134.209.29.219:31993/'
session = requests.session()
r = session.get(target_url)
bs = BeautifulSoup(r.text, 'html.parser')
hash = hashlib.md5(bs.find('h3').text.encode('utf-8')).hexdigest()
r = session.post(target_url, data={'hash': hash})
print(r.text)
