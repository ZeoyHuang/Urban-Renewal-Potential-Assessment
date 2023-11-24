# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:18:08 2022

@author: 11211
"""



#-*- coding:utf-8 -*-
import requests
import MySQLdb
import re
from bs4 import BeautifulSoup
import csv
 
#设置headers和cookies
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"
}
cookies = {'ASPSESSIONIDQCSRSBRS':'FBEPJPLCHEEMEHNLHFKCBCGB',
 'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208':'1483118719',
 'Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208':'1483120442'}

##用python连接数据库
#db = MySQLdb.connect(host="localhost",user="root",passwd='liao1234',db='liao',charset="utf8")
##cursor([cursorclass]):游标指针
#cursor = db.cursor()
#'''
#sql ="""create table company(name char(100) not null,
#    type char(50),
#    addr char(150),
#    leader   char(30),
#    date char(30))"""
#cursor.execute(sql)
#'''
#获取各地区链接
#r = requests.get("https://shanghai.11467.com/yangpu/",headers=headers,cookies=cookies)
#html = r.text
#soup = BeautifulSoup(html)
#for tag in soup.find(name='div', attrs={"class":"f_l"}).find_all('h4'):
#    print(tag.string)
 
base_url = "https://shanghai.11467.com/yangpu/"+'pn'
for i in range(2,21):
    a=[]
    url = base_url + str(i)
    r = requests.get(url,headers=headers,cookies=cookies)
    html = r.text
    soup = BeautifulSoup(html)
    for tag in soup.find(name='div', attrs={"class":"f_l"}).find_all('h4'):
        #print(tag.string)
        with open(r"H:\urban renewal\企业\company.csv","a",encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(tag.string)
    