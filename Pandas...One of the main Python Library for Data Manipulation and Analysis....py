
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# # Pandas DataFrame: Series...

# In[3]:


data=pd.Series([45,32,98,94,49,53,27,75]) # input of list in Series gave dtype(int64)
data     # values are only in sequence not sorted.


# In[10]:


data1=pd.Series(np.array([45,32,98,94,49,53,27,75])) # input of array gave dtype(int32)
data1               # values are only in sequence not sorted.


# In[11]:


data2=pd.Series([0.25,0.50,0.75,1.0]) # creating Series Df using python list..
data2                   


# In[13]:


data.values # it's just a NumPy Array


# In[14]:


data.index # it gave complete information abt index..


# In[15]:


data3=pd.Series([0.25,'a',12])  ''' as list acccept mixed type but finally it is 
                                  converted to one dtype ie,.(object)'''
data3


# In[16]:


data4=pd.Series(np.array([12,'a',15.5]))
data4


# In[6]:


x=np.array([12,10.9,18,'a',19,'d']) # list with mixed type values..
x


# In[7]:


x[0]


# In[8]:


x[1:3]


# In[9]:


x[2:6]


# In[20]:


np.sort(x) # sorting can be done as well..


# # Series as Generalized NumPy Array...

# In[11]:


data5=pd.Series([0.25,0.50,0.75,1.0],
               index=['a','b','c','d'])
data5


# In[13]:


data5['b']


# In[15]:


data5['a':'c'] # we can access slice 


# In[17]:


data5[['a','c']] # we can pick as per our need..


# In[18]:


data5[['c','a','d']] # we can pick as per our need.


# In[19]:


data6=pd.Series([0.25,0.50,0.75,1.0], # instead we used random int as index
               index=[2,5,7,3])
data6


# In[20]:


data6[7]


# In[21]:


data6[:4]


# In[24]:


data6[2]


# In[25]:


data6[:2]


# In[26]:


data7=pd.Series([0.25,0.50,0.75,1.0], # instead we used random int as index
               index=[2,'5','7',3])   # even string converted to int
data7


# In[27]:


data7=pd.Series([0.25,0.50,0.75,1.0], # instead we used random int as index
               index=[2,'a',7,'c'])
data7


# # Series as Specialized Dictionary:

# In[32]:


# Constructing a python dictionary...
population_dict={'TS':34276558,
                'AP':47537269,
                'TN':52863836,
                'JH':31928736}

population


# In[33]:


population_dict['JH']


# In[37]:


population_dict.keys()


# In[39]:


population_dict.values()


# In[40]:


# Constructing a python dictionary...
population_dict={'TS':34276558,
                'AP':47537269,
                'TN':52863836,
                'JH':31928736}
population=pd.Series(population_dict)


population


# In[44]:


population['TS'] # accessing using key as index..


# In[50]:


population[['JH','TS','JH']] # square bracket needed..


# In[51]:


population['TS':'JH'] # In slicing no square bracket required


# # Contructing Series Objects...

# In[14]:


''' Earlier we created Series from scratch, now we will 
    create from index ,list and Numpy array as data '''
import numpy as np
import pandas as pd


# In[15]:


# Series Construction using python list as data..
    
data8=pd.Series([12,16,23,37,19,45,76,55,90])
pd.Series(data8,index=[2,5,1,7])


# In[12]:


# Series Construction using index as data..

pd.Series(5,index=[100,200,300])


# In[13]:


# Series Construction using python Dictionary as data...

pd.Series({2:'a',1:'b',3:'c'})


# In[19]:


pd.Series({2:'a',1:'b',3:'c'},index=[1,3]) # index can be explicitly set to desired value..


# In[21]:


pd.Series({2:'a',1:'b',3:'c'},index=[1:3]) # slicing can't be done...


# In[22]:


data9=pd.Series({2:'a',1:'b',3:'c'}) # Series with Dictionary as data gives sorted data values..
data9


# In[23]:


data9[1:3]


# In[24]:


data9[:3]


# # The Pandas DataFrame Object :

# In[ ]:


''' pandas DataFrame can be thought as Generalization of NumPy Array
    and Specialization of Python Dictionary...'''


# In[29]:


''' DataFrame as a Generalized NumPy Array...DataFrame is a
    sequence of  allinged Series objects...meaning that they 
    share same index '''

population_dict={'TS':34276558,
                'AP':47537269,
                'TN':52863836,
                'JH':31928736}
