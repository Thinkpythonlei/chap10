# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 01:02:53 2023

@author: Surface
"""

#10.1/10.2/10.3/10.4/10.5/10.6/10.7/10.11/10.8/10.9

#10.1
def nested_sum(t):
    a=t[:]
    for i in range(len(a)):
        if isinstance(a[i],list):
             a[i]=nested_sum(a[i])
    return sum(a)

t = [[1 , 2] , [3] , [4 , 5 , 6]]
print(nested_sum(t))

#10.2
c=[1,2,3,4]
def cumsum(c):
    for i in range(len(t)):
        c[i]=sum(c[:i+1])
print(cumsum(c))

#10.3
t1=[1,2,3,4,5,6,7,8]
def middle(t1):
    n=len(t1)
    return t1[1:(n-1)]
print(middle(t1))

#10.4
t2=[10,11,12,13,14,15]
def chop(t):
    del t[0]
    del t[-1]
    return t
print(chop(t2))

#10.5
def is_sorted(t):
    a=t[:]
    a.sort()
    if t==a:
        return True
    else:
        return False
b=["a","b","c"]
print(is_sorted(b))

#10.6
x="abcdef"
y="fedcba"
def is_anagram(x,y):
    if set(list(x))==set(list(y)):
        return True
    else:
        return False
print(is_anagram(x, y))

#10.7
lst=[1,2,2,3,4,5,6,7,7,8,9]
new_list=[]
 
for i in lst:
    if i not in new_list:
        new_list.append(i)
        #这样能确保新的列表里包含原列表里所有种类的元素，且元素互不重复
 
if new_list==lst:
   print(False)
else:
   print(True)

#10.8
import numpy as np
index = np.random.randint(1, 365, 23)
def ten_times(index,n):
    n=1
    while n<10:
        print(index)
        n+=1
        
print(ten_times(index,10))

#10.9
with open("C:\words.txt",encoding="utf-8") as fin:
    content=fin.readlines()
#读取文本
new=[]
for x in content:
    first=x.strip("\n")
    new.append(first)
print(new)

with open("C:\words.txt",encoding="utf-8") as fin:
    content=fin.readlines()
#读取文本
new=[]
for x in content:
    first=x.strip("\n")
    new+=[x]
print(new)



#10.11
string1 = "abcd"
string2 = "dcba"
def is_reverseword(string1,string2):
    list1 = list(string1)
    list1.reverse()
    string3 = ''.join(list1)
    if string3==string2:
        print("string1 and string2 is reverse word")
    else:
        print("string1 and string2 is not reverse word")
print(is_reverseword(string1,string2))




























