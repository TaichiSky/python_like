#dir(__builtins__)    #view BIF list
#help(cmd-key)    #view usage

#View system modules and path
#import sys
#print(sys.modules.keys())
#print(sys.path)

#import modules
import time as t
import math as m

#init
a,b,c,f,g = 5,2,-2,-1,-5
h,i = 6.66,-6.66
d,e = complex(c),complex(1,c)

#int,float,complex
print('a = ',a,' ,type(a) = ',type(a)
,'\n i = ',i,' ,type(i) = ',type(i)
,'\n d = ',d,' ,e = ',e,' ,type(d) = ',type(d))

#built-in function
print()
print('abs(c) = ',abs(c)    #can be used for complex-type
,'\n divmod(a,b) = ',divmod(a,b)
,'\n divmod(a,c) = ',divmod(a,c)
,'\n pow(a,b) = ',pow(a,b)
,'\n pow(a,f) = ',pow(a,f)
,'\n round(i,abs(f)) = ',round(i,abs(f))
,'\n list(range(b,a)) = ',list(range(b,a)))

##math
#ceil,floor
print()
print('m.ceil(h) = ',m.ceil(h)
,'\n m.floor(h) = ',m.floor(h))

#fabs,copysign,factorial
print()
print('m.fabs(c) = ',m.fabs(c)    #can't be used for complex-type
,'\n m.copysign(a,f) = ',m.copysign(a,f)
,'\n m.factorial(5) = ',m.factorial(5))

#fmod,%
print()
print('a =',a,' ,g=',g,' ,b=',b,' ,c=',c
,'\n m.fmod(a,b) = ',m.fmod(a,b)
,'\n m.fmod(a,c) = ',m.fmod(a,c)
,'\n m.fmod(g,b) = ',m.fmod(g,b)
,'\n m.fmod(g,c) = ',m.fmod(g,c)
,'\n a % b = ',a % b
,'\n a % c = ',a % c
,'\n g % b = ',g % b
,'\n g % c = ',g % c
,'\n h =',h,' ,i=',i,' ,b=',b,' ,c=',c
,'\n m.fmod(h,b) = ',m.fmod(h,b)
,'\n m.fmod(h,c) = ',m.fmod(h,c)
,'\n m.fmod(i,b) = ',m.fmod(i,b)
,'\n m.fmod(i,c) = ',m.fmod(i,c)
,'\n h % b = ',h % b
,'\n h % c = ',h % c
,'\n i % b = ',i % b
,'\n i % c = ',i % c)

#modf,trunc
print()
print('m.modf(h) = ',m.modf(h)
,'\n m.modf(i) = ',m.modf(i))
print('m.trunc(h) = ',m.trunc(h)
,'\n m.trunc(i) = ',m.trunc(i))

#frexp,ldexp
print()
print('m.frexp(a) = ',m.frexp(a)    #result = (x,y) => a = x*(2**y)
,'\n m.ldexp(0.6225,3) = ',m.ldexp(0.625,3))    

#gcd,isfinite
print()
print('m.gcd(32,40) = ',m.gcd(32,40))    #max common divisor
print('m.isfinite(f) = ',m.isfinite(f))

#fsum
print()
list_a = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
print('sum(list_a) = ',sum(list_a)
,'\n m.fsum(list_a) = ',m.fsum(list_a))

#exp,expm1 | expm1 = exp - 1
print()
print('m.exp(0) = ',m.exp(0)
,'\n m.exp(1) = ',m.exp(1)
,'\n m.e = ',m.e
,'\n m.expm1(0) = ',m.expm1(0)
,'\n m.expm1(1) = ',m.expm1(1))

#log(x,base),log2,log10,log1p | math.log1p(x)=math.log(x+1,math.e)
print('m.log(m.e,m.e) = ',m.log(m.e,m.e)
,'\n m.log(1,m.e) = ',m.log(1,m.e)
,'\n m.log(1/m.e,m.e) = ',m.log(1/m.e,m.e)
,'\n m.log(8,2) = ',m.log(8,2)
,'\n m.log2(8) = ',m.log2(8)
,'\n m.log(1000,10) = ',m.log(1000,10)
,'\n m.log10(1000) = ',m.log10(1000))

#pow,sqrt
print()
print('m.pow(m.e,0) = ',m.pow(m.e,0)
,'\n m.pow(2,m.log2(m.e)) = ',m.pow(2,m.log2(m.e))
,'\n m.sqrt(16) = ',m.sqrt(16))    #m.sqrt(-1) : match domain error

#PI
print('\n m.pi = ',m.pi)
