import re
from w3lib.url import url_query_cleaner
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import extruct
from bs4 import BeautifulSoup
from urllib.request import urlopen

def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

# 'freeman' : Crawler that returns default parameters
class FreemanCrawler_Normal(CrawlSpider):
    name = 'freeman'
    allowed_domains = ['freemanmoore.net']
    start_urls = ['http://freemanmoore.net/']
    rules = (
        Rule(
            LinkExtractor(
                deny=[
                    re.escape('http://freemanmoore.net/offsite'),
                    re.escape('http://lyle.smu.edu'),
                    re.escape('http://www.gedpage.com/soundex.html'),
                    re.escape('https://en.wikipedia.org/wiki/Noindex'),
                ],
            ),
            process_links=process_links
        ),
    )

# 'freemanmoore' : Crawler that includes json data
class FreemanCrawler_Data(CrawlSpider):
    name = 'freemanmoore'
    allowed_domains = ['freemanmoore.net']
    start_urls = ['http://freemanmoore.net/']
    handle_httpstatus_list = [400, 410, 301, 500]
    rules = (
        Rule(
            LinkExtractor(
                deny=[
                    re.escape('http://freemanmoore.net/offsite'),
                    re.escape('http://lyle.smu.edu'),
                    re.escape('http://www.gedpage.com/soundex.html'),
                    re.escape('https://en.wikipedia.org/wiki/Noindex'),
                ],
            ),
            process_links=process_links,
            callback='parser',
            follow=True
        ),
    )

    def parser(self, response):

        url_response = urlopen(response.url).read()
        soup = BeautifulSoup(url_response, "lxml")
        updatess = soup.body.p.text
        print(updatess)
        if str(soup.body.p.text).find("Last Updated") != -1:
            dater = str(soup.body.p).find("Last Updated");
            print(dater)
        # updated = soup.body.p.textfindAll("p")

        # if str(updated).find("Last Updated"):
        #     updates = str(updated).find("Last Updated")
        #     print("Here: ", updates)

        return {
            'url': response.url,
            'title': soup.head.title.text,
            # 'metadata': extruct.extract(
            #    response.text,
            #    response.url,
            #),
        }
