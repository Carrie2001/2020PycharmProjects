"""
import pandas as pd

#将数据集存入一个名为chipo的数据框内
chi = pd.read_csv(r'G:\DAIDAI\2019-2020_Spring Course\python\陈默\final\data2020\chipotle.csv',\
                    sep=None,engine='python')

#查看前10行内容
chi.head(10)

#数据集中有多少个列(columns)？
chi.shape[1]

#打印出全部的列名称
chi.columns

#数据集的索引是怎样的？
chi.index

#被下单数最多商品(item)是什么?
chi[['item_name','quantity']].groupby(by=['item_name']).sum().sort_values(by=['quantity'],ascending=False)

#在item_name这一列中，一共有多少种商品被下单？
chi.item_name.nunique()

#在choice_description中，下单次数最多的商品是什么？
#chipo[['choice_description','quantity']].groupby(by=['choice_description']).sum().sort_values(by=['quantity'],ascending=False)
chi['choice_description'].value_counts().head()

#一共有多少商品被下单？
chi['quantity'].sum()

#将item_price转换为浮点数
#货币符号后取起
chi['item_price'] = chi['item_price'].apply(lambda x: float(x[1:]))

#在该数据集对应的时期内，收入(revenue)是多少？
(chi['quantity'] * chi['item_price']).sum()

#在该数据集对应的时期内，一共有多少订单？
chi['order_id'].nunique()

#每一单(order)对应的平均总价是多少？
chi['item_price_sum'] = chi['quantity'] * chi['item_price']
(chi[['order_id','item_price_sum']].groupby(by=['order_id']).sum()).mean()
"""""
#加州房价
"""
#导入一些可能要用到的包
import numpy as np
import pandas as pd
#housing.csv数据读入
house=pd.read_csv(r'G:\DAIDAI\2019-2020_Spring Course\python\chenmo\final\data2020\housing.csv',\
                    sep=None,engine='python')
#列数较多，设置可显示的最大列数
pd.set_option('display.max_columns',None)
#默认打开数据的前五行查看数据基本结构
house.head()
house.info()
# 导入matplotlib包
import matplotlib
import matplotlib.pyplot as plt
# 每个数值特征的分布可视化
house.hist(bins=50)
plt.savefig('Numerical feature distribution.png')
# 地理分布可视化
house.plot(kind="scatter", x="longitude", y="latitude")
# 将绘制的图保存
plt.savefig('Geographical distribution1.png')
# 房价的地理分布可视化
#plt.figure(figsize=(15,9))
sc=plt.scatter(house['longitude'],house['latitude'],alpha=0.4,
            s=house['population']/100,label='population',
            c=house['median_house_value'],cmap=plt.get_cmap("jet"))
# 图例
plt.legend()
matplotlib.rcParams["font.sans-serif"]=["SimHei"]
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.size'] =15
# x轴文本标签
plt.xlabel('经度longitude')
# y轴文本标签
plt.ylabel('纬度latitude')
color_bar=plt.colorbar(sc)
color_bar.set_label('meidan_house_value')
# 将绘制的图保存
plt.savefig('Geographical distribution2.png')
#以上为使用plt的完整代码，将坐标轴的内容以及添加colorbar，设置中文坐标轴标题
# house.plot(kind="scatter",x="longitude",y="latitude",alpha=0.4,
#              s=house["population"]/100,label="population",
#              c="median_house_value",cmap=plt.get_cmap("jet"),colorbar=True,sharex=False)
# plt.legend()
#使用pandas的fillna来用中位数填充缺失值
median = house["total_bedrooms"].median()
house["total_bedrooms"].fillna(median,inplace=True)
#再一次查看概要来检查非空值
house.info()
age_max=house["housing_median_age"].max()
age_min=house["housing_median_age"].min()
diff=lambda x:x.max()-x.min()
# house["housing_median_age"].apply(diff)

chi[['choice_description','quantity']].groupby(by=['choice_description']).sum().sort_values(by=['quantity'],ascending=False).head() 

ousing["ocean_proximity"].value_counts()
"""
#chipotle查询
"""
# 导入需要的包
import pandas as pd
# 将数据集存入一个名为chipo的数据框内
chi = pd.read_csv(r'G:\DAIDAI\2019-2020_Spring Course\python\chenmo\final\data2020\chipotle.csv',\
                    sep=None,engine='python')
# 列数较多，设置可显示的最大列数
pd.set_option('display.max_columns',None)
# 默认打开数据的前五行查看数据基本结构
chi.head()

#数据集中有多少个列(columns)？
chipo.shape[1]

#打印出全部的列名称
chipo.columns

#数据集的索引是怎样的？
chipo.index

#被下单数最多商品(item)是什么?
#查看不同item_name的购买数量并输出数量最多的前五个
chi[['item_name','quantity']].groupby(by=['item_name']).sum().sort_values(by=['quantity'],ascending=False).head()

#在item_name这一列中，一共有多少种商品被下单？
chi.item_name.nunique()

#在choice_description中查询下单次数前五的商品
#chi[['choice_description','quantity']].groupby(by=['choice_description']).sum().sort_values(by=['quantity'],ascending=False).head()
#chi['choice_description'].value_counts().head()

#一共有多少商品被下单？
chipo['quantity'].sum()

#将item_price转换为浮点数
#货币符号后取起
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

#查询在该数据集对应的时期内，收入(revenue)是多少？
(chipo['quantity'] * chipo['item_price']).sum()

#在该数据集对应的时期内，一共有多少订单？
chipo['order_id'].nunique()

#查询每一单order_id对应的平均总价
chi['item_price_sum'] = chi['quantity'] * chi['item_price']
(chi[['order_id','item_price_sum']].groupby(by=['order_id']).sum()).mean()

# 增加total列，查询每笔订单的总金额并输出金额最多的前五个
# 为了做乘法运算先对item_price进行处理
chi['item_price']=chi['item_price'].apply(lambda x:float(x[1:]))
chi['total']=round(chi['item_price']*chi['quantity'],2).head()

# 查询总订单数
# value_counts： 统计Series或者DataFrame中每个值出现的次数 
chi.order_id.value_counts().count()

# 计算每个订单的平均价格
# 总销售额/总订单数   
(chi.quantity*chipo.item_price).sum()/(chi.order_id.value_counts().count()) 


"""
#2012
"""
import pandas as pd
# euro2012_stats.csv读入并命名为euro
euro = pd.read_csv(r'G:\DAIDAI\2019-2020_Spring Course\python\chenmo\final\data2020\Euro2012_stats.csv',\
                    sep=None,engine='python')
# 用head()方法查看前五行
euro.head()
#只选取 Goals 这一列
euro12.Goals

#有多少球队参与了2012欧洲杯？
euro12.Team.nunique()

#该数据集中一共有多少列(columns)?
euro12.shape[1]

#将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框
discipline = euro[['Team','Yellow Cards','Red Cards']]
#对数据框discipline按照先Red Cards再Yellow Cards进行排序
discipline.sort_values(by=['Red Cards','Yellow Cards'],ascending = False)
#查询拿到的黄牌数的平均值并输出前五个
discipline.groupby('Team').agg({'Yellow Cards': ['sum', 'mean']}).head()
euro['Yellow Cards'].max()

#找到进球数Goals超过6的球队数据
euro12[euro12.Goals>6]

#选取以字母G开头的球队数据
euro12[euro12.Team.str.startswith('G')]

#选取前7列
euro12.iloc[:,0:7]

#选取除了最后3列之外的全部列
euro12.iloc[:,0:-3]

#找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
euro12.loc[euro12['Team'].isin(['England','Italy','Russia']),['Team','Shooting Accuracy']]

#12. 找到英格兰(England)、意大利 (Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
#设置索引并直接修改了原始数据 inplace=True
euro.set_index('Team', inplace=True)  
#通过索引直接访问数据
euro.loc[['England', 'Italy', 'Russia'], 'Shooting Accuracy']    

# 以字母e结束的球队
euro[euro.Team.str.endswith('e')]  

#loc：通过行标签索引数据
#iloc：通过行号索引行数据
#ix：通过行标签或行号索引数据（基于loc和iloc的混合）
"""
#apple时间序列 可视化
"""
import pandas as pd
#读取数据并存为apple
apple = pd.read_csv(r'G:\DAIDAI\2019-2020_Spring Course\python\chenmo\final\data2020\Apple_stock.csv',\
                    sep=None,engine='python')

#查看每一列的数据类型
apple.dtypes

#将Date这个列转换为datetime类型
apple.Date = pd.to_datetime(apple.Date)

#将Date设置为索引
apple = apple.set_index('Date')

#有重复的日期吗？
apple.index.is_unique

#将index设置为升序
apple = apple.sort_index(ascending = True)

#找到每个月的最后一个交易日(business day)
apple_month = apple.resample('BM').mean()
apple_month.head()

#数据集中最早的日期和最晚的日期相差多少天？
(apple.index.max() - apple.index.min()).days

#在数据中一共有多少个月？
len(apple_month)

#按照时间顺序可视化Adj Close值
#apple['Adj Close'].plot(title = 'Apple Stock').get_figure().set_size_inches(9,5)
import matplotlib
import matplotlib.pyplot as plt
apple['Adj Close'].plot(title = 'Apple Stock')
# 保存图片
plt.savefig('adj_close.png')
plt.show()
# 获取数据集的2014年的3到6月的数据
sum36=apple['2014-03':'2014-06']
# 计算2014年的3到6月的总成交量
sum36['Volume'].sum()
# 利用isin获得收盘价最大的日期
apple.loc[apple.Close.isin([apple['Close'].max()]),['Close']]
"""
# US Crime apply函数
"""
import pandas as pd
# US_Crime_Rates_1960_2014.csv数据导入并命名为crime
crime = pd.read_csv(r'G:\DAIDAI\2019-2020_Spring Course\python\chenmo\final\data2020\\US_Crime_Rates_1960_2014.csv',\
                    sep=None,engine='python')
#列数较多，设置可显示的最大列数
pd.set_option('display.max_columns',None)
#默认打开数据的前五行查看数据基本结构
house.head()
#每一列(column)的数据类型是什么样的？
crime.info()

# 将Year的数据类型转换为datetime64
crime.Year = pd.to_datetime(crime.Year,format='%Y')
# 将列Year设置为数据框的索引
crimes = crime.set_index('Year',drop=True)
#删除名为Total的列
del crime['Total']
crime.head()
#查询Year（每十年）对数据框分组求和
crimes = crime.resample('10AS').sum()
crimes
#人口是累计数，不能直接求和
population = crime.resample('10AS').max() 
crimes['Population'] = population

#查询美国历史上数据最大的年份
#最大值的索引值
crime.idxmax(0)


import pandas as pd
# US_Crime_Rates_1960_2014.csv数据导入并命名为crime
crime = pd.read_csv(r'G:\DAIDAI\2019-2020_Spring Course\python\chenmo\final\data2020\\US_Crime_Rates_1960_2014.csv',\
                    sep=None,engine='python')
# 将Year的数据类型转换为datetime64
crime.Year = pd.to_datetime(crime.Year,format='%Y')
# 将列Year设置为数据框的索引
crimes = crime.set_index('Year',drop=True)
# 求各种比率
crimes['violent_rate'] = crimes['Violent'] /crimes['Population']
crimes['property_ rate'] = crimes['Property'] /crimes['Population']
crimes['Murder_ rate'] = crimes['Murder'] /crimes['Population']
crimes['Rape_rate'] = crimes['Forcible_Rape'] /crimes['Population']
crimes['Robbery_ rate'] = crimes['Robbery'] /crimes['Population']
crimes['Agg_ rate'] = crimes['Aggravated_assault'] /crimes['Population']
crimes['Burglary _rate'] = crimes['Burglary'] /crimes['Population']
crimes['Larceny_ Theft_ rate'] = crimes['Larceny_Theft'] /crimes['Population']
crimes['Vehicle_ Theft_ rate'] = crimes['Vehicle_Theft'] /crimes['Population']
crimes_rate_list=[i for i in crimes.columns if 'rate'in i]
# 犯罪率可视化
import matplotlib.pyplot as plt
crimes[crimes_rate_list].plot()
# 保存图片
plt.savefig('crimes_rate.png')
"""
#Titanic可视化
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#数据读入并命名为titanic
titanic = pd.read_csv(r'G:\DAIDAI\2019-2020_Spring Course\python\chenmo\final\data2020\Titanic.csv',\
                    sep=None,engine='python')

