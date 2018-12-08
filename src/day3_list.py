#list
lista = [1,'hello',2.3,None,False]
print('type(lista):',type(lista),'\n lista:',lista
,'\n the length of list is :',len(lista))

#query
print()
print('lista[1]:',lista[1],',\n lista[:2]:',lista[:2]
,'\n lista[2:]:',lista[2:],'\n lista[:]:',lista[:])

#update
print()
lista[4] = "world"
print('after assign the "world1" on index of 4:',lista)    #若原位置有元素,则会被替换掉
#lista[5] = 'java'    #index out of range

#insert
print()
lista.insert(3, 'java')
print('after insert the element:',lista)

#append
print()
lista.append("False")
print('after append the "False":',lista)

print('list + list:',lista + ['python'])

#del
print()
del lista[-2:]
print('after delete the element:',lista)

#pop
print()
lista.pop(4)
print('after delete the element:',lista)    #default pop the last one

#for
print()
for index,element in enumerate(lista):
	print('lista[',index,'] = ',element)
	
#count
print()
lista.append('hello')
print('lista:',lista,
'\n the count of "hello":',lista.count('hello'))
#index
print()
print('the index of "hello":',lista.index('hello')) #return the first happen location

#sort
print()
list_number = ['java','python','go','scala']
list_number.sort()    #desc:reverse=True
print('after sort of list_number:',list_number)
