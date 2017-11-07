# -*- coding: utf-8 -*-

import os

part_file_names = ['004b77', '01c039', '021312', '02e5b2', '03c90e',
                '046eca', '05bc85', '07b6f9', '07d6ea', '080d8f',
                '086934', '090ab1', '0a511b', '0afebf', '0b4374',
                '0e5094', '0e5844', '0f0cb2', '0fe568', '1108df',
                '110c71', '111157', '112e86', '11c516']
num_part = len(part_file_names)

root_dir = u"E:\\试卷录入\\xkw_images"
dirs = os.listdir(root_dir)
file_names_file = open('file.txt', mode='w')
hit_count = 0
for item in dirs:
    if len(item) >= 6:
        prefix = item[:6]
        if prefix in part_file_names:
            hit_count += 1
            full_path = os.path.join(root_dir, item)
            full_path = full_path.replace('\\', '\\\\')
            file_names_file.write('"' + full_path.encode('gb18030') + '"\n')
file_names_file.close()
if hit_count != num_part:
    print 'hit count %d not equal num part %d' % (hit_count, num_part)

