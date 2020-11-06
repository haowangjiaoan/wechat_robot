# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
while (True):
    inputWord=input("请输入词条：")
    url='https://dict.baidu.com/s?wd='+inputWord+'&from=zici#detailmean'
    url1 = urllib.request.quote(url, safe=";/?:@&=+$,", encoding="utf-8")
    response=urllib.request.urlopen(url1)
    html_doc=response.read().decode('utf-8')
    soup = BeautifulSoup(html_doc, 'lxml')

    if len(soup.find_all(attrs={"id": "detailmean-wrapper"}))==0:
        print('成语库中无\"'+inputWord+'\"词条，请更换词条重新搜索！')
    else:
        tag = soup.find_all(attrs={"id": "detailmean-wrapper"})[0]
        tag=tag.find_all("li")
        if len(tag)==0:
            print('成语库中无\"'+inputWord+'\"词条，请更换词条重新搜索！')
        else:
            print(tag[0].text.replace('\n',''))

            if len(soup.find_all(attrs={"id": "story-wrapper"}))==0:
                print('【典故】：无。成语库中\"'+inputWord+'\"无典故')
            else:
                tag1 = soup.find_all(attrs={"id": "story-wrapper"})[0]
                tag=tag1.find_all("p")
                if len(tag)==0:
                    print('【典故】：无。成语库中\"'+inputWord+'\"无典故')
                else:
                    print('【典故】：'+tag[0].text.replace('\n',''))

            if len(soup.find_all(attrs={"id": "liju-wrapper"}))==0:
                print('【例句】：无。成语库中\"'+inputWord+'\"无例句')
            else:
                tag2 = soup.find_all(attrs={"id": "liju-wrapper"})[0]
                tag=tag2.find_all("p")
                if len(tag)==0:
                    print('【例句】：无。成语库中\"'+inputWord+'\"无例句')
                else:
                    print('【例句】：'+tag[0].text.replace('\n','').replace('～',inputWord))

