@echo on
python get_articles_list.py
cd zckx
rd /s /q posts
mkdir posts
scrapy crawl zckx -s LOG_LEVEL="WARNING"
python publish.py
pause