Populations=pd.Series(population_dict)

Populations


# In[30]:



area_dict={'TS':386340,
           'AP':409765,
           'TN':568720,
           'JH':309876}
Areas=pd.Series(area_dict)

Areas


# In[32]:


# Construting pandas DataFrame from a dictionary of Series Objects.

states=pd.DataFrame({'Populations':population,
                   'Areas':area})
states


# In[34]:


states['Populations']


# In[36]:


states[['Populations','Areas']]


# In[38]:


Populations['TS']


# In[39]:


Areas['JH']


# In[40]:


states.index


# In[41]:


states.columns


# In[42]:


states.values


# # DataFrame as Specialized Dictionary...

# In[43]:


'''IN this DataFrame dict..maps key and values, where as 
   DataFrame maps column name to a series of column data '''
states['Areas'] # Areas attribute returns a Series Object containing Area.


# In[47]:


# Construting pandas DataFrame from a single Series Object...

pd.DataFrame(Populations, columns=['population'])


# In[48]:


# Construting pandas DataFrame from a list of dictionary...

data10=[{'a':i,'b':2 * i}
       for i in range(3)] # i value 0,1,2
pd.DataFrame(data10)


# In[49]:


pd.DataFrame([{'a':1,'b':2},{'b':3,'c':4}])


# In[50]:


# Construction pandas DataFrame From a 2D NumPy Array...

pd.DataFrame(np.random.rand(3,2),
            columns=['foo','bar'],
            index=['a','b','c'])


# In[2]:


# Construting pandas DataFrame from a NumPy Structured Array..
# Pandas DF operates much like Structured Array,can be created directly from one..
A=np.zeros(3, dtype=[('A','i8'),('B','f8')])
A


# In[5]:


data11=pd.DataFrame(A)
data11


# In[14]:


data11[A]


# In[15]:


data11


# In[18]:


data11[0,0]=0
data11


# In[19]:


data11[A]


# In[22]:


data11['A']


# In[23]:


data11['A'][0]=3


# In[24]:


data11


# In[30]:


data11['A'][0]=3


# In[31]:


data11


# In[33]:


data11['A'][0,1,2]=5
data11


# In[34]:


data11['A'][0,1,2]=(2,3,4)
data11


# In[41]:


data11['A']='BC'
data11


# # The Pandas Index Object : It can be thought as immutable array or ordered set.
#     

# In[42]:


# Constructing an Index object from list of integer..
ind1=pd.Index([2,5,8,6,4,9])
ind1


# In[43]:


# Accessing index value from pandas index object..
ind1[0]


# In[44]:


ind1[::2]


# In[45]:


ind1[::-1]


# # Basic diff btw Index Object & NumPy Array is that Index Object is immutable, that is they cannot be modified by normal means.
# 

# In[46]:


# Various Attributes of Index Object is similar to NumPy Arrays..
print(ind1.size,ind1.shape,ind1.ndim,ind1.dtype)


# In[47]:


ind1[0]=1 # Index does not support mutable operation...


# In[48]:


# Index Object as Ordered Set...

indA=pd.Index([1,3,5,7,9])
indB=pd.Index([2,3,5,7,11])


# In[49]:


indA


# In[50]:


indB


# In[51]:


indA & indB # intersection


# In[52]:


indA | indB # union


# In[53]:


indA ^ indB # Symmetric difference ie,. those no. which is not in either A or B


# In[54]:


# These operations can be done using object methods.. 
indA.intersection(indB)


# In[55]:


indA.union(indB)


# In[59]:


indA.difference(indB)


# In[61]:


indA.symmetric_difference(indB)


# # Data Indexing and Selection :

# In[71]:


''' In Explicit index (ie.,data[a:d]) final index is also included while 
    In Implicit index (ie.,data[1:4]) final index is not included in the
    slice..'''
data12=pd.Series(['a','b','c','d'], index=[1,7,5,3])
data12


# In[72]:


data12[1] # This is explicit index..


# In[73]:


data12[1:3]


# In[74]:


data12[0:2] # this is implicit index in slice indexing


# In[75]:


''' Inorder to avoid such confusion in case of index integer , pandas has
    provided some special indexer attributes those are : loc , iloc & ix '''
data12.loc[1]


# In[76]:


data12.loc[1:3] # this is explicit indexing


# In[78]:


data12.loc[1:5] # Explicitly index values btw index 1 and 5 in data12.


