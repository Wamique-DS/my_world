
# coding: utf-8

# # Objects and Classes in Python :

# In[36]:


''' Concept of OOP in Python focuses on reating reusable code.
    This concept is also known as DRY(Don't Repeat Yourself) '''
# first of all we defined a function which is a class...
class MyClass:
    "This is my second class"
    a=10
    def func(self):
        print("Hello")
        
# we created an object from the above class...it can be printed in either way.  

ob=MyClass
print(ob.func)      
print(MyClass.func)


# In[41]:


# Create a Student class then object from the Student Class....

class Student:   # first off all we define class named as student
    def getData(self,rnum,name,marks):  # here fields used rollno ,name & marks.
        self.rnum=rnum
        self.name=name
        self.marks=marks
    def printData(self):
        print("Roll number =",self.rnum)
        print("Name = ",self.name)
        print("Marks =",self.marks)
        
s1=Student()     # Here we created an object from the above class named as student s1
s1.getData(1,"Wamique",80)  # with specific rollno, name amd marks.
s1.printData()


# In[49]:


# Create a class Circle and objects from it...
import math                  # math module is imported inorder to use pi
class circle:                # first off all we define class named as Circle
    def radius(self,radius):
        self.radius=radius
    def CalculateArea(self): # here feild used is radius
        return math.pi*self.radius*self.radius   # return is used to get the result back
    def CalculateCircumference(self):
        return math.pi*self.radius

c1=circle()    # Here we create two objects from the above class circle
c1.radius(10)   # namely c1 & c2
print("Area of circle 1 =",round(c1.CalculateArea(),2))    # here we calculated Area
print("Circumference of circle 1 =",round(c1.CalculateCircumference(),2)) # here we calculated circumference 

c2=circle()
c2.radius(15)
print("Area of circle 2 =",round(c2.CalculateArea(),2))
print("Circumference of circle 2 =",round(c2.CalculateCircumference(),2))


# In[50]:


# Create an Employee Class and different objects from it...
class Employee:
    def getData(self,EmpId,Name,Basic):
        self.EmpId=EmpId
        self.Name=Name
        self.Basic=Basic
    
    def printData(self):
        print("Employee Id=",self.EmpId)
        print("Name=",self.Name)
        print("Basic=",self.Basic)
    def calculateSalary(self):
        HRA=self.Basic*(20/100)
        DA=self.Basic*(35/100)
        PF=self.Basic*(12/100)
        Gsalary=self.Basic+HRA+DA+PF
        Tax=Gsalary*(10/100)
        Netsalary=Gsalary-Tax
        print("Housing rent allownace ", HRA)
        print("Dearness Allowance",DA)
        print("Provident fund ",PF)
        print("Gross Salary= ",Gsalary)
        print("Tax deducted= ",Tax)
        print("Net Salary= ",Netsalary)
        
E1=Employee()      # Here created an object Employee E1
E1.getData(1,"wamique",35000)
E1.printData()
E1.calculateSalary()



# In[51]:


