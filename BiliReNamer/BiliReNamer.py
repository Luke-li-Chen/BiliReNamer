from GetHTML import GetHTML

url = 'http://www.bilibili.com/video/av5974216/'
#url = 'http://www.baidu.com'
#url = 'https://api.douban.com/v2/book/2129650'

html = GetHTML(url)
print(html)


