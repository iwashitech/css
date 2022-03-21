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
    found_start = re.search(r'{', css_line)
    found_end = re.search('}', css_line)
    
    if found_start:
        tmp_element = css_line.replace("{\n", "").strip()
        tmp_element = re.sub(r'{.+', '', tmp_element)

    if found_img:
        result.append(tmp_element)

css_file.close()

with open(user_name + '/Desktop/css_element.txt', mode='w') as f:
    f.write('\n'.join(result))
