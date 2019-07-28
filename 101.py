#!/usr/bin/env python
# coding: utf-8

# In[6]:


#1:  Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]

import math
C=50
H=30
Q=[]
D=[]

x=int(input('How many elements you want in the list: '))
for i in range(x):
    y=int(input('Enter number: '))
    D.append(y)

for i in range(len(D)):
    n=math.sqrt((2*C*D[i])/H)
    Q.append(int(n))
    
print('\n',Q)






    

