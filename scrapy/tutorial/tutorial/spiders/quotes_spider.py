'''
Executar spider no terminal:
scrapy runspider scraper.py
'''

import scrapy
from scrapyd_api import ScrapydAPI
from scrapy.crawler import CrawlerProcess

'''
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
'''


# Alterando o código acima para percorrer todas as páginas
# ========================================================

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        '''if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)'''
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        '''
        Você também pode passar um seletor para response.follow em vez de uma string.
        Este seletor deve extrair os atributos necessários:

        for href in response.css('ul.pager a::attr(href)'):
            yield response.follow(href, callback=self.parse)
        Para os elementos <a>, existe um atalho: response.follow usa seu atributo href automaticamente.
        Portanto, o código pode ser reduzido ainda mais:
        
        for a in response.css('ul.pager a'):
            yield response.follow(a, callback=self.parse)
        
        Para criar várias solicitações de um iterável, você pode usar response.follow_all:

        anchors = response.css('ul.pager a')
        yield from response.follow_all(anchors, callback=self.parse)
        
        ou, encurtando ainda mais:
        
        yield from response.follow_all(css='ul.pager a', callback=self.parse)
        '''

        # from scrapy.shell import inspect_response
        #
        # def parse_details(self, response, item=None):
        #     if item:
        #         # populate more `item` fields
        #         return item
        #     else:
        #         inspect_response(response, self)

        # from scrapy.utils.response import open_in_browser
        #
        # def parse_details(self, response):
        #     if "item name" not in response.body:
        #         open_in_browser(response)


class AuthorSpider(scrapy.Spider):
    name = "author"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response, **kwargs):
        # author_page_links = response.css(".author + a")
        # yield from response.follow_all(author_page_links, self.parse_author)
        yield from response.follow_all(css=".author + a", callback=self.parse_author)

        # pagination_links = response.css("li.next a")
        # yield from response.follow_all(pagination_links, self.parse)
        self.log(f"\n\n\npagination_links = {response.css('li.next a')}\n\n\n")
        yield from response.follow_all(css="li.next a", callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            # from scrapy.shell import inspect_response
            # inspect_response(response, self)
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }


# class MySpider(scrapy.Spider):
#     name = "myspider"
#     start_urls = [
#         "http://example.com",
#         "http://example.org",
#         "http://example.net",
#     ]
#
#     def parse(self, response):
#         # We want to inspect one specific response.
#         if ".org" in response.url:
#             from scrapy.shell import inspect_response
#             inspect_response(response, self)


# process = CrawlerProcess(settings={
#         "FEEDS": {
#             "items.json": {"format": "json"},
#         },
#     })
#
# process.crawl(QuotesSpider)
# process.start()  # the script will block here until the crawling is finished



# scrapyd = ScrapydAPI()
# scrapyd.schedule('amauri', 'quotes')



