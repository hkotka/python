import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Retrieve json data into Python dictionary
url = "http://py4e-data.dr-chuck.net/comments_147422.json"
handle = urllib.request.urlopen(url)
data = handle.read().decode()
data = json.loads(data)

# Calculate total sum of counts
sum = 0
for item in data['comments']:
    sum = sum + int(item['count'])

print(sum)