# In[79]:


data12.iloc[1] # Implicit indexing..


# In[80]:


data12.iloc[0:2] # Implicit Indexing as final index value is excluded..


# In[81]:


# The 3rd index attribute is ix which is hybrid of both loc and iloc..
data12.ix[1]


# In[4]:


# Data Selection in DataFrame,lets a DataFrame as Dictionary...
area=pd.Series({'BhelTownship':24514,'Kukatpally':35254,'Ammerpet':46813,'HitechCity':24531})
pop=pd.Series({'BhelTownship':45285154,'Kukatpally':25115254,'Ammerpet':79846813,'HitechCity':73254531})
data13=pd.DataFrame({'area':area,'population':pop})
data13


# In[84]:


data13['area']


# In[86]:


data13.area


# In[87]:


data13.area is data13['area']


# In[5]:


data13.population is data13['population']


# In[6]:


data13['density']=data13['area']/data13['population']
data13


# In[8]:


data13['population'][1]=85412523
data13


# In[22]:


data13['area']['Kukatpally']=45254
data13


# In[26]:


# DataFrame as 2D Array

data13.values # it gave 2D Array of all values of DataFrame..


# In[27]:


# We can Transpose whole DF to swap rows and columns...using transpose 
data13.T


# In[31]:


data13.values[0] # passing single index to array access a row.. 


# In[32]:


data13['area'] # passing single index to Df access a column


# In[36]:


# indexing using hybrid ix...
data13.ix[:2,:'population']
data13


# In[37]:


data13


# In[38]:


data13.ix[:2,:'population']


# In[39]:


data13.ix[:3,'population':'density']


# In[40]:


# In loc indexer we can combine masking and fancy indexing...
data13.loc[data13.density>0.001,['area','density']]


# In[41]:


data13.loc[data13.density>0.0001,['area','population']] # density is condition


# In[42]:


data13.iloc[0,2]=90 # assigning value to 0th row & 2nd col..
data13


# In[43]:


# additinal indexing Convention..indexing refers to cols and slicing refers rows.
data13['BhelTownship':'Ammerpet'] #slicing using explicit index


# In[44]:


data13[1:3] # slicing using numbers


# In[47]:


data13.iloc[1,1]=90
data13


# In[52]:


data13.loc[:,'population':'density'] # explicit indexing


# In[59]:


data13.iloc[0:4,1:3] # implicit indexing,we have to give index int value


# In[65]:


# Direct maksing operations also returns row wise rather than column wise..
data13[data13.density>0.001]


# In[63]:


# Creating a Dummy DataFrame..as DataFrame is collection of Series Object..

data14=pd.DataFrame({'col1':pd.Series({1:0,2:0,3:0}),
                    'col2':pd.Series({1:0,2:0,3:0}),
                    'col3':pd.Series({1:0,2:0,3:0})})
data14


# # Operating on Data in Pandas:

# In[66]:


rng=np.random.RandomState(10)
ser=pd.Series(rng.randint(0,10,4))
ser


# In[70]:


df=pd.DataFrame(rng.randint(0,10,(3,4)),
               columns=['A','B','C','D'],
               index=['R1','R2','R3'])
df


# In[68]:


'''If we apply Numpy ufunc on either of these objects the 
   result will be another pandas object with same indices'''
np.exp(ser)


# In[71]:


np.sqrt(ser)


# In[75]:


np.sqrt(df)


# In[69]:


# Slightly more complex calculation...
np.sin(df * np.pi/4)


# # UFuncs: Index Alignment..

# In[81]:


# Index Alignment in Series...very useful when working with incomplete data..

area=pd.Series({'Alaska':3165,'Texas':1454,'California':5452},name='Ar')
area


# In[83]:


population=pd.Series({'California':545582,'Texas':435429,'Newyork':751123},name='pop')
population


# In[84]:


# Population Density..
population/area


# In[86]:


# union of indices.
population.index|area.index


# In[98]:


# intersection of indices..
population.index & area.index 


# In[89]:


# We can replace NaN by fill value by using an object methods in place of operators.
A=pd.Series([2,4,6],index=[0,1,2])
A


# In[91]:


B=pd.Series([1,3,5],index=[1,2,3])
B


# In[92]:


A+B


# In[97]:


A.add(B,fill_value=0)


# In[93]:


A.add(B,fill_value=0) # there individual values plus Zero..


# In[94]:


B.add(A,fill_value=1)


