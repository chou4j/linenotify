# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 23:11:50 2022

@author: chou4
"""
#import fiona
#from shapely.geometry import shape, Point
from matplotlib import pyplot as plt
import geopandas as gpd
'''
collection = fiona.open('D:\\GISDATA\鄉鎮市區界線(TWD97經緯度)\TOWN_MOI_1100415.shp')

shapes = {}
properties = {}

for f in collection:
    town_id = int(f['properties']['TOWNCODE'])
    shapes[town_id] = shape(f['geometry'])
    properties[town_id] = f['properties']


from rtree import index
idx = index.Index()
for town_id, shape in shapes.items():
    idx.insert(town_id, shape.bounds)
    
def search(x, y):
    return next((town_id
                 for town_id in idx.intersection((x, y))
                 if shapes[town_id].contains(Point(x, y))), None)
'''

data = gpd.read_file(r'D:\\GISDATA\鄉鎮市區界線(TWD97經緯度)\TOWN_MOI_1100415.shp')#讀取磁碟上的向量檔案
#data = gpd.read_file('shapefile/china.gdb', layer='province')#讀取gdb中的向量資料
print(data.crs)  # 檢視資料對應的投影資訊
print(data.head())  # 檢視前5行資料
data.plot()
plt.show()#簡單展示


