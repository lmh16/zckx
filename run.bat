@echo on
python get_articles_list.py
cd zckx
scrapy crawl zckx -o items.json
pause