# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request
from finance.items import FinanceItem

class EastmoneySpider(CrawlSpider):
    name = "eastmoney"
    allowed_domains = ["finance.eastmoney.com"]
    start_urls = (
        'http://www.eastmoney.com',
        'http://finance.eastmoney.com/yaowen.html',
        'http://finance.eastmoney.com/pinglun.html',
        'http://finance.eastmoney.com/news/cgnjj.html',
        'http://finance.eastmoney.com/news/cgjjj.html'
    )

    rules = (
        Rule(LinkExtractor(allow='.*?/n.*?.\/[0-9]*,[0-9]*\.html'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        item = FinanceItem()
        text    = response.xpath('//div[@class="Body"]/p/text()').extract()
        content = []
        for t in text:
            content.append(["p", t])
        item['content'] = content
        #item['source'] = 'eastmoney'
        item['datetime'] = response.xpath('//div[@class="time"]/text()').extract()[0]
        item['title'] = response.xpath('//div[@class="newsContent"]/h1/text()').extract()[0]
        item['href'] = response.url
        item['type'] = 'eastmoney'
 
        yield item
        #yield Request(response.url)
