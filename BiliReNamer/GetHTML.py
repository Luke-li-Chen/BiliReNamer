from urllib import request
from io import BytesIO
import gzip

def GetHTML(url) :
    f = request.urlopen(url)

    rawdata = f.read()
    headers = f.info()

    if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
        ('content-encoding' in headers and headers['content-encoding']):
        print('压缩')
        data = BytesIO(rawdata)
        gz = gzip.GzipFile(fileobj = data)
        rawdata = gz.read()
        gz.close()
    else:
        print('未压缩')

    html = rawdata.decode('utf-8')

    return html