#将PassengerId设置为索引
titanic = titanic.set_index('PassengerId')

#显示重复数据数量
titanic.duplicated().value_counts()

#显示有空值的列
titanic['Age'].isnull().value_counts()
titanic['Cabin'].isnull().value_counts()
titanic['Embarked'].isnull().value_counts()
#处理空值
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].mean()).astype(np.int64)
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode())
#删除无关的列
titanic = titanic.drop(['Ticket','Cabin'],axis='columns')

# 画图
fig = plt.figure(figsize=(10,4.5))
pclass_sp = fig.add_subplot(121)
age_sp = fig.add_subplot(122)
by_class = titanic.groupby('Pclass',
                          as_index=False)['Name'].count().sort_values(by='Name',ascending=False)
pclass_sp.bar(np.arange(3),by_class['Name'])
pclass_sp.set_xlabel('Pclass')
pclass_sp.set_xticks(np.arange(3))
age_sp.hist(titanic['Age'])
age_sp.set_xlabel('age')
# 保存图片
plt.savefig('pclass_age.png')



#男女乘客比例的可视化
Male = (titanic.Sex == 'male').sum()
Female = (titanic.Sex == 'female').sum()

proportions = [Male,Female]

plt.pie(proportions, labels=['Male','Female'],shadow=True,
        autopct='%1.1f%%',startangle=90,explode=(0.15,0))
plt.axis('equal')
plt.title('Sex Proportion')
plt.tight_layout()
plt.savefig('sex_percent.png')

# 船票Fare, 与乘客年龄和性别可视化
lm = sns.lmplot(x='Age',y='Fare', data=titanic,hue='Sex',fit_reg=False)
lm.set(title='Fare x Age')
# 保存图片
plt.savefig('fare_sex_age.png')


#设置坐标轴取值范围
axes = lm.axes
axes[0,0].set_ylim(-5,)
axes[0,0].set_xlim(-5,85)

# 查询生还人总数
titanic.Survived.sum()

#绘制一个展示船票价格的直方图
df = titanic.Fare.sort_values(ascending = False)

plt.hist(df,bins = (np.arange(0,600,10)))
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare Payed Histrogram')
# plt.savefig('fare.png')


#创建一个新字段isalone
titanic['isalone'] = titanic['SibSp'] + titanic['Parch']
titanic['isalone'].unique()
#转换isalone不为 0 的为 1
titanic.loc[titanic['isalone']>0,'isalone'] = 1
#查询独自一人的总数
isalone_count = titanic.groupby('isalone')['Survived'].count()
isalone_count

"""