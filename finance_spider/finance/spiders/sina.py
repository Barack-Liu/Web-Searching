# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from finance.items import FinanceItem

class BangbingSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['finance.sina.com.cn']
    start_urls = ['http://finance.sina.com.cn/']

    rules = (
        Rule(LinkExtractor(allow='.*?/doc-[a-z]*[0-9]*\.shtml'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=False)

    def parse_item(self, response):
        item = FinanceItem()
        item['content'] = ''.join(response.xpath('//div[@class="article"]/p/text()').extract())
        item['source']  = 'sina'
        item['time']    = response.xpath('//div[@class="date-source"]/span[@class="date"]/text()').extract()[0]
        item['title']   = response.xpath("/html/head/title/text()").extract()[0]
        item['url']     = response.url
      
        yield item
