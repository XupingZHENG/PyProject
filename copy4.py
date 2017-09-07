# -*- coding: utf-8 -*-

import os
import shutil

dstDir = u"E:\\Projects\\libcuttpl\\src"
srcDir = u"E:\\Projects\\DocumentAnalyzer\\source"

g = os.walk(srcDir)
allSrcFiles = []
for path, d, fileList in g:
    # print d
    for filename in fileList:
        allSrcFiles.append(os.path.join(path, filename))

for item in allSrcFiles:
    print item

allDstFiles = os.listdir(dstDir)
for dstItem in allDstFiles:
    for srcItem in allSrcFiles:
        if srcItem.find(dstItem) >= 0:
            print u"Src file %s found, copy to dst dir" % srcItem
            shutil.copy2(srcItem.encode("gb18030"), os.path.join(dstDir, dstItem).encode("gb18030"))
            break

