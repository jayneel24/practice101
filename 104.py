#!/usr/bin/env python
# coding: utf-8

# In[41]:


#4: Write a program to compute the frequency of the words from the input. The output
#should output after sorting the key alphanumerically.


str=input('Enter the sentence: ')
str=str.split()
str=sorted(str)
str2=[]

for i in str:
    
    if i not in str2:
        str2.append(i)
        
for i in range(0,len(str2)):
    print(str2[i],':',str.count(str2[i]))




    







