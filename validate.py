# -*- coding: utf-8 -*-

import os


def collectionContainsAllTargetItems(collection, items):
    numItems = len(items)
    found = [0 for i in range(numItems)]
    for i in range(numItems):
        if items[i] in collection:
            found[i] = 1
    return sum(found) == numItems


def pathContainsFolder(path, folder):
    arr = path.split(u"\\")
    return folder in arr


def findTargetFolders(rootDir, containedFolders):
    resultDirs = []
    tempDirs = []

    if os.path.isdir(rootDir):
        tempDirs.append(rootDir)

    while len(tempDirs) > 0:
        currDir = tempDirs[-1]
        tempDirs.pop()

        subDirs = os.listdir(currDir)
        if collectionContainsAllTargetItems(subDirs, containedFolders):
            resultDirs.append(os.path.join(currDir))
            continue

        for item in subDirs:
            fullSubDir = os.path.join(currDir, item)
            if os.path.isdir(fullSubDir):
                tempDirs.append(fullSubDir)

    return resultDirs


def keepStringsContainingSubString(arr, subStr):
    result = []
    for item in arr:
        if item.find(subStr) >= 0:
            result.append(item)
    return result


rootDirs = [
    u"E:\\简阅样本\\20170509阅卷系统扫描精度测试",
    u"E:\\简阅样本\\0510阅卷二次扫描",
    u"E:\\简阅样本\\20170515阅卷系统庐阳中学测试"
]
mustFolders = [u"答题卡模板", u"作答过的答题卡"]
resFolders = [u"200dpi", u"300dpi", u"400dpi", u"500dpi", u"600dpi"]
# resFolders = [resFolders[0]]

numRootDirs = len(rootDirs)
numResolutions = len(resFolders)

for j in range(numResolutions):
    resFolder = resFolders[j]
    srcFileName = u"result" + u"-" + resFolder + u".txt"
    dstFileName = u"info" + u"-" + resFolder + u".txt"

    for i in range(numRootDirs):
        rootDir = rootDirs[i]

        dirs = findTargetFolders(rootDir, mustFolders)
        dirs = keepStringsContainingSubString(dirs, resFolder)
        # resultTxtDir = u"result.txt"
        # infoTxtDir = u"info.txt"

        for item in dirs:
            print item

        for item in dirs:
            refRootDir = os.path.join(item, mustFolders[0])
            testRootDir = os.path.join(item, mustFolders[1])
            command = u"Validate %s %s %s" % (refRootDir, testRootDir, srcFileName)
            os.system(command.encode("gb18030"))

    srcFile = open(srcFileName, "r")
    dstFile = open(dstFileName, "w")
    for line in srcFile:
        arr = line.strip("\n").decode("gb18030").split(u",")
        # for item in arr:
        #     print item
        # print ""
        ok = int(arr[1].strip(u" ").split(u" ")[2])
        # print "ok =", ok
        if ok != 1:
            dstFile.write(arr[0].encode("gb18030") + "\n")
    srcFile.close()
    dstFile.close()


# srcFileName = u"E:\\Projects\\DocumentAnalyzer\\build\\PCFrontEnd\\result.txt"
# dstFileName = u"info.txt"
# srcFile = open(srcFileName, "r")
# dstFile = open(dstFileName, "w")
# for line in srcFile:
#     arr = line.strip("\n").decode("gb18030").split(u",")
#     # for item in arr:
#     #     print item
#     # print ""
#     ok = int(arr[1].strip(u" ").split(u" ")[2])
#     # print "ok =", ok
#     if ok:
#         dstFile.write(arr[0].encode("gb18030") + "\n")
# srcFile.close()
# dstFile.close()


