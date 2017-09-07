# -*- coding: utf-8 -*-

import os
import shutil

rootSrcDir = u"E:\\简阅样本\\精简结果\\去黑边"
rootDstDir = u"E:\\简阅样本\\精简结果\\原图"

dirs = os.listdir(rootSrcDir)
for item in dirs:
    if item.find(u"result") == -1:
        srcDir = os.path.join(rootSrcDir, item)
        dstDir = os.path.join(rootDstDir, item)
        shutil.copy(srcDir.encode("gb18030"), dstDir.encode("gb18030"))

