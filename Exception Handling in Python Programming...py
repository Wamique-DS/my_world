
# coding: utf-8

# # Exception Handling:Enables a program to deal with exceptions and continue    its normal execution.

# In[1]:


''' Errors That occured during run time is called Exception..'''
1/0  #  Gives zero division error,which is built in error


# In[3]:


open('love.txt') # It gives Error ,as it did not find any file with this name...


# In[4]:


import Silicon # Here Module is not found that's why it gives error


# In[9]:


# let's take an example to demonstrate  exception handling... 
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=a/b
print("Result=",c)  # here it gives zero division error


# In[16]:


''' Exception problem can be solved using (Try with Except) within the body of program'''

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
try:
    c=a/b
    print("Result=",c) 
except:
    print("Exception is Raised") # if b is equal to zero 


# In[20]:


# import module sys to get the type of exception
import sys
randomList = ['a', 0,'1.3',2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)


# In[22]:


# Pass just passes the control forward if condition is True...
x=20
if x>10:
    pass
else:
    print("Value is greater than 10")


# In[23]:


#
x=0
if x>10:
    pass
else:
    print("Value is lesser than 10")


# In[29]:


'''Excepton are raised when corresponding errors occur during run time,
   but we can forecfully raise it using Keyword raise '''

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
            print(ve)


# In[ ]:


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
try:
    if b==0:
        raise ZeroDivisionError("Stupid, you gave Zero to denominator")
    else:
        c=a/b
        print("Result=",c) 
except ZeroDivisionError as ze:
    print()


# In[30]:


def main():
    try:
        num1,num2=eval(input("Enter two numbers separated by comma"))
        result=num1/num2
        print("Result=",result)
    except ZeroDivisionError:
        print("ZeroDivisionError is raised")
    except SyntaxError:
        print("SyntaxError is raised")
    except:
        print("Some thing went wrong")
    else:
        print("No Exceptions")
    finally:
        print("This is Compulsary Statement")
        
main()
        


# In[31]:


# SyntaxError raised as we used space instead of comma...
def main():
    try:
        num1,num2=eval(input("Enter two numbers separated by comma"))
        result=num1/num2
        print("Result=",result)
    except ZeroDivisionError:
        print("ZeroDivisionError is raised")
    except SyntaxError:
        print("SyntaxError is raised")
    except:
        print("Some thing went wrong")
    else:
        print("No Exceptions")
    finally:
        print("This is Compulsary Statement")
        
main()


# In[32]:


# Errors of different types raised...
def main():
    try:
        num1,num2=eval(input("Enter two numbers separated by comma"))
        result=num1/num2
        print("Result=",result)
    except ZeroDivisionError:
        print("ZeroDivisionError is raised")
    except SyntaxError:
        print("SyntaxError is raised")
    except:
        print("Some thing went wrong")
    else:
        print("No Exceptions")
    finally:
        print("This is Compulsary Statement")
        
main()


# In[33]:


# Error something went wrong dispalyed as we entered three nos. but it asked for only two nos.
def main():
    try:
        num1,num2=eval(input("Enter two numbers separated by comma"))
        result=num1/num2
        print("Result=",result)
    except ZeroDivisionError:
        print("ZeroDivisionError is raised")
    except SyntaxError:
        print("SyntaxError is raised")
    except:
        print("Some thing went wrong")
    else:
        print("No Exceptions")
    finally:
        print("This is Compulsary Statement")
        
main()


# In[37]:


# Result displayed as there is No Exception...
def main():
    try:
        num1,num2=eval(input("Enter two numbers separated by comma"))
        result=num1/num2
        print("Result=",result)
    except ZeroDivisionError:
        print("ZeroDivisionError is raised")
    except SyntaxError:
        print("SyntaxError is raised")
    except:
        print("Some thing went wrong")
    else:
        print("No Exceptions")
    finally:
        print("This is Compulsary Statement")
        
main()


# In[38]:


# Custom Exception: define Python user-defined exceptions 

class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError
       elif i_num > number:
           raise ValueTooLargeError
       break
   except ValueTooSmallError:
       print("This value is too small, try again!")
       print()
   except ValueTooLargeError:
       print("This value is too large, try again!")
       print()

print("Congratulations! You guessed it correctly.")

