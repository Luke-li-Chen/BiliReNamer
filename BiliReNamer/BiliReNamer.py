import os
import GetURL
import shutil
import configparser

from GetHTML import GetHTML
from TitleHTMLParser import GetTitle

# 替换不能作为文件名的字符
def CharFilter(str):
    str = str.replace('\\', '_')
    str = str.replace('/', '_')
    str = str.replace(':', '：')
    str = str.replace('*', '_')
    str = str.replace('?', '？')
    str = str.replace('"', '“')
    str = str.replace('<', '《')
    str = str.replace('>', '》')
    str = str.replace('|', '_')
    return str

def InfoCharFilter(titleInfo):
    if titleInfo.nParts == 0:
        return
    titleInfo.title = CharFilter(titleInfo.title)
    titleInfo.author = CharFilter(titleInfo.author)
    for i in range(len(titleInfo.options)):
        titleInfo.options[i] = CharFilter(titleInfo.options[i])

def GetInfo(avNum):
    url = GetURL.urlRoot + avNum
    html = GetHTML(url)
    #print(html)
    info = GetTitle(html)
    InfoCharFilter(info)
    return info

# 读配置文件
config = configparser.ConfigParser()
config.readfp(open('config.ini'))

# 获取工作目录
GetURL.rootPath = config.get('WorkPath', 'Path')

# 更改工作目录
GetURL.ChToRootPath()

# 获取工作目录中所有AV号列表
AVNums = GetURL.GetAVNList()

for avNum in AVNums:
    info = GetInfo(avNum)

    # 网页不存在的跳过
    if info.nParts == 0:
        continue

    # 视频目录
    VideoPath = os.path.join(GetURL.rootPath, avNum)

    # 对多P视频，更改目录名
    if info.nParts > 1:
        VideoDirNameNew = info.title + '_' + info.author + '_av' + avNum
        VideoDirPathNew = os.path.join(GetURL.rootPath, VideoDirNameNew)
        os.rename(VideoPath, VideoDirPathNew)
        VideoPath = VideoDirPathNew

    # 进入视频目录
    os.chdir(VideoPath)
    VideoPath = os.path.abspath('.')

    for x in os.listdir('.') :
        # 跳过文件和非纯数字目录，只处理纯数字目录，即分P目录
        if (not (os.path.isdir(x) and GetURL.IsInteger(x))):
            continue
        # 进入分P目录
        os.chdir(x)

        # 获取分P目录路径
        PartPath = os.path.abspath('.')

        # 遍历，找到视频文件名和全路径
        fileNameOld = [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.mp4'][0]
        filePathOld = os.path.abspath(fileNameOld)

        # 整数分P号
        nP = int(x)

        if info.nParts == 1:    # 对单P视频
            # 产生新文件全路径
            fileNameNew = info.title + '_' + info.author + '_av' + avNum + '.mp4'
            filePathNew = os.path.join(GetURL.rootPath, fileNameNew)

            # 同时重命名并移动文件
            os.rename(filePathOld, filePathNew)


            # 回到根目录
            os.chdir('..')
            os.chdir('..')

            # 删除视频目录及其中剩余文件
            shutil.rmtree(VideoPath, True)
        else:                   # 对多P视频
            # 产生新文件全路径
            fileNameNew = info.options[nP - 1]
            fileNameNew += '.mp4'
            filePathNew = os.path.join(VideoPath, fileNameNew)

            # 同时重命名并移动文件
            os.rename(filePathOld, filePathNew)

            # 回到视频目录
            os.chdir('..')

            # 删除分P目录及其中剩余文件
            shutil.rmtree(PartPath, True)
    
