# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from finance.items import FinanceItem


class QqSpider(CrawlSpider):
    name = 'qq'
    allowed_domains = ['finance.qq.com']
    start_urls = ['http://www.finance.qq.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?/a/[0-9]*/[0-9]*\.htm'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        item = FinanceItem()
        item['content'] = ''.join(response.xpath('//div[@class="Cnt-Main-Article-QQ"]/p/text()').extract())
        item['source']  = 'qq'
        item['datetime']    = response.xpath('//div[@class="a_Info"]/span[@class="a_time"]/text()').extract()[0]
        item['title']   = response.xpath("/html/head/title/text()").extract()[0]
        item['href']     = response.url
        item['type']   = u'\u5373\u65f6'

        return item
