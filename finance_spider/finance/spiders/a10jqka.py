# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from finance.items import FinanceItem


class A10jqkaSpider(CrawlSpider):
    name = '10jqka'
    allowed_domains = ['m.10jqka.com.cn']
    
    start_urls = []
    with open('./finance/start_urls.txt') as fp:
        data = fp.readline().strip()
        while data !='':
            start_urls.append(data)
            data = fp.readline()

    rules = (
        Rule(LinkExtractor(allow='.*?/c[0-9]*\.shtml'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        print response.url,'---------------------'
        item = FinanceItem()
        text = response.xpath('//p/text()').extract()
        content = []
        for t in text:
            content.append(["p", t])
        item['content'] = str(content) 
        item['source']  = '10jqka'
        item['datetime']    = response.xpath('//div[@class="date"]/span/text()').extract()[0][:19]
        item['title']   = response.xpath("/html/head/title/text()").extract()[0]
        item['href']    = response.url
        item['type']    = '10jqka'

        yield item
