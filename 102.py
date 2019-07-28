#!/usr/bin/env python
# coding: utf-8

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

