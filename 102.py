#!/usr/bin/env python
# coding: utf-8

# In[20]:

row= int(input('Enter number of rows: '))
col= int(input('Enter number of columns: '))
mixlist = [[0 for col in range(col)] for row in range(row)]

for i in range(row):
    for j in range(col):
        mixlist[i][j]= i*j

print(mixlist)

