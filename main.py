


import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Data import load_data,Unfold_Data
#二、计算丰富度和香浓指数
#求信息熵函数
def caculate_shannonent(dataSet):
    #总的细菌总类数
    Sum=dataSet['Count'].sum()
    #增加概率p列
    dataSet['p']=''
    #计算每个细菌群落的丰富度-未校准
    for otu in dataSet['#Database_OTU']:
        dataSet['p']=dataSet['Count']/Sum
    #print(dataSet.head())
    shannonent=0.0
    for pnt in dataSet['p']:
        shannonent-=pnt*np.log10(pnt)
    return shannonent
#计算丰富度
def caculate_richness(dataSet):
    return dataSet.shape[0]

#三、稀释曲线处理
# 封装函数：从一个样本中抽取数据求出丰富度和香浓指数，用于做出稀释曲线


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #样本文件路径
    path = 'C:/Users/Yyyk/Desktop/mzbfile/final_projects_input/Single_Sample'
    #获取所有样本处理路径
    Filelist,Dirpath=load_data(path)
    print(Filelist[0])
    s0_data=pd.read_csv(Filelist[0],sep='\t')
    #s0_path='C:/Users/Yyyk/Desktop/mzbfile/final_projects_input/Unfold_Data/S9066B_unfold.csv'
    #s0_richness,s0_shannon=Dilution_curve(s0_path)
    #print(s0_richness)
    #print(s0_shannon)
