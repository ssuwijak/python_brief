# https://www.tutorialspoint.com/python/python_variable_types.htm

counter = 100          # An integer assignment
miles = 1000.0       # A floating point
name = "John"       # A string

print(counter)
print(miles)
print(name)

# multiple assignments
a = b = c = 1
print(a,b,c)

a,b,c = 1,2,"john"
print(a,b,c)

# delete var (reference value)
del c
print(a,b)