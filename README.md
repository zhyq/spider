# spider

### 使用方法
-------
    $ scrapy list
    # 抓取书籍数据
    $ scrapy crawl -o item.json book_subject # 收集书籍 Subject ID
    $ scrapy crawl book_meta # 收集书籍元数据
    $ scrapy crawl book_comment # 收集书籍评论
    
### tips
	1 定期设置动态 user agent
	2 download_delay 设置

感谢作者分享，参考地址：https://github.com/40robber/ScrapyDouban
