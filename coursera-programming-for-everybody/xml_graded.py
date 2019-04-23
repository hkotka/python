import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retrieve xml data from url
url = "http://py4e-data.dr-chuck.net/comments_147421.xml"
print('Retrieving', url)
handle = urllib.request.urlopen(url, context=ctx)
data = handle.read()
print('Retrieved', len(data), 'characters')

# Transform data into xml object and find all commet nodes
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')

sum = 0
counter = 0

# Loop trough commet nodes and add up counts
for item in counts:
    count = int(item.find('count').text)
    sum = sum + count
    counter = counter + 1

print('Count:', counter)
print('Sum:', sum)
