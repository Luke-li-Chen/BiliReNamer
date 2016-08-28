from html.parser import HTMLParser
from html.entities import name2codepoint

class TitleHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            if len(attrs) != 0:
                for (variable, value) in attrs:
                    if variable == "title":
                        self.links.append(value)


def GetTitle(html):
    hp = TitleHTMLParser()
    hp.feed(html)
    hp.close()
    if len(hp.links) == 1:
        return hp.links[0]
    else:
        return None


