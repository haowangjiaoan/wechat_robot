# coding:utf-8  
import json
import requests
from wxpy import *
import time
from PIL import ImageGrab
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import urllib.request
from bs4 import BeautifulSoup
import http.client
import hashlib
import urllib
import random
import json



#import unittest, re
#import pyttsx3
#from aip import AipSpeech
#from pydub import AudioSegment
from io import BytesIO
#AudioSegment.converter = r"C:\\app\\ffmpeg\\ffmpeg-20190425-1ae5a64-win64-static\\bin\\ffmpeg.exe"
#bot = Bot()
#bot.file_helper.send_image('ParticleSmoke.png')

# 回复 my_friend 发送的消息
#@bot.register(my_friend)
#def reply_my_friend(msg):
#    return 'received: {} ({})'.format(msg.text, msg.type)


#@bot.register(bot.self, except_self=False)
#def reply_self(msg):
#   return 'received: {} ({})'.format(msg.text, msg.type)

# 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# 这条注册消息是我们构建群聊机器人的基础
#@bot.register(Group, TEXT)
#def print_group_msg(msg):
#    if msg.is_at:
#        print(msg)
#        msg.reply(meg.text)
'''
engine=pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
'''
'''
APP_ID = '16110073'
API_KEY = 'yfKjNhsu0VOIyQo8QsC6eLlZ'
SECRET_KEY = 'zkb510dbkTLVna5Gmxvcy8oTrGL5yZ0g'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
   with open(filePath, 'rb') as fp:
    return fp.read()
    '''

def auto_ai(text):
    url = "http://www.tuling123.com/openapi/api"
    #url = "http://openapi.tuling123.com/openapi/api/v2"
    api_key="xxxxxxxxxxxxxxxxxxxxxxxxxx"
    payload={
        "key":api_key,
        "info":text,
        "userid":"666"
        }
    r = requests.post(url,data=json.dumps(payload))
    result = json.loads(r.content)
    if ('url' in result.keys()):
        return result["text"]+result["url"]
    else:
        return result["text"]


bot = Bot(cache_path=True)#登录缓存
#bot.file_helper.send('[奸笑][奸笑]')

#boring_group1 = bot.friends().search('凤儿')[0]
#boring_group1 = bot.groups().search('')[0]
boring_group1 = bot.groups().search('程序猿')[0]

#boring_group1.send("[Robot]你好，我是人类的好朋友\n我的基本技能有:\n1.运算，比如：1+1等于几？\n2.讲笑话，比如：讲个笑话\n3.查天气，比如：上海天气\n4.趣聊，比如：...\n5.英文翻译，比如：we are family\n......\n我的专属技能有：\n1.拍主人马屁，比如：张治安是个什么样的人？\n2.查岗，比如：工作电脑截屏\n3.检查服务器，比如：ping www.baidu.com\n......\n赶紧和我对话吧:")
boring_group1.send('''[Robot] 你好，我是机器人！我可以:\n1.查成语（输入格式：成语 三顾茅庐）\n2.查百科（输入格式：百科 机器人）\n3.中英文互译（输入格式：翻译 中文）等。''')

