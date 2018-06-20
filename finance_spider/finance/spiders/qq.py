# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from finance.items import FinanceItem


class QqSpider(CrawlSpider):
    name = 'qq'
    allowed_domains = ['finance.qq.com']
    start_urls = []

    with open('./finance/urls/qq.txt') as fp:
        data = fp.readline().strip()
        while data !='':
            start_urls.append(data)
            data = fp.readline().strip()

    rules = (
        Rule(LinkExtractor(allow=r'.*?/a/[0-9]*/[0-9]*\.htm'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        item = FinanceItem()
        text = response.xpath('//div[@class="Cnt-Main-Article-QQ"]/p/text()').extract()
        content = []
        for t in text:
            content.append(["p", t])
        item['content'] = content
        item['source']  = 'qq'
        item['datetime']    = response.xpath('//div[@class="a_Info"]/span[@class="a_time"]/text()').extract()[0]
        item['title']   = response.xpath("/html/head/title/text()").extract()[0]
        item['href']    = response.url
        item['type']   = 'qq'

        return item
