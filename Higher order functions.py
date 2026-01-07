# test_marks=[67,87,77,99,56,76]
# grace_marks=[]
'''for i in test_marks:
    i=i+5
    grace_marks.append(i)
print(grace_marks)'''

#using function
# def addfive(n):
#     return n+5

# test_marks=[67,87,77,99,56,76]
# grace_marks=[]

# for i in test_marks:
#         m=addfive(i)
#         grace_marks.append(m)
   
# print(grace_marks)

#using map() function
'''test_marks=[67,87,77,99,56,76]
grace_marks=list(map(addfive,test_marks))
print(grace_marks)'''
#-----------------------------------------------
#filter() function
'''test_marks=[67,87,77,99,56,76]

def topper(marks):
    return marks>85

topper_l=list(filter(topper,test_marks))
#topper2=list(map(topper,test_marks))
print(topper_l)
#print(topper2)'''
#--------------------------------------
#reduce() function
# from functools import reduce
# test_marks=[67,87,77,99,56,76]

'''def addtwo(a,b):
    return a+b

sum=reduce(addtwo,test_marks)
print(sum) '''    #462

'''def fmax(a,b):
    if a>b:
        return a
    else:
        return b
    
max_num=reduce(fmax,test_marks)
print(max_num)'''

'''def fmin(a,b):
    if a<b:
        return a
    else:
        return b
    
min_num=reduce(fmin,test_marks)
print(min_num)'''
#------------------------------------------------------
#self practice questions:
# Part 1: map() 

# 1. Square Numbers
# Given a list: nums = [1, 2, 3, 4, 5]
# Use map() to create a new list of squares.
'''nums = [1, 2, 3, 4, 5]
def square(n):
    return n*n

sq_l=list(map(square,nums))
print(sq_l)'''               #[1, 4, 9, 16, 25]
#----------------------------------------------------
#2.convert to uppercase.
'''names = ["python", "java", "c"]
def upper(name):
    return name.upper()

upper_name=list(map(upper,names))
print(upper_name)'''             #['PYTHON', 'JAVA', 'C']
#------------------------------------------
#3.Add 10 to each no.
'''nums = [5, 10, 15]
def add10(n):
    return n+10

new_num=list(map(add10,nums))
print(new_num) '''               #[15, 20, 25]
#--------------------------------------------
#4.Length of string
'''words = ["apple", "banana", "cherry"]
def find_length(w):
    return len(w)

new_words=list(map(find_length,words))
print(new_words)'''              #[5, 6, 6]
#===========================================================
#filter()

#5.Even Numbers
# nums = [1,2,3,4,5,6,7,8]
# Use filter() to get only even numbers.
'''nums = [1,2,3,4,5,6,7,8]
def even(n):
    if n%2==0:
        return n
even_l=list(filter(even,nums))
print(even_l) '''          #[2, 4, 6, 8]
#--------------------------------------------------
#6.Numbers greater than 10.
'''nums = [5, 12, 3, 20, 7, 15]
def greater_ten(n):
    return n>10

new_num=list(filter(greater_ten,nums))
print(new_num) '''      #[12, 20, 15]
#--------------------------------------
#7. Words Longer Than 4 Characters
'''words = ["cat", "tiger", "lion", "elephant"]
def longer_words(w):
    return len(w)>4

long_w=list(filter(longer_words,words))
print(long_w) '''             #['tiger', 'elephant']
#--------------------------------------------------
#8. Positive Numbers
'''nums = [-3, 4, -1, 6, -8, 2]
def positive_num(n):
    return n>0

new_l=list(filter(positive_num,nums))
print(new_l)'''        #[4, 6, 2]
#=================================================
#reduce()

#from functools import reduce

# 9.Sum of All Numbers
'''nums = [1, 2, 3, 4, 5]
def total(a,b):
    return a+b

sum=reduce(total,nums)
print(sum)'''            #15
#--------------------------------------------------------
# 10.Product of Numbers
'''nums = [1, 2, 3, 4]
def product(a,b):
    return a*b

pr=reduce(product,nums)
print(pr)'''             #24
#-------------------------------------------
# Combine map + filter + reduce
# Sum of Squares of Even Numbers
# Given:nums = [1,2,3,4,5,6]
# Use filter() → even numbers
# Use map() → square them
# Use reduce() → sum them
'''from functools import reduce

nums = [1,2,3,4,5,6]
def even(n):
    if n%2==0:
        return n
    
def square(n):
    return n*n

def sum(a,b):
    return a+b
    
even_nums=list(filter(even,nums))
square_list=list(map(square,even_nums))
even_sum=reduce(sum,square_list)

print(f'Even list:{even_nums}')              #Even list:[2, 4, 6]
print(f'Even_Square list:{square_list}')     #Even_Square list:[4, 16, 36]
print(f'Sum_of_square:{even_sum}')   '''        #Sum_of_square:56

