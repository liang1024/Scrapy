import scrapy

class QuotesSpider(scrapy.Spider):
    name = "demo4"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }


''' 如果你运行这个蜘蛛，它会输出提取的数据与日志：
   1. scrapy crawl demo4


2016-09-19 18:57:19 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'tags': ['life', 'love'], 'author': 'André Gide', 'text': '“It is better to be hated for what you are than to be loved for what you are not.”'}
2016-09-19 18:57:19 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'tags': ['edison', 'failure', 'inspirational', 'paraphrased'], 'author': 'Thomas A. Edison', 'text': "“I have not failed. I've just found 10,000 ways that won't work.”"}
'''

# 通过使用Feed exports,，使用以下命令，最简单的方法来存储刮除的数据：
#     2.scrapy crawl demo4 -o demo4.json
# demo4.json包含 所有Scrat项目的文件，并以JSON序列化。
#  注意:如果重复运行会造成数据叠加，导致json文件出错，建议删除后再运行


# 您也可以使用其他格式，如JSON Lines：
#   3.scrapy crawl quotes -o quotes.jl
# 该JSON行格式是有用的，因为它的流状，你可以很容易地新记录追加到它。当运行两次时，它没有相同的JSON问题。另外，由于每条记录都是单独的行，所以您可以处理大文件，而无需将内存中的所有内容都放在一起，还有JQ等工具可以帮助您在命令行中执行此操作。
#在小项目（如本教程中的一个）中，这应该是足够的。但是，如果要使用已刮取的项目执行更复杂的操作，则可以编写项目管道。在项目创建时，您已经为您设置了项目管道的占位符文件 tutorial/pipelines.py。虽然您只需要存储已刮取的项目，但不需要实施任何项目管道。


'''
启动项目
    scrapy crawl demo4

'''