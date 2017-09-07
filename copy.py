# -*- coding: utf-8 -*-

import os
import shutil


def isImage(path):
    arr = path.split(u".")
    ext = arr[-1]
    return ext == u"bmp" or ext == u"jpg" or ext == u"png" or ext == u"tif"


def collectImages(rootDir):
    imageDirs = []

    tempDirs = []
    if os.path.isdir(rootDir):
        tempDirs.append(rootDir)

    while len(tempDirs) > 0:
        currDir = tempDirs[-1]
        tempDirs.pop()

        subDirs = os.listdir(currDir)
        for i in range(len(subDirs)):
            subDirs[i] = os.path.join(currDir, subDirs[i])

        for item in subDirs:
            if (not os.path.isdir(item)) and isImage(item):
                imageDirs.append(item)
            if os.path.isdir(item):
                tempDirs.append(item)

    return imageDirs


# srcRootDir = u"E:\\简阅样本\\结果\\倾斜矫正"
# dstRootDir = u"E:\\简阅样本\\精简结果\\倾斜矫正"
srcRootDir = u"E:\\简阅样本\\结果\\去黑边"
dstRootDir = u"E:\\简阅样本\\精简结果\\去黑边"

imageDirs = collectImages(srcRootDir)
# for item in imageDirs:
#     print item

#
# if not os.path.exists(dstRootDir):
#     os.makedirs(dstRootDir.encode("gb18030"))
#
# for item in imageDirs:
#     imageName = item.split(u"\\")[-1]
#     print imageName
#     dstImageDir = os.path.join(dstRootDir, imageName)
#     shutil.copy(item.encode("gb18030"), dstImageDir.encode("gb18030"))



