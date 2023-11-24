# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 19:42:44 2022

@author: 11211
"""

import requests
import json
from bs4 import BeautifulSoup
import csv

#定义一个函数，传入线路名称相当于在高德地图搜索，来获取每趟公交的站点名称和经纬度       
def get_location(line):
    url_api = 'https://restapi.amap.com/v3/bus/linename?s=rsv3&extensions=all&key=559bdffe35eec8c8f4dae959451d705c&output=json&city=上海&offset=2&keywords={}&platform=JS'.format(
        line)
    res = requests.get(url_api).text
    # print(res) 可以用于检验传回的信息里面是否有自己需要的数据
    rt = json.loads(res)
    #print(rt)
    #print(rt['buslines'])
    i = 0
    line_name = rt['buslines'][0]['name']
    polyline = rt['buslines'][0]['polyline']
    info = [line_name, polyline]
    #print(info)
    stop = rt['buslines'][0]['busstops']
    for i in range(len(stop)):
        station = stop[i]['name']
        location = stop[i]['location']
        info_ = [line, station, location]
        print(info_)
        with open(r"C:\Users\Chenxi\Desktop\stop.csv","a",encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(info_)
        # with open(r'C:\Users\Chenxi\Desktop\stop.csv', 'a', encoding='utf-8')as f:
        #   f.write(str(info_))
        i += 1 


with open(r"C:\Users\Chenxi\Desktop\busline.csv",'r', encoding='UTF-8') as f:
    for line in f:
        line=line.strip('\n')
        get_location(line)



