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



# In[20]:


#2: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional
#array. The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡-Y-1.

row= int(input('Enter number of rows: '))
col= int(input('Enter number of columns: '))
mixlist = [[0 for col in range(col)] for row in range(row)]

for i in range(row):
    for j in range(col):
        mixlist[i][j]= i*j

print(mixlist)


# In[21]:


n=int(input('How many elements you want in the list: '))
samplelist=[]
for i in range(n):
    str=input('Enter string: ')
    samplelist.append(str)
    
sorted(samplelist)
    

