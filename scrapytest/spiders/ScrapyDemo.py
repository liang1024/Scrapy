import scrapy


class QuotesSpider(scrapy.Spider):
    name = "demo1"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'demo1-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

'''
name：识别蜘蛛。它在项目中必须是唯一的，也就是说，您不能为不同的Spiders设置相同的名称。
start_requests()：必须返回一个可迭代的请求（您可以返回一个请求列表或写一个生成器函数），Spider将开始爬行。随后的请求将从这些初始请求连续生成。
parse()：一种将被调用来处理为每个请求下载的响应的方法。response参数是一个TextResponse保存页面内容的实例，并且还有其他有用的方法来处理它。
该parse()方法通常解析响应，将刮取的数据提取为示例，并且还可以查找新的URL以从中创建新的请求（Request）。

'''



'''
要使我们的蜘蛛工作，请转到项目的顶级目录并运行：
scrapy crawl demo1

现在，检查当前目录下的文件。
您应该注意到，已经创建了两个新文件：quotes-1.html和quotes-2.html，
其中包含各个URL的内容，正如我们的parse方法指示。
'''