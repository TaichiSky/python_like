#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'OOP(Object-Oriented Programming)'

__author__ = 'dogsky'

##class

class Student(object) :

	def __init__(self) :
		self.name = 'xiao ming'
		self.age = 21
	
	def printStudentInfo(self) :
		print('name = ',self.name,'\n age = ',self.age)
	
	#set和get的属性不是必须的,但是是优秀的体现
	def setName(self, name) :
		self.name = name
	def setAge(self, age) :
		self.age = age
	def getName(self) :
		return self.name
	def getAge(self) :
		return self.name
		
student = Student()
student.printStudentInfo()

##继承(支持多继承)
print()
class SexStudent(Student) :
	def __init__(self, sex) :
		self.name = 'xiao hong'
		self.age = 23
		self.__sex = sex	#private attribute
		self.__birthday = '2001-10-06'
		
	#注掉此方法,会调用父类方法输出结果
	def printStudentInfo(self) :
		print('name = ',self.name,'\n age = ',self.age,'\n sex = ',self.__sex)
	#此处省略set和get属性的方法，不是必须的(用java描述就是：省略setter和getter方法)
sexStudent = SexStudent('female')
sexStudent.printStudentInfo()

#get private attribute
sexStudent1 = SexStudent('female')
#print('\n birthday = ',sexStudent1.birthday)    #no attribute
print('\n birthday = ',sexStudent1._SexStudent__birthday)    #normal print

#improved of get private attribute
if hasattr(sexStudent1, 'birthday') :
	print('get birthday = ',getattr(sexStudent1, 'birthday'))
elif hasattr(sexStudent1, '_SexStudent__birthday') :
	print('get _SexStudent__birthday = ',getattr(sexStudent1, '_SexStudent__birthday'))

#View class
if isinstance(sexStudent1, Student) :
	print('\n dir(sexStudent1) : ',dir(sexStudent1))
	
#相同名称的实例属性将屏蔽掉类属性

##动态绑定属性或方法
def setHobby(self, hobby) :
	self.hobby = hobby
SexStudent.setHobby = setHobby
sexStudent.setHobby('swimming')
print('\n sexStudent_hobby = ',sexStudent.hobby)
#print('\n sexStudent1_hobby = ',sexStudent1.hobby)    #no attribute

sexStudent1.setHobby('ping-ponng')
print('\n sexStudent1_hobby = ',sexStudent1.hobby)
