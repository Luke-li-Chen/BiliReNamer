from urllib import request
from io import BytesIO
import gzip


def GetHTML(url):
    try:
        f = request.urlopen(url)
    except BaseException as e:
        print('出现异常，url为 %s' % url)
        print(e)
        return null

    rawdata = f.read()
    headers = f.info()

    # 若网页压缩，则使用gzip解压
    if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
        ('content-encoding' in headers and headers['content-encoding']):
        data = BytesIO(rawdata)
        gz = gzip.GzipFile(fileobj = data)
        rawdata = gz.read()
        gz.close()

    # 字节流转字符串
    html = rawdata.decode('utf-8')

    return html

