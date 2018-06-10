#!/bin/sh
scrapy crawl eastmoney -o ./output/eastmoney.json
scrapy crawl 10jqka -o ./output/a10jqka.json
scrapy crawl qq -o ./output/qq.json
scrapy crawl sina -o ./output/sina.json
scrapy crawl cnstock -o ./output/cnstock.json
scrapy crawl sohu -o ./output/sohu.json
