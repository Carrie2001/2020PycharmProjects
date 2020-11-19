# 统计购方单位数
"""
import pandas as pd
buyer  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex01.xlsx',sheet_name='销项发票信息',usecols=[0,3,6,7])
buyer=buyer[buyer['价税合计']>0]
buyer=buyer[~buyer['发票状态'].str.contains('作废发票')]
buyercount=buyer['购方单位代号'].groupby(buyer['企业代号']).value_counts()
buyercount.to_csv(r"C:\Users\HP\Desktop\123buyers.csv")
buyercounts=pd.read_csv(r"C:\Users\HP\Desktop\123buyers.csv",names=['企业代号','购方单位代号','交易次数'])
# buyercounts.set_index(['企业代号'], inplace=True)
bc=buyercounts[buyercounts['交易次数']>=10].groupby(['企业代号'])['购方单位代号'].nunique()
bc.to_csv(r"C:\Users\HP\Desktop\123bc.csv")
"""""

# 作废发票
"""
import pandas as pd
invoice0  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex1.xlsx',sheet_name='进项发票信息',usecols=[0,3,4,6,7])
invoice1 = invoice0[~invoice0['发票状态'].str.contains('有效发票')]
invoice2 = invoice0[~invoice0['发票状态'].str.contains('作废发票')]
zuofeicount1 = invoice1['发票状态'].groupby(invoice1['企业代号']).value_counts()
zuofeicount1.to_csv(r"C:\Users\HP\Desktop\123zuofei.csv")
youxiaocount1 = invoice2['发票状态'].groupby(invoice2['企业代号']).value_counts()
youxiaocount1.to_csv(r"C:\Users\HP\Desktop\123youxiao.csv")
invoice00  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex2.xlsx',sheet_name='进项发票信息',usecols=[0,3,4,6,7])
invoice01 = invoice00[~invoice00['发票状态'].str.contains('有效发票')]
invoice02 = invoice00[~invoice00['发票状态'].str.contains('作废发票')]
zuofeicount2 = invoice01['发票状态'].groupby(invoice01['企业代号']).value_counts()
zuofeicount2.to_csv(r"C:\Users\HP\Desktop\302zuofei.csv")
youxiaocount2 = invoice02['发票状态'].groupby(invoice02['企业代号']).value_counts()
youxiaocount2.to_csv(r"C:\Users\HP\Desktop\302youxiao.csv")
"""

# 统计每半年的收益负债情况
"""
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


Rexpend0=pd.read_csv(r"C:\Users\HP\Desktop\123Yearout.csv")
Rexpend0=pd.read_csv(r"C:\Users\HP\Desktop\123Yearout.csv",names=['企业代号','年份','支出'])
Rexpend=Rexpend0[Rexpend0['支出']>0]
Rexpend.to_csv(r"C:\Users\HP\Desktop\123YRexpend.csv")

Rincome0=pd.read_csv(r"C:\Users\HP\Desktop\123Yearin.csv")
Rincome0=pd.read_csv(r"C:\Users\HP\Desktop\123Yearin.csv",names=['企业代号','年份','收入'])
Rincome=Rincome0[Rincome0['收入']>0]
Rincome.to_csv(r"C:\Users\HP\Desktop\123YRincome.csv")
"""

# 公司名称的字段识别分类
"""
import pandas as pd
name0  = pd.read_excel(r'C:\Users\HP\Desktop\annex\annex2.xlsx',sheet_name='企业信息',usecols=[0,1])
name0['企业名称'] = name0['企业名称'].str.replace(r'[^\w\s]+', '')
name0.to_csv(r"C:\Users\HP\Desktop\302nameunsign.csv")

Self = name0[name0['企业名称'].str.contains('个体经营')]
Self.to_csv(r"C:\Users\HP\Desktop\Self.csv")
name1 = name0[~name0['企业名称'].str.contains('个体经营')]

name1.to_csv(r"C:\Users\HP\Desktop\246.csv")

name2 = name1[name1['企业名称'].str.contains('建筑|建设|工程')]
name2.to_csv(r"C:\Users\HP\Desktop\建筑建设工程.csv")
name2 = name1[~name1['企业名称'].str.contains('建筑|建设|工程')]

name3 = name2[name2['企业名称'].str.contains('商业|商贸|贸易|工贸')]
name3.to_csv(r"C:\Users\HP\Desktop\商业商贸.csv")
name4 = name2[~name2['企业名称'].str.contains('商业|商贸|贸易|工贸')]

name5 = name4[name4['企业名称'].str.contains('电子|网络|软件|科技')]
name5.to_csv(r"C:\Users\HP\Desktop\电子软件网络科技.csv")
name6 = name4[~name4['企业名称'].str.contains('电子|网络|软件|科技')]

name7=name6[name6['企业名称'].str.contains('文化|体育|媒体|图书|传媒')]
name7.to_csv(r"C:\Users\HP\Desktop\文娱传媒.csv")
name8=name6[~name6['企业名称'].str.contains('文化|体育|媒体|图书|传媒')]

name9=name8[name8['企业名称'].str.contains('物流|运输|快递|运业|运')]
name9.to_csv(r"C:\Users\HP\Desktop\运输物流.csv")
name10=name8[~name8['企业名称'].str.contains('物流|运输|快递|运业|运')]

name11=name10[name10['企业名称'].str.contains('医药|药材|药|医')]
name11.to_csv(r"C:\Users\HP\Desktop\医疗.csv")
name12=name10[~name10['企业名称'].str.contains('医药|药材|药|医')]

name13=name12[name12['企业名称'].str.contains('汽车|机器|机电|机|设备|轮胎')]
name13.to_csv(r"C:\Users\HP\Desktop\汽车机械.csv")
name14=name12[~name12['企业名称'].str.contains('汽车|机器|机电|机|设备|轮胎')]

name15=name14[name14['企业名称'].str.contains('材|电气|石|料|资|纸|塑')]
name15.to_csv(r"C:\Users\HP\Desktop\材料物资.csv")
name16=name14[~name14['企业名称'].str.contains('材|电气|石|料|资|纸|塑')]

name17=name16[name16['企业名称'].str.contains('服务|务')]
name17.to_csv(r"C:\Users\HP\Desktop\服务业.csv")
name18=name16[~name16['企业名称'].str.contains('服务|务')]

name19=name18[name18['企业名称'].str.contains('食品|家居|家具|酒店|纺织|卫浴|服装|五金|地毯|童装')]
name19.to_csv(r"C:\Users\HP\Desktop\生活用品需求业.csv")
name20=name18[~name18['企业名称'].str.contains('食品|家居|家具|酒店|纺织|卫浴|服装|五金|地毯|童装')]

name20.to_csv(r"C:\Users\HP\Desktop\其他.csv")
"""

