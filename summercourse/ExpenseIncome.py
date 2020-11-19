# 统计每月的收益负债情况
# 将附件1重命名为annex1.xlsx

import pandas as pd
income0  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex1.xlsx',sheet_name='销项发票信息',usecols=[0,2,4,7])
income0=income0[~income0['发票状态'].str.contains('作废发票')]
income1=income0.set_index('开票日期',drop=True)
income1=income1['金额'].groupby(income1['企业代号']).resample('M').sum()
income1.to_csv(r"C:\Users\HP\Desktop\123Monthin.csv")

expend0  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex1.xlsx',sheet_name='进项发票信息',usecols=[0,2,6,7])
expend0=expend0[~expend0['发票状态'].str.contains('作废发票')]
expend1=expend0.set_index('开票日期',drop=True)
expend1=expend1['价税合计'].groupby(expend1['企业代号']).resample('M').sum()
expend1.to_csv(r"C:\Users\HP\Desktop\123Monthout.csv")

# 统计每年受益负债情况
import pandas as pd
income0  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex1.xlsx',sheet_name='销项发票信息',usecols=[0,2,4,7])
income0=income0[~income0['发票状态'].str.contains('作废发票')]
income1=income0.set_index('开票日期',drop=True)
income1=income1['金额'].groupby(income1['企业代号']).resample('Y').sum()
income1.to_csv(r"C:\Users\HP\Desktop\123Yearin.csv")

expend0  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex1.xlsx',sheet_name='进项发票信息',usecols=[0,2,6,7])
expend0=expend0[~expend0['发票状态'].str.contains('作废发票')]
expend1=expend0.set_index('开票日期',drop=True)
expend1=expend1['价税合计'].groupby(expend1['企业代号']).resample('Y').sum()
expend1.to_csv(r"C:\Users\HP\Desktop\123Yearout.csv")

# 剔除收入支出金额为负数的数据条
Rexpend0=pd.read_csv(r"C:\Users\HP\Desktop\123Yearout.csv")
Rexpend0=pd.read_csv(r"C:\Users\HP\Desktop\123Yearout.csv",names=['企业代号','年份','支出'])
Rexpend=Rexpend0[Rexpend0['支出']>0]
Rexpend.to_csv(r"C:\Users\HP\Desktop\123YRexpend.csv")

Rincome0=pd.read_csv(r"C:\Users\HP\Desktop\123Yearin.csv")
Rincome0=pd.read_csv(r"C:\Users\HP\Desktop\123Yearin.csv",names=['企业代号','年份','收入'])
Rincome=Rincome0[Rincome0['收入']>0]
Rincome.to_csv(r"C:\Users\HP\Desktop\123YRincome.csv")