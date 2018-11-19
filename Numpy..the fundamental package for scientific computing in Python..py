
# coding: utf-8

# # Numpy.....

# In[7]:


# one dim array
import numpy as np

a=np.array(range(10))
a


# In[3]:


print(a[2:3])
print(a[:7:1])
print(a[::])
print(a[::-2])


# In[11]:


b=np.array([12,19,8,45,20,25,50,55,30,60])
b


# In[12]:


b[:]


# In[13]:


b[1:7]


# In[14]:


b[:9]


# In[15]:


b[:5:2]


# In[19]:


b[6::-2]


# In[18]:


b[5::-2]


# In[20]:


b[5::2]


# In[21]:


# Two dimensional array..
import numpy as np
b=np.array([[1.3,2,3,4],[6,7,8,9]],dtype=float)
b


# In[7]:


# Three dimensional array..
import numpy as np
c=np.array([[[1,2,3],[4,5,6]],[[9,8,7],[5,4,3]]])
c


# # Few Functions in Numpy....

# In[20]:


np.zeros(10,dtype=int) # ten zero values in a list...


# In[11]:


np.ones((3,5),dtype=float) # 3 by 5 matrix with ones...as float


# In[12]:


np.full((3,5),3.14)  # 3 by 5 matrix with all element 3.14


# In[13]:


np.arange(0,20,2) # values btw 0 & 20 with diffrence 2...


# In[14]:


np.linspace(0,1,5) # 5 values btw o & 1 with equal distance or space..


# In[15]:


np.random.random((3,3)) # by deafult random values btw 0 & 1 in 3 by 3 . 


# In[16]:


np.random.normal(0,1,(3,3)) #normal random values whose mean is 0 and std dev is 1 in 3 by 3 matrix


# In[17]:


np.random.randint(0,10,(3,3)) # random integer values btw 0 and 10 in 3by3 matrix


# In[18]:


np.eye(3) # gives square matrix with diagonal elements 1.


# In[19]:


np.empty(3) ''' it creates three empty spaces in  a onr D array
             whose value is almost zero which we can change latter.'''


# # Array Manipulation...
# 

# In[3]:



import numpy as np
np.random.seed(0)
x1=np.random.randint(10,size=(6))
x2=np.random.randint(10,size=(3,4))
x3=np.random.randint(10,size=(3,4,5))


# In[4]:


x1


# In[5]:


x2


# In[6]:


x2[0,0] # element at 0th row and 0th col.


# In[7]:


x1[::-1] # all elments but each time decreamented by 1


# In[8]:


x1[4::-2] # from 4th index to 0th index ,decreament by 2


# In[59]:


x3


# In[60]:


x3.ndim # whether 1D ,2D or 3D array


# In[61]:


x3.shape # no. of rows & columns


# In[62]:


x3.size # total no. of elements in the Array


# In[63]:


x3.dtype # type of data in Array


# In[64]:


x3.itemsize # no. of bytes for each item


# In[65]:


x3.nbytes # total no. of bytes for all elements


# # Array Slicing...  x[start:stop:step]

# In[9]:


# Slicing in Multidimensional Array..using Row & Col.
x2


# In[10]:


x2[:2,:3] # 0th,1st row & 0th,1st,2nd column


# In[11]:


x2[:3,::2] # 0th,1st,2nd row & 0th,2nd column bcz step by2 


# In[12]:


x2[::-2,::-2] # all rows but step by -2 & all columns but step by -2


# In[13]:


x2[::-1,::-1] #  gives inverse matrix...


# In[18]:


print(x2[:,2]) # all rows but only column at  2nd index


# In[15]:


print(x2[2,:]) # only 2nd index row and all columns in that row....


# In[16]:


print(x2[0]) # oth row


# In[19]:


print(x2[1]) # by default it gives row wise...here row at 1st index.


# # subarray as no-copy views

# In[20]:


x2_sub=x2[:2,:2] # ist 2 rows and ist 2 coumn values..
x2_sub


# In[21]:


x2_sub[0,0]=99 # assigned new value in place of [0,0]
x2_sub


# In[22]:


x2 # changes made in sub array(virtual table) resulted change in original array..


# # Creating copies of Array using copy() method:

# In[23]:


x2_sub2_copy=x2[:2,:2].copy()
x2_sub2_copy


# In[25]:


