import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Initial url
url = "http://py4e-data.dr-chuck.net/known_by_Conley.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

while count >= 1:
    for i, tag in enumerate(tags):
        if i == position - 1:
            print(tag.get('href', None))
            # Set new url to follow
            url = tag.get('href', None)
            # Open and parse url
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            # Retrieve all of the anchor tags
            tags = soup('a')
            count = count - 1
