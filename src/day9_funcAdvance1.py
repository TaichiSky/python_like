#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'advanced features of the function'

_author_ = 'dogsky'

import os

###generate list formula

list_a = range(11)
print('list = ',list(list_a))

#compute the square of each number(List or tuple)
print()
list_aa = [x * x for x in list_a]
print('x*x of list = ',list_aa)

#list odd of 1-10
print()
list_odd = [x for x in list_a if x % 2 == 1]
print('odd of 1-10 = ',list_odd)

#convert list_a to str of list
print()
list_as = map(str, list_a)
print('convert list_a to str of list = ',[x for x in list_as])

#combination of str
print()
comStr1 = 'abc'
comStr2 = '123'
list_combin = [x + y for x in comStr1 for y in comStr2]
print('combination of comStr1 to comStr2 = ',list_combin)

#list of map
print()
map_info = {'name':'luckydog','height':'178cm','hobby':'swimming'}
list_info = [k + '=' + v for k, v in map_info.items()]
print('list of map_info = ',list_info)

#list the files and directories under the current location
print()
list_dirFile = [dirFile for dirFile in os.listdir('.')]
print('list the files and directories = ',list_dirFile)

##map | map(op, value)
print()
def func1 (n) :
	return n * 2 -1
test_list = range(1,11)
print('after map(func1, test_list) = ',list(map(func1, test_list)))

##filter
print()
def is_odd(n) :
	return n % 2 == 1
print('filter(is_odd, list_a) = ',list(filter(is_odd, list_a))
,'\n map(is_odd, list_a) = ',list(map(is_odd, list_a)))

##sorted/sort
print()
list_sort1 = [66,12, 6, -12, 9, -21]
list_sort1.sort()
list_sort2 = [66,12, 6, -12, 9, -21]
print('after list_sort1.sort() = ',list_sort1
,'\n after sorted(list_sort2) = ',sorted(list_sort2)
,'\n after sorted(list_sort2, key = abs) = ',sorted(list_sort2, key = abs))

print()
list_sortA = ['bob', 'about', 'Zoo', 'Credit']
print('after sorted(list_sortA) = ',sorted(list_sortA)
,'\n after sorted(list_sortA, key = str.lower) = ',sorted(list_sortA, key = str.lower)
,'\n after sorted(list_sortA, key = str.lower, reverse = True) = ',sorted(list_sortA, key = str.lower, reverse = True))
