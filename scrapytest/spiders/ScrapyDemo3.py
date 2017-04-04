import scrapy
'''
<div class="quote">
    <span class="text">“The world as we have created it is a process of our
    thinking. It cannot be changed without changing our thinking.”</span>
    <span>
        by <small class="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
    </span>
    <div class="tags">
        Tags:
        <a class="tag" href="/tag/change/page/1/">change</a>
        <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
        <a class="tag" href="/tag/thinking/page/1/">thinking</a>
        <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
</div>

'''
class QuotesSpider(scrapy.Spider):
    name = "demo3"
    start_urls = [
        'http://quotes.toscrape.com',
        # 'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'demo3-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

        # 1.获取引用 [<Selector xpath="descendant-or-self::div[@class and contains(concat(' ......
        print("------------------1",response.css("div.quote"))
        # 选择第一个
        quote = response.css("div.quote")[0];
        # 2.title  :“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
        title=quote.css("span.text::text").extract_first();
        print("------------------2",title)
        # 3.获取author  :Albert Einstein
        author = quote.css("small.author::text").extract_first()
        print("------------------3",author)

        # 4. 鉴于标签是字符串列表，我们可以使用该.extract()方法来获取所有这些：  ['change', 'deep-thoughts', 'thinking', 'world']
        tags = quote.css("div.tags a.tag::text").extract()
        print("------------------4",tags)

        # 5. 已经弄清楚如何提取每一个位，我们现在可以遍历所有引号元素，并把它们放在一个Python字典中：
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            print("------------------5",dict(text=text, author=author, tags=tags))

# ------------------5 {'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'ta
# gs': ['change', 'deep-thoughts', 'thinking', 'world']}
# ------------------5 {'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
# ------------------5 {'text': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'author': 'Alber
# t Einstein', 'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles']}
# ------------------5 {'text': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'author': 'Jane Austen', 'tags': ['aliterac
# y', 'books', 'classic', 'humor']}
# ------------------5 {'text': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'author': 'Marilyn Monroe', 'tags':
# ['be-yourself', 'inspirational']}
# ------------------5 {'text': '“Try not to become a man of success. Rather become a man of value.”', 'author': 'Albert Einstein', 'tags': ['adulthood', 'success', 'value']}
# ------------------5 {'text': '“It is better to be hated for what you are than to be loved for what you are not.”', 'author': 'André Gide', 'tags': ['life', 'love']}
# ------------------5 {'text': "“I have not failed. I've just found 10,000 ways that won't work.”", 'author': 'Thomas A. Edison', 'tags': ['edison', 'failure', 'inspirational', 'para
# phrased']}
# ------------------5 {'text': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'author': 'Eleanor Roosevelt', 'tags': ['misattributed-eleanor
# -roosevelt']}
# ------------------5 {'text': '“A day without sunshine is like, you know, night.”', 'author': 'Steve Martin', 'tags': ['humor', 'obvious', 'simile']}


'''
启动项目
    scrapy crawl demo3

提取全部数据
Extracting Total data
scrapy shell "http://quotes.toscrape.com/page/1/"

'''