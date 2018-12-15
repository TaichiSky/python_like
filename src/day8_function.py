#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'function'

_author_ = 'dogsky'

import math as m

##input name and print welcome message
def welcome_guest (*names) :
	for name in names :
		print('welcome you,',name)

welcome_guest('python')
welcome_guest('java','python','go')

##solving equation
def sove (a,b,c) :
	defValue = b*b - 4*a*c
	if ( defValue < 0.000001 ) :
		print('param is error')
		return ('error','error')
	else :
		x1 = (-b + m.sqrt(defValue))/(2*a)
		x2 = (-b - m.sqrt(defValue))/(2*a)
		return x1,x2

x1, x2 = sove(1, -5, 6)
print('x1 = ',x1,', x2 = ',x2)

##default param
##note:the default parameter must point to an invariant object[eg:strings,tuples,numbers]
def listScenOfBeijing (scenName, scenName1='Great Wall') :
	print('interesting place of Beijing:',scenName,', ',scenName1)

listScenOfBeijing('TianAnMen')

##keyword parameter,increased scalability
def myInfo (name, **otherInfo) :
	print('name = ',name,', other info = ',otherInfo)

otherInfos = {'hobby':'swimming', 'height':'178cm'}
myInfo('luckdog')
myInfo('luckdog', hobby = 'swimming', height = '178cm')
myInfo('luckdog', **otherInfos)

#limit keyword parameter
def limitMyInfo (name, *, hobby, height) :
	print('name = ',name,',hobby = ',hobby,',height = ',height)

limitMyInfo('luckdog', hobby = 'swimming', height = '178cm')
#limitMyInfo('luckdog', 'swimming','178cm')    #error

##recursive function
def factorial (n) :
	if not isinstance(n, int) :
		raise TypeError('type error!')
	else :
		if 1 == n :
			return 1
		else :
			return n * factorial(n-1)

print('5! = ',factorial(5))
