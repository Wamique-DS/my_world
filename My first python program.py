
# coding: utf-8

# In[4]:


# Program to find Area of Triangle
l = float (input ('Enter lenght of trianlge: ')) # Input statement is used to enter values by user
b = float (input ('Enter breadth of triangle: ')) # Here values of respective sides of a triangle is entered 
h = float (input ('Enter height of triangle: '))
a = (l*b*h)
print ('Area of triangl is', a) # single quotes or double quotes can be used but python prefers single quotes.


# In[5]:


# Program to find Area of a Circle
import math           # import function is used to call a module

r = float (input ('radius of circle: '))
a = (math.pi*r**2)      # here we have used pi which is in math module              
print ('Area of circle is: ', a)


# In[12]:


# Program to calculate Area of a triangle with three sides

s = int (input('Enter the value of fisrt side: '))
t = int (input ('Enter the value of second side: '))
r = int (input ('Enter the value of third side: '))

 
p =float((s+t+r)/2)  #  Here Half perimeter is calculated
print ('Half perimeter  is:', p)

import math                           # import function is used to import math module        

area = math.sqrt(p*(p-s)*(p-t)*(p-r)) # square root function is imported from math module 

print ('Area of triangle with three sides  {0},{1},{2} is:'.format(s, t, r), area)


# In[14]:


# Program to convert given number into mins and seconds

x = int(input('Enter the number :'))
mins = int(x/60)            # Here minute is calculated             
print('Number of mins : ', mins)
secs = x%60                 # Here second is calculated
print('Number of seconds :', secs)


# In[15]:


# Program to calculate no. of yrs , months and days

x = int(input('Enter the number:'))
years= int (x/365)     # Here yrs calculated

print ('Number of year is:', years)
d = x%365              
months= int((d)/30)    # Here months calculated

print ('Number of month:', months)
days = d%30            # Here days calculated

print('Number of day:', days)


# In[18]:


# Program to calculate BMI for given weight in kgs and height in mts best BMI lies between 18.5 and 25

w = float (input('Enter the weight of body in kgs:'))
h = float (input ('Enter the height of body in feets:'))

hm = float(0.3048*h) # Here height is converted into mtrs from feets


BMI = float(w/hm**2) # Now Body Mass index is Calculated

print ('Your Body Mass Index is:', BMI)


# In[21]:


# Program to find Area of Right Angled Triangle

b = float (input('Enter breadth of right angled triangle: '))
h = float (input ( 'Enter height of right angle tringle: '))

a = (1/2*b*h)    # Here Area is calculated

print ('Area of right angled triangle:', a)


# In[22]:


# Program to find Area of Rectangle

l = float (input('Enter lenght of rectangle:'))
b = float (input('Enter breadth of rectangle:'))

a = (l*b)   # Here area is calculated

print ('Area of Rectangle is' ,a)


# In[24]:


# Program to convert temperature in Celcius into Fehrenhite

c = float(input('Enter the temperature in celcius :'))
f = float((c*1.8)+32)     # Fehrenhite is calculated using formula

print ('Temprature in fahrenhite is:' , f)


# In[27]:


# program to convert temperature in fahrenhite into celcius

f = float(input('Enter the temperature in fahrenhite:'))
c = float((f-32)/1.8)      # Here celcius is calculated 

print ('Tempreture in Celcius is:' , c)


# In[28]:


# Program to calculate Body Mass Index for given weight in kgs and height in mts best BMI lies between 18.5 and 25

w = float (input('Enter the weight of body in kgs:'))
h = float (input ('Enter the height of body in feets:'))

hm = float(0.3048*h)     # Converting feet into mts

BMI = float(w/hm**2)     # Calculating your BMI

print("Your BMI is : " , BMI)


if BMI<18.5:             # IF ELSE IS USED IN NESTED FORM
    print("Underweight")
elif BMI>=18.5 and BMI<24.9:
    print("Normal")
elif BMI>=24.9 and BMI<=30:
    print("Overweight")
else:
    print("Obese")


# In[1]:


# Program  to illustrate the use of  while statement

i=1           # i is assigned initial value 1

while i<=10:  # Here condition is checked whether i is less than or equal to 10.
    
    print(i)  # Using print statement i is printed.
    i+=1      # Here by simply changing the increament we can print numbers with any equal diffrences.


# In[2]:


# Program  to illustrate the use of  while statement

i=1           # i is assigned initial value 1

while i<=10:  # Here condition is checked whether i is less than or equal to 10.
    
    print(i)  # Using print statement i is printed.
    i+=2      # Here by simply changing the increament we can print numbers with any equal diffrences.


# In[10]:


# Program to find Multiplication Table of a number using while statment

n = int(input("Enter a number"))  # user asked to enter a number
i = 1                             # i is assinged a value 1

while i<=10:                     # i is cheked for whether it is less than or equal to 10.
    print (n,'*',i,'=',(n*i))    # Print statement is used to print
    i+=1                         # Each time i is incremented by 1.
        
                             


# In[11]:


# Program to illustrate the use of while ,if and break 