@bot.register(boring_group1)
def group_message(msg):
    '''
    if (msg.type=='Recording'):
        audio = AudioSegment.from_mp3(BytesIO(msg.get_file()))
        export = audio.export( format="amr", bitrate="12.20k")
        ret=aipSpeech.asr(export.read(), 'amr', 8000, {'lan': 'zh',} )
        return ret
        '''
    if (msg.type!='Text'):
        return '[Robot] 你发送的是: {} ({})'.format(msg.text, msg.type)
    elif ('张治安' in msg.text):
        ret = '[Robot] 用几首诗来形容张治安这么优秀的人：\n1、陌上人如玉，公子世无双。\n2、积石有玉，列松如翠。郎艳独绝，世无其二。\n3、身长八尺，风姿特秀，萧萧肃肃，爽朗清举，龙章凤姿，天质自然。\n4、面若中秋之月，色如春晓之花，鬓若刀裁，眉如墨画，面如桃瓣，目若秋波。虽怒时而若笑，即嗔视而有情。\n5、面如傅粉，唇若施脂，转盼多情，语言常笑。天然一段风韵，全在眉梢；平生万种情思，悉堆眼角。'
        return ret
    elif ('百科' in msg.text):
        inputWord=msg.text[3:]
        url='https://baike.baidu.com/item/'+inputWord
        url1 = urllib.request.quote(url, safe=";/?:@&=+$,", encoding="utf-8")
        response=urllib.request.urlopen(url1)
        html_doc=response.read().decode('utf-8')
        soup = BeautifulSoup(html_doc, 'lxml')
        tag = soup.find(attrs={"class": "para"})
        if 'NoneType' in str(type(tag)):
            ret='[Robot] 百科库中无\"'+inputWord+'\"词条，请更换词条重新搜索！'
        else:
            ret='[Robot] \n'+tag.text.replace('\n','')
        return ret
    elif ('翻译' in msg.text):
        appid = '20200523000467908'  # 填写你的appid
        secretKey = '1BksD1ZNftY4VU6zyccu'  # 填写你的密钥

        httpClient = None
        myurl = '/api/trans/vip/translate'

        fromLang = 'auto'   #原文语种
        toLang = 'auto'   #译文语种
        salt = random.randint(32768, 65536)
        q=msg.text[3:]
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
        
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)


        ret='[Robot] \n'+result['trans_result'][0]['dst']

        return ret
    
    elif ('成语' in msg.text):
        ret='[Robot]'
        inputWord=msg.text[3:]
        url='https://dict.baidu.com/s?wd='+inputWord+'&from=zici#detailmean'
        url1 = urllib.request.quote(url, safe=";/?:@&=+$,", encoding="utf-8")
        response=urllib.request.urlopen(url1)
        html_doc=response.read().decode('utf-8')
        soup = BeautifulSoup(html_doc, 'lxml')

        if len(soup.find_all(attrs={"id": "detailmean-wrapper"}))==0:
            ret=ret+'\n'+'成语库中无\"'+inputWord+'\"词条，请更换词条重新搜索！'
        else:
            tag = soup.find_all(attrs={"id": "detailmean-wrapper"})[0]
            tag=tag.find_all("li")
            if len(tag)==0:
                ret=ret+'\n'+'成语库中无\"'+inputWord+'\"词条，请更换词条重新搜索！'
            else:
                ret=ret+'\n'+tag[0].text.replace('\n','')

                if len(soup.find_all(attrs={"id": "story-wrapper"}))==0:
                    ret=ret+'\n'+'【典故】：无。成语库中\"'+inputWord+'\"无典故'
                else:
                    tag1 = soup.find_all(attrs={"id": "story-wrapper"})[0]
                    tag=tag1.find_all("p")
                    if len(tag)==0:
                        ret=ret+'\n'+'【典故】：无。成语库中\"'+inputWord+'\"无典故'
                    else:
                        ret=ret+'\n'+'【典故】：'+tag[0].text.replace('\n','')

                if len(soup.find_all(attrs={"id": "liju-wrapper"}))==0:
                    ret=ret+'\n'+'【例句】：无。成语库中\"'+inputWord+'\"无例句'
                else:
                    tag2 = soup.find_all(attrs={"id": "liju-wrapper"})[0]
                    tag=tag2.find_all("p")
                    if len(tag)==0:
                        ret=ret+'\n'+'【例句】：无。成语库中\"'+inputWord+'\"无例句'
                    else:
                        ret=ret+'\n'+'【例句】：'+tag[0].text.replace('\n','').replace('～',inputWord)
        return ret


        
    elif ('ping' in msg.text)|('Ping' in msg.text)|('PING' in msg.text):
        boring_group1.send('[Robot] 请稍等...')
        p = os.popen(msg.text)
        buff = p.read() 
        '''
        p=subprocess.Popen(msg.text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        #buff=p.stdout.read()
        buff=''
        while True:
          buff = buff+p.stdout.readline()+'\n'
          if buff == '' and p.poll() != None:
            break
        buff,err=p.communicate()
        if err:
            buff=err
        else:
            pass
            '''
        #print('[Robot]'+buff)
        ret='[Robot]'+buff
        #boring_group1.send('[Robot]请求已结束。')
        p.close()
        return ret
    elif ('截屏' in msg.text):
        im=ImageGrab.grab()#全屏截图
        im.save("screen.png")
        boring_group1.send_image("screen.png")
    
    
    elif (msg.type=='Text'):
        ret = '[Robot] '+auto_ai(msg.text)
        #r=engine.say(auto_ai(msg.text))#合成语音
        #engine.runAndWait()
        #boring_group1.send_video(r)
        return ret
    
    

        
    
'''
    #print('[接收]'+str(msg))
    if (msg.type=='Text'):
        #ret = '[奸笑][奸笑]'
        boring_group1.send('识别消息为：'+msg.text)
    #elif(msg.type=='Map'):
        #ret = '识别位置为：'+msg.map
    #elif(msg.type=='Card'):
        #ret = '识别名片为：'+msg.cad
    #elif(msg.type=='Note'):
        #ret = '识别提示为：'+msg.note
    elif(msg.type=='Picture'):
        boring_group1.send('识别消息为：')
        boring_group1.send_image(msg.Picture)
    #elif(msg.type=='Recording'):
        #boring_group1.send_video('识别语音为：'+msg.recording
    elif(msg.type=='Attachment'):
        boring_group1.send('识别消息为：')
        boring_group1.send_file(msg.attachment)
    elif(msg.type=='Video'):
        boring_group1.send('识别消息为：')
        boring_group1.send_video(msg.video)

        #ret = auto_ai(msg.text)
    #print('[发送]'+str(ret))]
    return ret
    '''
    
'''
rst=bot.search("Huang X")
guy=rst[0]
guy.send("看到这个消息后输入命令：")

@bot.register(guy)
def forward_message(msg):
    if (msg.type=='Text'):
        ret = auto_ai(msg.text)
        return ret
    else :
        return '你发送的是: {} ({})'.format(msg.text, msg.type)
'''
'''
bot.file_helper.send("hello,send to file helper!")
#@bot.register(bot.self)
@bot.register(bot.file_helper)
def reply_file_helper(msg):
   #return 'received:{}({})'.format(msg.text, msg.type)
    bot.file_helper.send(msg.text)
'''
'''
bot.self.add()
bot.self.accept()
bot.self.send("hello,send to self!")   
@bot.register(bot.self)
#@bot.register(bot.file_helper)
def reply_self(msg):
   #return 'received:{}({})'.format(msg.text, msg.type)
    bot.self.send(msg.text)
    '''

embed()