x2_sub2_copy[0,0]=40


# In[26]:


x2_sub2_copy


# In[27]:


x2 # here changes made in subarray has not affect in the original array...bcz it was a copy of array.


# # Reshaping Of Array...

# In[28]:


y=np.array([1,2,3,4,5,6])
y


# In[29]:


y.reshape((2,3))  # row vector via reshape.


# In[30]:


y[np.newaxis,:] # row vector via new axis..


# In[31]:


y.reshape((3,2))  # column vector via reshape.


# In[32]:


y[:,np.newaxis] # column vector via newaxis.


# # Array Concatenation....

# In[33]:


x=np.array([1,2,3])
y=np.array([4,5,6])
np.concatenate([x,y])


# In[34]:


z=[99,99,99]
print(np.concatenate([x,y,z]))


# In[35]:


a=np.array([[1,2,3],[4,5,6]])
np.concatenate([a,a]) # axis=0


# In[36]:


np.concatenate([a,a],axis=1)


# In[38]:


x=np.array([1,2,3])
a=np.array([[4,5,6],[7,8,9]])


# In[40]:


np.vstack([x,a])


# In[41]:


y=np.array([[99],[99]])
np.hstack([a,y])


# # Array Spliting...

# In[42]:


x=np.array([1,2,3,99,99,3,2,1])
x1,x2,x3=np.split(x,[3,5])
print(x1,x2,x3)


# In[43]:


a=np.arange(16).reshape(4,4)
a


# In[44]:


upper,lower=np.vsplit(a,[2])
print(upper)
print(lower)


# In[46]:


left,right=np.hsplit(a,[2])
print(left)
print(right)


# # Aggregations : Summing the Values in an Array.... Min & Max..

# In[3]:


import numpy as np
l=np.random.random(100) # humdred random float values btw 0 & 1.
l


# In[4]:


sum(l) # total of all values using usual sum()


# In[5]:


np.sum(l) # total of all values using NumPy version of sum()


# In[6]:


np.max(l) # max of all values using NumPy version of max()


# In[7]:


np.min(l)# min of all values using NumPy version of min()


# In[11]:


big_array=np.random.random(1000000)
get_ipython().run_line_magic('timeit', 'sum(big_array)')
get_ipython().run_line_magic('timeit', "np.sum(big_array) # we can clearly see the difference in time...that's why we use Numpy..")


# In[12]:


min(big_array)


# In[14]:


max(big_array)


# In[15]:


np.min(big_array)


# In[16]:


np.max(big_array)


# In[20]:


get_ipython().run_line_magic('timeit', 'min(big_array) # time to calculate using python min()')
get_ipython().run_line_magic('timeit', 'np.min(big_array) # time to calculate using NumPy version of min()')


# In[19]:


get_ipython().run_line_magic('timeit', 'max(big_array) # time to calculate using python max()')
get_ipython().run_line_magic('timeit', 'np.max(big_array) # time to calculate usingNumPy version of max()')


# In[21]:


print(big_array.sum(),big_array.max(),big_array.min()) # can be calculated like this


# # Multidimentional Aggregates.... axis=0 col, axis=1 row.

# In[11]:


import numpy as np
m=np.array([[12,76,43,16],
           [27,46,98,61],
           [30,12,45,90]])

m
#print(m)


# In[8]:


np.sum(m) # sum of all elements in matrix using numpy aggregate.


# In[5]:


m.sum() # sum of all values in the given matrix


# In[12]:


m.min() # min value in the given matrix


# In[14]:


np.min(m)  # min among all elements in matrix using numpy aggregate.


# In[16]:


m.min(axis=0)


# In[17]:


np.min(m,axis=0)


# In[18]:


m.min(axis=1)


# In[19]:


np.min(m,axis=1)


# In[20]:


m.max() # maximum value in the given matrix..


# In[21]:


np.max(m)


# In[27]:


np.max(m,axis=0)


# In[26]:


np.max(m,axis=1)


# In[28]:


# random.random()  Return random floats in the half-open interval [0.0, 1.0).
# Results are from the “continuous uniform” distribution over the stated interval
M=np.random.random((3,4))
M


# In[29]:


M.sum()


# In[36]:


print(M.min())
print(np.min(M))

print(M.max())
print(np.max(M))

print(np.min(M,axis=0))
print(np.min(M,axis=1))

