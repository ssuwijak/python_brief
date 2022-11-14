# https://www.tutorialspoint.com/python/python_variable_types.htm

counter = 100          # An integer assignment
miles = 1000.0       # A floating point
name = "John"       # A string

print(counter)
print(miles)
print(name)

# multiple assignments
print("\nmultiple assignment 1")
a = b = c = 1
print(a,b,c)

print("\nmultiple assignment 2")
a,b,c = 1,2,"john"
print(a,b,c)

# unpack a collection
print("\nunpack a collection")
fruits = ['apple','banana','cherry']
x,y,z = fruits
print(fruits)
print(x,y,z)

# delete var (reference value)
del c
print(a,b)