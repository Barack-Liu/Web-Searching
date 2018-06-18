In this section, I'll be going through some of the main features of Scrapy and sharing how we used it in our project.

## Tasks:

For each website given, we need to crawl all the news starting from year 2015 (including 2015) up to now. Additionally, the system should work in real-times.
Our data sources are from Chinese financail news. Here they are.
```
Data Source (Chinese financial news):
http://www.eastmoney.com
http://finance.sina.com.cn
http://www.10jqka.com.cn
http://finance.qq.com
http://www.cnstock.com
http://business.sohu.com
```

## Scrapy

Let's first initialize a new Scrapy project. This is done as follows:
```
scrapy startproject finance
```
We can create a project structure as follows:
```
|-- finance
|   |-- __init__.py
|   |-- items.py
|   |-- pipelines.py
|   |-- settings.py
|   `-- spiders
|       |-- a10jqka.py
|       |-- cnstock.py
|       |-- eastmoney.py
|       |-- __init__.py
|       |-- qq.py
|       |-- sina.py
|       `-- sohu.py
|-- output
|   |-- a10jqka.json
|   |-- cnstock.json
|   |-- eastmoney.json
|   |-- qq.json
|   |-- sina.json
|   `-- sohu.json
|-- README.md
|-- scrapy.cfg
`-- start.sh
```

The first file we'll take a look at it is items.py, which specifies Scrapy classes that represent the items to be scraped.
Since our data should be stored in plain text format. Each line should be a json of one document. For each document json should be like,

```
doc= {"content": "xxx", "source": "xxx", "time": "xxx", "title": "xxx", "url": "xxx"}.
```

A sample class could look like this:
```
import scrapy


class FinanceItem(scrapy.Item):
    content = scrapy.Field()
    source = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()

    pass
```

The type of the Scrapy Field is a Python type and we can access the item using the common Python dictionary syntax.
For example:
```
item = FinanceItem()
item['content'] = ''.join(response.xpath('//div[@class="article"]/p/text()').extract())
item['source']  = 'sina'
item['time']    = response.xpath('//div[@class="date-source"]/span[@class="date"]/text()').extract()[0]
item['title']   = response.xpath("/html/head/title/text()").extract()[0]
item['url']     = response.url
```

Now, let's take a look at the more interesting spiders directory. Note that there is no file created for you by default. Scrapy expects you to create these spiders as separate files, and then they can be invoked by scrapy crawl `SPIDER_NAME_HERE`. Let's write up a sample spider now.

```
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
```

Note that the class takes in a CrawlSpider as the class parameter. A CrawlSpider simply clicks on all the links on a page, as a web crawler usually does, and verifies each of the link with the rules tuple. The tuple is ordered in terms of significance, meaning that the earlier elements in the tuple are rated higher than the later ones. Each Rule relies on the LinkExtractor class, which is essentially a regex verifying the links.

We define several rules as follows.
```
'sina':'.*?/doc-[a-z]*[0-9]*\.shtml',
'10jqka':'.*?/c[0-9]*\.shtml',
'cnstock':'.*?/news,bwkx-[0-9]{6}-[0-9]{7}.htm',
'eastmoney':'.*?/n.*?.\/[0-9]*,[0-9]*\.html',
'qq':'.*?/a/[0-9]*/[0-9]*\.htm',
'sohu':'.*?/a/[0-9]{9}_[0-9]{6}'
```

Finally, we can begin parsing the page with response and response.body. We do this primarily with Beautiful Soup, and by simply finding tags on the page. It's easiest to scrape website which uses `xpath`.
For example:
```
def parse_item(self, response):
    item = FinanceItem()
    item['content'] = ''.join(response.xpath('//article[@class="article"]/p/text()').extract())
    item['source']  = 'sohu'
    item['time']    = response.xpath('//div[@class="article-info"]/span[@class="time"]/text()').extract()[0]
    item['title']   = response.xpath("/html/head/title/text()").extract()[0]
    item['url']     = response.url
```

We can get the output in JSON format with the following call:
```
scrapy crawl qq -o ./output/qq.json
```

To make the system work in real-times, we save the command to `start.sh` and create a crontab task to execute it.
start.sh
```
#!/bin/sh
mkdir -p ./output
scrapy crawl eastmoney -o ./output/eastmoney.json
scrapy crawl 10jqka -o ./output/a10jqka.json
scrapy crawl qq -o ./output/qq.json
scrapy crawl sina -o ./output/sina.json
scrapy crawl cnstock-o ./output/cnstock.json
scrapy crawl sohu -o ./output/sohu.json
```

crontab
```
0 0 * * * /bin/sh start.sh
```

So, running the spider leads to the following log:
```
...
2018-06-10 19:20:15 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 73585,
 'downloader/request_count': 280,
 'downloader/request_method_count/GET': 280,
 'downloader/response_bytes': 3064684,
 'downloader/response_count': 280,
 'downloader/response_status_count/200': 280,
 'dupefilter/filtered': 1659,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2018, 6, 10, 11, 20, 15, 349395),
 'item_scraped_count': 279,
 'log_count/DEBUG': 561,
 'log_count/INFO': 8,
 'request_depth_max': 4,
 'response_received_count': 280,
 'scheduler/dequeued': 280,
 'scheduler/dequeued/memory': 280,
 'scheduler/enqueued': 280,
 'scheduler/enqueued/memory': 280,
 'start_time': datetime.datetime(2018, 6, 10, 11, 20, 12, 60623)}
2018-06-10 19:20:15 [scrapy] INFO: Spider closed (finished)
```
