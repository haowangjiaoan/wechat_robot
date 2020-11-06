# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
inputWord='520'
url='https://baike.baidu.com/item/'+inputWord
url1 = urllib.request.quote(url, safe=";/?:@&=+$,", encoding="utf-8")
response=urllib.request.urlopen(url1)
html_doc=response.read().decode('utf-8')
soup = BeautifulSoup(html_doc, 'lxml')
tag = soup.find(attrs={"class": "para"})
if 'NoneType' in str(type(tag)):
    print('百科库中无\"'+inputWord+'\"词条，请更换词条重新搜索！')
else:
    text=tag.text.replace('\n','')
    print(text)



