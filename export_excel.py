#!/usr/bin/python3
#-*-coding=utf-8-*-

import os
import xlwt
# import xlrd
file_path='/root/zhuq/test.xls' #要插入的excel文件
#检测文件是否存在，如存在，则删除
if os.path.exists(file_path):
	os.remove(file_path)
f=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=f.add_sheet('sheet1') #建立excel文件

#初始化单元格样式
#边框
borders=xlwt.Borders()
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1
borders.bottom_colour=0x3A

#背景色
pattern = xlwt.Pattern() #创建一个模式
pattern.pattern = xlwt.Pattern.SOLID_PATTERN     # 设置其模式为实型
pattern.pattern_fore_colour = 3
# 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,  the list goes on


style0 = xlwt.XFStyle()
style0.borders = borders
style0.pattern = pattern
#打开读取数据的文件
f1=open('/root/zhuq/sub/ip.txt','r')
#将文件内容读取到数据lines中  分行读取
lines=f1.readlines() 
#初始化循环数值
row_num=0
col_num=0
#循环按行读取文件内容
len_col=[0]*100
for line in lines:
	#将读取的行用空格进行分割
	str1=line.split()
	#读取每个字符串
	for data in str1:
		#判断列宽，根据最大长度设置
		if len_col[col_num] < len(data):
			len_col[col_num]=len(data)
		sheet.col(col_num).width = 256*len_col[col_num]
		#写入内容
		sheet.write(row_num,col_num,data,style0)
		col_num=col_num+1
	row_num=row_num+1	
	col_num=0
#保存文件
f.save(file_path)
