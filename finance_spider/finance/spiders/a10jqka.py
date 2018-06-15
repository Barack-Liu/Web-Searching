# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from finance.items import FinanceItem


class A10jqkaSpider(CrawlSpider):
    name = '10jqka'
    allowed_domains = ['m.10jqka.com.cn']
    start_urls = ['http://m.10jqka.com.cn/']

    rules = (
        Rule(LinkExtractor(allow='.*?/c[0-9]*\.shtml'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        print response.url,'---------------------'
        item = FinanceItem()
        item['content'] = ''.join(response.xpath('//p/text()').extract())
        item['source']  = '10jqka'
        item['datetime']    = response.xpath('//div[@class="date"]/span/text()').extract()[0][:19]
        item['title']   = response.xpath("/html/head/title/text()").extract()[0]
        item['href']    = response.url
        item['type']    = u'\u5373\u65f6'

        yield item
