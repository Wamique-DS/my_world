
# coding: utf-8

# # FUNCTIONS AND MODULES

# In[1]:


# Function that does not return a value is known as void function ,here it's calculate.

def Calculate(h,w):  
    
    hm=(0.3048*h)
    bmi=w/hm**2
    print(round(bmi,2))
   
    if bmi<18.5:
        print("underweight") 
    elif bmi>=18.5 and bmi<24.9:
        print("Normal") 
        
    elif bmi>=24.9 and bmi<=30:
        print("overweight") 
    else:
        print("Obese")


# In[2]:


# Calling function more than once but defining only once....

h=eval(input("enter your height :"))  
for w in range(50,70):
    Calculate(h,w)
    print("bmi is ")


# In[6]:


# print grade for score...This is another example of Function that does not return a value..
def printGrade(score):
    if score >=90.0:
        print('A')
    elif score >=80.0:
        print('B')
    elif score >=70.0:
        print('C')
    elif score >=60.0:
        print('D')
    else:
        print('F')
        
def main():
    score=eval(input("Enter your score:"))
    print("The Grade is ", end=" ")
    printGrade(score)


# In[7]:


main() # Now calling the main () function....


# In[10]:


# Let's take an example of positional Argument...
def nprintln(message,n):
    for i in range(n):
        print(message)
        
nprintln('Wamique',3)


# In[11]:


def nprintln(message,n):
    for i in range(n):
        print(message)
        
nprintln(3,'Wamique') ''' since in positional agr we need to pass arg with same
                          position otherwise it will give error '''


# In[12]:


# let's take an example of Keyword Argument...in this order of passing agrument does not matter
def nprintln(message,n):
    for i in range(n):
        print(message)
        
nprintln(n=3,message='Wamique')


# In[19]:


# We can mix both argument in a function but positional argument can't appear after keyword argument.
def f(p1,p2,p3):
    print(p1,p2,p3)
    
f(10,p2=30,p3=80)
   


# In[20]:


def f(p1,p2,p3):
    print(p1,p2,p3)
    
f(p2=30,p3=80,10) # here it displays error as positional can't appear after keyword argument 
   


# In[38]:


# program to illustrate function with agrs and with return value

def add2(num1,num2): # with agruments
    num3=num1+num2     
    return num3      # with return value

x=10                 # statement 
y=20                 #statement
z=add2(x,y)          # calling function
print("result=", z)    


# In[39]:


# program to illustrate function without agruments and with return value

def add2():
    num1=10
    num2=20
    num3=num1+num2
    return num3

ans=add2()
print("result=", ans)


# In[40]:


# program to illustrate function with agrs and without return value

def add2(num1,num2):
    num1=10
    num2=20
    num3=num1+num2
    print("result=", num3)
    
x=10
y=20
add2(x,y)


# In[41]:


# program to illustrate function without agrs and without return value

def add2():
    num1=10
    num2=20
    num3=num1+num2
    print("result=", num3) # No return value so we print here
    
add2()              # since no agrs and no return value


# In[42]:


# we can do above program like this also without return value

def add2(num1,num2):
    num3=num1+num2
    print("Result=",num3)
    
a=int(input("enter first number"))
b=int(input("Enter Second Number"))
add2(a,b)


# # The Scope Of Variables...i.e Global and Local Variables

# In[21]:


x=1
if x<0:
    y=-1
else:
    y=1
print("y is",y)


# In[22]:


globalvar=1
def  f1():
    localvar=2
    print(globalvar)
    print(localvar)
    
f1()
print(globalvar)
print(localvar)  '''out of scope, so this gives error. i.e we can access global var 
                    anywhere but local var only inside the function only in which it is defined '''


# In[23]:


x=eval(input("Enter a number :"))
if x > 0:
    y = 4
    
print(y)  # This gives an error if y is not defined....


# In[28]:


x=1
def f1():
    x=2
    print(x) # it displays 2
    
f1()
print(x) # it displays 1


# In[30]:


x=1
def increase():
    global x
    x=x +1
    print(x) # displays 2
    
