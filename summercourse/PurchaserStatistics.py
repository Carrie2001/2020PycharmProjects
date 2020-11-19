# 统计购方单位数
# 导入pandas
import pandas as pd

# 将附件1名字修改为annex01，读取附件1销项发票信息表
buyer  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex01.xlsx',sheet_name='销项发票信息',usecols=[0,3,6,7])

# 剔除作废发票和价税合计为零的数据条
buyer=buyer[buyer['价税合计']>0]
buyer=buyer[~buyer['发票状态'].str.contains('作废发票')]

# 统计每家企业不同购方单位的交易次数
buyercount=buyer['购方单位代号'].groupby(buyer['企业代号']).value_counts()
buyercount.to_csv(r"C:\Users\HP\Desktop\123buyers.csv")
buyercounts=pd.read_csv(r"C:\Users\HP\Desktop\123buyers.csv",names=['企业代号','购方单位代号','交易次数'])

# buyercounts.set_index(['企业代号'], inplace=True)
# 统计每家企业交易次数大于10的交易单位数目
bc=buyercounts[buyercounts['交易次数']>=10].groupby(['企业代号'])['购方单位代号'].nunique()
bc.to_csv(r"C:\Users\HP\Desktop\123bc.csv")
