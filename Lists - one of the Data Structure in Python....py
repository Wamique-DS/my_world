
# coding: utf-8

# # Lists: One of the Type Of Data Structure in Python

# In[2]:


''' Lists: Collection of values in square bracket,elements in a list are  separated by 
    comma and enclosed within a square bracket.Elements can be of samne or mix type,
    list is a sequence of any elements and it's mutable as well..'''
list1=list() # Create an empty list.
print(list1)


# In[11]:


list2=list([2,8,4,6,3]) # Create a list with elements 2,8,4,6,3.
print(list2) 


# In[4]:


list3=list(["Green","White","Red"]) # Create a list with strings
print(list3)


# In[10]:


list4=list(range(3,6)) # Create a list with range
print(list4)


# In[14]:


# list can be created in simple way like this as well....this shows that list can contain mix type as well.
list6=[2,3,"A",'abc',8]
print(list6)


# In[27]:


list5=list("abcd") # Create a list with Character a,b,c,d
print(list5)


# In[29]:


list=["Wamique",6,3.5]
print(list)


# In[1]:


list7=list("Wamique")
print(list7)


# In[4]:


list8=list("hussain")
print(list8)


# In[5]:


# Function for lists..
max(list2)


# In[13]:


list9=[1,5,"Wamique","234",90.0]
print(list9)


# In[22]:


# Mutable meaning that we can change values.....
list9[1]=7
print(list9)


# In[24]:


list9=[1,5,"Wamique","234",90.0]
for x in list9:
    print(x)


# In[26]:


names=["Wamique","Ajaz","lala","Harsha"]
for name in names:
    print(name,"Please get up. class is getting over")


# In[27]:


names=["Wamique","Ajaz","lala","Harsha"]
for index in range(0,len(names)):
    print(names[index],"Please getup. class is getting over")


# In[31]:


# Below comparing 2 lists....which is compared in lexicographical order
list1 = ["green", "red", "blue"]
list2 = ["red", "blue", "green"]
print(list2 == list1)
print(list2 != list1)
print(list2 >= list1)
print(list2 > list1)
print(list2 < list1)
print(list2 <= list1)


# In[43]:


list11=[1,5,6,9]
list12=[1,5,6,0]
list11<list12


# In[46]:


'''List Comprehension provides a concise way to create a sequential list of elements '''
list1 = [x for x in range(5)] # Returns a list of 0, 1, 2, 3, 4

print(list1)


# In[50]:


list2=[0.5*x for x in range(5)]
print(list2)


# In[51]:


list3 = [x for x in list2 if x < 1.5]
print(list3)


# In[82]:


''' List methods:Once a list is created, We can use the list class’s methods  to manipulate the list'''
list1 = [2, 3, 4, 1, 32, 4]
print(list1)
list1.append(19)
print(list1)
list1.insert(1, 25) # Insert 25 at position index 1

print(list1)
list1.index(4) # Return the index of number 4
print(list1.index(4)) 

list2 = [99, 54]
print(list2)
list1.extend(list2)
print(list1)
list1.remove(32)# Remove number 32

print(list1)


# In[77]:


list1.count(4) # Return the count for number 4

print(list1)


# In[86]:


print(list1)
list1.pop(2)
print(list1)


# In[88]:


print(list1)
list1.pop()
print(list1)


# In[96]:


list=[2,34,56,32,4]
print(list)
list.pop() # it delets the last element from list
print(list)


# In[99]:


list=[2,4,8,5,9,34,23]
print(list)
list.reverse()
print(list)


# In[102]:


list=[9,23,54,12,5,87,43,30,1]
print(list)
list.sort()
print(list)


# In[2]:


list12=list([2,5,3,9,8,11,16,25])
list12
for x in range(0,len(list12),2):  # gives values of odd no. position in list..
    print(list12[x])


# In[109]:


'''Spiliting a string into a list'''
msg="Wamique is a good boy, do not belive him...Heee"
msg.split()


# In[110]:


Today="17/08/2018"
Today.split()


# In[4]:


'''Inputting Lists : These are three ways of creating a list,in first values 
   are given directly but in last one valye sare given by Keyboard '''

list1=list([12,45,36])
print(list1)


# In[113]:


list2=[12,45,36]
print(list2)


# In[117]:


list3=[]
for x in range(4):
    ele=int(input("Enter Element"+str(x)))
    list3.append(ele)
print(list3)


# In[118]:


numbers=input("Enter numbers separated by space")
list4=numbers.split()
print(list4)


# In[129]:


def LeftShift(lst):
    tmp=lst[0]
    count=len(lst)
    for i in range(1,count):
        lst[i-1]=lst[i]
    lst[count-1]=tmp
    return lst

list1=[8,56,83,99,102]
list1=LeftShift(list1)
print(list1)


# In[130]:


'''Copying a list'''
list1=[16,78,85]
list2=[]+list1
print(list2)


# In[6]:


'''Passing and Returing a list to a function'''
def LeftShift(lst):
    tmp=lst[0]
    count=len(lst)
    for i in range(1,count):
        lst[i-1]=lst[i]
    lst[count-1]=tmp
    return lst

list1=[8,56,83,99,102]
list1=LeftShift(list1)
print(list1)


# In[7]:


# Concept of Copying....
list1=[16,78,98]
list2=[23,56]
print(id(list1))
print(id(list2))
list2=list1 # list2 is assigned list1
print(id(list2))# only refrence is copied not the value.
print(list2)


# In[9]:


# Another way to copy a list is...
list1=[16,78,98]
list2=[]+list1
print(list2)


# In[1]:


def add(x, lst=[]):
    if x not in lst:
        lst.append(x)
        
    return lst
