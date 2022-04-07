import pandas as pd
import os
#批量读取数据
def load_data(fpath):
    #文件夹路径列表
    dirpath = []
    #文件夹下文件路径列表
    filelist = []
    #使用os.listdir()将路径下的文件夹存储进一个列表dirlist
    dirlist=os.listdir(fpath)
    #print(dirlist)
    for i in dirlist:
        dirpath.append(os.path.join(fpath,i))
    for j in dirpath:
        filepath=os.path.join(j,'classification.txt')
        #将文件路径加入filelist中
        filelist.append(filepath)
    #检查是否保存完整文件路径
    #print(filelist)
    return filelist,dirlist,dirpath
#将样本数据展开并保存
def Unfold_Data(filelist,dirpath):
    for filepaths, dirpathes in zip(filelist, dirpath):
        class_data = pd.read_csv(filepaths, sep='\t')
        # print(class_data.shape)
        unfold_data = pd.DataFrame({'#Database_OTU': [], 'Taxonomy': []})
        unfold_data['#Database_OTU'] = unfold_data['#Database_OTU'].astype('int')
        unfold_data['Taxonomy'] = unfold_data['Taxonomy'].astype('object')
        # 展开classification.txt
        # 获取class_data行列数
        m, n = [class_data.shape[0], class_data.shape[1]]
        for i in range(0, m):
            # 插入数据
            if class_data.iloc[i, 1] <= 1:
                unfold_data = unfold_data.append(class_data.iloc[i, [0, 3]], ignore_index=True)
            else:
                for j in range(0, class_data.iloc[i, 1]):
                    unfold_data = unfold_data.append(class_data.iloc[i, [0, 3]], ignore_index=True)
        # print(unfold_data.shape)
        dirpath1 = dirpathes.split('\\')
        unfold_data.to_csv('C:/Users/Yyyk/Desktop/mzbfile/final_projects_input/Unfold_Data/' + dirpath1[1] + '_unfold.csv')
