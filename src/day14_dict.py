#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'dict'

_author_ = 'dogsky'

#init
dict_info = {'name':'dogsky','info':{'height':178.0,'weight':'73kg','skill':'java'}}

#tuple
print('type((1,2,3)):',type((1,2,3)))

#get
print()
print(type(dict_info),
'\n name is :',dict_info['name']
,'\n info is :',dict_info['info']
,'\n skill is :',dict_info.get('info').get('skill')
,'\n weight is :',dict_info['info']['weight'])

#determine if an element exists
print()
if ('hobby' in dict_info.keys()) :
	print('hobby :',dict_info.get('hobby'))
else :
	print('no key of "hobby" in dict_info!')

#key,value
print()
print('keys:',dict_info.keys()
,'\n values:',dict_info.values())

#key
print()
for key in dict_info.keys() :
	print('key : {}'.format(key))
	if 'info' == key :
		for key_internal in dict_info.get(key).keys() :
			print('key_internal : {}'.format(key_internal))

#value
print()
for value in dict_info.values() :
	print('value : {}'.format(value))
	if dict == type(value) :
		for value_internal in value.values() :
			print('value_internal : {}'.format(value_internal))

#key-value
print()
for key,value in dict_info.items() :
	print(key,'==',value)
	if 'info' == key :
		for key_inter,value_inter in dict_info[key].items() :
			print(key_inter,'==',value_inter)

#convert to tuple and print
print()
print('after converting to an array:')
for (index,item) in enumerate (dict_info.items()) :
	print('index:',index,',item is:',item)    #print the type is tuple
	if (1 == index) :
		for (index_internal,item_internal) in enumerate(item[1].items()) :
			print('index_internal:',index_internal,',item_internal:',item_internal)

#pop
print()
dict_info.pop('info')
print('after pop("info") :',dict_info)

#setdefault
print()
dict_info['sex'] = 'female'
dict_info.setdefault('hobby','swimming')
print('after set key :',dict_info)

#popitem
print()
dict_info.popitem()
print('after popitem :',dict_info)
