# 2020第十一周周五
"""
通用函数：对每个输入元素都进行的函数
一元二元：输入个数为1个，2个

"""
"""
比较运算返回的是true false 
返回的也就是bool数组
ndarray比较运算与布尔索引结合

python的布尔运算（逻辑运算）
and 合取 
or  析取
not 取非

ndarray的布尔运算（数组运算）
& 按位与   合取
| 按位或   析取
^ 按位异或 相异返回1
~ 按位取反 取非
ndarray的布尔运算优先级高于比较运算

ndarray的统计运算
统计函数NaN(缺失值)版本可以忽略缺失值进行计算
np.sum(数组名)   数组名.sum()

max与maximum
nanmax与

std标准差var方差ptp极差
只能用np.avera（）进行加权平均计算
count_nonzero(a,axis=None)统计非零值的个数
any(a,axis=None)统计数组存在True就返回True
all(a,axis=None)统计数组所有的都是True就返回True
"""
"""
ndarray的随机函数
numpy的随机函数字库np.random.函数名
np.random.random(size=None):[0.0,1.0)中随机的浮点数，size相当于数组的shape属性，size等于5那就是生成五个随机数
np.random.rand(m,n):类似于上一个，直接生成m行n列
np.random.randn():均值为0，标准差为1的标准正态分布的随机数数组
np.random.randint(low[,high=None,size=None]):范围是[0，low)，[low,high)，没有size的话就直接随机返回一个符合范围内的整数
np.random.seed():随机数种子，用于指定随机数生成所用算法开始的初始值，固定一组得到的随机数
np.random.uniform(low,high,size):默认产生[0.0,1.0)随机浮点数
np.random.normal(loc,scale,size):从正态分布中抽取随机数创建随机数组
np.random.shulffle(a):在原数组a上直接o轴乱序
np.random.permutation(b):不改变原数组的对0轴做乱序
"""
"""
ndarray的广播运算在NumPy中不同形状数组之间的运算
小维度数组在左边补1
某一维度上不匹配，在维度为1的维度上进行拓展

中心化（零均值化）：变量减去均值（一个平移的过程），平移后所有数据的中心是（0,0）
"""
"""
数组的重复与排序
np.repeat(a,repeats,aixs=None):
np.sort(a,axis=-1,kind='quicksort'):默认沿着最后的一个轴进行排序，从小到大的排序，不改变原数组
np.argsort()返回的是一个原数组排好序的索引数组不修改原数组
"""
"""
ndarray的基本操作；增删改查
np.insert(arr,obj,values,axis=None)默认按行展开为一位数组进行插入
np.delete(arr,obj,axis):二维数组删除元素
np.where(condition,x,y):x if condidtion else y,condition为true则x，为false则y
np.concatenate((a1,a2,……),axis=0):每个数组必须具有相同的形状，可以多个数组进行拼接
np.vstack(tup):垂直堆叠函数=np.concatenate(tup,axis=0)
np.hstack(tup)：水平堆叠函数np.concatenate(tup,axis=1)
np.split(ary,indices,axis=0)
np.vsplit():0轴方向的分裂
np.hsplit():1轴方向上的分裂
"""
#2020第十二周周五数据可视化matplotlib
"""
plt.plot(x1,y1,z1,x2,y2.z2......)
一次执行xyz1和xyz2
画多条线的时尽量多plot几次不要一次性
点虚线形是：，点是co
plt.title，xlabel,ylabel,
利用字典dict花括号，逗号分隔的是键值对，键值对冒号链接键和值（一种映射关系），设置字体的特色fontdict=a_dict等
数据标签：plt.text(x,y,str,ha,va,fontsize......)（位置，ha是right，va是center）
网格线的设置plt.grid(bool,axis,color,linestyle,linewide)
箭头注释：plt.annotate()arrowprops=dict()
图例：plt.legend()
坐标轴刻度的设置xticks(ticks,[label],**kwargs)
坐标轴范围：plt.xlim()
子图：subplot(nrows(行),ncols（列),)
plt.savefig('xxx.png'，dpi=分辨率):把图片存在工作文件夹（保存之后可以不用再写show了）
family设置字体
"""
"""
plt.***画图法
面向对象的画图法
"""
"""
figure画布
"""
"""
线形图操作实例
疫情趋势图
散点图：scatter可以控制每个散点与数据匹配，cmap是色彩盘（viridis松石绿转化为灰度图最清晰），colorbar是色彩条，alpha是透明度
饼图：plt.pie()explode：突出外扩显示
plt.axis('equal')
"""
# 2020第十三周周五pandas，DataFrame
"""
import  pandas as pd
http://pandas.pydata.org
"""
"""
series 类似于一维数组加上一维索引（索引在左边，值在右边（数据标签与数据））
pd.Series()创建Series对象
pd.Series(
data=数据，
index=索引，
dtype=类型
)
会自动生成索引0 1 2 3......
也可以自定义一个索引......
传入一个标量（根据索引做广播类似于numpy的ones等）
向pd.Series()传入一个字典：字典里面的key作为index（要是还要自定义索引了，就不根据字典的key，永远以自定义的index为根据结合key来填充数据）
Series可以与ndarray结合使用pd.Series(np.arange())
Series的值可以类型不同，NumPy的必须同类型
不同的话返回之后Series对象的dtype是object（指针形式，内存要求就变大了）
"""
"""
Series的基本操作
.index返回index类型对象
.values返回ndarray
自定义索引的时候访问时字符串要记得打''
花式索引
列表类型的索引
不能混合使用自定义与自动索引
切片功能
a[1:3]默认索引是切不到3对应的数据，但是用自定义所以的切片范围是包含的
.mean()等方法只对values做运算
布尔索引
索引对齐：series对象可以直接相加得到values的相加结果，若果一个对象中有一个缺失值，他结果也是缺失值，所以每个对象里面都是有values的才行
属性.name()：series对象的唯一名称
"""
"""
DataFrame:一组数据和一对索引（行索引index，列索引columns）
pd.DataFrame（
data=数据，
index=行索引，（也会自动生成索引）
columns=列索引，（也会自动生成索引）
dtype=
）
字典的value构成DF的一列，key作为列索引
嵌套列表，每一个列表表示一行
series的索引是df的行索引
"""
"""
DataFram的数据选择
.index行索引
.columns列索引
.values返回 ndarray
获取列数据
a[math]或者是a.math来获取math列索引的列数据及相应的行索引
添加列的操作不能用属性a.math but we can use a[math]
a[[1,2],[2,1]]花式索引返回的是坐标为[1,0]and[2,1]two points
DF沿用numpy的数据操作
比较运算 布尔运算 布尔索引 
DF的切片
行数据切片：类似series切片规则
列数据的花式索引：列表索引，列索引不能做切片，但是能单列索引，花式索引
"""
"""
pandas has indexer 索引器indexer
iloc，loc提供灵活的索引
loc：自定义索引（对于列a[:,index]要加上：，）
iloc:自动索引
对于行和列的同时索引
a[[1,2],[0,1]]不同于series的，是一整行，一整列进行的
loc和iloc与布尔索引的结合
"""
"""
增删改查
reindex：重新索引（数据跟着索引一起变，相应的数据）
method='ffill'：填充方法的前项填充'bfill':后项填充（对单调的进行填充。先排序后bfill，ffill）
a.index.insert(位置，索引值)
排序a.sort_index(inplace=True(true就做原地操作))ascending:默认排序
a>A
a.index.delet()
DataFrame.drop()
删除列
append添加到DataFrame
ignore_index=True:添加之后重新自动索引
索引名称的修改不改数据等rename
a.rename(index={新的索引名称：旧的索引名称})（键值对）

"""
# 2020第十四周周五pandas数据处理操作
"""
add，div。。。。。。
相同纬度运算会索引对齐，合并索引，对齐处进行计算（有缺失值进行运算就是NaN）
A.sub（B(A-B)，fill_value=0(设置缺失值为0)）（填充后都是缺失值结果还是NaN）
符号运算和算数方法运算磨人的都是行运算，对于算数方法的运算可以设置列索引方向（axis=‘columns’或者axis=1）
两个dataframe的比较运算结果为布尔值
dataframe和series比较运算，把series进行广播
numpy的通用函数同样可以使用在series和dataframe上
数值排序A.sort_values（by，ascending=True就是升序)
多列排序：主次关键字na_position 设置缺失值排的位置
熟数值的查找：A[].isin[]
数值的替换：批量替换df.replace(80,80.5)把80换成80.5，字典实现多对多的替换
"""
"""
统计分析
基本统计分析方法的axis默认为0
累计统计函数：cumsum累加，。。。
数值计数：只能对series做，a.value_counts(normalize=True)计算出现的次数以及所占比重 
统计不同值个数a.nunique(dropna=True(不不包含缺失值))series.unique获取元素中的唯一值，不同的值，去掉重复值
模拟数据的生成np.random.seeds()
map函数a.map()映射
dataframe没有map
map是series的对象方法
自定义函数
series的apply方法
lambda表达式
数据分组groupby
拆分split应用apply合并combine
A.groupby(by,axis=0)
"""
#2020第十五周周五数据文件读取
"""
csv文件读取（逗号分隔值）
文件地址：\的使用，直接拖到Windows键+R键打开的窗口可以查看地址
把注释信息去掉，保留数据
不设置表头那么第一行就是表头
index_col设置行索引
usecols来选择读取哪几列
使用pandas的read_csv将数据读入DF或series，读成DF自动填充缺失值为NaN
r表示非转义字符，encoding设置导入数据的编码格式：utf-8，gbk（没用中文时候可以直接导入，不需要设置encoding）
skiprows可以跳过一些行文本数据
写入数据使用to_csv方法，sep设置分隔符，na_rep设置缺失值为NA：not avaliable
float_format:'%.2f'pandas设置NaN为浮点型，None本身就是空值类型
使用none或者是np.nan标记缺失值为float
np.mean(),np.nanmean()(忽略缺失值)
发现缺失值
info()统计非缺失值
isnull和notnull
isnull().any()只要有一个null就会用any返回true告诉我们有缺失值
再利用columns[isnull().any()]直接返回空值的地方
index[isnull().any(axis=1)]找出哪些行上面有缺失值
isnull().sum()每一列缺失值得个数isnull().sum().sum()统计所有列的缺失值
dropna()剔除有缺失值的一个整行列，how设置如何剔除，设置thresh=n有n项值就保留
用n填充缺失值fiilna(n)，设置method为ffill,bfill(后项填充)
"""
"""
删除重复值
drop_duplicates(subset=[列]，keep='first'(保留第一个出现的))
"""
"""
异常值处理
describe()针对各列汇总统计
分位数，箱型图botplot()画出箱型图
where方法where（g<90,100）:小于90不动，别的换成100，相应的用缺失值填充异常值
"""