# In[96]:


A.add(B,fill_value=10)


# In[126]:


# Index Alignment in DataFrame..similar things happen in both row & col.

A=pd.DataFrame(rng.randint(0,20,(2,2)),
              columns=list('AB')) # list of stings will divide..
A


# In[127]:


B=pd.DataFrame(rng.randint(0,10,(3,3)),
              columns=list('ABC'))
B


# In[101]:


A+B


# In[106]:


# calculating mean of A..
A.stack().mean()


# In[102]:


# Using any arithematic method and passing any desired fill values we can missing values.
fill=A.stack().mean() # mean value is added to respective NaN
A.add(B,fill_value=fill)


# In[128]:


fill=A.stack().mean() # mean value is subtracted to respective NaN
A.subtract(B,fill_value=fill)


# In[129]:


fill=A.stack().mean() # mean value is multiplied to respective NaN
A.mul(B,fill_value=fill)


# In[130]:


fill=A.stack().mean() # mean value is added to respective NaN
A.truediv(B,fill_value=fill)


# In[134]:


fill=A.stack().mean() # mean value is divided to respective NaN
A.div(B,fill_value=fill) # truediv and div same..


# In[131]:


fill=A.stack().mean() # mean value is floordiv to respective NaN
A.floordiv(B,fill_value=fill)


# In[132]:


fill=A.stack().mean() # mean value is mod to respective NaN
A.mod(B,fill_value=fill)


# In[133]:


fill=A.stack().mean() # mean value is pow to respective NaN
A.pow(B,fill_value=fill)


# In[107]:


# UFuncs: Operation Btw DataFrame & Series...

A=rng.randint(10,size=(3,4))
A


# In[108]:


# Diff btw 2D Array and one of its Row..
A-A[0]


# In[111]:


# In pandas similar operation is done like this...
df=pd.DataFrame(A,columns=list('QRST'))
df-df.iloc[0] # df is sub from ist row...


# In[117]:


# we can operate same in col wise using axis..
df.subtract(df['R'],axis=0)


# In[118]:


# Automatic alignment of indices btw two elements..
halfrow=df.iloc[0,::2] # see line 107 then check..
halfrow # in 0th row ,all col but step by 2


# In[119]:


df - halfrow


# # Handling Missing Data : NaN,NA,null,None..

# In[ ]:


'''Missing Data in Table and DataFrame generally revolve around two stategies..
   Using a Mask(boolen entry) that globally indicates missing value and choosing a Sentinal 
   (Numerical Value)value that indicates a missing entry '''


# # None: Pythonic Missing Data

# In[2]:


''' First Sentinal Value used by Pandas is None. Since None is Python Object
    so, can be used only in Arrays with Data type (Object)'''

vals1=np.array([1,None,3,4]) ''' we cannot use any other misssing value refrences like 
                                 null,NA or NaN here otherwise it will give error'''
vals1                         


# In[3]:


'''Operation by data type object is slower than the other dtype like int,float etc
   so inorderto check which is faster lets take an example..'''
for dtype in ['object' , 'int']:
    print('Type of Data is',dtype)
    get_ipython().run_line_magic('timeit', 'np.arange(1E6,dtype=dtype).sum()')
    print()  # from output it is clear which is faster..


# # NaN: Missing Numerical Data

# In[7]:


# It is Used for Floating Numbers..
vals2=np.array([1,np.nan,3,4])
vals2


# In[8]:


vals2.dtype


# In[9]:


vals1.min() # these operation gives error as it does not support 


# In[11]:


''' NaN is bit like virus it infects any other object it touches.Arithematic
    Operation with NaN will be another NaN'''

print(1+np.nan)
print(1*np.nan)


# In[13]:


vals2.sum(),vals2.min(),vals2.max() # bcz of NaN


# In[17]:


np.nansum(vals2),np.nanmin(vals2),np.nanmax(vals2)


# # NaN and None in Pandas..

# In[14]:


''' Both NaN and None Can be togather in Table Or DataFrame but
    NaN will always replace other missing Values refrences and will
    convert other to NaN'''

pd.Series([1,np.nan,2,None])


# In[18]:


np.array([1,2.6,None,'wamique',np.nan])


# In[19]:


np.array([1,2.6,'wamique',np.nan])


# In[20]:


# if we have both NaN & None Value in the Series..then None is converted to NaN.

pd.Series([1,np.nan,2.5,None])


# In[21]:


# if there is string Value in the Series..then

