#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'dir, func_module, search_path, package structure'

__author__ = 'dogsky'

import sys
import math as m
import os as o
import time as t
import datetime as dt
import calendar as cal

##return the contents of the module
content_math = dir(m)
print('math :',content_math)

content_sys = dir(sys)
print('\n sys :',content_sys)

content_os = dir(o)
print('\n os :',content_os)

content_time = dir(t)
print('\n time :',content_time)

content_datetime = dir(dt)
print('\n datetime :',content_datetime)

content_calendar = dir(cal)
print('\n calendar :',content_calendar)

##define module
print()
def getSysArgs() :
	args = sys.argv
	print('len(args) = ',len(args),'\n args = ',args)

#when being imported,it will doesn't run
if __name__ == "__main__" :
	getSysArgs()
	
##search path when import and load module
##当我们试图加载一个模块时，Python会在当前指定的路径下搜索对应的.py文件，如果找不到，就会报错

##默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
print('\n system_path :',sys.path)

##add search path
#method1 : sys.path.append('')	#will invalid after running
#method2 : 设置环境变量 PYTHONPATH


##package structure

#test.py
#package_name
#	__init__.py
#	a1.py
#	a2.py
#	...
