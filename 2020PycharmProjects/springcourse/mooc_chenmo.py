#MOOC2
"""
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = a.copy()
b = b.flatten()
b[:3] = 0
c = a[:2,1:]
print(a)
print(b)
print(c)
"""""
#MOOC3
"""
import numpy as np              # 导入numpy包
a = np.ones((8,8))              # 生成8*8的全为1的矩阵
a[1:7,1:7]=0                    # 切片化赋值，出边界为全为0
print(a)                        # 打印出a
a = np.where(a>0,2,-2)          # 利用np.where(),1变为2,0变为-2
print(a)                        # 打印出a


b = np.random.randint(2,90,(3,4))       # 创建一个形状为（3,4）的随机整数数组b，数组取值范围为[2,90)
print(b)                                # 打印出b
c = [0,3,6,9]                           # 数组c = [0,3,6,9]
b = np.insert(b,0,c,axis=0)             # 对数组b进行修改：在b的第0行插入一组数据[0,3,6,9]
print(b)                                # 打印出b
b = np.delete(b,-1,axis=1)              # 对数组b进行修改：删除b的最后一列数据
print(b)                                # 打印出b
print(np.max(b,axis=0))                 # 打印
print(np.mean(b))                       # 打印
"""
#MOOC4
"""
import numpy as np                                                           # 导入numpy包，并记作np
import matplotlib.pyplot as plt                                              # 导入matplotlib.pyplot，并记作plt
x = np.arange(5)                                                             # x为y对应元素的索引
y = [314,322,334,342,350]                                                    # y的具体数据
title_font = {'size':12, 'color':'b', 'family':'SimHei'}                     # 设置title的一些格式
legend_font = {'size':12, 'family':'SimHei'}                                 # 设置legend的一些格式
plt.title('COVID-19全球确诊病例', fontdict = title_font)                      # 标题
plt.plot(x,y,'ro-',label = '确诊病例')                                        # 画图，添加图例
plt.legend(loc = 0, fontsize = 14, prop = legend_font)                       # 图例格式
plt.xticks(x,['4-29', '4-30', '5-1', '5-2', '5-3'], size=12)                 # x坐标的刻度
plt.yticks(size=12)
plt.xlabel('日期', family = 'SimHei', size = 12)                             # x轴文本标签
plt.ylabel('人数(万)', family = 'SimHei', size = 12)                         # y轴文本标签
plt.grid(True,axis='y',ls=':')                                               # 设置网格线
plt.savefig('COVID.png')                                                     # 将绘制的图保存为COVID.png
"""
"""
import matplotlib as mpl                                                       # 导入matplotlib包，并记作mpl
import matplotlib.pyplot as plt                                                # 导入matplotlib.pyplot，并记作plt
plt.figure(figsize=[4,4], dpi= 400)                                            # 设置画布及分辨率
data = [70809.84, 64580.78, 1028.20, 10418.33]                                 # 饼图数据
mpl.rcParams['font.sans-serif']=['SimHei']                                     # 设置汉字字体为黑体以免乱码
grade_label = ['线上消费', '线下消费', '手机充值', '其他']                       #  饼图的对应文字标签
plt.title('支付宝各类消费', size = 14, color = 'g')                             # 饼图标题
plt.pie(data, autopct="%0.1f%%", labels=grade_label)                           # 画图
plt.savefig('bill.png')                                                        # 将绘制的图保存为bill.png
"""
#MOOC5
"""
import numpy as np
import pandas as pd
# 创建一个DataFrame（假设命名为grade）如图所示，学生姓名为行索引，各课程为列索引
a=np.arange(80,96).reshape(4,4)
grade = pd.DataFrame(a, index = ['Alex','Ben','Jason','Mike'], columns = ['Matlab','Python','C','Java'])
# 在grade上添加C++课程成绩，成绩数据为对应的Java成绩+2
grade['C++']=grade['Java']+2
# 分别基于自动索引和自定义索引进行切片操作，返回Alex、Ben、Jason的成绩数据
print(grade.iloc[0:3])
print(grade.loc['Alex':'Jason'])
# 返回Java成绩大于90的学生所有科目的成绩数据
print(grade[grade['Java']>90])
# 返回Mike、Ben的Python，C，Java成绩（注：行索引顺序为Mike、Ben ，使用loc或iloc）
print(grade.loc[['Mike','Ben'],'Python':'Java'])
# 将Jason的Python成绩改为92
grade.loc['Jason','Python']=92
# 返回Ben小于86的科目及成绩
print(grade.loc['Ben',grade.loc['Ben']<86])
# 返回Matlab成绩小于90的学生的C++成绩
print(grade.loc[grade.loc[:,'Matlab']<90,'C++'])
# 按照C、C++、Java、Matlab、Python顺序重排课程列（对grade进行修改）
grade.sort_index(axis=1,ascending=True,inplace=True)
# 插入学生名为Carl的成绩数据，采用后向填充
Carl=grade.index.insert(3,'Carl')
grade.reindex(index=Carl,method='bfill')
# 删除C++和Matlab的课程列（对grade进行修改）
grade.drop(axis=1,columns=['C++','Matlab'],inplace=True)
# 将Jason改为James，将Python改为R（对grade进行修改）
grade.rename(index={'Jason':'James'},columns={'Python':'R'},inplace=True)
"""
#wordcloud
"""
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = open('ciyun.txt',encoding = 'utf-8').read()
wc=WordCloud(
  font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",
  width=800,
  repeat=True,
  height=800).generate(text)
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
plt.savefig('wangzixuan.png')
interpolation='bilinear'
"""
#MOOC6
"""
import numpy as np
import pandas as pd
gender=['m','f']
boolean=[True,False]
company=['A','B','T']
np.random.seed(0)
mc_df = pd.DataFrame({\
    'company': [company[x] for x in np.random.randint(0, len(company), 100)],\
    'gender':[gender[x] for x in np.random.randint(0,2,100)],\
    'age':np.random.randint(20,60,100),\
    'height':np.random.randint(150,190,100),\
    'weight':np.random.randint(40,90,100),\
    'salary':np.random.randint(5,20,100)})
mc_df0=mc_df.head(20)
print(mc_df0)
print(mc_df0.sort_values(by='age'))
print(mc_df0.sort_values(by='salary',ascending=False))
print(mc_df0['age'].isin([20,33,46]))
print(mc_df0.replace({mc_df0.loc[:,'age'].min():'Y',mc_df0.loc[:,'age'].max():'O'}))
print(mc_df0['gender'].value_counts())
#自定义查询
diff=lambda x:x.max()-x.min()
print(diff(mc_df0['weight']))
print(diff(mc_df0['height']))
def BMI(x):
    w=x['weight']
    h=x['height']
    bmi=w/h**2
    return bmi
print(BMI(mc_df0))
#groupby方法
print(mc_df0.groupby(['gender'])['height'].mean())
print(mc_df.groupby(['company','gender'])['age'].mean())
"""
