from GetHTML import GetHTML
from TitleHTMLParser import GetTitle

#url = 'http://www.bilibili.com/video/av5687666'
url = 'http://www.bilibili.com/video/av965983'
#url = 'http://www.bilibili.com/video/av5974216'     # 已被删除


html = GetHTML(url)
#print(html)
title, options = GetTitle(html)

if title == None:
    print('---')
else:
    print(title)
    print(options)