def main():
    list1=add(1)
    print(list1)
    
    list2=add(2)
    print(list2)
    
    list3=add(3,[11,12,13,14]) # it add 3 to this list [11,12,13,14]
    print(list3)
    
    list4=add(4)
    print(list4)
    
main()


# In[9]:


def printlist(lst):
    for ele in lst:
        print(ele)
        
list1=[10,90,0,98,111]
printlist(list1)


# In[11]:


def main():
    n=10
    lst=[10,90,54]
    sample(n,lst)
    print(n)
    print(lst)
    
def sample(n,lst):
    n=99
    lst[0]=88
    
main()


# In[21]:


''' Searching a List: There are two types of search (1)Linear Search & (2)Binary Search'''

def linearSearch(lst,key):
    n=len(lst)
    found=False
    for i in range(0,n):
        if lst[i]==key:
            pos=i
            found=True
            break
    if found:
        print("Element found at position",pos)
    else:
        print("key is not found")
            
list1=[12,45,32,98,76,56,43,98,66]
k=98
linearSearch(list1,k)


# In[22]:


def linearSearch(lst,key):
    n=len(lst)
    found=False
    for i in range(0,n):
        if lst[i]==key:
            pos=i
            found=True
            break
    if found:
        print("Element found at position",pos)
    else:
        print("key is not found")
            
list1=[12,45,32,98,76,56,43,98,66]
k=99
linearSearch(list1,k)


# In[43]:


def BinarySearch(lst,key):
    n=len(lst)
    low=0
    high=n-1
    found=False
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==key:
            found=True
            pos=mid
            break
        elif key>lst[mid]:
            low=mid+1
        else:
            high=mid-1
    if found:
        print("Key is found at position", pos)
    else:
        print("The key is not found")
            
            
list1=[13,45,76,98,890]
k=98
BinarySearch(list1,k)
            


# In[44]:


def BinarySearch(lst,key):
    n=len(lst)
    low=0
    high=n-1
    found=False
    while low<=high:
        mid=(low+high)//2
        if lst[mid]==key:
            found=True
            pos=mid
            break
        elif key>lst[mid]:
            low=mid+1
        else:
            high=mid-1
    if found:
        print("Key is found at position", pos)
    else:
        print("The key is not found")
            
            
list1=[13,45,76,98,890]
k=100
BinarySearch(list1,k)
            


# # Two Dimensional List :

# In[45]:


''' TWo Dimensional List: List That Contains other Lists as its elements'''
rows=int(input("Enter number of rows"))
cols=int(input("Enter number of columns"))
matrix=[]

for i in range(0,rows):
    matrix.append([])
    for j in range(0,cols):
        ele=int(input("Enter element for row"+str(i)+",column"+str(j)))
        matrix[i].append(ele)
        
print(matrix)


# In[6]:


import random
matrix=[]
rows=int(input("Enter number of rows"))
cols=int(input("Enter number of columns"))


for row in range(rows):
    matrix.append([])
    for column in range(cols):
        matrix[row].append(random.randint(0,99))
        
print(matrix)


# In[8]:


matrix[3][3]


# In[1]:


import random
rows=int(input("Enter number of rows"))
cols=int(input("Enter number of columns"))
matrix=[]

for i in range(0,rows):
    matrix.append([])
    for j in range(0,cols):
        ele=random.randint(0,99)
        matrix[i].append(ele)
        
print(matrix)


# In[2]:


list2D=[[12,43,65,43],[19,87,54,77],[20,37,63,90]]
print(len(list2D))
print(len(list2D[0]))


# # Accessing TWo-Dimensional List....

# In[3]:


list2D=[[12,43,65,43],[19,87,54,77],[20,37,63,90]]
rows=len(list2D)
cols=len(list2D[0])

for i in range(0,rows):
    for j in range(0,cols):
        print(list2D[i][j])
    print()


# In[4]:


list2D=[[12,43,87,99],[19,87,54,77],[20,37,63,90]]
rows=len(list2D)
cols=len(list2D[0])

for i in range(0,rows):
    for j in range(0,cols):
        print(list2D[i][j],end="\t")
    print()


# In[5]:


# Finding total of the matrix...
matrix = [[1,2,3],[4,5,6],[7,8,9]]
total=0
for row in matrix:
    for value in row:
        total+=value
        
print("Total is ",total)


# In[9]:


matrix = [[1,2,3],[4,5,6],[7,8,9]]
for column in range(len(matrix[0])):
    total=0
    for row in range(len(matrix)):
        total +=matrix[row][column]
    print("Sum for columns", column,"is",total) # print sum for columns indivisually


# In[10]:


matrix[0][0] # accessing element at 0th row and 0th column from above matrix...


# In[11]:


# Finding row with maximum sum...
matrix=[[1,2,3],[4,5,6],[7,8,9]]
maxRow=sum(matrix[0])
indexofMaxRow=0

for row in range(1,len(matrix)):
    if sum(matrix[row])>maxRow:
        maxRow=sum(matrix[row])
        indexofMaxRow=row
        
print("Row",indexofMaxRow,"has the maximum sum of",maxRow)


# In[12]:


import random
matrix=[[1,2,3],[4,5,6],[7,8,9]]

for row in range(len(matrix)):
    for j in range(len(matrix[row])):
        i=random.randint(0,len(matrix)-1)
        j=random.randint(0,len(matrix[row])-1)
        matrix[row][column], matrix[i][j]=        matrix[i][j],matrix[row][column]

print(matrix)


# In[14]:


points=[[4,2],[1,7],[4,5],[1,2],[1,1],[4,1]] # lets take lists within list
points.sort()                                  # sorting lists
print(points)

