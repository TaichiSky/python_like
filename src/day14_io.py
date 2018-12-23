#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'io [file, pickle, json]'

__author__ = 'dogsky'

import pickle as pick
import json

##input
str_input = input('please input what you want print :')
print('print result : ',str_input)

##file
try :
	testFile1 = open('test.txt','r', encoding='gbk', errors='ignore')
	print('method1 file content :\n',testFile1.read())    #read():一次性读取全部内容,慎重
finally:
	if testFile1 :
		testFile1.close()
		
#下面2行可替换上面6行写法
with open('test.txt', 'r', encoding='gbk', errors='ignore') as testFile2 :
	print('\n method2 file content :\n',testFile2.read())
	
##read(size), readline, readlines
with open('test.txt', 'r', encoding='gbk', errors='ignore') as testFile3 :
	print('\n readline file content :')
	while True :
		tf3 = testFile3.readline()
		if tf3 == '' :
			break
		print(tf3)

with open('test.txt', 'r', encoding='gbk', errors='ignore') as testFile4 :
	print('\n readlines file content :\n',[line.strip() for line in testFile4.readlines()])
	
##write
with open('test1.txt', 'w') as testFile5 :
	testFile5.write('hello world!')

##pickling(serialization)
myInfo = dict(name='dogsky', age='23', hobby='swimming')
print('\n picking myInfo : ',pick.dumps(myInfo))

myInfoFile = open('dump.txt', 'wb')
pick.dump(myInfo, myInfoFile)
myInfoFile.close()

##反序列化
readMyInfoFile = open('dump.txt', 'rb')
readMyInfo = pick.load(readMyInfoFile)
readMyInfoFile.close()

print('\n read content of dump.txt :',readMyInfo)

##json
#python -> json
myInfoJsonStr = json.dumps(myInfo)
print('\n json.dumps(myInfo) : ',myInfoJsonStr
,'\n type(myInfoJsonStr) : ',type(myInfoJsonStr))

jsonStr = '{"name":"dogsky" ,"info":{"height":"177cm", "weight":"74kg", "hobby":"swimming"}}'
print('\n json.load(jsonStr) : ',json.loads(jsonStr)
,'\n type(json.load(jsonStr)) : ',type(json.loads(jsonStr)))

#class-object -> json
class User(object) :
	def __init__(this, name, age, sex) :
		this.name = name
		this.age = age
		this.sex = sex
user = User('xiao ming', 18, 'female')
#print('\n json.dumps(user) : ',json.dumps(user))    #error
print('\n json.dumps(user, default = lambda obj : obj.__dict__) : ',json.dumps(user, default = lambda obj : obj.__dict__))

#print('\n usage of file :',dir(testFile1))

#print('\n usage of pickle :',dir(pick))

#print('\n usage of json :',dir(json))
