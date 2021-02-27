import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['https://zh.wikipedia.org/wiki/%E9%87%91%E6%AD%A3%E6%81%A9']

    def parse(self, response):
        content = response.body
        soup = BeautifulSoup(content, "html5lib")
        root = soup.find('div',class_="toc")
        print(root)   

process = CrawlerProcess()
process.crawl(ExampleSpider)
process.start()