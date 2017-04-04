
'''
这是另一个蜘蛛，说明回调和以下链接，这次是为了刮取作者信息：
'''
import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages  跟随作者的链接页面
        for href in response.css('.author + a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href),callback=self.parse_author)

        # follow pagination links 遵循分页链接
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
'''
这个蜘蛛将从主页面开始，它将跟随所有到作者页面的链接parse_author，每个页面都调用它们的parse回调，以及我们之前看到的回调的分页链接。

该parse_author回调定义了一个辅助函数从CSS查询提取和清理数据，并产生了Python字典与作者的数据。

这个蜘蛛演示的另一个有趣的事情是，即使同一作者有许多引号，我们也不用担心多次访问同一作者页面。默认情况下，Scrapy会将重复的请求过滤出已访问的URL，避免了由于编程错误导致服务器太多的问题。这可以通过设置进行配置 DUPEFILTER_CLASS。

希望现在您对Scrapy的使用以下链接和回调的机制有很好的了解。

作为利用以下链接机制的蜘蛛蜘蛛，请查看CrawlSpider一个通用蜘蛛的类，实现一个小型规则引擎，您可以使用它来将爬虫编写在其上。

另外，一个常见的模式是用多个页面的数据构建一个项目，使用一个技巧将附加数据传递给回调。
'''

'''
启动项目
    scrapy crawl author

'''