increase()
print(x) # displays 2


# # Default Arguments in a Function

# In[32]:


def printArea(width=1, height=2):
    area=width*height
    print("width:",width,"\theight:",height,"\tarea:",area)
    
printArea()


# In[33]:


printArea(4.5,3.9) # Positional Arguments


# In[34]:


printArea(width=5, height=6) # Keyword Arguments


# In[35]:


printArea(width=2.5) # here height is default Argument which is = 2


# In[36]:


printArea(height=5) # here width is default which is = 1


# # Returing Multiple Values....

# In[37]:


def sort(num1,num2):
    if num1<num2:
        return num1,num2
    else:
        return num2,num1
    
n1,n2 = sort(4,1)
print("n1 is :", n1)
print("n2 is :", n2)
        


# In[43]:


# program to illustrate Returning multiple values

def arithematic(a,b):
    return a+b,a-b,a*b,a/b,a//b,a%b

total,diff,product,quo1,quo2,rem=arithematic(7,3)
print(total,diff,product,quo1,quo2,rem)


# # Throwaway Variable....

# In[44]:


# throwaway used to ignore a value...here _ is used to throw a value..if we want single value to ignore.

# program to illustrate the use of 'underscore' as through away variable

def arithematic(a,b):
    return a+b,a-b,a*b,a/b,a//b,a%b

total,_,product,quo1,_,rem=arithematic(7,3)
print(total,product,quo1,rem)


# In[45]:


# In order to ingore multiple values we use _ along with * ,to throwaway multiple values...
# program to illustrate the use of  ' *_ ' for multiple unpacking

x,*_,y=(1,2,3,4,5)
print(x,y)
print(_)


# In[46]:


# program to illustrate the use of  ' *_ ' for multiple unpacking

*_,x,y=(1,2,3,4,5)
print(x,y)
print(_)


# In[47]:


# program to illustrate the use of  ' *_ ' for multiple unpacking

x,y,*_=(1,2,3,4,5)
print(x,y)
print(_)


# In[48]:


# programe to illustrate use of range
for x in range(10):
    print(x)
    


# In[49]:


# program to illustrate the use of underscore
for _ in range(10):
    print ("hello world")


# # Recursion...A Function that calls itself and it works with a base condition, In order to avoid calling itself infinitely....

# In[50]:


# program to illustrate the use of recurssion

def fact(n):
    
    if n==1:      # Recurssion occurs iff this condition is false
        return 1
    else:
        return n*(n-1)
    
print("Ans=",fact(5))


# In[51]:


# program to illustrate the us of recurssion

def fact(n):
    
    if n==1:      # Recurssion occurs iff this condition is false
        return 1
    else:
        return n*(n-1)
    
    
n=int(input("Enter a number:"))
ans=fact(n)
print("factorial value=", ans)


# In[52]:


# program to find fibonacci series(0 1 1 2 3 5 8....)using recurssion 
def fibo(n):
    if n <= 1:  # since we have to go till f(0) taht is why <= condition used
        return n
    else:
        return (fibo(n-1) + fibo(n-2))
    
print("fibo(5) =",fibo(5))


# In[53]:


# program to find sereis in fibonoic series in given range
def fact(n):
    
    if n==1:      # Recurssion occurs iff this condition is false
        return 1
    else:
        return n*(n-1)
    
    
for n in range(20):
    print(fibo(n),end=" ")
    


# In[54]:


# program to find sum of natural numbers

def sum_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_natural(n-1)
    
    
n=int(input("enter a number"))
print("sum_natural(n)=", sum_natural(n))


# # Modules:A file containing Python statements and definations...eg. MyMath.py is called module and its module name is MyMath

# In[56]:


# Module is defined inorder to call it in different function without the need to define it again and again...

# Creating own module

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2


# In[59]:


# I defined my module MyMath, which i called here without defining it again an again....this is the beauty of module.
import MyMath
print(add(2,4))
print(sub(9,3))
print(mul(5,6))
print(divide(10,2))


# In[60]:


dir(MyMath) # we can check all names that are defined inside my module i.e MyMath using dir().

