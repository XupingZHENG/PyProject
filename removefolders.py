# -*- coding: utf-8 -*-

import os
import sys
import shutil


def removeDebugReleaseFolders(rootDir):
    tempDirs = []
    if os.path.isdir(rootDir):
        tempDirs.append(rootDir)

    while len(tempDirs) > 0:
        currDir = tempDirs[-1]
        tempDirs.pop()

        subDirs = os.listdir(currDir)
        for item in subDirs:
            fullPath = os.path.join(currDir, item)

            folder = item.lower()
            if folder == "debug" or folder == "release":
                shutil.rmtree(fullPath)
                # print "we are going to remove items inside " + fullPath

            if os.path.isdir(fullPath):
                tempDirs.append(fullPath)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        removeDebugReleaseFolders(os.getcwd())
    else:
        removeDebugReleaseFolders(sys.argv[1])
