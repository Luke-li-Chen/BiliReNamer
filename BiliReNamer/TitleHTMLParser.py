from html.parser import HTMLParser
from html.entities import name2codepoint

# 派生的 HTML 分析器类
class TitleHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)   # 继承父类的构造函数
        self.titles = []            # 存储总标题
        self.options = []           # 存储分P标题
        self.processing = None
        self.author = None          # 存储UP主
        self.authorFlag = False

    def handle_starttag(self, tag, attrs):
        # 总标题获取
        # <h1 title="XXX">XXX</h1>
        if tag == "h1" and len(attrs) != 0:
            for (variable, value) in attrs:
                if variable == "title":
                    self.titles.append(value)   # 存储总标题

        # 分P标题获取
        # <option value='/video/av1234567/index_1.html'>XXX</option>
        # <option value='/video/av1234567/index_2.html'>YYY</option>
        # <option value='/video/av1234567/index_3.html'>ZZZ</option>
        if tag == "option" and len(attrs) != 0:
            self.processing = tag       # 准备存储分P标题

        # UP主获取
        # <meta name="author" content="XXX" />
        if tag == 'meta' and len(attrs) != 0:
            for (variable, value) in attrs:
                if (variable == "name") and (value == 'author'):
                    self.authorFlag = True      # 准备存储UP主
                if (variable == "content") and self.authorFlag:
                    self.author = value         # 存储UP主
                    self.authorFlag = False     # 取消准备存储UP主

    def handle_data(self, data):
        if self.processing:
            self.options.append(data)   # 存储分P标题

    def handle_endtag(self, tag):
        if tag == self.processing:      # 即 </option>
            self.processing = None      # 取消准备存储分P标题


# 信息存储类
class TitleInfo(object):
    def __init__(self, nParts, title, author, options):
        self.nParts = nParts
        self.title = title
        self.author = author
        self.options = options


# 由 HTML 代码获取标题和UP主信息
def GetTitle(html):
    parser = TitleHTMLParser()
    parser.feed(html)           # 分析HTML
    parser.close()

    if len(parser.titles) == 1: # 有正确内容时
        nParts = len(parser.options)
        if nParts == 0:
            nParts = 1
            parser.options.append(parser.titles[0]) # 对于单P视频，将总标题作为第1P标题
        info = TitleInfo(nParts, parser.titles[0], parser.author, parser.options)
        return info;
    else:       # 无正确内容时（视频不存在）
        info = TitleInfo(0, None, None, [])
        return info;