i=1           # i is assigned a value 1
while i<10:   # i is checked for less than 10
    
    if i==5:  # here if i value is equal to 5 then only braek works
        break  # all values before 5 is printed
        
    print(i)   
    i +=1      # i value is increamented by 1 each time till the if condition is satisfied


# In[12]:


# Program to illustrate the use of while ,if and break 

i=1           # i is assigned a value 1
while i<10:   # i is checked for less than 10
    
    if i==8:  # here if i value is equal to 5 then only braek works
        break  # all values before 5 is printed
        
    print(i)   
    i +=1      # i value is increamented by 1 each time till the if condition is satisfied


# In[13]:


# Program to illustrate the use of for , if & continue 

i=1                   # i is assigned a initial value 1
for i in range(1,11): # for statement is used with range function
    if i==5:          # if statement is used to check condition
        continue      # here if i value is equal 5 then continue acts and current iteration stops and next iteration is executed
    print(i)
    i+=1              # i value is increamented each time by 1  
        


# In[14]:


# Program to illustrate the use of for , if & continue 

i=1                   # i is assigned a initial value 1
for i in range(1,11): # for statement is used with range function
    if i==8:          # if statement is used to check condition
        continue      # here if i value is equal 5 then continue acts and current iteration stops and next iteration is executed
    print(i)
    i+=1              # i value is increamented each time by 1  

    


# In[15]:


# Program to illustrate the use of for,if and break statement
i=1                  # i is assigned a value 1
for i in range(1,11): # for statement is used 
    if i==5:          # if statement is used to check condition
        break         # if condition satisfies break works & iteration stops
    print(i)          # Here only values less tahn 5 is printed


# In[16]:


# Program for printing a range of no.s using for ,if and break statement
i=-5                 # i is assigned a value -5
for i in range(-5,5): # for statement is used 
    if i==5:        # if statement is used to check condition
        break       # here if i value is equal 5 then break statement terminates the loop . 
    print(i)        # value from -5 to 4 is printed


# In[18]:


# Program for printing a range of no.s using for,if nad break statement
i=-10                   # i is assigned a value -10
for i in range(-10,10): # for statement is used 
    if i==8:            # if statement is used to check condition
        break           # here if i value is equal 8 then break statement terminates the loop . 
    print( i,end=",")   # value from -10 to 7 is printed


# In[22]:


# Program to find which number is largest and smallest using if else statement

num1=int(input("Enter a number ")) # entering values using input statement
num2=int(input("Enter a number "))
num3=int(input("Enter a number "))

if num1>num2:                     # checks whether num1 is greater than num2
    if num1>num3:                 # checks whether num1 is greater than num3
        big=num1                  # if so biggest number is num1
        print("Biggest number is ", num1) # using print statement to print result
    else:                                  # else condition is used if above condition fails
        if num2>num3:           # checks whether num2 is greater than num3
            big=num2            # if so biggest number is num2
            print("Biggest number is ", num2) # result printed using print statement
        else:                    # else condition is used if above condition fails
            big=num3             # if so biggest number is num3
            print(" biggest number of three numbers is " ,  num3) # finally print biggest no. is num3 if all above conditions fail


# In[24]:


# Program to compute grade of a student in a exam using if  else statment

score=int(input("Enter a number :")) # enter a score
if score>=80:               # check whether score is greter than or equal to 80
    grade='A'               # grade is A
elif score>=70:             # if above condition fails this condition is checked 
    grade='B'               # if so grade is B
elif score>=60:             # if above condition fails this condition is checked
    grade='C'               # if so grae is C
else:                       # if all above conditions fail then 
    grade='F'               # grade is F which means student fail
print(" Your grade = ", grade) # using print statement respective grades were printed


# In[26]:


# Program to find prime number

num=int(input("Enter a number :")) # enter a number
i=1                    # i is assigned a value 1
factorcount=0          # initially factor is zero
while i<=num:          # check whether i is less than or equal to number
    if num%i==0:       # if remainder is zero then we get first factor
        factorcount+=1 # now we have one factor
    i+=1               # i value is increment by 1
if factorcount==2:     # if we get second factor
    print("prime")     # then print number is prime
else:                  # if above condition fails
    print("not prime") # print the number is not prime 


# In[27]:


# Program to find prime number

num=int(input("Enter a number :")) # enter a number
i=1                    # i is assigned a value 1
factorcount=0          # initially factor is zero
while i<=num:          # check whether i is less than or equal to number
    if num%i==0:       # if remainder is zero then we get first factor
        factorcount+=1 # now we have one factor
    i+=1               # i value is increment by 1
if factorcount==2:     # if we get second factor
    print("prime")     # then print number is prime
else:                  # if above condition fails
    print("not prime") # print the number is not prime 


# In[28]:


# Program to find prime number in a range of numbers

