#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'time,datetime,calendar'

__author__ = 'dogsky'

import time as t
import datetime as dt
import calendar as cal

##time
print('t.time() = ',t.time())

#localtime | print date of tuple
print()
print('t.localtime() = ',t.localtime())

#asctime
print()
print('t.asctime() = ',t.asctime())

#strftime(formatter,localtime)
print()
print('t.strftime("%Y-%m-%d",t.localtime()) = ',t.strftime("%Y-%m-%d",t.localtime()))
print('t.strftime("%H:%M:%S",t.localtime()) = ',t.strftime("%H:%M:%S",t.localtime()))
print('t.strftime("%Y-%m-%d %H:%M:%S",t.localtime()) = ',t.strftime("%Y-%m-%d %H:%M:%S",t.localtime()))

#mktime,strptime
print()
mk_time = t.mktime(t.strptime("2018-12-9","%Y-%m-%d"))
print('mk_time = ',mk_time)

##datetime
print()
print('dt.datetime.today() = ',dt.datetime.today()
,'\n dt.datetime.now() = ',dt.datetime.now()
,'\n dt.date.today() = ',dt.date.today()
,'\n assign datetime = ',dt.datetime(2018,12,9,14,32))

#datetime => timestamp
print()
time_stamp = dt.datetime(2018,12,9,14,32).timestamp()
print('time_stamp = ',time_stamp)

#datetime => str
print()
str_time = dt.datetime(2018,12,9,14,32).strftime('%Y-%m-%d %H:%M:%S')
print('str_time = ',str_time)

#timestamp => datetime
s_time = 1544337120.0
print()
print(dt.datetime.fromtimestamp(s_time))

#str => datetime
print()
d_time = dt.datetime.strptime("2018-12-9 14:44:00","%Y-%m-%d %H:%M:%S")
print('d_time = ',d_time)

#get yesterday
print()
print('yeaterday is :',dt.date.today() - dt.timedelta(days = 1))

#weekdays
print()
print(f'weekday of today = {dt.date.today().weekday()+1}')

##calendar
print()
print('month of text-format : \n',cal.TextCalendar(cal.SUNDAY).formatmonth(2018,12))

print()
#print('month of html-format : \n',cal.HTMLCalendar(cal.SUNDAY).formatmonth(2018,12))

#iterator the date of the current month
print()
str_date_list = []
for cur_date in cal.TextCalendar(cal.SUNDAY).itermonthdates(2018,12) :
	str_time = cur_date.strftime('%Y-%m-%d')
	str_date_list.append(str_time)
	str_date_list.append(' ,')
str_date_list.pop()    #str_date_list = str_date_list[:len(str_date_list)-1]
print('cur_date of cur_month :',''.join(str_date_list))

#iterator the month
print()
str_mon_list = []
for con_month in cal.month_name :
	str_mon_list.append(str(con_month))
str_mon_list.pop(0)
print('const_month :',str_mon_list)

#iterator the weekday
print()
str_week_list = []
for con_month in cal.day_name :
	str_week_list.append(str(con_month))
print('const_month :',str_week_list)
