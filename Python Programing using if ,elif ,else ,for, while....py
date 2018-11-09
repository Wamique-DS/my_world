
# coding: utf-8

# In[3]:


# use of one way if statement
import math
radius=eval(input("Enter radius of circle"))
if radius>=0:
    area=radius**2*math.pi
    print("Area of circle",area)


# In[7]:


# use of two way if statment

from math import pi
radius = eval(input("Enter radius of circle "))
if radius>=0:
    area=radius*radius*pi
    print("Area of circle",round(area,2))
else:
    print("negative input")


# In[12]:


# Check for leap years

year=eval(input("Enter a year"))

# cheak if year is leap
isLeapYear=(year%4==0 and year%100!=0 or year%400==0)

# dispaly result
print(year,"is a leap year",isLeapYear)


# In[23]:


# Genrate random number between o and 20

from random import randint
for i in range(10):
    print(randint(0,20))


# In[25]:


# Generte random number between 10 and 20

from random import*
for i in range(10):
    print(randint(10,20))


# In[27]:


# Generate random between 10 and 50

from random import*
for i in range(10):
    print(randint(10,50))


# In[28]:


# Generate random number between 0 and 1

from random import*
for i in range(10):
    print(randint(0,1))


# In[22]:


# Assign value 1 to x when y>0.
y=int(input("enter any number:"))

if y>0:
    x=1
    print(x)


# In[13]:


# checking conversion
i=True
int(bool(i))


# In[15]:


# checking conversion
i=int(True)
print(i)


# In[16]:


# checking conversion
j=int(False)
print(j)


# In[17]:


# checking conversion
b1=bool(4)
print(b1)


# In[18]:


# checking conversion
b2=bool(0)
print(b2)


# In[27]:


# checking complete divisibility of a number. 

count=int(input("Enter any number:"))
if count % 10==0:
    newline=True
else:
    newline=False
print("newline is ", newline)


# In[41]:


# Program to sum two numbers.

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
if x>2:
    if y>2:
        z=x+y
        print("z is ",z)
    else:
        print("x is",x) #if value of x is greater than 2.


# In[48]:


# Program to sum two numbers.

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
if x==2:
    if y==2:
        z=x+y
        print("z is ",z)
    else:
        print("x is",x) #if value of x is equal to 2.


# In[56]:


# Program to age for dl
age=eval(input("Enter your age:"))
if age <=16:
    print("can't get driver's licence")
else:
    print("can get driver's licence")


# In[58]:


# Program to check for even,odd and multiple of 5.
x=int(input("enter a number:"))
if x%2==0:
    print(x,"number is even ")
elif x%5==0:
    print(x, "number is divisble by 5")
else:
    print(x, "number is odd")


# In[1]:


income=230000
if income<10000:
    tax=income*0.1
elif (income>=10000 and income<=20000):
    tax=1000+(income-10000)*0.15
else:
    tax=1000+(income-10000)*.5
print(tax)

