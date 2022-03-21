# -*- coding: utf-8 -*-
"""
"""

import re
import codecs
import os

user_name = os.environ['USERPROFILE'].replace('\\', '/')

css_file = codecs.open(user_name + '/Desktop/base.css', 'r', 'shift_jis')
css_list = css_file.readlines()

result = []

for css_line in css_list:
    found_img = re.search(r'.+(\.png|\.jpg|\.gif)', css_line)

    if found_img:
        img_line = css_line.strip()
        img_line = re.sub(r'^.*url\((.+)\).*', r'\1', img_line)
        img_line = re.sub(r'\?.+', '', img_line)
        img_line = img_line.replace('"', '')
        result.append(img_line)

css_file.close()

with open(user_name + '/Desktop/css_img.txt', mode='w', encoding='shift_jis') as f:
    f.write('\n'.join(result))