for num in range(1,101): # for statement is used 
    fcount=0            # we have zero factor
    i=1                 # i is assigned a value 1
    while i<=num:       # check whether i value is less than or equal to number
        if num%i==0:    # if remainder is zero then we get first factor
            fcount+=1   # now we have first factor
        i+=1            # i value is incremented by 1 
    if fcount==2:       # if we get second factor
        if i<=97:       # and if number is less than equal to 97
            print(num)  # print statment is used to print all numners between the given range 


# In[31]:


# Program to find prime number in a range of numbers

for num in range(1,101): # for statement is used 
    fcount=0            # we have zero factor
    i=1                 # i is assigned a value 1
    while i<=num:       # check whether i value is less than or equal to number
        if num%i==0:    # if remainder is zero then we get first factor
            fcount+=1   # now we have first factor
        i+=1            # i value is incremented by 1 
    if fcount==2:       # if we get second factor
        if i<=97:       # and if number is less than equal to 97
            print(num, end=",") # print statment is used to print all numners between the given range with comma
        else:
            print(num,end=".") # print last number wih fullstop.


# In[34]:


# Program to find a number is Armstrong number or not

num=int(input("Enter a number")) # a number is entered
num1=num                         # consider num1 is equal to num
s=0                              # initially sum is zero
while num>0:                     # check whether number is greater than zero 
    r=num%10                     # here  we get remainder 
    s=s*10+r                     # sum is calculated
    num=num//10                  # integer division is used
if s==num1:                      # check if our sum is equal to num1 
    print(" Armstrong Number")   # print given number is Armstrong number
else:                            # if above condition fails
    print("Not Armstrong Number")# print given number is not Armstrong numner


# In[35]:


# Program to find number is Armstrong number or not

num=int(input("Enter a number")) # a number is entered
num1=num                         # consider num1 is equal to num
s=0                              # initially sum is zero
while num>0:                     # chech whether number is greater than zero 
    r=num%10                     # here  we get remainder 
    s=s*10+r                     # sum is calculated
    num=num//10                  # integer division is used
if s==num1:                      # check if our sum is equal to num1 
    print(" Armstrong Number")   # print given number is Armstrong number
else:                            # if above condition fails
    print("Not Armstrong Number")# print given number is not Armstrong numner


# In[36]:


# Program to find number is palindrome or not

num=int(input("Enter a number :")) # a number is entered
num1=num                           # consider num1 is equal to num  
s=0                                # initially sum is zero
while num>0:                       # chech whether number is greater than zero 
    r=num%10                       # here  we get remainder
    s=s*10+r                       # sum is calculated
    num=num//10                    # integer division is used
if s==num1:                        # check if our sum is equal to num1
    print("Palindrome")            # print given number is Palindrome number
else:                              # if above condition fails
    print("Not palindrome")        # print given number is Palindrome number


# In[37]:


# Program to find number is palindrome or not

num=int(input("Enter a number :")) # a number is entered
num1=num                           # consider num1 is equal to num  
s=0                                # initially sum is zero
while num>0:                       # chech whether number is greater than zero 
    r=num%10                       # here  we get remainder
    s=s*10+r                       # sum is calculated
    num=num//10                    # integer division is used
if s==num1:                        # check if our sum is equal to num1
    print("Palindrome")            # print given number is Palindrome number
else:                              # if above condition fails
    print("Not palindrome")        # print given number is Palindrome number


# In[1]:


# Program to write in triangular order a series of stars

n= int(input("enter a number: ")) # a number is entered
for i in range(1, (n+1)):         # for statemnet is used to control flow of iteration between 1 and n+1
    for j in range(1,(i+1)):      # again for statement is used for j to control iteration
            print('*', end=" ")   # print statment used to print
    print()
        


# In[2]:


# Program to write in squar order a series of stars

n= int(input("enter a number: ")) # a number is entered
for i in range(1, (n+1)):    # for statement is used to control flow of iteration for i values
    
    for j in range(1,(n+1)): # for statement is used to control flow of iteration for j values
        print('*', end=" ")  # print statement is used to print output
    print()


# In[12]:


# Program to write in this order a series of stars
n= int(input("enter a number: "))
for i in range(1, (n+1)):
    for j in range(1,(n+1)):
        print('Datascience', end=" ")
    print()
    


# In[13]:


# Program to write in triangular order a series of stars

n= int(input("enter a number: ")) # enter a number
i=n                               # i ia assigned n values
while i>=1:                       # check whether given i value is greater than or equal to zero
    for j in range(1,(i+1)):      # for statment is used to control iteration for j values
            print('*', end=" ")   # print statment is used
    print()
    i-=1                          # negative increament is made each time in i value


# In[16]:


# program to display matrix multiplication

n=int(input(" Enter a number : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j ,end=" ")
    print()


# In[18]:


# Program to write lenth of  a word and its reverse

w = 'WAMIQUE'
print("length of the word is : " ,len(w)) # length function is used
a = w[0]+w[1]+w[2]+w[3]+w[4]+w[5]+w[6]
b = w[6]+w[5]+w[4]+w[3]+w[2]+w[1]+w[0]
print('word is', a)                      # word in its original order is printed
print('word in reverse order is', b)     # word in its reverse order is printed

