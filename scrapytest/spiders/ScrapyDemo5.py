import scrapy
'''
现在您已经知道如何从页面中提取数据，我们来看看如何跟踪它们的链接。
首先是提取我们想要跟踪的页面的链接。检查我们的页面，我们可以看到有一个链接到下一个页面与以下标记：

<ul class="pager">
    <li class="next">
        <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
    </li>
</ul>

我们可以尝试在shell中提取它：

>>> response.css('li.next a').extract_first()
'<a href="/page/2/">Next <span aria-hidden="true">→</span></a>'

这得到了锚点元素，但是我们需要该属性href。为此，Scrapy支持CSS扩展，您可以选择属性内容，如下所示：

>>> response.css('li.next a::attr(href)').extract_first()
'/page/2/'



让我们看看现在我们的蜘蛛修改为递归地跟随链接到下一页，从中提取数据：
'''
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "demo5"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

'''
现在，在提取数据之后，该parse()方法会查找到下一页的链接，使用该urljoin()方法构建完整的绝对URL （由于链接可以是相对的），并且向下一页产生一个新的请求，将其注册为回调以处理下一页的数据提取，并保持爬行遍历所有页面。

您在这里看到的是Scrapy的以下链接机制：当您以回调方式生成请求时，Scrapy将安排该请求发送，并注册一个回调方法，以在该请求完成时执行。

使用它，您可以根据您定义的规则构建复杂的跟踪链接，并根据访问页面提取不同类型的数据。

在我们的示例中，它创建一个循环，跟随到所有到下一页的链接，直到它找不到一个方便的抓取博客，论坛和其他站点分页。
'''




'''
启动项目
    scrapy crawl demo5

'''