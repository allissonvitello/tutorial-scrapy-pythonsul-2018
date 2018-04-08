from scrapy import Spider

class HomeRobot(Spider):
    name = 'porco_aranha'
    start_urls = ['http://pt.wikipedia.org/wiki/Python']

    def parse(self, response):
        self.log('Visitei o site: %s' % response.url)