pd.Series([1,np.nan,2.5,'wamique',None]) '''if there is string in the missing values then
                                            refrence remains as it is '''


# In[22]:


''' If we set a value in an integer array to np.nan ,pandas will automatically
    be upcast to a floating type to accomadate the NA....'''

x=pd.Series(range(2), dtype=int)
x


# In[23]:


# imp. Pandas string data is always stored with an Object dtype..Remember
x[0]=None
x


# # Operating On Null values :

# In[ ]:


'''There are various methods for detecting,removing and replacing
   null values in Pandas Data Structure'''
# isnull(): generates a boolean mask indiaction missing values..
# notnull(): opposite of isnull()
# dropna(): Returns a filtered version of data
# fillna(): Return a copy of data with misiing value filled or imputed 


# In[3]:


data=pd.Series([1,np.nan,'wamique',None])
data


# In[25]:


data.isnull()


# In[26]:


data.notnull()


# In[27]:


# Boolean Mask can be used directly as a Series or DataFrame...
# isnull() and notnull() returns Boolean results in DataFrames..
data[data.notnull()]


# In[4]:


data.dropna()


# In[13]:


df=pd.DataFrame([[1,  np.nan, 2],
                 [2,      3,  5],
                 [np.nan, 4, 6 ]])
df


# In[7]:


# by deafault dropna will drop all rows in which any null value is present..
df.dropna()


# In[34]:


df.dropna(axis='columns')


# In[35]:


df[3]=np.nan
df


# In[9]:


df.dropna(axis='columns',how='all') # drop row or column with all null values.


# In[15]:


''' Thresh parameter helps us to keep min no. of non null 
    values to be kept in a row/column..'''

df.dropna(axis='rows',thresh=3)


# In[16]:


''' Thresh parameter helps us to keep min no. of non null 
    values to be kept in a row/column..'''
df.dropna(axis='rows',thresh=2)


# In[19]:


''' Thresh parameter helps us to keep min no. of non null 
    values to be kept in a row/column..'''
df.dropna(axis='columns',thresh=3)


# # Filling Null Values:

# In[21]:


''' pandas provides a fillna() method to fill missing values 
     and returns a copy of array with replaced missing values'''
data15=pd.Series([1,np.nan,2,None,3], index=list('abcde'))
data15


# In[22]:


# Now we can fill NaN values with single value, such as Zero
data15.fillna(0) # Nan replaced by zero


# In[23]:


# We can also use forward-fill (ffill) to replace NaN values from Object Series..
data15.fillna(method='ffill') # all NaN replaced by previous values...


# In[24]:


# We can also use back-fill (bfill) to replace NaN values from Object Series..
data15.fillna(method='bfill') # all NaN replaced by Next values...


# In[25]:


''' For DataFrame fillna works similar but we can specify an 
    axis along which fills take place..'''
df # Take a DataFrame..with missing values..


# In[27]:


''' Now filling missing values with another values clearly mentioning
    axis along which fill should to take palce..'''
df.fillna(method='ffill' , axis=1) ''' since there is no previous value in  2nd row's first value
                                      that is why NaN remained as it is..'''


# In[30]:


''' Now filling missing values with another values clearly mentioning
    axis along which fill should to take palce..'''

''' since there is no previous value in  2nd row's 
    first value that is why NaN remained as it is..'''

df.fillna(method='ffill' , axis='columns') 


# In[28]:


''' Now filling missing values with another values clearly mentioning
    axis along which fill should to take palce..'''

''' since there is no previous value in  2nd column's 
    first value that is why NaN remained as it is..''' 

df.fillna(method='ffill' , axis=0)


# In[33]:


''' Now filling missing values with another values clearly mentioning
    axis along which fill should to take palce..'''

''' since there is no previous value in  2nd column's 
    first value that is why NaN remained as it is..''' 

df.fillna(method='ffill' , axis='rows')  # used to check if axis=0 is row or column


# # Combining Datasets : Series and DataFrame 

# In[2]:


''' Here we will do simply do concatenation of Series and DataFrame
    with the pd.concat() function '''
# for this we created a df to use here...

def make_df(cols,ind):
    '''Making a DataFrame Quikly..'''
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    
    return pd.DataFrame(data,ind)


# In[3]:


# Take a DataFrame..
make_df('ABC',range(3))


# In[40]:


# Creating an empty dataframe...
pd.DataFrame(data=np.nan,columns=['A','B'],index=[0,1,2]) 


