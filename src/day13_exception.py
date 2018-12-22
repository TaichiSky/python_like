#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'exception'

__author__ = 'dogsky'

import logging as log

##exception-hierarchy:https://docs.python.org/3/library/exceptions.html#exception-hierarchy

class Compute(object) :
	def __init__(self, x, y) :
		self.x = x
		self.y = y
	def divise(self) :
		print('x / y = ',self.x / self.y)

compute0 = Compute(5, 0)
#compute0.divise()	#ZeroDivisionError

##try...except
class Compute1(Compute) :
	def divise(self) :
		try :    #must
			result = self.x / self.y
			print('x / y = ',result)
		except ZeroDivisionError as zde:    #不是必须的，但若不加上则使得异常捕捉没有太大意义
			print('operate error-ZeroDivisionError : ',zde)    #log.exception(zde)
			#raise    #it will not execute down
		except Exception as ex :
			print('operate error-Exception : ',ex)
		except BaseException as be :
			print('operate error-BaseException : ',be)
		else :    #not must
			print('no error.')
		finally :    #非必须,常用来执行一些后续工作,如关闭文件流等
			print('end...')
compute1 = Compute1(5, 0)
compute1.divise()

##raise
class Compute2(Compute) :
	def divise(self) :
		if 0 == self.y :
			raise Exception('divisor cannot be 0')    #I think unfriendly
			print('divisor cannot be 0')
		else :
			result1 = self.x / self.y
			print('x / y = ',result1)

compute2 = Compute2(5, 0)
compute2.divise()

##self-define exception
##继承某类型异常类,然后用 raise 触发就可以，类似于Java的throw
