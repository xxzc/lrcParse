# -*- coding: utf-8 -*-
from scrapy import Request
import scrapy
from lrctime.items import Lrc
import HTMLParser


class LrcspiderSpider(scrapy.Spider):
    name = "lrcspider"
    allowed_domains = ["www.kasi-time.com"]

    def start_requests(self):
        return [Request('http://www.kasi-time.com/item-%d.html' % n, meta={'lid': n})
                for n in range(2, 4)]

    def parse(self, response):
        lid = response.meta['lid']
        sel = response.xpath('//*[@id="song_info_table"]')[0]
        lrc = Lrc()
        lrc['title'] = sel.xpath('./h1/text()')[0].extract().strip()
        lrc['singers'] = sel.xpath('.//tr[1]/td[2]//a/text()').extract()
        lrc['lyricists'] = sel.xpath('.//tr[2]/td[2]//a/text()').extract()
        lrc['composers'] = sel.xpath('.//tr[3]/td[2]//a/text()').extract()
        r = sel.xpath('.//tr[3]/td[4]/text()').extract()[0]
        lrc['access_rank'] = r[3:r.find(u'\u3000')]

        return Request('http://www.kasi-time.com/item_js.php?no='+str(lid),
                       meta={'lrc': lrc, 'lid': lid}, callback=self.parse_text)

    def parse_text(self, response):
        h = HTMLParser.HTMLParser()
        lrc = response.meta['lrc']
        raw = response.body_as_unicode()[18:-3]
        raw = h.unescape(raw)
        lrc['lyric'] = raw.replace('<br>', '\n')
        return lrc