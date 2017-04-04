
'''
  使用 spider arguments

  您可以通过-a 在运行它们时使用该选项为您的蜘蛛提供命令行参数：

    scrapy crawl demo7 -o demo7-humor.json -a tag=humor

    __init__默认情况下，这些参数传递给Spider的方法并成为spider属性。

    在这个例子中，为tag参数提供的值将通过self.tag。您可以使用它来使您的蜘蛛仅使用特定标记提取引号，并根据参数构建URL：

'''
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "demo7"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)


'''
如果您将tag=humor参数传递给此蜘蛛，您会注意到它只会访问humor标记中的URL ，例如 http://quotes.toscrape.com/tag/humor。

您可以在这里了解更多关于处理蜘蛛参数的信息。https://doc.scrapy.org/en/latest/topics/spiders.html#spiderargs
'''

'''
启动项目
    scrapy crawl demo7

    scrapy crawl demo7 -o demo7-humor.json -a tag=humor

    过滤没有带 humor的
'''