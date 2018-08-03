# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
result = requests.get('https://www.ptt.cc/bbs/NBA/index.html')
result.encoding = 'utf8'  
# print(result.text)

soup=BeautifulSoup(result.text, "html.parser")
print (soup.select('.board')[0].text)
for line in soup.select('.r-ent'):
    print (line.select('.title')[0].text)
    print (line.select('.date')[0].text,line.select('.author')[0].text)