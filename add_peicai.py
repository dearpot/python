#!/usr/bin/env python3
#-*-coding:utf8
#
message1='请输入配料:'
message2='我们会在配料中加入'
message3='如需结束,请输入quit！'

active=True
while active:
	peiliao=input(message1)
	if peiliao!='quit':
		print(message2,peiliao,'!')	
		print(message3)
	else:
		active=False
