# -*- coding: utf-8 -*-

import os
import shutil

rootSrcDir = u"E:\\简阅样本\\批改测试5\\作答过的答题卡原图"
rootDstDir = u"E:\\简阅样本\\批改测试5\\作答过的答题卡"

dirs = os.listdir(rootSrcDir)
count = 0
for item in dirs:
    srcDir = os.path.join(rootSrcDir, item)
    dstFolder = os.path.join(rootDstDir, str(count))
    os.mkdir(dstFolder.encode("gb18030"))
    dstDir = os.path.join(dstFolder, (u"Image%d.jpg" % count))
    print dstDir
    shutil.copy(srcDir.encode("gb18030"), dstDir.encode("gb18030"))
    count = count + 1
