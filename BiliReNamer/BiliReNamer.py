from GetHTML import GetHTML
from TitleHTMLParser import GetTitle

#url = 'http://www.bilibili.com/video/av5687666'     # 1Part
#url = 'http://www.bilibili.com/video/av965983'      # 3Part
url = 'http://www.bilibili.com/video/av5974216'     # 已被删除


html = GetHTML(url)
info = GetTitle(html)

if info.nParts == 0:
    print('---')
else:
    print(info.title)
    for i in range(info.nParts):
        print(info.options[i])
