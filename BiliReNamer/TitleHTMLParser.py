from html.parser import HTMLParser
from html.entities import name2codepoint

class TitleHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)   # 继承父类的构造函数
        self.links = []
        self.options = []
        self.processing = None

    def handle_starttag(self, tag, attrs):
        if tag == "h1" and len(attrs) != 0:
            for (variable, value) in attrs:
                if variable == "title":
                    self.links.append(value)
        if tag == "option" and len(attrs) != 0:
            self.processing = tag

    def handle_data(self, data):
        if self.processing:
            self.options.append(data)

    def handle_endtag(self, tag):
        if tag == self.processing:
            self.processing = None

def GetTitle(html):
    hp = TitleHTMLParser()
    hp.feed(html)
    hp.close()
    if len(hp.links) == 1:
        #print(hp.options)
        return (hp.links[0], hp.options)
    else:
        return None


