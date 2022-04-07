#存储绘制稀释曲线所用的数据
#读取展开数据文件
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import random
from dilution_curve import Dilution_curve_data
np.set_printoptions(formatter={'float':'{:.4f}'.format})
path='C:/Users/Yyyk/Desktop/mzbfile/final_projects_input/Unfold_Data'
#使用os.listdir()将路径下的文件夹存储进一个列表filelist
filelist=os.listdir(path)
#文件路径列表
filepath=[]
for key in filelist:
    filepath.append(os.path.join(path,key))
#print(filepath[0])
for key in filepath:
    key1=key.split('\\')
    key1=key1[1].split('_')
    #获取样本id
    Sample_id=key1[0]
    #print(Sample_id)
    #计算并保存数据
    Dilution_curve_data(key, Sample_id)


