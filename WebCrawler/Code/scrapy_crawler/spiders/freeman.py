import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FreemanCrawler(CrawlSpider):
    name = 'freemanmoore'
    allowed_domains = ['freemanmoore.net']
    start_urls = ['http://freemanmoore.net/']
    rules = (
        Rule(LinkExtractor(
            deny=[
                re.escape('http://freemanmoore.net/offsite'),
            ],
        )),
    )
