import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
info = json.loads(data)
comments = info['comments']

print('Comment count:', len(comments))
sum = 0
for comment in comments:
    sum += int(comment['count'])

print(sum)
