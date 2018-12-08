#list
lista = [1,'hello',2.3,None,False]
print('type(lista):',type(lista),'\n lista:',lista
,'\n the length of list is :',len(lista))

#query
print('lista[1]:',lista[1],',\n lista[:2]:',lista[:2]
,'\n lista[2:]:',lista[2:],'\n lista[:]:',lista[:])

#update
lista[4] = "world"
print('after assign the "world1" on index of 4:',lista)    #若原位置有元素,则会被替换掉
#lista[5] = 'java'    #index out of range

#insert
lista.insert(3, 'java')
print('after insert the element:',lista)

#append
lista.append("False")
print('after append the "False":',lista)

print('list + list:',lista + ['python'])

#del
del lista[-2:]
print('after delete the element:',lista)

#pop
lista.pop(4)
print('after delete the element:',lista)    #default pop the last one

#for
for index,element in enumerate(lista):
	print('lista[',index,'] = ',element)
	
#count
lista.append('hello')
print('lista:',lista,
'\n the count of "hello":',lista.count('hello'))
#index
print('the index of "hello":',lista.index('hello')) #return the first happen location

#sort
list_number = ['java','python','go','scala']
list_number.sort()    #desc:reverse=True
print('after sort of list_number:',list_number)
