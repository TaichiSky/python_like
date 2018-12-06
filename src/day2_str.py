#str
print('type(\'hello\'):',type('hello'),'\n type("world"):',type("world"))

#strip()
print()
print('usage of strip():',' mmy name is python,'.strip().lstrip('m').rstrip(','))

#join,split,splitlines[按照换行符分割,参数决定返回是否包含换行符]
print()
print('"hello"+"world":','hello'+'world'
,'\n len("hello world"):',len('hello world')
,'\n ":".join("1111"):',':'.join('1111')
,'\n "hello-world-python".split("-"):',"hello-world-python".split("-")
,'\n "hello \\n world \\r\\n python".splitlines(False):',"hello \n world \r\n python".splitlines(False))

#index/rindex,find/rfind,partition/rpartition | left/right
print()
print('usage of index:','hello,world'.index('or') #若不存在会报异常
,'\n usage of find:','hello,world'.find('or')
,'\n usage of partition:','hello,world'.partition('or'))

#and,or
print()
print('usage of and:','123' and '456'
,'\n usage of or:','123' or '456')

#upper,lower,swapcase
print()
print('usage of upper:','heLlo'.upper()
,'\n usage of lower:','WORld'.lower()
,'\n beijing:','beijing'.capitalize()
,'\n swapcase:','HashMap'.swapcase())

#str_get,similar to [x,y)
print()
s = '0123456789'
print('s:',s,',s[::-1]',s[::-1])
print('s[2]:',s[2],',s[-8]:',s[-8]
,'\n s[0:3]:',s[0:3],',s[:3]:',s[:3],',s[0:-7]:',s[0:-7]
,'\n s[7:]:',s[7:],',s[-3:]:',s[-3:]
,'\n s[::2]',s[::2],',s[1::2]',s[1::2],',s[2::3]',s[2::3]
,'\n s[:4:1]',s[:4:1],',s[:4:2]',s[:4:2],',s[:7:3]',s[:7:3]
,'\n s[:-2:]',s[:-2:],',s[:-4:]',s[:-4:]    #逆序截取
,'\n s[::-2]',s[::-2],',s[::-3]',s[::-3],',s[::-4]',s[::-4]
,'\n s[:-4:-2]',s[:-4:-2],',s[:-3:-2]',s[:-3:-2],',s[:-2:-2]',s[:-2:-2]) #why?

#count
print()
print('usage of count:',"hellohelloworlddahello".count('hello'))

#startswith,endswith
print()
print('usage of startswith:',"helloworld".startswith('hello')
,'\n usage of endswith:',"helloworld".endswith('ld'))

#max,min
print()
print('usage of max:',max('helloworld')
,'\n usage of min:',min('helloworld')) #若有空格,则空格是最小的
