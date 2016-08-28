from GetHTML import GetHTML
from TitleHTMLParser import GetTitle

#url = 'http://www.bilibili.com/video/av5687666'
url = 'http://www.bilibili.com/video/av965983'


#url = 'http://www.baidu.com'
#url = 'https://api.douban.com/v2/book/2129650'

html = GetHTML(url)
#print(html)
print(GetTitle(html))

