# to import packages to python env, in cmd prompt pip install <package name>

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# some pages won't open with a 403, you have to change headers to access this as the site trying to block bots



