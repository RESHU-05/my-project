#!/usr/bin/env python
# coding: utf-8

# # Data Analytics and Machine Learning using Python![image.png](attachment:image.png)

# # Lab Exercise &emsp;   Week-1&emsp; &emsp;Submission Date :- 24 May 2020   Before 6 P.M.

# # Lab-1
# 
# * Create GitHub Account.
# * Clone the repository from………………
# * Add a file to src folder say “Myprofile.txt”
# * Use < git add > command to add that file to the repository.
# * Use command to commit your changes. ( write meaningful message with commit)
# * Use command to send your change in your repository. 
# * Look online and check if changes has been pushed or not.
# 
# 
# #### After completing above steps write your github repository URL Below
# 

# In[ ]:


# Write Github URL 
https://github.com/RESHU-05/my-project.git
    # the above steps are done while doing day 2 assignment therefore this is the url of that.


# # Lab-2 
# ### Write a Python program to input a number from the user and check if it is positive, negative or zero.
# 

# In[ ]:


n=int(input("Enter any number"))
if n>0:
    print("Number is positive")
elif n<0:
    print("Number is negative")
else:
    print("Number is Zero")



# # Lab-3
# ### Write a Python Program to Find the Largest Among Three Numbers, using the least number of lines of code.
# 

# In[ ]:


a,b,c=input("Enter first number,sedcond number,third number").split( )
print(max(a,b,c))


# # Lab-4
# ### Write a Python program to input a month name and print number of days in it.
# 
# Eg., January – 31
# 
# February – 28/29
# 

# In[ ]:


m=input("Enter a month")
if m in ["january","march","may","july","august","october","december"]:
    print(m,"-","31")
elif m in "february":
    print(m,"-","28/29")
else:
    print(m,"-","30")




# # Lab-5
# ### Write a Python Program to Find the Factorial of a Number.
# n! = n * n-1 * n-2 * n-3 * …. *3 * 2 * 1
# 

# In[ ]:


import math
n=int(input("Enter a number"))
print(math.factorial(n))



# # Lab-6
# At a certain school, student email addresses end with <b>@student.college.edu</b>, while professor email addresses end with <b>@prof.college.edu</b> 
# 
# Write a program that first asks the user how many email addresses they will be entering, and then has the user enter those addresses.
# 
# After all the email addresses are entered, the program should print out a message indicating either that all the addresses are student addresses or that there were some professor addresses entered.

# In[ ]:


x=int(input("enter the number of user"))
print("enter all  the email addresses")
l=[]
c=0
d=0
for y in range(x):
    r=input()
    l.append(r)
for y in range(x):
    if "@student.college.edu" in l[y]:
        c=c+1
    elif "@prof.college.edu" in l[y]:
        d=d+1
if c==x:
    print("only student adresses")
elif d==x:
    print("only professor adresses")
else:
    print("some are student adresses and some are professor adresses.")
        



# # Lab-7
# ### Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# 
#  Suppose the following input is supplied to the program:
#     
#     without,hello,bag,world
# 
# Then, the output should be:
# 
#     bag,hello,without,world
# 

# In[ ]:


a= [item for item in input().split(",")] 
a.sort()
print(a)


# # Lab-8
# ### Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000

# In[ ]:


def showEmployee(name,salary=9000):
    print("name is ",name)
    print("salary is ",salary)
a=input("enter name")
b=int(input("enter salary"))
showEmployee(a,b)
showEmployee(a)# function call when salary is missing and it takes default value 


# # Lab-9
# ### Create an inner function to calculate the addition in the following way
# 
# * Create an outer function that will accept two parameters a and b say <b>outerFun(a, b)</b>
# 
# * Create an inner function(<b>e.g. innerFun(a,b)</b>) inside an outer function that will calculate the addition of a and b 
# * At last, an outer function will add 5 into addition and return it

# In[ ]:


def outerfun(a,b):
    def innerfun(a,b):
        return a+b
    d=innerfun(a,b)+5
    return d
print(outerfun(5,7))




# # Lab-10
# ### Assign a different name to function and call it through the new name
# 
# Below is the function displayStudent(name, age). Assign a new name showStudent(name, age)  to it and call through the new name

# In[ ]:


def displayStudent(name,age):
        print(name)
        print(age)
name=input()
age=int(input())
showStudent=displayStudent
showStudent(name,age)


# # Lab-11
# Write a program that gets a string from the user containing a potential telephone number.The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise. 
# 
# A phone number is considered valid as long as it is written in the form
# abc-def-hijk or 1-abc-def-hijk. 
# 
# The dashes must be included, the phone number should contain only numbers and dashes, and the number of digits in each group must be correct.
# 
# Test your program with the output shown below.
# 
# Enter a phone number: 301-447-5820
# 
# Valid
# 
# Enter a phone number: 301-4477-5820
# 
# Invalid
# 
# Enter a phone number: 3X1-447-5820
# 
# Invalid
# 
# Enter a phone number: 3014475820
# 
# Invalid

# In[ ]:


n=input("Enter a telephone number")
c=len(n)
d=n[0:3]+n[4:7]+n[8:13]
if c==12  and n[3]=="-" and n[7]=="-" and d.isdigit()==True:
    print("Valid")
else:
    print("Invalid")



# In[ ]:





# In[ ]:




