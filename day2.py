#printing power of a numberusing ** operator
b = 5
c = b**2   # 5^5 power function
print(c)

#size of operator -- importing from system library
import sys
int_size = sys.getsizeof(10)
print(int_size)  #size of int=28 byte


float_size = sys.getsizeof(9.8)
print(float_size)  # float = 24 byte

str_size = sys.getsizeof("Nepal")
print(str_size)   #46

#complex_size = 



#asking user temperature in farenheight and convertinf it to celcuis
# Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
f = float(input("Enter the value of temperature in Fahrenheit:"))
c = (f -32) * 5/9

print(c)

#calculating simple interest
p = int(input("Enter principle:"))
t = float(input("Enter time:"))
r = float(input("Enter float:"))
SI = (p*t*r)/100
print("Simple Interest is ",SI)
 

#sort - function in list