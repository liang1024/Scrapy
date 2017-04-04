import scrapy

class QuotesSpider(scrapy.Spider):
    name = "demo2"

    '''
    start_requests方法的快捷方式
    您可以使用URL列表来定义一个类属性，而不是实现从URL start_requests()生成scrapy.Request对象的方法
    start_urls。此列表将被默认实现start_requests()用于为您的蜘蛛创建初始请求：
    '''
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
    ]

# 该parse()方法将被调用来处理这些URL的每个请求，即使我们没有明确地告诉Scrapy这样做。发生这种情况是因为parse()Scrapy的默认回调方法，对于没有明确分配的回调的请求而言。

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        # 1.使用CSS选择元素： <Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]
        print("------------------1",response.css('title'))
        # 2.从上面的标题中提取文本，您可以执行以下操作 :['Quotes to Scrape']
        print("------------------2",response.css('title::text').extract())
        # 3.没有指定::text，我们将获得完整的标题元素 ['<title>Quotes to Scrape</title>']
        print("------------------3",response.css('title').extract())
        # 4.  .extract()是列表(SelectorList)   只是想要第一个结果可以使用:extract_first()  :'Quotes to Scrape'
        print("------------------4",response.css('title::text').extract_first())
        # 5. 或者你可以写：                   : 'Quotes to Scrape'
        print("------------------5",response.css('title::text')[0].extract())
        # 但是，当没有找到与选择匹配的元素时，.extract_first()避免使用IndexError并返回 None。
        # 这里有一个教训：对于大多数刮削代码，您希望它能够因为页面上找不到的错误而具有弹性，因此即使某些部件无法被刮除，您至少可以获取一些数据。


# 除了extract()和 extract_first()方法之外，您还可以re()使用正则表达式提取该方法：

        # 6.       :['Quotes to Scrape']
        print("------------------6",response.css('title::text').re(r'Quotes.*'))
        # 7.       :['Quotes']
        print("------------------7",response.css('title::text').re(r'Q\w+'))
        # 8.       :['Quotes', 'Scrape']
        print("------------------8",response.css('title::text').re(r'(\w+) to (\w+)'))

#   除了CSS，Scrapy选择器还支持使用XPath表达式：
        # 9.[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]
        print("------------------9",response.xpath('//title'))
        # 10.'Quotes to Scrape'
        print("------------------10",response.xpath('//title/text()').extract_first())




'''

    scrapy crawl demo2

Extracting Total data
scrapy shell "http://quotes.toscrape.com/page/1/"

'''