'''
stackoverflow
https://stackoverflow.com/questions/44228851/scrapy-on-a-schedule

Scrapy on a schedule

Getting Scrapy to run on a schedule is driving me around the Twist(ed).

I thought the below test code would work, but I get a twisted.internet.error.ReactorNotRestartable error when the 
spider is triggered a second time:

from quotesbot.spiders.quotes import QuotesSpider
import schedule
import time
from scrapy.crawler import CrawlerProcess

def run_spider_script():
    process.crawl(QuotesSpider)
    process.start()


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
})


schedule.every(5).seconds.do(run_spider_script)

while True:
    schedule.run_pending()
    time.sleep(1)
I'm going to guess that as part of the CrawlerProcess, the Twisted Reactor is called to start again, when that's not 
required and so the program crashes. Is there any way I can control this?

Also at this stage if there's an alternative way to automate a Scrapy spider to run on a schedule, I'm all ears. I 
tried scrapy.cmdline.execute , but couldn't get that to loop either:

from quotesbot.spiders.quotes import QuotesSpider
from scrapy import cmdline
import schedule
import time
from scrapy.crawler import CrawlerProcess


def run_spider_cmd():
    print("Running spider")
    cmdline.execute("scrapy crawl quotes".split())


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
})


schedule.every(5).seconds.do(run_spider_cmd)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    
EDIT

Adding code, which uses Twisted task.LoopingCall() to run a test spider every few seconds. Am I going about this 
completely the wrong way to schedule a spider that runs at the same time each day?

from twisted.internet import reactor
from twisted.internet import task
from scrapy.crawler import CrawlerRunner
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        quotes = response.xpath('//div[@class="quote"]')

        for quote in quotes:

            author = quote.xpath('.//small[@class="author"]/text()').extract_first()
            text = quote.xpath('.//span[@class="text"]/text()').extract_first()

            print(author, text)


def run_crawl():

    runner = CrawlerRunner()
    runner.crawl(QuotesSpider)


l = task.LoopingCall(run_crawl)
l.start(3)

reactor.run()


edited May 29 '17 at 21:30
asked May 28 '17 at 15:14

itzafugazi
11111 silver badge77 bronze badges
Why not simply use cron or systemd timers? – Granitosaurus May 28 '17 at 15:40
The web-scraping of data is only one part of the intended application, and I am hoping to have everything run as part 
of a single program. But yes, if I can't get this working as described, I will use an OS task scheduler to run the 
Scrapy script, with the rest of application running separately. – itzafugazi May 28 '17 at 16:15

First noteworthy statement, there's usually only one Twisted reactor running and it's not restartable (as you've 
discovered). The second is that blocking tasks/functions should be avoided (ie. time.sleep(n)) and should be replaced 
with async alternatives (ex. 'reactor.task.deferLater(n,...)`).

To use Scrapy effectively from a Twisted project requires the scrapy.crawler.CrawlerRunner core API as opposed to 
scrapy.crawler.CrawlerProcess. The main difference between the two is that CrawlerProcess runs Twisted's reactor for 
you (thus making it difficult to restart the reactor), where as CrawlerRunner relies on the developer to start the 
reactor. Here's what your code could look like with CrawlerRunner:

from twisted.internet import reactor
from quotesbot.spiders.quotes import QuotesSpider
from scrapy.crawler import CrawlerRunner

def run_crawl():
    """
    Run a spider within Twisted. Once it completes,
    wait 5 seconds and run another spider.
    """
    runner = CrawlerRunner({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        })
    deferred = runner.crawl(QuotesSpider)
    # you can use reactor.callLater or task.deferLater to schedule a function
    deferred.addCallback(reactor.callLater, 5, run_crawl)
    return deferred

run_crawl()
reactor.run()   # you have to run the reactor yourself



answered May 28 '17 at 17:41

notorious.no
4,12133 gold badges1717 silver badges3030 bronze badges
Thanks @notorious.no , this has begun clearing things up for me, but unfortunately I couldn't get this working on a 
schedule. I'm probably missing something obvious, but I don't see how I would implement this to run a spider at a 
specific time each day? The closest I can get is using Twisted task.LoopingCall(), which I could use to run a spider 
every 86400 seconds for a daily scrape, but am I going about this the wrong way? I've updated my post with the code 
for the loop, would really appreciate your guidance! – itzafugazi May 29 '17 at 21:27
2
LoopingCall will work fine and is the simplest solution. You could also modify the example code (ie. addCallback(
reactor.callLater, 5, run_crawl)) and replace 5 with the number of seconds that represents when you want to scrape 
next. This will give you a bit more precision as opposed to LoopingCall – notorious.no Jun 2 '17 at 14:46
Thanks @notorious.no . I misunderstood what was happening with the deferred.addCallback, a bit of timestamping in 
debug and it's starting to make sense. This is finally going to work for me, thanks a lot for your help! – itzafugazi 
Jun 3 '17 at 23:35
I'm getting an error that says assert callable(_f), "%s is not callable" % _f builtins.AssertionError: 8 is not 
callable. Using version 2.3.0. Please help! – ProgramSpree Oct 21 '20 at 4:19
'''
