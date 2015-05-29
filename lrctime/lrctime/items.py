# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Lrc(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    singers = scrapy.Field()
    lyricists = scrapy.Field()
    composers = scrapy.Field()
    access_rank = scrapy.Field()
    lyric = scrapy.Field()
    pass
