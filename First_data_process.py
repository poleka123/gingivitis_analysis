
import pandas as pd
import numpy as np
from Data import load_data,Unfold_Data
from pandas.core.frame import DataFrame

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
#处理数据1
path = 'C:/Users/Yyyk/Desktop/mzbfile/final_projects_input/Single_Sample'
Filelist,Dirlist,Dirpath=load_data(path)
#对路径列表中的每个文件求出丰富度与香浓指数
#丰富度列表
richness=[]
#信息熵列表
shannonents=[]
for key in Filelist:
    source_data = pd.read_csv(key, sep='\t')
    # print(source_data.shape)
    # 求得丰富度
    richnum = caculate_richness(source_data)
    # 将该样本的丰富度加入丰富度列表
    richness.append(richnum)
    shannonent = caculate_shannonent(source_data)
    # print(shannonent)
    shannonents.append(shannonent)
rich_shannon={'ID':Dirlist,'Richness':richness,'ShannonEnt':shannonents}
df=DataFrame(rich_shannon)

#保存样本信息
metapath='C:/Users/Yyyk/Desktop/mzbfile/final_projects_input/meta.txt'
meta_data=pd.read_csv(metapath,sep='\t')
#合并df和meta_data
#print(meta_data.head())
meta1_data=pd.concat([meta_data,df],join="inner",axis=1)
meta1_data=pd.merge(meta_data,df, on='ID', how='outer')
#print(meta1_data.head())
meta1_data.to_csv('C:/Users/Yyyk/Desktop/mzbfile/final_projects_input/meta1.csv')

#展开数据，方便后续从样本中抽取信息
Unfold_Data(Filelist,Dirpath)