#!/usr/bin/env python
# coding: utf-8

# In[48]:


#5: Make a class named Practice, convert all the previous programs into functions and
#add them to the class and then access all four using an object of the class.

class Practice:
    
    def first(self):
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
        
    def second(self):
        row= int(input('Enter number of rows: '))
        col= int(input('Enter number of columns: '))
        mixlist = [[0 for col in range(col)] for row in range(row)]

        for i in range(row):
            for j in range(col):
                mixlist[i][j]= i*j

        print(mixlist)
        
    def third(self):
        n=int(input('How many elements you want in the list: '))
        samplelist=[]
        for i in range(n):
            str=input('Enter string: ')
            samplelist.append(str)

        print(sorted(samplelist))
        
    
    def fourth(self):
        str=input('Enter the sentence: ')
        str=str.split()
        str=sorted(str)
        str2=[]

        for i in str:

            if i not in str2:
                str2.append(i)

        for i in range(0,len(str2)):
            print(str2[i],':',str.count(str2[i]))
            

a=Practice()
print('\nExecuting first function...')
w=a.first()
print('\n\nExecuting second function...')
x=a.second()
print('\n\nExecuting third function...')
y=a.third()
print('\n\nExecuting fourth function...')
z=a.fourth()
        

