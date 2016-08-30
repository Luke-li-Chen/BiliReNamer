from GetHTML import GetHTML
from TitleHTMLParser import GetTitle

##url = 'http://www.bilibili.com/video/av5687666'     # 1Part
#url = 'http://www.bilibili.com/video/av965983'      # 3Part
##url = 'http://www.bilibili.com/video/av5974216'     # 已被删除
##url = 'http://www.bilibili.com/video/av1234567'      # 特殊符号 &quot;


#html = GetHTML(url)
#info = GetTitle(html)

#if info.nParts == 0:
#    print('---')
#else:
#    print(info.title)
#    print(info.author)
#    for i in range(info.nParts):
#        print(info.options[i])


import os
import GetURL

def GetInfo(avNum):
    url = GetURL.urlRoot + avNum
    html = GetHTML(url)
    info = GetTitle(html)
    return info


GetURL.ChToRootPath()

#print(os.path.abspath('.'))

AVNums = GetURL.GetAVNList()

for avNum in AVNums:
    info = GetInfo(avNum)
    
    if info.nParts == 0:
        print('---')
    else:
        print(info.title)
        for i in range(info.nParts):
            print(info.options[i])

    newPath = os.path.join(GetURL.rootPath, avNum)
    os.chdir(newPath)
    DirPath = os.path.abspath('.')

    for x in os.listdir('.') :
        if (os.path.isdir(x) and GetURL.IsInteger(x)):
            os.chdir(x)
            #DirPath = os.path.abspath('.')
            #print(os.path.abspath('.'))

            fileNameOld = [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.mp4'][0]
            filePathOld = os.path.abspath(fileNameOld)
            
            nP = int(x)

            if info.nParts == 1:
                pass
            else:
                fileNameNew = info.options[nP - 1]
                fileNameNew += '.mp4'
                filePathNew = os.path.join(DirPath, fileNameNew)
                #print(filePathNew)
                os.rename(filePathOld, filePathNew)
            


            os.chdir('..')
            #print(x)
    #print(newPath)

    print('\n')


#GetURL.GetURLs()

    
