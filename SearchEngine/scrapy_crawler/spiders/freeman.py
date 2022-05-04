import re, extruct, unicodedata
from w3lib.url import url_query_cleaner
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

# 'freemanmoore' : Crawler that includes json data
class FreemanCrawler_Data(CrawlSpider):
    name = 'freemanmoore'
    allowed_domains = ['freemanmoore.net']
    start_urls = ['http://freemanmoore.net/']
    handle_httpstatus_list = [400, 410, 301, 500]
    response_text = {}
    stop_words = list(set(stopwords.words('english')))
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
        # The following code was modeled after a snippet of code here:
        # https://www.traindex.io/blog/event-driven-data-pipelines-in-aws-480i/
        def preprocess(txt, stop_words, stem=False):
            char_rm = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
            emailAddr, htmlTags = "[\w.+-]+@[\w-]+\.(?:[\w-]\.?)+[\w-]", "<[^>\s]+>"

            txt = txt.lower()
            txt = unicodedata.normalize("NFKD",''.join(txt))
            txt = txt.replace('\t'," ").replace('\r'," ").replace('\n'," ")
            txt = re.sub(emailAddr, "", str(txt)).strip()
            txt = re.sub(htmlTags, "", str(txt)).strip()

            # Remove link, user and special characters
            txt = re.sub(char_rm, ' ', str(txt)).strip()
            txt_token = word_tokenize(txt)
            tokens = []
            for token in txt_token:
                if token not in stop_words:
                    if stem:
                        tokens.append(stemmer.stem(token))
                    else:
                        tokens.append(token)
            wordLemm = WordNetLemmatizer()
            finalwords=[]
            for w in tokens:
                if len(w) > 1:
                    word = wordLemm.lemmatize(w)
                    finalwords.append(word)
            return ' '.join(finalwords)
        
        def url_format(response):
            if response.url.endswith('.txt'):
                url_format = 'txt'
            elif response.url.endswith('.php'):
                url_format = 'php'
            elif response.url.endswith('.htm'):
                url_format = 'htm'
            elif response.url.endswith('.html'):
                url_format = 'html'
            else:
                url_format = 'NaN'
            return url_format


        url_response = urlopen(response.url).read()
        soup = BeautifulSoup(url_response, "lxml")

        for tag in soup.find_all(['script', 'style', 'head', 'title']):
            tag.decompose()

        txt = ' '.join(soup.findAll(text=True))
        txt = " ".join(txt.split())
        txt = preprocess(txt, self.stop_words)
        link_format = url_format(response)

        if txt in self.response_text.keys():
            None
        else:
            self.response_text[txt] = response.url

        return {
            'url': response.url,
            'format': link_format,
            'title': response.css('title::text').extract(),
            'text': txt
        }
