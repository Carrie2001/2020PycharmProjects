# 作废发票
# 将附件1重命名为annex1.xlsx
# 将附件2重命名为annex2.xlsx
import pandas as pd

invoice0  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex1.xlsx',sheet_name='进项发票信息',usecols=[0,3,4,6,7])
invoice1 = invoice0[~invoice0['发票状态'].str.contains('有效发票')]
invoice2 = invoice0[~invoice0['发票状态'].str.contains('作废发票')]
zuofeicount1 = invoice1['发票状态'].groupby(invoice1['企业代号']).value_counts()
# 记录各家企业的作废发票数
zuofeicount1.to_csv(r"C:\Users\HP\Desktop\123zuofei.csv")
youxiaocount1 = invoice2['发票状态'].groupby(invoice2['企业代号']).value_counts()
# 记录各家企业的有效发票数
youxiaocount1.to_csv(r"C:\Users\HP\Desktop\123youxiao.csv")

# 类似于123家企业，统计附件2的302家企业的发票作废和有效数据
invoice00  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex2.xlsx',sheet_name='进项发票信息',usecols=[0,3,4,6,7])
invoice01 = invoice00[~invoice00['发票状态'].str.contains('有效发票')]
invoice02 = invoice00[~invoice00['发票状态'].str.contains('作废发票')]
zuofeicount2 = invoice01['发票状态'].groupby(invoice01['企业代号']).value_counts()
zuofeicount2.to_csv(r"C:\Users\HP\Desktop\302zuofei.csv")
youxiaocount2 = invoice02['发票状态'].groupby(invoice02['企业代号']).value_counts()
youxiaocount2.to_csv(r"C:\Users\HP\Desktop\302youxiao.csv")
