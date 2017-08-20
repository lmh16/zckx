#https://github.com/Chyroc/WechatSogou
# -*- coding:utf-8 -*- 
import wechatsogou

ws_api = wechatsogou.WechatSogouAPI()
articles = ws_api.get_gzh_artilce_by_history('交大威威')

file = open('./articles_list.txt','w')
for titles in articles.get('article'):
    file.write(titles.get('content_url')+'\n')
