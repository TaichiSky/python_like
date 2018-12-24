#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'threading'

__author__ = 'dogsky'

import threading

#print('\n usage of threading :',dir(threading))

#create thread
class PrintThreadName(object) :
	print('PrintThreadName current thread is : ',threading.current_thread().name)

def PrintThreadName1() :
	print('PrintThreadName1 current thread is : ',threading.current_thread().name)

def PrintThreadName2() :
	print('PrintThreadName2 current thread is : ',threading.current_thread().name)

thread1 = threading.Thread(target=PrintThreadName1)
thread2 = threading.Thread(target=PrintThreadName2)
thread = threading.Thread(target=PrintThreadName)

thread1.start()
thread2.start()
thread.start()

thread1.join()
thread2.join()
thread.join()

#lock
money = 10
####无效的模拟
#def saveMoney() :
#	global money
#	money = money + 10
#def getMoney() :
#	global money
#	money = money - 10
#for i in range(10000) :
#	t1 = threading.Thread(target=saveMoney)
#	t1.start()
#	t1.join()
#for i in range(10000) :
#	t2 = threading.Thread(target=getMoney)
#	t2.start()
#	t2.join()

#此测试下,会出现线程不同步问题
def operate_money(n) :
	global money
	money = money + n
	money = money - n

def create_thread(n) :
	for i in range(100000) :
		operate_money(n)

#improved
lock = threading.Lock()
def create_thread_security(n) :
	for i in range(100000) :
		lock.acquire()
		try :
			operate_money(n)
		finally :
			lock.release()
			
t1 = threading.Thread(target=create_thread, args=(5,))
t2 = threading.Thread(target=create_thread, args=(6,))

#t1 = threading.Thread(target=create_thread_security, args=(5,))
#t2 = threading.Thread(target=create_thread_security, args=(6,))

t1.start()
t2.start()
t1.join()
t2.join()

print('finally, money = ',money)
