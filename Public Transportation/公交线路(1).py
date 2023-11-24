# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:10:34 2022

@author: 11211
"""

import requests
from bs4 import BeautifulSoup
import csv
 
url = "https://shanghai.8684.cn/line2"
# 伪装请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
# 通过requests模块模拟get请求
res = requests.get(url=url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")
div = soup.find('div', class_='list clearfix')
lists = div.find_all('a')
for item in lists:
    line = item.text  #获取a标签下的公交线路
    # print(line)
    with open(r'traffic.csv', 'a', encoding='utf-8')as f:
     f.write(str(line) + ',')