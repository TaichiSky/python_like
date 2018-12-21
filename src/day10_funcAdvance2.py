#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'function-advance2 [closure, anonymous function, decorator]'

__author__ = 'dogsky'

import sys
import time as t

##return function as result
#usually
def compute(*params) :
	sum = 0;
	for n in params :
		sum = sum + n;
	return sum

fun_sum = compute(1,2,3,4,5)
print('fun_sum = compute(1,2,3,4,5) = ',fun_sum)

#lazy call
def lazy_compute(*params) :
	def sum() :
		sum = 0;
		for n in params :
			sum = sum + n;
		return sum
	return sum

fun_sum1 = lazy_compute(1,2,3,4,5)
print()
print('fun_sum1 = lazy_compute(1,2,3,4,5) = ',fun_sum1
,'\n fun_sum1() = ',fun_sum1())

fun_sum2 = lazy_compute(1,2,3,4,5)
print('fun_sum2() = ',fun_sum2()
,'\n fun_sum1 == fun_sum2 ? ',fun_sum1 == fun_sum2)

##closure
def squareOfNum() :
	list_result = []
	for i in range(1,4) :
		def square() :
			return i * i
		list_result.append(square)
	return list_result

fun_s1, fun_s2, fun_s3 = squareOfNum()
print()
print('fun_s1() = ',fun_s1()    #9 , why not the 1
,'\n fun_s2() = ',fun_s2()    #9 , why not the 4
,'\n fun_s3() = ',fun_s3())    #9

#the return function doesn't reference any loop variables, or variables that will change later.
#closure of improved
def squareOfNum1() :
	
	def square1(i) :
		def s() :
			return i * i
		return s

	list_result = []
	for i in range(1,4) :
		#def square() :
		#	return i * i
		list_result.append(square1(i))
	return list_result

fun_s11, fun_s22, fun_s33 = squareOfNum1()
print()
print('fun_s11() = ',fun_s11()    #1
,'\n fun_s22() = ',fun_s22()    #4
,'\n fun_s33() = ',fun_s33())    #9

##anonymous function
print()
list_anony1 = list(map(lambda x : x * 2 - 1, list(range(1,11))))
print('list_anony1 = ',list_anony1)

##decorator,[dynamically add functionality while the code is running]
#similar to annotation of java
def getDate() :
	current_time = t.strftime("%Y-%m-%d %H:%M:%S",t.localtime())
	return current_time

print()
print('getDate : ',getDate())

#print log before the function is executed
def getDateLog(func) :    ##how to get the name of this parameter function?
	def beforePrint(*args, **otherParams) :
		print('server is started...current method is',sys._getframe().f_code.co_name)
		return func(*args, **otherParams)
	return beforePrint

@getDateLog
def getDateImproved() :
	current_time = t.strftime("%Y-%m-%d %H:%M:%S",t.localtime())
	return current_time

print()
print('getDate : ',getDateImproved())
