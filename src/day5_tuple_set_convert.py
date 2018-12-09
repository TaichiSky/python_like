###tuple,set

##tuple
#attributes:Once initialized, it cannot be modified

#init
tuple_a = (1,"hello",True)
list_a = [1,"hello",True]
print('type(tuple_a):',type(tuple_a)
,'\n type(list_a):',type(list_a))

#merge a new tuple
print()
tuple_b = (6.66,'world')
tuple_c = tuple_a + tuple_b
print('tuple_c:',tuple_c)

#tuple_a[0] = 2    #error

#go-language is also used
print()
x,y,z = 1,'hello',[1,False,6.66]
print('x = ',x,' ,y = ',y,' ,z = ',z)

#convert the list to cuple
print()
tuple_aa = tuple(list_a)
print('tuple_aa:',tuple_aa)

##set
print()
set_a = {1,"hello",None}
set_b = set([6.66,'hello',False,6.66])
dict_a = {'name':'dogsky','weight':'73kg'}
print('type(set_a):',type(set_a),' ,set_a:',set_a
,'\n type(set_b):',type(set_b),' ,set_b:',set_b
,'\n type(dict_a):',type(dict_a),' ,dict_a:',dict_a)

#non-repeatable and unordered
print()
set_c = {1,"hello",True,1,"hello",'world'}
print('set_c :',set_c)

#add,remove
print()
set_c.add(False)
print('after add set_c :',set_c) 
set_c.remove(1)
print('after remove set_c :',set_c)

#union and cross (|,&)
print()
print('set_a | set_b :',set_a | set_b)
print('set_a & set_b :',set_a & set_b)

##conversion between type

#str -> list
str_a = 'hello'
print('after str convert to list:',list(str_a))

#str -> tuple
print('after str convert to tuple:',tuple(str_a))

#list -> str
list_a = ['hello','world']
print()
print('after list convert to str:',"".join(list_a))
print('after list convert to tuple:',tuple(list_a))

#tuple -> str
tuple_a = ('java','python','go')
print()
print('after tuple convert to str:',"".join(tuple_a))
print('after tuple convert to list:',list(tuple_a))
