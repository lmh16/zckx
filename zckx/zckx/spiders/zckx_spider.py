# -*- coding: UTF-8 -*-
import scrapy
import time

from zckx.items import ZckxItem

file = open(r'D:\zckx\articles_list.txt','r')
articles_list = file.read()
urls=articles_list.split()

class ZckxSpider(scrapy.Spider):
    name = "zckx"
    start_urls = urls

    def parse(self, response):
        item = ZckxItem()
        
        #check if item is posted today
        #if response.xpath('//*[@id="post-date"]').extract() != [time.strftime("%Y-%m-%d", time.localtime())]:
        if response.xpath('//*[@id="post-date"]/text()').extract() == ["2017-08-19"]:
            
            item['title'] = response.xpath('//title/text()').extract()
            
            item['content'] = []
            for line in response.xpath('//p/text()|//img'):
                if(line in response.xpath('//img[@data-src]')):
                    item['content'].append(line)
                    break
                line = line.extract()
                if(line.split()!=[]):
                    item['content'].append(line)
                
            yield item
        
            #format into html
            pic_count=0;
            if not u"\u3010\u5a01\u5a01\u5feb\u8baf\u3011" in item['title'][0]:
                return
            file_html = open(str(hash(item['title'][0]))+'.txt','w')
            for line in item['content']:
                if "!important" in line:
                    break
                if "src" in line:
                    if "http" in line:
                        pic_count+=1
                        file_html.write(("<p><img src=\"cid:image"+str(pic_count)+"\"></p>\n"))
                        #save the pic
                else:
                    file_html.write(("<p>"+line+"</p>\n").encode('utf-8'))
                    
                
            file_html.close()
        
        