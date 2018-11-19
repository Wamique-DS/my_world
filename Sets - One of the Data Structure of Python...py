
# coding: utf-8

# # Sets: One of the type of Data Structure in Python.

# In[7]:


# Create a set 

pythonSet = {'Book','Pen','NoteBook','Pencil','Book'} # set is represeted by curli braces
print(pythonSet)
pythonSet.add("Eraser") # we can add an element in a set
print(pythonSet)
pythonSet.remove("Pen") # an element can be removed as well
print(pythonSet)        # it will throw an exception   if elemnet is not in the set


# In[12]:


# Create two sets to check which is subset and superset 

s1 = {1, 2, 4}
s2 = {1, 4, 5, 2, 6}
s1.issubset(s2) # s1 is a subset of s2
s2.issuperset(s1) # s2 is a superset of s1
print(s1.issubset(s2))
print(s2.issuperset(s1))


# In[17]:


# Comparing two sets

s1 = {1,2,4}
s2 = {1,4,2}
s1 == s2   # these operators are used to check if they have same elements
s1 != s2    # or they have different elements
print(s1==s2)
print(s1!=s2)


# In[21]:


# Create two set and see different opertions on it

s1 = {1,2,4}
s2 = {1,3,5}
print(s1.union(s2)) # all elements including common elements
print(s1|s2)

print(s1.intersection(s2)) # common elemnets in two sets
print(s1&s2)

print(s1.difference(s2)) 
print(s1-s2)

print(s1.symmetric_difference(s2)) # all elements except common elements
print(s1^s2)


# In[28]:


# Create a set and print 

s1 = {1,3,4}

print(s1)


# In[30]:


# lets check if the set is valid or not

s = {{1,2},{3,4}}
print(s)


# In[31]:


# lets check if the set is valid or not

s = {[1,2],[3,4]}
print(s)


# In[32]:


# lets check if the set is valid or not

s = {(1,2),(3,4)} 
print(s)


# In[49]:


# Creating a set

students = {"john" , "peter"}

print(students)


# In[47]:


# Adding same element to the set

students = {"john" , "peter"}
students.add("john")


print(students)


# In[48]:


# Adding different element to the set

students = {"john" , "peter"}
students.add("peterson")

print(students)


# In[50]:


# Removing an elemnet from set

students = {"john" , "peter"}
students.remove("peter")
print(students)


# In[56]:


# comparing two sets for subset and superset

student1 = {"peter","john","tim"}
student2 = {"peter","johnson","tim"}
print(student1.issuperset(s2)) # for that s1 needs to have all elements of s2 and 1 more element
print(student1.issubset(s2)) # for that s2 needs to have all elements of s1

print({1,2,3}=={1,2,4}) # lengths are same  but not the elements
print({1,2,3}>{1,2,4}) # lenght same but elements are different
print({1,2,3}<{1,2,4,}) # same here also
print({1,2}<{1,2,4})  # difference in lenght 
print({1,2}<={1,2,4}) # few elemnets are same but lenghts are different


# In[1]:


# Program to test which is faster: set or list

import random
import time
 
Number_of_elements=10000

# create a list

lst=list(range(Number_of_elements))
random.shuffle(lst)

# Creat a set fronm the list
s=set(lst)

#Test whether if elemnets is in the set

startTime=time.time() # Get start time
for i in range(Number_of_elements):
    i in s
endTime= time.time()
runTime=int(endTime - startTime *1000)
print("To test if",Number_of_elements,"Elements are in the set\n","The run time is",runTime , "milliseconds")

# To test if elements are in the list

startTime=time.time()
for i in range(Number_of_elements):
    i in lst
endTime=time.time()
runTime=int(endTime-startTime * 1000)
print("\nTo test if",Number_of_elements,"Elements are in the lst\n"," The runTime is", runTime,"milliseconds")

# Remove elements from set one at a time

starTime= time.time()
for i in range(Number_of_elements):
    s.remove(i)
endTime=time.time()
runTime=int(endTime-startTime * 1000)
print("\nTo remove ",Number_of_elements,"Elements from the set","The runTime is",runTime,"milliseconds")

# Remove elements from lst one at a time

startTime=time.time()
for i in range(Number_of_elements):
    lst.remove(i)
endTime=time.time()
runTime=int(endTime-startTime * 1000)
print("\nTo remove",Number_of_elements,"Elements from the lst","The runtime is",runTime,"milliseconds")

