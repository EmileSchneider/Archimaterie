import scrapy
import BeautifulSoup as bs

class ZefixSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [ ]
        start_url = "https://www.zefix.ch/en/search/entity/list/firm/"
        for i in range(0,150000):
            urls.append(start_url+i)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = bs(response)


