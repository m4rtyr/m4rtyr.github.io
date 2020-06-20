#!/usr/bin/env python3.7

import sys
import datetime

layout = 'layout: post'
title = 'title: ' + sys.argv[1]
category = 'category: '
tags = 'tags: '

now = datetime.datetime.now()
filename = now.strftime('%Y-%m-%d') + '-' + sys.argv[1].replace(' ', '-') + '.md'
with open('_posts/' + filename, 'a') as f:
    f.write('---\n')
    f.write(layout + '\n')
    f.write(title + '\n')
    f.write(category + '\n')
    f.write(tags + '\n')
    f.write('excerpt_separator: <!--eof-->\n---\n')
    f.write('\n\n<!--eof-->')
