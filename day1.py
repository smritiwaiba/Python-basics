print("Hello World")

#---------------------
a =5
b = 7
print(a+b)   #will simply print sum
c = a+b
print("The sum is",c)    #will also print value of c, i.e. sum

#-----------------data types ----------
a = 5
print(type(a))  #<class 'int'>

b = 7.5
print(type(b))  #<class 'float'>

c = True
print(type(c))  #<class 'bool'>

d = "Nepal"
print(type(d))  #<class 'str'>

e = 3 + 2j
print(type(e))  #<class 'complex'>

#---------------------------------------------
#taking integers from user and adding them
a = int (input("Enter first number"))   #int - changing the initial string data into int
b= int (input("Enter second number"))

sum = a+b
print("Sum:",sum)

#taking floating value from user and multiplying them

c = float(input("Enter first floating number:"))
d = float(input("Enter second floating number:"))

product = c*d
print("Product: ", product)

#-------------

e = '1'
f = '2'
g = e+f
print(g)

#------------

k = "Hello\n"
l = "world"
m = k+l
print(m)

#----------
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = a%b
print("remainder:", c)

#----------
a = 5
b = 2.7
c = "hi"
print(a,b,c)  #output: 5 2.7 hi

#-------------



name = "ram"
age = 20
print(f"My name is {name} and age is {age}") #formatted printing, for variables


#------------------

#wap to ask user its name and display
name = input("Enter your name:")

print("Your name is", name)
#-----------------------
a = "python "
b  = a*2
print(b)

"""
a = "Nepal"
b = 2
c = a+b #Nepal+2: TypeError: can only concatenate str (not "int") to str
print(c)
"""