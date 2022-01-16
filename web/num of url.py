import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup


url=input('Enter - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('a')
for tag in tags:
    print(tag.get('href', None))
"""
sum=0
for tag in tags:
    a=int(tag.contents[0])
    sum=sum+a
print(sum)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
"""