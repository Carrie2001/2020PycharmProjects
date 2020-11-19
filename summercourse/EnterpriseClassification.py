# 公司名称的字段识别分类
# 查看Excel表格企业名称给出一些关键词，选取分类企业
# 将附件2改名为annex2.xlsx

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
