from scrapy import Spider

class Venom(Spider):
    name = 'Venom'
    start_urls = ['http://quotes.toscrape.com/page/1/',
                  'http://quotes.toscrape.com/page/2/'
                  ]

    def parse(self, response):
        for quote in response.csv('div.quote'):
            yield{
                'text': quote.css('span.text::text').extract(),
                'author': quote.css('small.author::text').extract(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }