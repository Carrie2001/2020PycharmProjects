import pandas as pd
from math import log
import myTreeVisualization

def shannonEnt(dataSet):
    """
    计算信息熵
    :param data:西瓜数据集
    :return: 信息熵shannonEnt
    """
    # 计算数据集样本总数
    dataSize = dataSet.shape[0]
    # 九三数据集属性个数（西瓜数据中的列数，包括最后一列）
    colSize = dataSet.shape[1]
    # 创建字典，统计数据集样本各个类别和键值即为相应的类别出现数目
    labelCounts = dict(dataSet.iloc[:, colSize - 1].value_counts())
    # 初始化信息熵
    shannonEnt = 0.0
    # 计算
    for key in labelCounts:
        """
        计算类别出现的频率当做概率，利用这个概率计算信息熵
        """
        prob = float(labelCounts[key]) / dataSize
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, colName, colValue):
    """
    按照给定特征划分数据集
    :param data: 西瓜数据集
    :param colName: 划分的特征
    :param colValue: 特征的返回值
    :return: 划分后的新数据集retDataSet
    """
    # 划分前的数据集个数
    dataSize = dataSet.shape[0]
    # 初始化新的数据集,并且列索引和原数据集一致
    retDataSet = pd.DataFrame(columns=dataSet.columns)
    for rowNumber in range(dataSize):
        """
        按照给定的特征，将符合特征的数据提取出来
        """
        if dataSet.iloc[rowNumber][colName] == colValue:
            # 将划分属性等于该属性值的样本划给新数据集
            retDataSet = retDataSet.append(dataSet.iloc[rowNumber, :], ignore_index=True)
    # 去掉该属性列
    retDataSet.drop([colName], axis=1, inplace=True)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    """
    选择最好的数据集划分方式，选择划分特征，选择数据集，
    利用最大的信息增益，计算得到最好的划分特征
    :param dataSet: 西瓜数据集
    :return:最好的特征划分的索引值bestFeature
    """
    # 数据集样本个数
    dataSize = dataSet.shape[0]
    # 数据集属性个数
    numFeature = dataSet.shape[1] - 1
    # 划分前样本集的信息熵
    entropyBase = shannonEnt(dataSet)
    # 初始化最大信息熵
    infoGainMax = 0.0
    # 初始化最佳划分属性
    bestFeature = ''
    for col in range(numFeature):
        featureValueCount = dict(dataSet.iloc[:, col].value_counts())  # 统计该属性下各个值及其数目
        entropyNew = 0.0
        for key, value in featureValueCount.items():
            # 计算该属性划分下各样本集的信息熵加权和
            entropyNew += shannonEnt(splitDataSet(dataSet, dataSet.columns[col], key)) * float(value / dataSize)
        # 计算该属性下的信息增益
        infoGain = entropyBase - entropyNew
        if infoGain > infoGainMax:
            infoGainMax = infoGain
            # 寻找最佳划分属性对应的索引值
            bestFeature = dataSet.columns[col]
    return bestFeature


def majorityCnt(dataSet):
    """
    采用多数表决的方法决定该叶子节点的分类
    :param dataSet:西瓜数据集
    :return:返回dict中出现次数最多的分类名称
    """
    labelCounts = dict(dataSet.iloc[:, dataSet.shape[1] - 1].value_counts())
    return list(labelCounts.keys())[0]


def creatTree(dataSet):
    """
    创建决策树，递归实现
    递归停止的条件有两个
    1.所有的类标签完全相同，并且直接返回该类标签
    2.将所有的类标签都使用了，仍然不能将数据集划分为仅包含唯一类别的分组，
       此时，以出现次数最多的类别作为返回值
    :param dataSet:西瓜数据集
    :return:字典变量myTree,包含特征名称，叶子节点
    """
    if (dataSet.shape[1] == 1 or len(dataSet.iloc[:, dataSet.shape[1] - 1].unique()) == 1):
        return majorityCnt(dataSet)
    # 选择最佳划分属性
    bestFeature = chooseBestFeatureToSplit(dataSet)
    # 以字典形式创建决策树
    myTree = {bestFeature: {}}
    # 统计该属性下的所有属性值
    bestFeatureValueCount = dict(dataSet.loc[:, bestFeature].value_counts())
    for key, value in bestFeatureValueCount.items():
        # 递归调用完善决策树
        myTree[bestFeature][key] = creatTree(splitDataSet(dataSet, bestFeature, key))
    return myTree


def classify(inputTree, valSple):
    """
    对于新样例进行分类
    :param inputTree: 输入的决策树
    :param valSple:
    :return:
    """
    # 选择第一个划分属性
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    for key in secondDict.keys():
        if (valSple[firstStr] == key):
            # 将该样本在该划分属性的值与决策树中的值进行一一对应的判断
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], valSple)  # 递归调用分类函数
            else:
                classLabel = secondDict[key]
    return classLabel

# 读取西瓜数据集2.0
watermelon = pd.read_excel('watermelon20.xlsx', encoding='gbk')
# 创建西瓜数据集2.0的决策树
watermelonTree = creatTree(watermelon)
print(watermelonTree)

# 决策树可视化
myTreeVisualization.createTree(watermelonTree, "西瓜数据集2.0（ID3方法）")


