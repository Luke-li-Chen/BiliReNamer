from html.parser import HTMLParser
from html.entities import name2codepoint

class TitleHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)   # 继承父类的构造函数
        self.titles = []            # 存储总标题
        self.options = []           # 存储分P标题
        self.processing = None

    def handle_starttag(self, tag, attrs):
        if tag == "h1" and len(attrs) != 0:
            for (variable, value) in attrs:
                if variable == "title":
                    self.titles.append(value)   # 存储总标题
        if tag == "option" and len(attrs) != 0:
            self.processing = tag       # 准备存储分P标题

    def handle_data(self, data):
        if self.processing:
            self.options.append(data)   # 存储分P标题

    def handle_endtag(self, tag):
        if tag == self.processing:
            self.processing = None

class TitleInfo(object):
    def __init__(self, nParts, title, options):
        self.nParts = nParts
        self.title = title
        self.options = options

def GetTitle(html):
    parser = TitleHTMLParser()
    parser.feed(html)           # 分析HTML
    parser.close()

    if len(parser.titles) == 1: # 有正确内容时
        nParts = len(parser.options)
        if nParts == 0:
            nParts = 1
            parser.options.append(parser.titles[0])
        info = TitleInfo(nParts, parser.titles[0], parser.options)
        return info;
    else:       # 无正确内容时（视频不存在）
        info = TitleInfo(0, None, None)
        return info;


