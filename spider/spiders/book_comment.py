#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import random
import string

from douban.items import Comment

from scrapy import Request, Spider

import codecs


class BookCommentSpider(Spider):
    name = 'book_comment'
    allowed_domains = ['book.douban.com']
    books=[line.strip() for line in codecs.open('./book_id.txt','r','utf8').readlines()]
    books=filter(lambda x:len(x)>0,books)
    start_urls = {
        str(i): ('https://m.douban.com/rexxar/api/v2/book/%s/interests?count=5&order_by=hot' % i) for i in books
    }

    def start_requests(self):
        for (key, url) in self.start_urls.items():
            headers = {
                'Referer': 'https://m.douban.com/book/subject/%s/comments' % key
            }
            bid = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))
            cookies = {
                'bid': bid,
                'dont_redirect': True,
                'handle_httpstatus_list': [302],
            }
            yield Request(url, headers=headers, cookies=cookies)

    def parse(self, response):
        if 302 == response.status:
            print(response.url)
        else:
            douban_id = response.url.split('/')[-2]
            items = json.loads(response.body)['interests']
            for item in items:
                comment = Comment()
                comment['douban_id'] = douban_id
                comment['douban_comment_id'] = item['id']
                comment['douban_user_nickname'] = item['user']['name']
                comment['douban_user_avatar'] = item['user']['avatar']
                comment['douban_user_url'] = item['user']['url']
                comment['content'] = item['comment']
                comment['votes'] = item['vote_count']
                yield comment