print(np.max(M,axis=0))
print(np.max(M,axis=1))


# # Other Aggregation Functions....

# In[37]:


np.prod(M) # Function Name


# In[90]:


np.nanprod(M) # NaN safe Version


# In[41]:


np.mean(M)


# In[42]:


np.median(M)


# In[43]:


np.var(M)


# In[44]:


np.std(M)


# In[57]:


np.any(0)


# In[61]:


np.all(50)


# In[62]:


np.argmin(M)


# In[65]:


np.argmin(M,axis=0)


# In[66]:


np.argmin(M,axis=1)


# In[67]:


np.argmax(M)


# In[69]:


np.argmax(M,axis=0)


# In[70]:


np.argmax(M,axis=1)


# In[72]:


np.percentile(M,50) # calculates 50th percentile


# In[73]:


np.percentile(M,25)


# In[74]:


np.percentile(M,75)


# In[76]:


# Diff between 3rd and 1st quatile gives interquartile Range.
np.percentile(M,75)-np.percentile(M,25) # This gives Interquartile Range...


# In[82]:


np.any(m,0)


# In[83]:


m


# In[89]:


np.any(m>100,axis=0)


# # Comparisions: comparision operators are implemented as ufuncs  in numpy

# In[92]:


x=np.array([1,2,3,4,5,6])
x


# In[93]:


x<4


# In[94]:


x<=4


# In[95]:


x==4


# In[99]:


2*x


# In[97]:


x**2


# In[103]:


(x*2)==(2**x)


# In[104]:


np.less(x,4)


# In[106]:


np.greater_equal(x,4)


# In[108]:


rng=np.random.RandomState(0)
x=rng.randint(10,size=(3,4))
x


# In[109]:


x<3


# In[110]:


np.less(x,3)


# # Working with Boolean Arrays... 

# In[112]:


# Counting Entries...
rng=np.random.RandomState(0)
x=rng.randint(10,size=(3,4))
x


# In[113]:


np.count_nonzero(x<6) # no. of valus less than 6


# In[114]:


np.sum(x<6) # we can get no. of values less than 6.


# In[115]:


np.sum(x<6,axis=0) # total no. of values less than 6 along column


# In[116]:


np.sum(x<6,axis=1) # total no. of values less than along row


# In[117]:


np.any(x<6) # returns True if any value in matrix is less than 6  


# In[118]:


np.all(x<6) # returns true if all values in matrix less than 6


# In[127]:


# Using Keywords and/or and operators bitwise & and |
bool(49),bool(0),bool(-7) # it gives boolean value


# In[128]:


bool(49 and 0) # T and F returns F, as in and T when both T.


# In[129]:


bool(49 or 0) # T or F returns T, T when either of them is T.


# In[125]:


bin(49),bin(0),bin(-7) # it converts to bit


# In[130]:


bin(49 & 0) # it coverts 49 and 0 to bit then applies & and returns bit


# In[131]:


bin(49 | 0)


# In[132]:


bin(49 & 30) # below rseult of 40 & 30 proves bin(49 & 30)


# In[133]:


(49&30)


# In[134]:


np.bitwise_and(49,30)


# In[135]:


# Now applying above operators on 2D Arrays...
A=np.array([1,0,1,0,1,0]) # its integer value is 49
B=np.array([1,1,1,0,1,1]) # its integer value is 59
A|B


# In[139]:


A=np.array([1,0,1,0,1,0]) # its integer value is 49
B=np.array([1,1,1,0,1,1]) # its integer value is 59
A or B ''' this means that (and or) works only on single values ie.,
           1D array while (& |) works on multidimensinal Array as well '''


# In[136]:


A=np.array([1,0,1,0,1,0]) # its integer value is 49
B=np.array([1,1,1,0,1,1]) # its integer value is 59
A&B


# In[137]:


C=np.array([1,1,0,0,0,1]) # its integer value is 49
D=np.array([0,1,1,1,1,0]) # its integer value is 30
C&D


# In[138]:


C=np.array([1,1,0,0,0,1]) # its integer value is 49
D=np.array([0,1,1,1,1,0]) # its integer value is 30
C|D


# # Fancy Indexing:

# In[140]:


''' Main benefit of Fancy indexing is that it's not mandatory to access
    index in sequence rather we can access any index from any where '''
x=np.array([12,31,45,37,76,87,56,90,97,65,77,80])
x


