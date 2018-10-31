[oracle@oracle test]$ cat mail.py 
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#

import smtplib
import sys
from email.mime.text import MIMEText
import email
import os
import importlib
from email.mime.multipart import MIMEMultipart

###############################################
# set email server host,user,password,postfix #
###############################################

mail_host="smtp.chinacloud.com.cn"
mail_user="zhuqiang"
mail_pass="kk524524"
mail_postfix='chinacloud.com.cn'

##################################

def transfer_utf8_to_gb2312(filename):
	f=open(file_name)
	s=f.read()
	f.close()
	u=s.decode("utf-8")
	s=u.encode("gb2312")
	f=open(file_name,"w");
	f.write()

def send_mail(to_list,sub,content_file_name):
	me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
	msg=email.mime.multipart.MIMEMultipart()
	content=open(content_file_name.encode("utf-8"),'rb')
	content_msg = MIMEText(content.read(),"plain","utf-8")
	msg.attach(content_msg)
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ";".join(to_list)
	try:
		s = smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user+"@"+mail_postfix,mail_pass)
		s.sendmail(me,to_list,msg.as_string())
		s.close()
		return True
	except Exception as e:
		print ("error",str(e))
		return False

def send_mail_with_attachment(to_list,sub,content_file_name,attachment_file_name):
	me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
	msg=email.MIMEMultipart.MIMEMultipart()
	content=open(content_file_name.encode("utf-8"),'rb')
	content_msg=MIMEText(content.read(),"plain","utf-8")
	msg.attach(content_msg)
	for tmp_attachment_file_name in attachment_file_name.split(","):
		contype = 'application/octet-stream'
		maintype,subtype=contype.split('/',1)
		file_data=open(tmp_attachment_file_name.encode("utf-8"),'rb')
		file_msg=email.MIMEBase.MIMEBase(maintype,subtype)
		file_msg.set_payload(file_data_read())
		file_data.close()
		email.Encoders.encode_base64(file_msg)
		basename=os.path.basename(tmp_attachment_file_name)
		file_msg.add_header('Content-Disposition','attachment',filename=basename.encode("uth-8"))
		msg.attach(file_msg)
	msg['Subject']=sub
	msg['From']=me
	msg['To']=";",join(to_list)
	try:
		s=smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user+"@"+mail_postfix,mail_pass)
		s.sendmail(me,to_list,msg.as_string())
		s.close
		return True
	except	Exception as e:
		print ("error:",str(e))
		return False

def print_usage():
	print ("Usage:")
	print ("  %s email_send_list(XXX@163.com,xxx@qq.com,....) subject content_file_name" % (sys.argv[0]))
	print ("  %s email_send_list(xxx@163.com,xxx@qq.com,...) subject content_file_name attachment_file_name(file_name1,file_name2,...) if_transform_attachment_to_gb2312(yes or not)" % (sys.argv[0]))
	
###################start from here###############
if __name__ == '__main__':
	importlib.reload(sys)
	#sys.setdefaultencoding('utf8')
	if len(sys.argv) == 6:
		send_list=sys.argv[1].split(",")
		subject=sys.argv[2]
		content_file_name=sys.argv[3]
		attachment_file_name=sys.argv[4]
		if(sys.argv[5] == "yes"):
			transfer_utf8_to_gb2312(attachment_file_name.decode("uth-8"))
		elif(sys.argv[5] == "not"):
			pass
		else:
			print_usage()

		if send_mail_with_attachment(send_list,subject,content_file_name,attachment_file_name):
			print ("Send email success!")
		else:
			print ("Send email fail!")
			sys.exit(1)
	elif len(sys.argv) == 4:
		send_list=sys.argv[1].split(",")
		subject = sys.argv[2]
		content_file_name=sys.argv[3]
		if send_mail(send_list,subject,content_file_name):
			print ("Send email success!")
		else:
			print ("Send email fail!")
			sys.exit(1)
	else:
		print_usage()
