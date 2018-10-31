#!/usr/bin/env python3
#-*- coding:utf8 -*-
#

'mysql backup script'

import os
import time
import string

import urllib,sys,json,smtplib
from email.mime.text  import MIMEText

mailto_list=['zhuqiang@chinacloud.com.cn']
mail_host='smtp.chinacloud.com.cn'
mail_user='zhuqiang@chinacloud.com.cn'
mail_pass='kk524524'
mail_postfix='chinacloud.com.cn'

def send_mail(to_list,sub,content):
	me="hello"+"<"+mail_user+"@"+mail_postfix+">"
	msg=MIMEText(content,_subtype='plain')
	msg['Subject']=sub
	msg['From']=me
	msg['To']=";".join(to_list)
	try:
		server=smtplib.SMTP(mail_host,25)
		#server.set_debuglevel(1)
		server.login(mail_user,mail_pass)
		server.sendmail(me,to_list,msg.as_string())
		server.close()
	except :
		return False

#########################################

""" mysql  dump"""

databases=['test','test1']
mysql_user='root'
mysql_pass='123456'
mysql_host='192.168.136.100'
back_server_path='/opt/mysql'

#########获取当前时间 ###########
datatime=time.strftime('%Y%m%d-%H%M')

###### 创建备份目录  ############
if not os.path.exists(back_server_path):
	os.mkdir(back_server_path)

######## 开始备份 ############
print("##########"+datatime+"################")
print("##########  mysql backup  begin ##############")
os.chdir(back_server_path)  #切换到备份目录
for database_name in databases:
	database_file_name=database_name+"_"+datatime+'.sql'
	sql_comm="mysqldump -u"+mysql_user+" -p"+mysql_pass+" -h "+ mysql_host+" "+ database_name+" > "+database_file_name
	print("###########"+database_name+" backuping#############")
	if os.system(sql_comm) == 0:
		print(database_name,'is backup success!')
		send_mail(mailto_list,'mysql backup success!',mysql_host+' '+database_name+' is backup success!')
	else:
		print(database_name,'is backup false!')
		send_mail(mailto_list,'mysql backup false!',mysql_host+' '+database_name+' is backup false!')
	print("############mysql backup over#############")
print("##############"+time.strftime('%Y%m%d-%H%M')+"###########")
