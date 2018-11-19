
# coding: utf-8

# # Tuples: one of the type of Data structure in Python

# In[4]:


t1 = () # Create an empty tuple
t2 = (1, 3, 5) # Create a tuple with three elements

# Create a tuple from a list

t3=tuple([x for x in range(1,5)])
t4 = tuple([2 * x for x in range(1, 5)])

#create a tuple from a string. 
t5 = tuple("abac") # t4 is ('a', 'b', 'a', 'c')

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)


# In[8]:


# type of tuple
pythonTuple = (2.0,9,"a",True,"a")
type(pythonTuple)


# In[9]:


# indexing of tuple
pythonTuple = (2.0,9,"a",True,"a")
pythonTuple[2]


# In[10]:


# tuple is immutable ,lets see
pythonTuple = (2.0,9,"a",True,"a")
pythonTuple[1] = 5   # it gave an exception


# In[13]:


# Getting index of a tuple

pythonTuple = (2.0,9,"a",True,"a")
pythonTuple.index('a')


# In[14]:


# counting tuple means no. of times that element occured
pythonTuple = (2.0,9,"a",True,"a")
pythonTuple.count("a")


# In[17]:


# created a tuple
tuple1 = ("Green","Red","Blue")
tuple2 = (7,1,2,23,4,5)
print(tuple1)
print(tuple2)
print("length is",len(tuple2))
print("max is ",max(tuple2))
print("min is ",min(tuple2))
print("sum is ",sum(tuple2))

print("first element is", tuple2[0]) # gives value at position zero




# In[18]:


# combining two tuples

tuple3 = tuple1+tuple2
print(tuple3)


# In[27]:


# Dublicating a tuple
tuple3 = 2 * tuple1
print(tuple3)
print(tuple2[2:4]) # silcing means taking out a part 
print(tuple1[-1]) # here value at postion -1 asked  
print(tuple2[:-1])
print(tuple2[-6:-1])
print(tuple2[-5:]) # hence this illustrates reverse slicing

print(2 in tuple2) # checking whether 2 is in tuple2 or not

for v in tuple1:   # for loop ,v means values in tuple1
    print(v, end=" ")
print()


# In[29]:


list1=list(tuple2) # list is created from tuple2
list1.sort()       # then list is sorted, since tuple is immutable
tuple4=tuple(list1) # again tuple is create from sorted list1
tuple5=tuple(list1) # one more tuple is create from list1
print(tuple4)
print(tuple4==tuple5)


# In[34]:


# Example to illustrate that tuple is immutable
t = (1,2,3)
t.append(4) # we can not append in a tuple


# In[35]:


# Example to illustrate that tuple is immutable
t = (1,2,3)
t.remove(3) # we can't remove an element from tuple


# In[36]:


# Example to illustrate that tuple is immutable
t = (1,2,3)
t[0]=1  # we can not modify an element in a tuple


# In[39]:


# comparing two tuples
t1 = (1,2,3,7,9,0,5)
t2 = (1,2,5)
t1 == t2


# In[41]:


# exapmle to illustrate indexing in tuple
t1 = (1,2,3,7,9,0,5)
print(t1)
print(t1[0])
print(t1[1:3])
print(t1[-1])
print(t1[:-1])
print(t1[1:-1])


# In[42]:


t1 = (1,2,3,7,9,0,5)
t2 = (1,3,23,7,9,0,5)
print(t1==t2) # first length then elemnets are compared
print(t1!=t2) # while comparing elements it follows lexicographic ordering
print(t1>t2)  # meaning first two elements then next two elements
print(t1<t2)

