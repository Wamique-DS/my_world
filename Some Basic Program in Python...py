
# coding: utf-8

# In[3]:


# prgogarm to find Area of circle

radius=eval(input("Enter the radius of circle ")) # eval takes any value either integer or float

# calculate area
area=radius*radius*3.14

# Display result
print("Area of circle of radius", radius,"is",round(area,2))


# In[8]:


# Program to find area of cirle

import math
r=float(input("Enter radius of a cirlce "))

# using import function
area=math.pi*math.pow(r,2)

# display result
print("Area of circle of radius",radius,"is",round(area,2))


# In[14]:


# Prgogram to find average of three numbers

a=eval(input("Enter the first number "))
b=eval(input("Enter the second number "))
c=eval(input("enter the third number "))

avg=(a+b+c)/3

print("Average of three number is",round(avg,3))
print("Average of ",a,b,c,"is",round(avg,2))


# In[19]:


str(12) # usde to convert int into string


# In[20]:


str(12.76)


# In[25]:


import random
# generate random number

num1=random.randint(0,9)
num2=random.randint(0,9)

answer=eval(input("what is "+str(num1)+ "+" + str(num2) + "?"))
print(num1, "+", num2, "=",answer,"is", num1+num2==answer)


# In[29]:


# Program to generate an OTP of 6 digit

from random import randint
for i in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))




# In[31]:


a = 2
print('id(a) =', id(a))
a = a+1
print('id(a) =', id(a))
print('id(3) =', id(3))
b = 2
print('id(2) =', id(2))


# In[51]:


x="mohammad wamique hussainmm"
len(x)
x.count('a')
x.count('k')
'i' in x
'p' in x
x.index('n')
#x.strip('m')
#x.strip('m')
x.strip('m')


# In[52]:


x="mohammad wamique hussainmm"
x.strip('m') # it strips all m from both start and end

