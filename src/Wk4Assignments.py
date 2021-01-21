from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def followassignment():
    starturl = input('Enter URL: ')
    countinput = input('Enter count: ')
    positioninput = int(input('Enter position: '))
    followlink = starturl
    for i in range(0, int(countinput)+1):
        followlink = getlink(followlink, positioninput)


def getlink(urltofollow, positioninput):
    print("Retrieving: ", urltofollow)
    # Ignore SSL cert errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(urltofollow, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    position = 0
    # Retrieve all anchor tags
    tags = soup('a')
    for tag in tags:
        position += 1
        if position == positioninput:
            return tag.get('href', None)


followassignment()

def sumwebpage():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('span')
    sum = 0
    count = 0
    for tag in tags:
        sum = sum + int(tag.contents[0])
        count += 1
    print("Count ", count)
    print("Sum ", sum)
