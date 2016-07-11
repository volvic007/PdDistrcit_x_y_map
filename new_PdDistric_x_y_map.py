# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 14:20:18 2016

@author: volvic
"""
"""
Kaggle SanFranciscoCrimeのPdDistrict別のMapを作成
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## trainのデータの読み込み
train = pd.read_csv('/Users/volvic/Desktop/python/Kaggle/SanFranciscoCrime/data/train.csv', header = 0)
## 地図データの読み込み
mapdata = np.loadtxt('/Users/volvic/Desktop/python/Kaggle/SanFranciscoCrime/data/sf_map.txt')
print " Start...."

## 不要な列を削除
drops = ["Category", "Dates", "Resolution", "Descript", "Address", "DayOfWeek"]
for drop in drops:
    train = train.drop(drop, 1)

## 各PdDistrict別のDataFrameを作成
southern = train[train["PdDistrict"] == "SOUTHERN"]
mission = train[train["PdDistrict"] == "MISSION"]
northern = train[train["PdDistrict"] == "NORTHERN"]
bayview = train[train["PdDistrict"] == "BAYVIEW"]
central = train[train["PdDistrict"] == "CENTRAL"]
tenderloin = train[train["PdDistrict"] == "TENDERLOIN"]
ingleside = train[train["PdDistrict"] == "INGLESIDE"]
taraval = train[train["PdDistrict"] == "TARAVAL"]
park = train[train["PdDistrict"] == "PARK"]
richmond = train[train["PdDistrict"] == "RICHMOND"]

## プロット点の描画
fig = plt.figure(figsize=(15,15))
plt.scatter(southern["X"], southern["Y"], color = "r", marker = "8", alpha = 0.5, label = ": SOUTHERN")
plt.scatter(mission["X"], mission["Y"], color = "m", marker = "8", alpha = 0.5, label = ": MISSION")
plt.scatter(northern["X"],northern["Y"], color = "g", marker = "8", alpha = 0.5, label = ": NORTHERN")
plt.scatter(bayview["X"], bayview["Y"], color = "c", marker = "8", alpha = 0.5, label = ": BAYVIEW")
plt.scatter(central["X"], central["Y"], color = "b", marker = "8", alpha = 0.5, label = ": CENTRAL")
plt.scatter(tenderloin["X"], tenderloin["Y"], color = "y", marker = "8", alpha = 0.5, label = ": TENDERLOIN")
plt.scatter(ingleside["X"], ingleside["Y"], color = "g", marker = "x", alpha = 0.5, label = ": INGLESIDE")
plt.scatter(taraval["X"], taraval["Y"], color = "r", marker = "x", alpha = 0.5, label = ": TARAVAL")
plt.scatter(park["X"], park["Y"], color = "b", marker = "x", alpha = 0.5, label = ": PARK")
plt.scatter(richmond["X"], richmond["Y"], color = "k", marker = "x", alpha = 0.5, label = ": RICHMOND")
plt.xlim([-122.5247, -122.3366])
plt.ylim([37.699, 37.8299])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("PdDistrict Map")
plt.subplots_adjust(right = 0.77)
plt.legend(loc = "upper left", bbox_to_anchor =(0.9, 1))

## 地図の描画
lon_lat_box = (-122.5247, -122.3366, 37.699, 37.8299)
plt.imshow(mapdata,extent=lon_lat_box, cmap=plt.get_cmap('gray'))
plt.show()




