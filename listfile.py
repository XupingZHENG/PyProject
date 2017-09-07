# -*- coding: utf-8 -*-

import os

rootDir = u"E:\\简阅样本\\精简结果\\倾斜矫正"
files = os.listdir(rootDir)
leftFiles = []
for item in files:
    if item.find(u"result") < 0:
        leftFiles.append(item)

leftFiles.sort()

f = open(u"filelist.txt", "w")
for item in leftFiles:
    f.write(item.encode("gb18030") + "\n")
f.close()