# In[38]:


# Concatenation in Numpy array...
x=[1,2,3]
y=[4,5,6]
z=[7,8,9]
np.concatenate([x,y,z])


# In[41]:


''' First argument is either tuple or list in concatenation funs additionally
    it takes axis= 0 or 1 which allows us to cancatenate along that axis...'''
x=[[1,2],[3,4]] # This is 2D list..
x        


# In[42]:


np.concatenate([x,x], axis=1) # this is column wise concated


# In[47]:


# taking a 2D array...
y=np.array([[1,2,3],[4,5,6]])
y


# In[48]:


# concatenating two 2D arrays
np.concatenate([y,y], axis=1)


# In[49]:


np.concatenate([x,y]) # we can not cancat 1D and 2D array...


# In[43]:


''' Simple Concatenation with pd.cancat() of Series Object and 
    DataFrame in pandas...'''
ser1=pd.Series(['A','B','C'], index=[1,2,3])
ser2=pd.Series(['D','E','F'], index=[4,5,6])
pd.concat([ser1,ser2])


# In[46]:


''' pd.Concat() is also used with DataFrame... '''
df1=make_df('AB',[1,2])
df2=make_df('AB',[3,4])
print(df1);print(df2)


# In[45]:


# Concatenating two DataFrame..
print(pd.concat([df1,df2]))


# In[52]:


''' By default concatenation takes place row wise but we can specify
    axis to concate along that axis..'''
df3=make_df('AB', [0,1])
df4=make_df('CD', [0,1])
print(df3);print(df4)


# In[56]:


# Now concatenating along an axis...
pd.concat([df3,df4], axis='columns') # clearly write columns or rows for axis..


# In[59]:


# Now concatenating along an axis...
pd.concat([df3,df4], axis=1) # clearly write columns or rows for axis..


# In[60]:


# Now concatenating along an axis...
pd.concat([df3,df4], axis='rows') # clearly write columns or rows for axis..


# In[61]:


# Now concatenating along an axis...
pd.concat([df3,df4], axis=0) # clearly write columns or rows for axis..


# In[63]:


# By default concatenation takes place row wise.
pd.concat([df3,df4]) 


# In[69]:


'''Now concatenating along an axis., major difference btw np.conactenatoon and pd.concat
   is that pandas preserve indices even if result will have dublicate indices.'''
 

x1=make_df('AB', [1,2])
y1=make_df('AB', [3,4])
y1.index = x1.index # make duplicate indices..
print(x1);print(y1)


# In[71]:


pd.concat([x1,y1]) # repeated indices in result but pd.concat() gives us few ways to handle it.


# # Catching the Repeats As an Error :

# In[74]:


''' In order to check if indices dont overlap in result of pd.concat() just use
    verify_integrity flag,with this set as TRUE ,concat will raise an exception
    if there are duplicate indices..'''
try:
    pd.concat([x1,y1], verify_integrity=True)
except ValueError as e :
        print("Exception Raised : ", e) # Catching duplicate indices..


# In[75]:


''' Another way to solve duplicate indices problem is by using ignore_index=True,
    now concat() will create a new integer index'''

print(x1);print(y1)


# In[76]:


# now concatenating and ignoring index...
print(pd.concat([x1,y1], ignore_index=True))


# In[77]:


''' Another way is to keys to label Data sources, reslt will be hierarchically 
    indexed series containing the data'''
print(pd.concat([x1,y1], keys=['x1','y1']))


# # Combining Dataset: Concatenation with joins

# In[78]:


''' How pd.concat() performs its function if not all columns are same in two df'''

df5=make_df('ABC',[1,2])
df6=make_df('BCD',[3,4])
print(df5);print(df6)


# In[80]:


''' By default concatenation using join is union of input columns that is
    join('outer') but we can change this to intersection of columns using
    join('inner')..'''
print(pd.concat([df5,df6])) # missing values are displayed as NaN


# In[82]:


''' Intersection of columns means only those columns which is present in both dataframe'''
print(pd.concat([df5,df6], join='inner')) # inner for intersection


# In[83]:


''' Another way to join is by specifying the index of columns using join_axes argument'''

print(df5);print(df6)


# In[84]:


''' Concatenating by specifying columns of DataFrame..'''
print(pd.concat([df5,df6],join_axes=[df5.columns]))


# In[85]:


