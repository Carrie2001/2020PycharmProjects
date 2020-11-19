"""
路径问题
Linux与Windows的文件路径 表示方法
Windows的驱动器C,D,E,F,G,H：C:\testwenjianjia\testwenjian.txt
Linux下的文件：/home/wenjian.txt
python是跨平台的语言，Linux，Windows，Apple下装的python
相对路径，绝对路径的\/斜杠python都能正确判断出你要写的
when遇到转义的情况，连写两个\\open('d:\\n.py')
或者是加上r不去进行转义open(r'd:\n.py')
文件与文件夹操作——os（操作系统）模块
库：os,os.path,pathlib

"""""