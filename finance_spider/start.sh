#!/bin/sh
scrapy crawl eastmoney -o result.json 
scrapy crawl 10jqka -o result.json
scrapy crawl qq -o result.json
scrapy crawl sina -o result.json
scrapy crawl cnstock -o result.json
scrapy crawl sohu -o result.json