''' Concatenating by specifying columns of DataFrame..'''
print(pd.concat([df5,df6],join_axes=[df6.columns]))


# In[87]:


''' The same concatenation can be done using the append() in few key strokes
    but append() is applicable to only single dataframe,object or elemnet.
    With below example we get clear picture about it..'''

print(df1);print(df2)


# In[89]:


''' Now using append() to concatenate them but we cannot append more than 
    one df to another df. As in concat() we can pass multiple df to concat them'''
print(df1.append(df2))
print(df2.append(df1)) # 


# # Combining Datasets: Merge and Join

# In[4]:


''' pd.merge() is applied on a number of types of joins: one-to-many,many-to-one,
    many-to-many joins..To merge two DataFrame atleast one column has to be common '''

df1=pd.DataFrame({'empolyee':['Wamique','Santosh','Narendra','Narsimha','Shruti'],
                 'group':['Msc','B.Tech','Msc','M.Tech','B.Tech']})

df2=pd.DataFrame({'empolyee':['Pradeep','Ravi','Wamique','Santosh','Ajaz'],
                 'year':[2018,2005,2016,2013,2011]})

print(df1);print(df2)


# In[5]:


df3=pd.merge(df1,df2) # merge() gives intersection..
df3


# In[6]:


df4=pd.DataFrame({'group':['Msc','B.Tech','M.Tech'],
                  'supervisor':['C.R. Rao','P.S.Bimra','S.S Ravi']})
print(df4)


# In[7]:


'''In many-to-one join of DataFrame one of the two key columns must
   contain Duplicate entries,then result is many to one merge....'''
pd.merge(df3,df4)


# In[8]:


''' In many-to-many join of DataFrame if key columns in both left and right 
     dataframe contains Duplicate entries, then result is many to many merge'''

df5=pd.DataFrame({'group':['Msc','M.Tech','B.Tech','B.Tech','Msc','Msc'],
                  'skills':['Python','R','Python','SQL','SQL','R']})
df5


# In[9]:


print(df1)


# In[10]:


'''In this way we can merge many to many dataframe...'''
print(pd.merge(df1,df5))


# In[11]:


'''Merging using explicitly key word name column, which is common in both dataframe..'''
print(pd.merge(df1, df2, on='empolyee'))


# In[13]:


''' Now merging using two different column names,here we use left_on and
    right_on to specify the two column names.. '''

df6=pd.DataFrame({'empolyee':['Wamique','Santosh','Narendra','Narsimha','Shruti'],
                'group':['Msc','B.Tech','Msc','M.Tech','B.Tech']})

df7=pd.DataFrame({'name':['Pradeep','Ravi','Wamique','Santosh','Ajaz'],
                'year':[2018,2005,2016,2013,2011]})

print(df6);print(df7)


# In[14]:


''' merging with key column name from each df..'''
print(pd.merge(df6, df7, left_on='empolyee', right_on='name'))


# In[15]:


''' Here column 'name' from df13 is droped and only common rows are 
    displayed with all column values'''
print(pd.merge(df6, df7, left_on='empolyee', right_on='name').drop('name',axis=1))


# In[16]:


''' Here column 'empolyee' from df14 is droped and only common rows are 
    displayed with all column values'''
print(pd.merge(df6, df7, left_on='empolyee', right_on='name').drop('empolyee',axis=1))


# In[17]:


''' Rather than merging on a column we can merge on an index.. '''

df1a=df1.set_index('empolyee')
df2a=df2.set_index('empolyee')
print(df1a);print(df2a) # now we can see empolyee names are actually index of df.


# In[18]:


'''Now Merging using index that is left_index and/or right_index in pd.merge()'''
print(pd.merge(df1a,df2a,left_index=True,right_index=True))


# In[57]:


print(pd.merge(df1a,df2a,right_index=True,left_on='empolyee'))


# In[3]:


print(pd.merge(df1a,df2a,left_index=True,right_on='name'))


# In[19]:


print(df1a.join(df2a)) # empolyee names of df1a came here


# In[20]:


print(df2a.join(df1a)) # empolyee names of df2a came here


# In[32]:


'''In this type of merge one common column is considered as Index for DataFrame'''
print(pd.merge(df1a,df2a, left_index=True,right_index=True))


# In[44]:


df6=pd.DataFrame({'empolyee':['Wamique','Santosh','Narendra','Narsimha','Shruti'],
                 'group':['Msc','B.Tech','Msc','M.Tech','B.Tech']})

