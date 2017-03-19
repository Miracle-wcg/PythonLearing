# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib

response = urllib.urlopen('http://www.baidu.com/')

print(response.getCode())

print(response.read())
