# -*- coding: utf-8 -*-
"""18-37918-2-week-1-v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XkEClQeKoksFgjeXSh4UvIvZ1NHMaAHU

# Name: Md. Jamil Istiaq, Id: 18-37918-2, Sec:F, week-1 v2

Number example
"""

a= 23
b=4.3
c=5
a+b

a-b

a*b

a/b-c

a+b+c

"""import math
math.pi
math.sqrt(a)

sqrt of the sum of a and b
"""

math.sqrt(a+b)

import random

random.random()

random.choice([1,3,5])

a**2

"""mod of b

math.modf(b)

sin value for the sum a and b
"""

math.sin(a+b)

"""sting examples"""

st= 'IEEE AIUB Student Branch'

st

"""length of the string"""

len(st)

"""last letter"""

st[-1]

st[1:-3]

st[-6:]

"""concate new word"""

st + ' R10'

"""find a word in the string"""

st.find('dent')

"""replace a word"""

st.replace('IEEE','ieee')

"""Immutability"""

st='J'+st[1:]

st

st.split(' ')

st.upper()

st.lower()

"""how many string are there"""

st.count(st)

st.isalpha()

"""list example"""

list=[1,2.3, 'jamil', 'ai', 'cs', 'ieeer10']
len(list)

list[0]

list[2]

"""add new iteam in list"""

list+['aiub', 'cse']

len(list)

list.append('aiub')

len(list)

list

"""delete last one """

del list[-1]

list

"""matrix"""

mat=[[1,2,3],['a','b','c'],[4,5,7]]

mat

mat[1]

mat[1][2]

"""dictionary"""

dis={'name':'jamil', 'id':'18-37918-2','dept':'CSE'}

dis

dis['name']

dis={'a':'10','x':'12','y':'14','z':'15'}

"""print keys"""

d=dis.keys()
d

for key in d:
    print(key,'=>',dis[key])

for key in sorted(d):
    print(key,'=>',dis[key])

"""squre all value in a list """

sq=[x**2 for x in [2,4,6]]
sq

"""touple"""

t=(2,3,5,7,8,9)
len(t)

"""Function Home Work

define a function cal_add(), it take two parameter for sum, we gave two value and return the sum. finaly printout the result.
"""

def cal_add(x,y):
    sum=x+y
    return sum
a=3
b=7

print('The Sum is',cal_add(a,b))

"""file """

f=open('ai.txt','w')

f.write('Hello, This is the first lab\n')

f.write('Name: Md. Jamil Istiaq\n')

f.close()

f=open('ai.txt')
bytes=f.read()
bytes

print(bytes)

bytes.split()

bytes.upper()