# In[141]:


[x[2],x[5],x[7]] # value at index 2,5 and 7,it returned a list


# In[142]:


np.array([x[2],x[5],x[7]]) # same index vales returned as Array


# In[143]:


x[[2,5,7]] # it also gave an Array


# In[144]:


rand=np.random.RandomState(0) # used to get same values every time 
x=rand.randint(100,size=10) # 10 random int values btw 0 and 100 excluding 100. 
print(x)


# In[145]:


x[[3,7,2]] # we can directly access index values like this


# In[146]:


ind=[3,7,2] # another way of accessing index values
x[ind]


# In[6]:


ind=np.array([3,7],
            [4,5])
x[ind]


# In[153]:


x[ind]


# In[156]:


x=np.arange(12).reshape((3,4)) # In 3by4 matrix arange 0 to 11
x


# In[6]:


row=np.array([0,1,2])
col=np.array([2,1,3])
x[row,col]


# In[158]:


row=np.array([0,1,2,1,2,0,2])
col=np.array([2,1,3,2,1,3,2])
x[row,col]


# In[161]:


row=np.array([0])
col=np.array([2])
x[row,col]


# In[162]:


# Combined Fancy Indexing ...
x[2,[2,0,1]] # in row2 elements at col 2,0 and 1


# In[163]:


x[1,[1,0,2]]


# In[164]:


# Fancy Indexing using Slicing...
x[1:,[1,0,2]]


# In[18]:


# Fancy Indexing using masking..
x=np.arange(12).reshape((3,4))
print(x)
mask=np.array([1,0,1,0],dtype=bool) # 1st and 3rd column taken
x[row[:,np.newaxis],mask] # here row=np.array([0,1,2])


# In[5]:


x=np.arange(12).reshape((3,4))
print(x)
mask=np.array([1,0,1],dtype=bool) # 1st and 3rd row taken
col=np.array([2,1,3])
x[col[np.newaxis,:],mask] # here col=np.array([2,1,3,0])


# In[3]:


x = np.array([1,3,-1, 5, 7, -1]) 
x
mask = (x < 0) 
mask 


# In[36]:


x[mask]=0 ''' using mask we can access and replace any value 
              in our array without knowing there index, which
              can be done without using for loop'''
x         # mask values <0 will be replaced by 0


# In[168]:


# Modifying Values using Fancy Indexing...
x=np.arange(10)
i=np.array([2,1,8,4])
x[i]=99
print(x)


# In[5]:


x=np.arange(10)
i=np.array([2,4,6]) # can explicitly assign different values to different index
x[2]=90
x[4]=95
x[6]=99
print(x)


# In[6]:


x=np.arange(10)
i=np.array([2,4,6]) # each index values can be increamented as our need..
x[2]+=1
x[4]+=2
x[6]+=3
print(x)


# In[37]:


x=np.arange(10)
x
mask=(x>7) # another way of assigning values
mask


# In[38]:


x[mask]=99
x


# In[40]:


x=np.zeros(10)
x[[0,0]]=[4,6] '''here ist value at index 0 is replaced by 4 then 
                 again it is replaced by 6,fially x[0] holds 6 '''
print(x)


# In[41]:


i=[2,3,3,4,4,4] ''' here we would think that each time 1 is increamented and
                    finally we get 1,2,2 but it is not like that ,actually 
                    we can increament only once in each index then value is 
                    stored in indices of array ,rest can be seen below
                   '''
x[i] +=1
x


# In[43]:


# at() method is used if we want to do multiple operation on single index ,reduceat() is similar .
x=np.zeros(10)
print(x)
np.add.at(x,i,1) # here i=[2,3,3,4,4,4]
print(x)  # here in this example value is 1 at index 2 then increamented at indices 3 & 4.


# # Sorting Array..

# In[44]:


import numpy as np
def selection_sort(x): # it is sequential sorting of unsorted list,for 5 values 5 times sorted, time taken n2
    for i in range(len(x)):
        swap=i + np.argmin(x[i:])
        (x[i],x[swap])=(x[swap],x[i]) # here ist value is replaced by min value
        return x


# In[45]:


x=np.array([2,1,3,5,4])
selection_sort(x)


# In[80]:


def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
        return x
    


# In[93]:


x=np.array([2,1,4,3,5])
bogosort(x) # valus omly randomly shuffled...


