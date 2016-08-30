import os

urlRoot = 'http://www.bilibili.com/video/av'
rootPath = r'E:\Chen_Li\Videos\Test'


global g_avNums
g_avNums = []

def IsInteger(x_str):
    try:
        i = int(x_str)
    except ValueError:
        return False
    else:
        return True

def ChToRootPath():
    #rootPath = input()
    os.chdir(rootPath);

def GetAVNList():
    global g_avNums
    g_avNums = [x for x in os.listdir('.') if (os.path.isdir(x) and IsInteger(x))]
    return g_avNums

#def GetURLs():
#    global g_avNums
#    for avNum in g_avNums:
#        url = urlRoot + avNum
#        print(url)