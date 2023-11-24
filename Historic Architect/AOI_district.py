# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:30:16 2022

@author: 11211
"""

import json
import urllib3
#import sys
import os
import basics
import arcpy
from arcpy import env
from arcpy import da
env.overwriteOutput = True
#功能：采集行政区边界
#返回保存边界信息的BoundryWithAttr对象
def getDistrictBoundry(ak,citycode):
    districtBoundryUrl = 'https://restapi.amap.com/v3/config/district?keywords='\
        + citycode + '&subdistrict=2&key=' + ak
    print(districtBoundryUrl)
    json_obj = urllib3.urlopen(districtBoundryUrl)
    json_data = json.load(json_obj)
    districts = json_data['districts']
    try:
        polyline = districts[0]['polyline']
        centerLon = districts[0]['center'].split(',')[0]
        centerLat = districts[0]['center'].split(',')[1]
    except Exception as e:
        print('Error')
    pointscoords = polyline.split(';')
    point = basics.PointWithAttr(0, centerLon, centerLat, '行政区域', citycode)
    districtBoundry = basics.BoundryWithAttr(point, pointscoords)
    return districtBoundry

if __name__ == '__main__':
    #高德api key
    ak = '1d4a993bad7c864beadd29b7772971e3'
    #数据保存在AOI文件夹里
    output_directory = 'H:\\urban renewal\\AOI\\'
    citycodes = {'昆山市':'320583'}
    #
    outshp = output_directory + 'nanjing.shp'
    #创建空白shapefile
    arcpy.CreateFeatureclass_management(os.path.dirname(outshp),\
                                        os.path.basename(outshp),'POLYGON')
    arcpy.AddField_management(outshp,'Citycodes','Text','','','')
    arcpy.AddField_management(outshp,'Name','Text','','','')
    fields = ['SHAPE@','Citycode','Name']
    for citycode in citycodes.keys():
        districtBoundry = getDistrictBoundry(ak, citycode)
        cur = da.InsertCursor(outshp,fields)
        array = arcpy.Array()
        boundrycoords = districtBoundry.boundrycoords
        for coordPair in boundrycoords:
            try:
                lon,lat = coordPair.split(',')
            except Exception as e:
                coordPair1 = coordPair.split('|')
                for one in coordPair1:
                    lon,lat = coordPair.split('|')
                    pnt = arcpy.Point(float(lon),float(lat))
                    array.add(pnt)
                continue
            pnt = arcpy.Point(float(lon),float(lat))
            array.add(pnt)
        polygon = arcpy.Polygon(array)
        array.removeAll()
        newFields = [polygon,citycode,citycodes[citycode]]
        cur.insertRow(newFields)
        del cur