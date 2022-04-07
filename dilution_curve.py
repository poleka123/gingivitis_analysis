
import random
import pandas as pd
from main import caculate_shannonent,caculate_richness
#从start到stop随机选取长度为length的数组
def random_int_list(start,stop,length):
    start,stop=(int(start),int(stop)) if start<=stop else (int(stop),int(start))
    length=int(abs(length)) if length else 0
    random_list=[]
    for i in range(length):
        random_list.append(random.randint(start,stop))
    return random_list

#数据转换函数
def InvertData(sample_data,dup_data):
    #sample_data是去重后的数据,dup_data是重复的数据
    #声明一个新的DataFrame
    new_data=pd.DataFrame({'#Database_OTU':[],'Count':[],'Taxonomy':[]})
    #将不重复的数据插入
    for i in range(0,sample_data.shape[0]):
        new_data=new_data.append(sample_data.iloc[i,[0,1]],ignore_index=True)
        new_data.iloc[i,1]=1
    #x修改数据类型
    new_data['#Database_OTU']=new_data['#Database_OTU'].astype('int64')
    new_data['Count']=new_data['Count'].astype('int64')
    new_data['Taxonomy']=new_data['Taxonomy'].astype('object')
    #print(new_data.T.index[0])
    #print(dup_data.shape)
    #当去重中的数据在去重后的数据中时，给去重后的数据加1
    for i in range(0,dup_data.shape[0]):
        #new_data.T.index[0]是Database_OTU
        new_data.iloc[:,1][new_data[new_data.T.index[0]]==dup_data.iloc[i,0]]+=1
        #print(new_data.iloc[:,[0,1]][new_data[new_data.T.index[0]]==dup_data.iloc[i,0]])
    #print(new_data)
    return new_data

def Dilution_curve_data(sample_path,sample_id):
    # 常量声明
    richnesses = []
    shannons = []
    randnum = []
    nums = 5
    s_data = pd.read_csv(sample_path, sep=',')
    s_data = s_data.drop(columns='Unnamed: 0')
    # 返回行数
    m = s_data.shape[0]
    if m>4000:
        m=4000
    for step in range(0, m+100, 100):
        # 从0到样本总长度，依次以100递增从样本中抽取细菌信息
        # 总丰富度与总香浓指数
        sum_richness = 0
        sum_shannon = 0
        randnum.append(step)
        for i in range(0, nums):
            # 随机生成5个数组
            random_list = []
            # 每个数组随机在(1,m)中生成step个数
            random_list = random_int_list(1, m, step)
            # print('random_list:',random_list)
            # 找出数组对应的样本信息
            s_random_data = s_data.iloc[[x - 1 for x in random_list]]
            # 找出重复的数据
            dup_data = s_random_data[s_random_data.duplicated()]
            # 去除重复数据
            s_random_data = s_random_data.drop_duplicates()
            # 将数据重新转化为原格式，方便求丰富度和香浓指数
            new_s_data = InvertData(s_random_data, dup_data)
            # 计算总的丰富度和香浓指数求平均值
            sum_richness += caculate_richness(new_s_data)
            sum_shannon += caculate_shannonent(new_s_data)
        # mean_richness为整数
        mean_richness = int(sum_richness / nums)
        # mean_shannon保留5位小数
        mean_shannon = round(sum_shannon / nums, 5)
        # 将平均丰富度和香浓指数添加到两者对应的数组中
        richnesses.append(mean_richness)
        shannons.append(mean_shannon)
        #保存数据
        df=pd.DataFrame({'Randnum':[],'Richness':[],'Shannon':[],'New_measure':[]})
        df['Randnum']=randnum
        df['Richness']=richnesses
        df['Shannon']=shannons
        df.to_csv('C:/Users/Yyyk/Desktop/mzbfile/final_projects_input/drawing/'+sample_id+'.csv')
    #return richnesses, shannons