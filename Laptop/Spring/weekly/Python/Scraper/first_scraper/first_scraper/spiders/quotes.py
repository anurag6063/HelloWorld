import scrapy
import requests

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
			'https://en.oxforddictionaries.com/definition/well'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            requests.post('http://135.36.0.89:9201/scrapy_first_scraper_2/doc/', json={"fileName": page, "url": response.url, "fileContent":response.text} )
        self.log('Saved file %s' % filename)
        
		