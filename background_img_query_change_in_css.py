# -*- coding: utf-8 -*-
"""
css query update
"""

import os
import re
import codecs

user_name = os.environ['USERPROFILE'].replace('\\', '/')
QUERY_STRING = "?0000000000"

#img.txtはクエリを更新したい画像リストの一覧（手作業で作成する）
with codecs.open(user_name + '/Desktop/img.txt', 'r') as img_file:
    img_list = img_file.readlines()


with codecs.open(user_name + '/Desktop/base.css', 'r', 'shift_jis') as css_file:
    css_list = css_file.readlines()

new_css = codecs.open(user_name + '/Desktop/new.css', 'w', 'shift_jis')

for css_line in css_list:
    for img_line in img_list:
        bgimg = img_line.replace("\n", "")
        re_img = re.compile((bgimg))
        css_text = css_line
        found = re.search(re_img, css_text)
        
        if found:
            digit = "(\?\d{4,})"
            img_query = "(" + bgimg + ")" + digit
            re_img_query = re.compile((img_query))
            re_digit = re.compile((digit))
            
            query_found = re.search(re_img_query, css_text)
            if query_found:
                css_text = re.sub(re_digit, "", css_text)
            css_text = re.sub(re_img, found.group(0) + QUERY_STRING, css_text)
            break
    new_css.write(css_text)

new_css.close()