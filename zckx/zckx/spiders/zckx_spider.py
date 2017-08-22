import scrapy
import time
import urllib
import re
import os

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
        #if response.xpath('//*[@id="post-date"]/text()').extract() == [time.strftime("%Y-%m-%d", time.localtime())]:
        if response.xpath('//*[@id="post-date"]/text()').extract() == ["2017-08-20"]:
            item['title'] = response.xpath('//title/text()').extract()
            
            text_linecount=0
            item['content'] = []
            for line in response.xpath('//p//text()|//img'):
                if(line in response.xpath('//img[@data-src]')):
                    item['content'].append(line)
                    break
                line = line.extract()
                if(line.split()!=[]):
                    #delete useless lines befor post
                    if(text_linecount>4):
                        item['content'].append(line)
                    else:
                        text_linecount+=1
                
            yield item
        
            #save pic using re
            reg = r'src="(.+=(jpeg|png))"'
            imgre = re.compile(reg)
            
            #format into html
            pic_count=0;
            #check if the post belongs to zckx
            if not item['title'][0][0:6] == u"\u3010\u5a01\u5a01\u5feb\u8baf\u3011":
                return
            
            
            os.mkdir('posts/'+str(hash(item['title'][0])))
            os.chdir('posts/'+str(hash(item['title'][0])))
            file_html = open('content.txt','w')
            file_html.write(item['title'][0][6:]+'\n')
            
            for line in item['content']:
                if "!important" in line:
                    break
                if "src" in line:
                    if "http" in line:
                        pic_count+=1
                        file_html.write(("<section><img src=\"cid:image"+str(pic_count)+"\"></section>\n"))
                        #save the pic
                        imgurl=re.findall(imgre,line)
                        urllib.urlretrieve(imgurl[0][0],'%s.' % pic_count+imgurl[0][1])
                        #TODO: delete unrelated pictures
                        
                else:
                    file_html.write(("<section>"+line+"</section>\n").encode('utf-8'))
                    
                
            file_html.close()
        
        