#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


from douban.items import Comment, BookMeta,  Subject

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.misc import arg_to_iter
from scrapy.utils.python import to_bytes

from twisted.internet.defer import DeferredList


import codecs
import json

import csv
class DoubanPipeline(object):
    def __init__(self):
        self.filee = open('book_id.txt', 'w+')
        #self.filee = open('book_meta.txt', 'w+')

    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        print(line)
        if len (item['douban_id'])> 1:
            self.filee.write(item['douban_id']+'\n')
        #self.filee.write(item['douban_id']+'\t'+item['name']+'\t'+item['tags']+'\n')
        return item
    def close_spider(self, spider):
        self.filee.close()
