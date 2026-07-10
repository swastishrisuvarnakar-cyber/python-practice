"""
Topic: Variables and Type Casting

Concepts Covered:
- Integer
- Float
- String
- Boolean
- type() function
- Implicit Type Casting
- Explicit Type Casting

Author: Swastishri Suvarnakar
Date: 10 July 2026
"""

#python consist of various kind of variables which are of different data type
#for example - int , float,string,double,bool etc.

#so we are going to look about them , their inputs and type conversion
#declaring and initialization of variable
num = 1
a = 1.23
msg = "hello there!!"
result = True

#printing the type of each variable
# using type function
print(type(num))
print(type(a))
print(type(msg))
print(type(result))

#performing Type casting(Converting one data type into another data type)

#implicit type casting - python automatically does for you
total = num + a
print(type(total)) #python automatically converts the integer type into the float type before adding

# explicit Type casting - performed by the user itself
print(float(num)) ##output 1.0
print(float("123.34")) #output - 123.34

print(int(a)) #output 1
print(int("10")) #output 10

print(str(a)) # output "1.23"
