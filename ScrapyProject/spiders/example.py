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
        # here is use find with css print 
        root = soup.find('id',class_="toc")
        print(root) 
        # here is use find with html print
        root = soup.find('div',class_="toc")
        print(root)
        # here is use find_all with css print
        root_child = root.find_all('li',class_='toclevel-1')  
        print(root_child)
        # here is use select with html print
        select_data = soup.select('div.toc > ul > li.toclevel-1')
        print(select_data)
        
        

process = CrawlerProcess()
process.crawl(ExampleSpider)
process.start()