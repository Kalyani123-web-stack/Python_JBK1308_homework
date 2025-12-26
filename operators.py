#Perform Arithmatic  operation on all data types.
#Fundamental data types
#1.int(supported arithmetic)
'''a=10
b=3

print(a+b)  #13
print(a-b)  #7 
print(a*b)  #30
print(a/b)  #3.33
print(a%b)  #1  (gives remainder)
print(a//b)'''  #3  (gives quotient)
#-------------------------------------------
#2.float(supported arithmetic)
'''x=10.5
y=2.0

print(x+y)  #12.5
print(x-y)   #8.5
print(x*y)   #21.0
print(x/y)   #5.25
print(x%y)   #0.5
print(x//y)'''  #5.0
#--------------------------------------------
#3.int+float(supported;result is always float)
'''a=10
b=2.5

print(a+b) #12.5
print(a-b) #7.5
print(a*b)  #25.0
print(a/b)  #4.0
print(a%b)  #0.0
print(a//b) '''#4.0
#------------------------------------------------
#4.Complex
'''a=2+3j
b=1+1j

print(a+b) #(3+4j)
print(a-b) #(1+2j)
print(a*b) #(-1+5j)
print(a-b) #(1+2j)
print(a/b) #(2.5+0.5j)
print(a%b) #not supported
print(a//b)''' #not supported
#----------------------------------------------
#5.bool
'''print(True+True) #2
print(True+False) #1
print(False*5) '''  #0
#====================================================
#Collective Data Types
#1.string 
# addition-str1+str2 --->concatination of 2 strings
'''str1='Welcome'
str2='python batch'
res=str1 +' '+ str2
print(res) '''                 #Welcome python batch

#---------------------------------
#2.List 
# addition-l1+l2 --->first list appendes to second list
'''l1=[10,20,30]
l2=[20,30,40]
res=l1+l2
print(res)                 #[10, 20, 30, 20, 30, 40]


#subtraction-l1-l2 --->not supported
res1=l1-l2
print(res1)                #TypeError: unsupported operand type(s) for -: 'list' and 'list'


#multiplication-l1*l2 --->not supported
res2=l1*l2
print(res2)'''               #TypeError: unsupported operand type(s) for -: 'list' and 'list'

#---------------------------------------------------------
#3.Tuple
#addition-t1+t2 --->concatination of 2 tuples
'''t1=(1,2,3)
t2=(4,5,6)
# res=t1+t2
# print(res)          #(1, 2, 3, 4, 5, 6)

#subtraction-t1-t2 --->not supported
# res2=t1-t2
# print(res2)         #TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'

#multiplication-t1*t2 --->not supported
# res3=t1*t2
# print(res3)         #TypeError: unsupported operand type(s) for *: 'tuple' and 'tuple'

#multiplication-t1*2 --->repeats the tuple twice
print(t1*2)    '''        #(1, 2, 3, 1, 2, 3)
#-------------------------------------------------------
#4.Set
# s1={10,20,30}
# s2={40,50,10}
#addition
'''res1=s1+s2
print(res1)  '''          #TypeError: unsupported operand type(s) for +: 'set' and 'set'

#subtraction-
'''res2=s1 - s2         #removes common elements from s1
print(res2)'''            #{20, 30}

'''res3=s2-s1              #removes common elements from s2
print(res3) '''              #{40, 50}

#multiplication
'''res4=s1 *s2
print(res4) '''             #TypeError: unsupported operand type(s) for *: 'set' and 'set'
#---------------------------------------------------------
#5.Dictionary
# d1={'a':100,'b':200}
# d2={'c':300,'d':400}
#addition
'''res1=d1+d2
print(res1)  '''            #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

#subtraction
'''res2=d1 - d2
print(res2) '''             #TypeError: unsupported operand type(s) for -: 'dict

#multiplication
'''res3=d1 * d2
print(res3) '''               #TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
#-----------------------------------------------------
#6.bytes and bytearray
'''b1=bytes([65,66,67,68])
b2=bytes([69,70,71,72])

#addition-concatination of 2 bytes
res1=b1 + b2
print(res1)                  #b'ABCDEFGH'

#subtraction-not supported
res2=b1 - b2
print(res2)                 #TypeError: unsupported operand type(s) for -: 'bytes' and 'bytes'

#multiplication-not supported
res3=b1 * b2
print(res3)'''                 #TypeError: unsupported operand type(s) for *: 'bytes' and 'bytes'

#----------------------------------------------------
'''by1=bytearray([65,66,67])
by2=bytearray([68,69,70])

#addition-concatination of 2 bytearray
res1=by1 + by2
print(res1)                  #bytearray(b'ABCDEF')

#subtraction-not supported
res2=by1 - by2
print(res2)                 #TypeError: unsupported operand type(s) for -: 'bytearray' and 'bytearray'

#multiplication-not supported
res3=by1 * by2
print(res3)'''                 #TypeError: unsupported operand type(s) for *: 'bytearray' and 'bytearray'
#-----------------------------------------------------
#7.range
# r1=range(10)
# r2=range(20)

#addition
'''res1=r1+r2
print(res1)  '''          #TypeError: unsupported operand type(s) for +: 'range' and 'range'

#subtraction
'''res2=r1-r2
print(res2)'''              #TypeError: unsupported operand type(s) for -: 'range' and 'range'

#multiplication
'''res3=r1*r2
print(res3) '''             #TypeError: unsupported operand type(s) for *: 'range
#-------------------------------------------------------------------
#8.none data type
'''var1=None
var2=None

#addtion
res1=var1 + var2
print(res1)'''                #TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
#===============================================================================================
#Summary Table
# + = Addition, - = Subtraction, * = Multiplication, / = Division

# Data Type   |  +  |  -   |  *  |  /  |  %   |  //
# --------------------------------------------------
# int         |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔
# float       |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔
# complex     |  ✔  |  ✔  |  ✔  |  ✔  |  ✖  |  ✖
# bool        |  ✔  |  ✔  |  ✔  |  ✔  |  ✔  |  ✔
# string      |  ✔  |  ✖  |  ✔  |  ✖  |  ✖  |  ✖
# list        |  ✔  |  ✖  |  ✔  |  ✖  |  ✖  |  ✖
# tuple       |  ✔  |  ✖  |  ✔  |  ✖  |  ✖  |  ✖
# set         |  ✖  |  ✔  |  ✖  |  ✖  |  ✖  |  ✖
# dict        |  ✖  |  ✖  |  ✖  |  ✖  |  ✖  |  ✖
# bytes       |  ✔  |  ✖  |  ✔  |  ✖  |  ✖  |  ✖
# bytearray   |  ✔  |  ✖  |  ✔  |  ✖  |  ✖  |  ✖
# range       |  ✖  |  ✖  |  ✔  |  ✖  |  ✖  |  ✖
# NoneType    |  ✖  |  ✖  |  ✖  |  ✖  |  ✖  |  ✖

# Key Memory Tips (Very Important)
#Only numeric types fully support / % //.
#complex does not support % and //.
#Sequence types (str, list, tuple, bytes, bytearray):
'''+ → concatenation
* → repetition'''
#set:Only - (difference) works
#NoneType:No arithmetic operations at all