# In[94]:


# Fast sorting in NumPy... np.sort and np.agrsort
x=np.array([2,1,4,5,3])
np.sort(x)


# In[6]:


# Sorting can diectly using sort as above...
x1=np.array([2,1,4,5,3])
x1.sort()
print(x1)


# In[104]:


# argsort() gives index  of each element/value in an array...
x=np.array([3,4,2,5,1])
i=np.argsort(x)
print(i)


# In[102]:


x=np.array([6,4,1,5,3,2])
i=np.argsort(x)
print(i)


# In[105]:


# Sorting Array..
x[i]


# In[8]:


# Sorting along rows and columns
rand=np.random.RandomState(1)
x=rand.randint(0,10, (4,6))
print(x)


# In[110]:


# sort each column of x
np.sort(x,axis=0) # all values along column is sorted


# In[111]:


# Sort each row of x
np.sort(x,axis=1) '''all values along row is sorted.after sorting in this
                      way any relation between them will be lost.'''


# In[112]:


#Sorting Arrays: Partial Sorts:Partitioning
x=np.array([7,3,2,1,6,5,4])
np.partition(x,3) '''it takes an array and value k which is 3 here, the result is 
                     new array with ist three smallest values in a new
                     array and rest values in arbitaray order '''


# In[116]:


# Partition can be done along axis as well..
rand=np.random.RandomState(0)
x=rand.randint(0,10, (4,6))
print(x)
np.partition(x, 2, axis=1) '''along row first two min value in each row takes first two position 
                              and rest values comes as it is..'''


# # Structured Data:  NumPy's Structured Array

# In[119]:


# created data structure with list....
name=['Alice','Bob','Kathey','doug']
age=[24,47,37,19]
weight=[55.0,85.0,68.5,61.0]
data=np.zeros(4,dtype={'names':('name','age','weight'),
                      'formats':('U10','i4','f8')})
print(data.dtype)


# In[121]:


# we can fill array with our list of names..
data['name']=name
data['age']=age
data['weight']=weight
print(data)


# In[123]:


#  With Structured data we can access values using index 0r names..
data['name'] # get all names


# In[124]:


data[0] # first row


# In[125]:


data[-1] # last row


# In[126]:


data[-1]['name'] # get name from last row


# In[127]:


data[data['age']<30]['name'] # age less than 30


# In[134]:


data_rec= data.view(np.recarray)
data_rec.age


# In[128]:


get_ipython().run_line_magic('time', "data['age']")


# In[131]:





# In[132]:


get_ipython().run_line_magic('time', "data_rec['age']")


# In[133]:


get_ipython().run_line_magic('time', 'data_rec.age')


# In[7]:


# We created an empty container Array...then filled with our list of array.. 
data1=np.zeros(4,dtype={'names':('name','age','weight'),
                      'formats':('U10','i4','f8')})
print(data1.dtype)


# In[18]:


weight=[50.1,48,62,76]
name=['wam','sam','tom','jack']
age=[29,36,54,70]
data1['age']=age
data1['name']=name
data1['weight']=weight
data1


# In[19]:


data1[0]


# In[20]:


data1[-1]


# In[21]:


data1[-1]['name']


# In[22]:


data1[-2]['name']


# In[23]:


data1[data1['age']>40]['name'] # those with age >40


# In[ ]:


# Structured Array data types can be specified in no. of ways.... 

np.dtype({'name':('name','age','weight'),
         'formats':('U10','i4','f8')})

# Numerical types can be specified with python types or NumPy dtypes.. 

np.dtpye({'name':('name','age','weight'),
         'formats':((np.str_, 10), int , np.float32)})

# A compound type can be specified as a tuples...

np.dtype([('name','S10'),('age','i4'),('weight','f8')])

# we can specify types alone in comma-separated string...

np.dtype('S10,i4,f8')


# In[32]:


# RecordArrays: Stuructured Arrays with a twist...
# here fields can be accessed as attributes rather than as dictionary keys..
data1_rec = data1.view(np.recarray) # view function used to view 
print(data1_rec.age)
print(data1_rec.name)


# In[30]:


get_ipython().run_line_magic('timeit', "data1['age']")
get_ipython().run_line_magic('timeit', "data1_rec['age']")
get_ipython().run_line_magic('timeit', 'data1_rec.age')