# Create a Complex Class and different Objects from that Class..
class Complex:
    def getData(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def printNumber(self):
        print(self.real,"+i",self.imaginary)
    
c1=Complex()
c1.getData(1,2)
c1.printNumber()
c2=Complex()
c2.getData(3,6)
c2.printNumber()


# In[52]:


# Create a Complex Class and different Objects from that Class...then add two complex numbers.
class Complex:
    def getData(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def printNumber(self):
        print(self.real,"+i",self.imaginary)

        
def addComplex(c1,c2):
    result=Complex()
    result.real=c1.real+c2.real
    result.imaginary=c1.imaginary+c2.imaginary
    return result
c1=Complex()
c1.getData(1,2)

c2=Complex()
c2.getData(3,6)

c3=addComplex(c1,c2)
c3.printNumber()


# In[53]:


# Use of Constructors __init__() in Python Programming
class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def printNumber(self):
        print(self.real,"+i",self.imaginary)
    
c1=Complex(1,2)

c1.printNumber()
c2=Complex(3,6)

c2.printNumber()


# In[54]:


''' Use of Constructors __init__() in Python Programming..,This special function  
    gets called whenever a new Object of that calss is instantiated'''
class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def printNumber(self):
        print(self.real,"+i",self.imaginary)

        
def addComplex(c1,c2):  
    result=Complex(0,0)  # this is dummy that is passed (0,0)
    result.real=c1.real+c2.real
    result.imaginary=c1.imaginary+c2.imaginary
    return result
c1=Complex(1,2)
c2=Complex(3,6)

c3=addComplex(c1,c2)
c3.printNumber()


# In[ ]:


# Any attributes of an Object can be deleted any time ,using del statement. 
class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def printNumber(self):
        print(self.real,"+i",self.imaginary)
    
c1=Complex(1,2)

c1.printNumber()


# In[55]:


del c1.real


# In[56]:


c1.printNumber() # AttributeError as we have deleted real attribute from class Complex


# In[58]:


del Complex.printNumber # here we deleted the function


# In[59]:


c1.printNumber # Again error dislayed as we have deleted the function printNumber()


# In[60]:


c1


# In[61]:


del c1 # here we deleted an object namely c1.


# In[62]:


c1 # Error displayed as c1  object is deleted 


# In[63]:


dir() '''Here we don't find c1 means that automatic destruction of object,
         which is also called Garbage Collection in Pyton.'''


# In[2]:


# Destructor function __del__ 
class life:
    def __init__(self,name='unknown'):
        print('hello',name)
        self.name = name
    def __del__(self):
        print ('goodbye',self.name)
        
brian= life('Brian')
brain='loretta'


# In[3]:


class Time:
    def __init__(self,hh,mm,ss):
        self.hh=hh
        self.mm=mm
        self.ss=ss
    def printTime(self):
        print(self.hh,":",self.mm,":",self.ss)
    def __del__(self):
        print(self,"is Destoryed")
        
t=Time(12,59,59)
t.printTime()


# In[6]:


class Time:
    def __init__(self,hh,mm,ss):
        self.hh=hh
        self.mm=mm
        self.ss=ss
    def printTime(self):
        print(self.hh,":",self.mm,":",self.ss)
    def __del__(self):
        print(self,"is Destoryed")
    def Tick(self):
        self.ss=self.ss+1
        if self.ss==60:
            self.ss=0
            self.mm=self.mm+1
        if self.mm==60:
            self.mm=0
            self.hh=self.hh+1
        if self.hh>=12:
            self.hh=self.hh-12
            
t=Time(12,59,59)
t.printTime()
t.Tick()
t.printTime()
        
        


# In[ ]:


# Increament and Decreament in time by Second...
class Time:
    def __init__(self,hh,mm,ss):
        self.hh=hh
        self.mm=mm
        self.ss=ss
    def printTime(self):
        print(self.hh,":",self.mm,":",self.ss)
    def __del__(self):
        print(self,"is Destoryed")
    def tick(self):
        self.ss=self.ss+1
        if self.ss==60:
            self.ss=0
            self.mm=self.mm+1
        if self.mm==60:
            self.mm=0
            self.hh=self.hh+1
        if self.hh>=12:
            self.hh=self.hh-12
            
    def dtick(self):
        if self.ss>0 and self.ss<=59:
            self.ss=self.ss-1
        else:
            self.ss=59
        if self.mm>0 and self.mm<=59:
            self.mm=self.mm-1
        else:
            self.mm=59
        if self.hh>0 and self.hh<=12:
            self.hh=self.hh-1
            
t=Time(7,59,59)
t.printTime()
t.tick()
t.printTime()
t.dtick()
t.printTime()


# # Concept of Inheritance in Python Programming...

# In[7]:


''' Inheritance in this we can create a Class from Parent Class which possess the same 
   Attribute as Parent Class.That is we need not define them again ( Code Re-usabilty)'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printPerson(self):
        print("Name=",self.name)
        print("Age=",self.age)
        
class Employee(person):
    def __init__(self,name,age,enum,salary):
        super().__init__(name,age)
        self.enum=enum
        self.salary=salary
    def printEmployee(self):
        print("Employee Number=",self.enum)
        print("Salary=",self.salary)
        
E1=Employee("Wamique",30,1,90000)
E1.printPerson()
E1.printEmployee()


# In[8]:


# This is an example of Single Inheritance Class in Python Programe ...
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printPerson(self):
        print("Name=",self.name)
        print("Age=",self.age)
        
class Employee(person):
    def __init__(self,name,age,enum,salary):
        person.__init__(self,name,age)
        self.enum=enum
        self.salary=salary
    def printEmployee(self):
        print("Employee Number=",self.enum)
        print("Salary=",self.salary)
        
E1=Employee("Wamique",30,1,90000)
E1.printPerson()
E1.printEmployee()


# In[9]:


# This is an example of Multiple Inheritance Class in Python Programe ...
class Student:
    def __init__(self,rnum,name):
        self.rnum=rnum
        self.name=name
        
class Marks:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
class Grade(Student,Marks):
    def __init__(self,rnum,name,m1,m2,m3):
        Student.__init__(self,rnum,name)  # This is better than using super()
        Marks.__init__(self,m1,m2,m3)     # Mostly this is preferred
    def CalculateGrade(self):
        avg=(self.m1+self.m2+self.m3)/3
        if avg>=60:
            Grade="A"
        elif avg>=50:
            Grade="B"
        elif avg>=40:
            Grade="C"
        else:
            Grade="F"
            
        print(self.name,"has got grade ",Grade)

        
g=Grade(1,"Wamique",85,90,95)
g.CalculateGrade()


# In[11]:


# This is an example of Multiple Level Inheritance Class in Python Programe ...

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,rnum,marks):
        self.rnum=rnum
        self.marks=marks
class GradeStudent(Student):
    def __init__(self,name,age,rnum,marks,grade):
        Person.__init__(self,name,age)
        Student.__init__(self,rnum,marks)
        self.grade=grade
    def printall(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Roll Number=",self.rnum)
        print("Marks Obtained=",self.marks)
        print("Grade=",self.grade)
        
G=GradeStudent("Wamique",30,10,999,"A")
G.printall()
        


# # Encapsulation :Prevention Of Direct Modification Of Data... 

# In[12]:


''' Encapsulation: Using OOP inPython one can restrict access to Methods and Variables.
    This Prevents Data from Direct Modification  '''

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell() 


# # Polymorphisim: Ability in (OOP) to use common interface for multiple form (Datatypes)

# In[15]:


class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def printNumber(self):
        print(self.real,"+i",self.imag)
    def __add__(self,c2):
        result=Complex(0,0)
        result.real=self.real+c2.real
        result.imag=self.imag+c2.imag
        return result
        
        
        
c1=Complex(5,6)
c2=Complex(7,8)
c3=c1+c2
c3.printNumber()
        

