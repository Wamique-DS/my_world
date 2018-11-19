
# coding: utf-8

# # File input and output Statement in Python:

# In[12]:


''' File is a Collection of Data stored permanently on a disk,where as I/O are carried 
    out using these files, input is taken from file and output is printed to file '''

def main():
    outfile = open("Presidents.txt", "w")  # Open file for output
    outfile.write("Bill Clinton\n")  # Write data to the file
    outfile.write("George Bush\n")
    outfile.write("Barack Obama")
    outfile.close() # Close the output file


# In[4]:


outfile = open("Presidents of india.txt", "w")

outfile.write("Ram nath kovind\n")
outfile.write("Paranab Mukherjee\n")
outfile.write("Pratibha Dev singh Patil\n")
outfile.write("A p j kalam Azad")

outfile.close()


# In[5]:


with open("Presidents of india.txt","w") as outfile: # here we need not close explicitlly ,it does internally
    outfile.write("R N Kovind\n")
    outfile.write("P Mukharejee\n")
    outfile.write("P D S Patil\n")
    outfile.write("A PJ K Azad\n")


# In[6]:


# we can append using function "a" 
outfile=open("Presidents of India.txt","a")

outfile.write("K R Narayan\n")

outfile.close()


# In[7]:


import os.path

if os.path.isfile("E:/wamique/Agriculture Insurance Company of India (AICI)_.pdf"):
    print("This file already exists")
else:
    print("This file does not exists ")


# In[13]:


'''Reading from a file '''
import os.path
if os.path.isfile("Presidents of india.txt"):
    infile=open("Presidents of india.txt","r")
    msg=infile.read()
    print(msg)
    infile.close()
else:
    print("There is no such file")


# In[14]:


import os.path
if os.path.isfile("Presidents of india.txt"):
    infile=open("Presidents of india.txt","r")
    msg1=infile.read(4)
    print(msg1)
    msg2=infile.read(10)
    print(msg2)
    infile.close()
else:
    print("There is no such file")


# In[15]:


# Reading lines from a file...
import os.path
if os.path.isfile("Presidents of india.txt"):
    infile=open("Presidents of india.txt","r")
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    line4=infile.readline()
    line5=infile.readline()
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    infile.close()
else:
    print("There is no such file")


# In[16]:


# Reading all lines at once....
import os.path
if os.path.isfile("Presidents of india.txt"):
    infile=open("Presidents of india.txt","r")
    lines=infile.readlines()
    print(lines)
    infile.close()
else:
    print("There is no such file")


# In[19]:


# Using Try and finally in the program...
import os.path
if os.path.isfile("Presidents of india.txt"):
    try:
        infile=open("Presidents of india.txt","r")
        lines=infile.readlines()
        print(lines)
    finally:
        infile.close()
else:
    print("There is no such file")


# In[21]:


# It demonstrate the seek and tell function...
if os.path.isfile("Presidents of india.txt"):
    
    try:
        infile=open("Presidents of india.txt","r")
        msg=infile.read(4)
        print(msg)
        print(infile.tell())
        infile.seek(10)
        msg=infile.read(4)
        print(msg)
    finally:
        infile.close()
else:
    print("There is no such file")


# In[23]:


# Using for loop to read all lines...
if os.path.isfile("Presidents of india.txt"):
    
    try:
        infile=open("Presidents of india.txt","r")
        for line in infile:
            print(line,end="") # end is used remove spaces btw each line..
    finally:
        infile.close()
else:
    print("There is no such file")


# In[28]:


# Writing and Reading Numbers...
from random import randint

def main():
    # open file for writing data
    outfile=open("Numbers.txt","w")
    for i in range(10):
        outfile.write(str(randint(0,9))+" ")
    outfile.close() # close the file
    
    # open the file for reading data
    infile=open("Numbers.txt","r")
    s= infile.read()
    numbers=[eval(x) for x in s.split()]
    for numbers in numbers:
        print(numbers, end=" ")
    infile.close() # close the file
    
main() # call the main function

