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
            
            item['title'] = response.xpath('//title/text()')
            
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
        #post=""
        
        