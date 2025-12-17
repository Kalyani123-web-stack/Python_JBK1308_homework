'''s=set()
print(s)
print(type(s))

#add method
s.add(10)
s.add(20)
s.add(30)
s.add(60)
s.add(20)
print(s)      #{10, 20, 30, 60}

#remove() method
s.remove(60)
print(s)'''  #{10, 20, 30}
#---------------------------
#add 2 set together using update()method
s1={10,5,8,3,'z'}
s2={'hi','g','z'}
# s1.update(s2)
# print(s1)          #{3, 'hi', 5, 'g', 8, 10, 'z'}

#union()
# s1.union(s2)  
# print(s1)           #{3, 'hi', 5, 'g', 8, 10, 'z'}

#print(s2.union(s1))   #{3, 'hi', 5, 'g', 8, 10, 'z'}

#------------------------------------------
#intersection(),& operator-to find common elements
# print(s1.intersection(s2))  #{'z'}
# print(s1 & s2)    #{'z'}
#--------------------------------------
#difference()-to find elements present in s1 but not in s2
# print(s1.difference(s2))          #{8, 10, 3, 5}
#-------------------------------------------------
#symmetric_difference()-elements present in s1 and s2 but not in both
# print(s1.symmetric_difference(s2))   {3, 'hi', 5, 'g', 8, 10}

#------------------------------------------------
#frozenset()
'''fs1=frozenset([1,2,3])
print(fs1)        #frozenset({1, 2, 3})
print(type(fs1))  #<class 'frozenset'>

a = frozenset({1, 2, 3})
b = frozenset({3, 4})
print(a.union(b))                #frozenset({1, 2, 3,4})
print(a.intersection(b)) '''        # frozenset({3})
#-----------------------------------------------------------
#try to add tuple and list in set
s={1,2,3}
# s.add((4,'hi',9))
# print('Add tuple in set:',s)      #{1, 2, 3, (4, 'hi', 9)}

s.add(['a','b'])

print('Add list in set:',s)       #TypeError: unhashable type: 'list'
