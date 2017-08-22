@echo on
python get_articles_list.py
cd zckx
scrapy crawl zckx -s LOG_LEVEL="WARNING" -o items.json
pause