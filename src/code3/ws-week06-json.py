import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import json
import ssl

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

#url = "http://py4e-data.dr-chuck.net/comments_42.json"
url = "http://py4e-data.dr-chuck.net/comments_1602385.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
jsdata = json.loads(data)
sum = 0
#print(json.dumps(jsdata, indent=2))
for comment in jsdata["comments"]:
    # print(comment['count'])
    sum = sum + int(comment['count'])

print(sum)

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])