df7=pd.DataFrame({'name':['Pradeep','Ravi','Wamique','Santosh','Ajaz'],
                 'year':[2018,2005,2016,2013,2011]})

print(df6);print(df7)


# In[54]:


print(pd.merge(df6,df7,left_on='empolyee',right_on='name'))


# In[23]:


df8=print(pd.merge(df6,df7,left_on='empolyee',right_on='name').drop('name',axis=1))


# In[28]:


print(df1a);print(df7)


# In[64]:


print(pd.merge(df1a, df7, left_index=True, left_on='name'))


# In[63]:


print(pd.merge(df1a, df7, left_index=True,right_on='name'))


# In[49]:


'''Specifying Set Arithematic for joins:'''

df9=pd.DataFrame({'name':['peter','paul','mary'],
                  'food':['fish','bean','bread']},
                 columns=['name','food'])
df10=pd.DataFrame({'name':['mary','joshep'],
                  'drinks':['wine','bear']},
                 columns=['name','drinks'])
print(df9);print(df10)


# In[50]:


print(pd.merge(df9,df10))


# In[51]:


''' Here we can specify clearly using how keyword'''
print(pd.merge(df9,df10,how='inner')) # meaning intersection


# In[52]:


print(pd.merge(df9,df10,how='outer')) # meaning union


# In[53]:


print(pd.merge(df9,df10,how='left')) # all names of df9 only and its coressponding rows


# In[55]:


print(pd.merge(df10,df9,how='left'))


# In[54]:


print(pd.merge(df9,df10,how='right')) # all names of df10 only and its coressponding rows


# # Overlapping Column Names: The Suffixes keyword

# In[65]:


'''There are cases when we have conflicting column names in two DataFrames'''
df1=pd.DataFrame({'name':['Bob','Jack','Lisa','Sue'],
                 'rank':[1,2,3,4]})
df2=pd.DataFrame({'name':['Bob','Jack','Lisa','Sue'],
                 'rank':[3,1,4,2]})
print(df1);print(df2)


# In[70]:


print(pd.merge(df1,df2,  on='name'))


# In[75]:


'''Now we can specify a custom name using suffixes keyword, it works
   even if there are multiple overlapping columns..'''
print(pd.merge(df1,df2,  on='name', suffixes=["_L", "_R"]))


# # Verctorized String Operations:

# In[76]:


''' NumPy Vectorization example.. '''
x=np.array([2,3,5,7,11,13])
x*2


# In[79]:


'''Introducing  Pandas string operation..'''
data1=['peter','Paul','MARY','gUIDo']
[s.capitalize() for s in data1]  # only first char of each word is capitalized


# In[80]:


''' Another example with missing value..'''
data2=['peter','Paul',None,'MARY','gUIDo']
[s.capitalize() for s in data2] # that means with missing value we canot perform this operation


# In[81]:


'''To over come missing value problem ,pandas included a feature 
   to tackle this via pandas Series object and index Object '''
names=pd.Series(data2)
names


# In[82]:


'''Applying pandas vectorization str methods..'''
names.str.capitalize()


# In[5]:


'''There are many Pandas string methods that we will use ,let take an example...'''
monte=pd.Series(['Graham Chapman','John Cleese','Terry Gilliam',
                'Eric Idle','Terry Jones','Michale Palin'])
monte


# In[84]:


monte.str.len()


# In[85]:


monte.str.lower()


# In[87]:


monte.str.startswith('T')


# In[88]:


monte.str.split()


# In[89]:


monte.str.split().str.get(-1)


# In[90]:


monte.str.extract('([A-Za-z]+)')


# In[91]:


'''finding all srtrings that starts with and ends with a consonant,
   making use of start of string(^) and end of string($)'''
monte.str.findall(r'^[^AEIOU].*[^aeiou]$')


# In[92]:


''' Vectorized items access and slicing.'''

monte.str[0:3]


# In[94]:


monte.str.slice(0,3)


# In[97]:


monte.str.get()?????


# In[6]:


monte


# In[98]:


monte.str[i]?????


# In[99]:


monte.str.split().str.get(-2)


# In[100]:


''' Indicator Variable..'''

full_monte= pd.DataFrame({'name':monte,
                        'info':['B|C|D','B|D','A|C','B|D','B|C','B|C|D']})
full_monte


# In[101]:


''' Getting dummies in DataFrame using get_dummies()'''
full_monte['info'].str.get_dummies('|')

