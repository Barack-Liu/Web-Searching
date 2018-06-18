# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from finance.items import FinanceItem

class CnstockSpider(CrawlSpider):
    name = 'cnstock'
    allowed_domains = ['news.cnstock.com']
    start_urls = ['http://news.cnstock.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?/news,bwkx-[0-9]{6}-[0-9]{7}.htm'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        item = FinanceItem()
        text = response.xpath('//div[@class="content"]/p/text()').extract()
        text = response.xpath('//p/text()').extract()
        content = []
        for t in text:
            content.append(["p", t])
        item['content'] = str(content)
        item['source']  = 'cnstock'
        item['datetime']    = response.xpath('//div[@class="bullet"]/span[@class="timer"]/text()').extract()[0]
        item['title']   = response.xpath("/html/head/title/text()").extract()[0]
        item['href']    = response.url
        item['type']    = 'cnstock'

        yield item
