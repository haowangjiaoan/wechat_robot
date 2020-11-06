# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import time
while (True):
    inputWord=input("请输入词条：")
    url='https://fanyi.baidu.com/?aldtype=16047#zh/en/'+inputWord
    url1 = urllib.request.quote(url, safe=";/?:@&=+$,", encoding="utf-8")
    response=urllib.request.urlopen(url1)
    html_doc=response.read().decode('utf-8')
    soup = BeautifulSoup(html_doc, 'lxml')
    tag = soup.find(attrs={"class": "output-bd"})
    #tag = soup.find_all('p')
    print(tag)
    if 'NoneType' in str(type(tag)):
        print('百科库中无\"'+inputWord+'\"词条，请更换词条重新搜索！')
    else:
        text=tag.text.replace('\n','')
        print(text)



