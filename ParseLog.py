# -*- coding: utf-8 -*-

import json
import os
import re
import shutil
import time
import urllib


def extract_request_and_response(file_name, start_time, end_time):
    f = open(file_name)
    request_list = []
    response_list = []
    while True:
        r = f.readline()
        if r == '':
            break

        # 标准行内容如下:
        # 0915 08:54:05.255 I 22139 Service.cpp 905 matchService: Proc time 0.000355368
        # 这种情况下 rr[0] = 0915, rr[1] = 08:54:05.255
        rr = r.split(' ')
        if len(rr) > 2:
            if rr[0][0] == '[':
                continue

            # 用 : 和 . 作为分割符, 对 rr[1] 进行分割
            # 注意!!! 把 . 作为分隔符，需要转义 http://blog.csdn.net/qq1124794084/article/details/51536528
            hour_minute_second_msecond = re.split(':|\.', rr[1])
            if len(hour_minute_second_msecond) != 4:
                continue

            curr_time_str = '2017' + rr[0] + hour_minute_second_msecond[0] + \
                            hour_minute_second_msecond[1] + hour_minute_second_msecond[2]
            curr_time = time.mktime(time.strptime(curr_time_str, '%Y%m%d%H%M%S'))

            # 如果日志行在规定的时间范围内
            if start_time <= curr_time < end_time:
                # 看有没有 Match request
                index = r.find('Match request')
                if index >= 0:
                    curl_brace_index = r.find('{', index)
                    if curl_brace_index >= 0:
                        request = r[curl_brace_index:].replace('\n', '')
                        request_list.append(request)

                # 看有没有 Match response
                index = r.find('Match response')
                if index >= 0:
                    curl_brace_index = r.find('{', index)
                    if curl_brace_index >= 0:
                        response_list.append(r[curl_brace_index:].replace('\n', ''))
    f.close()
    return request_list, response_list


def save_request(request_list, root_dir):
    if len(request_list) <= 0:
        return

    if os.path.exists(root_dir):
        shutil.rmtree(root_dir)
    os.mkdir(root_dir)

    for i, request in enumerate(request_list):
        file_name = os.path.join(root_dir, str(i))
        file_name += '.json'
        f = open(file_name, 'w')
        f.write(request)
        f.close()


def download_ref_and_test_images(request_list, root_dir):
    if len(request_list) <= 0:
        return

    first_request = request_list[0]
    ref_uri_set = set([])
    first_request_obj = json.loads(first_request)
    ref_questions = first_request_obj['ref_questions']
    for question in ref_questions:
        areas = question['area']
        for area in areas:
            ref_uri_set.add(area['uri'])

    ref_images_dir = os.path.join(root_dir, 'ref')
    if os.path.exists(ref_images_dir):
        shutil.rmtree(ref_images_dir)
    os.makedirs(ref_images_dir)
    for image_url in ref_uri_set:
        seg = image_url.split('/')
        urllib.urlretrieve(image_url, os.path.join(ref_images_dir, seg[-1]))

    test_images_root_dir = os.path.join(root_dir, 'test')
    if os.path.exists(test_images_root_dir):
        shutil.rmtree(test_images_root_dir)
    os.makedirs(test_images_root_dir)
    count = 0
    for request in request_list:
        request_obj = json.loads(request)
        test_uris = request_obj['test_uris']
        for item in test_uris:
            test_images_dir = os.path.join(test_images_root_dir, str(count))
            os.mkdir(test_images_dir)
            count += 1
            for uri in item:
                seg = uri.split('/')
                urllib.urlretrieve(uri, os.path.join(test_images_dir, seg[-1]))


# 抓取日志的起始时间
start_time_str = '20171011170000'
start_time = time.mktime(time.strptime(start_time_str, '%Y%m%d%H%M%S'))
# start_time = 0.

# 抓取日志的结束时间
end_time_str = '20171011180000'
end_time = time.mktime(time.strptime(end_time_str, '%Y%m%d%H%M%S'))
# end_time = float('inf')

log_file_name = 'C:\\Users\\Wenba\\Desktop\\logfile-2'
request_list, response_list = extract_request_and_response(log_file_name, start_time, end_time)
# download_ref_and_test_images(request_list, 'local')
save_request(request_list, 'local')