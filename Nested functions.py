#Wap to find factorial of 5.
'''def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(fact(5))'''

#Recursive function
'''def fact(n):
    print(f'computing factorial of {n}')
    if n==1:
        return 1
    return n*fact(n-1)

res=fact(5)
print(res)'''
#-------------------------------------------------
#Nested function
'''def outerfunc(x):
    print(x)

    def innerfunc():
        print('This is inner function')
        print(x)

    print('calling inner function')
    innerfunc()

outerfunc(10) '''
#----------------------------------------
#Closures
'''def outerfunc(a):

    def innerfunc(b):
        return a+b
    
    return innerfunc

add=outerfunc(10)

res=add(5)     #10+5
print(res)      #15

res2=add(20)  #10+20
print(res2)    #30'''


#2.
'''def multiply(a):

    def f2(b):
        return(a*b)
    return f2

m=multiply(20)
print(m(5))'''    #100
#================================================
# self-Practice Question 2 (Nested Function)

# Question:
# Write a function outer() that:
# Takes one string as input
# Inside it, define an inner function
# The inner function should:
# Print the string in uppercase
# Call the inner function from the outer function

'''def outer(s):
    def upper():
        return s.upper()
    return upper()

s1=outer('hello world')
print(s1)'''            #HELLO WORLD


# Sum of Two Numbers
# Task:Write a function add_outer(x) that defines a nested function add_inner(y) and prints the sum of x + y.

'''def add_outer(x):
    def add_inner(y):
        return x+y
    return add_inner

s=add_outer(10)
print(s(10))'''  #20

# Prefix Text
# Task:Write a function prefixer(pre) that returns a function which takes a string and adds pre before it.
'''def prefixre(x):
    def s1(str):
        return x + ' ' +str
    return s1

p=prefixre('hello')
print(p('guys'))'''  #hello guys
#-----------------------------------------------------------------
# Power Function
# Task:Write a function power(n) that returns an inner function which takes x and returns x ** n.

'''def power(n):
    def num(x):
        return x**n
    return num

square=power(2)  
cube=power(3)    
print(square(5))  #25
print(cube(5))'''  #125

# Advanced (Real Closure Usage)
#  Counter
# Task: Create a closure that keeps track of how many times it was called
'''def counter(n):
    li=[1,1,2,3,5,5]
    def f1():
        cnt=0
        for num in li:
            if num==n:
                cnt+=1
        
        return cnt
    return f1
c=counter(1)
c1=counter(5)
print(c())  #2
print(c1())'''#2
#--------------------------------------
# Task:Write a function logger(msg) which returns a function that prints "[LOG] {msg}: {value}" when called with value.
'''def logger(msg):
    def value(v):
        return f"[Log]'{msg}:{v}"
    return value

m=logger('Price')
print(m(100))'''   #[Log]'Price:100
#-----------------------------------------
# String Length
# Write a function outer(s) that:
# Defines an inner function
# Prints the length of the string s
# Calls the inner function        
'''def outer(s):
    def find_length():
        return len(s)
    return find_length

str1=outer('Academy')
print(str1())  '''      #7
#---------------------------------------------------
# Print Message
# Write a function outer() that:
# Prints "Outer function"
# Defines an inner function that prints "Inner function"
# Calls the inner function
'''def outer():
    m= 'Outer function'
    def inner():
     return m
    return inner
    
o=outer()    
print(o()) '''           #Outer function
#----------------------------
