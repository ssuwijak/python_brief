'''
Python has five standard data types −

Numbers : int, long (oct||hex), float, complex
String
List : [] similar to collection in C#
Tuple : innit by () but access by [index] Tuples can be thought of as read-only lists. (no resize & no change)
Dictionary : init by {} but assigned/accessed by [key]  hash of key-value

'''

print("\nString Examples\n")

ss = 'Hello World!'

print(ss)         # Prints complete ssing
print(ss[0])      # Prints first character of the string
print(ss[2:5])   # Prints characters starting from 3rd to 5th
print(ss[2:])    # Prints string starting from 3rd character
print(ss * 2)    # Prints string two times
print(ss + "TEST")  # Prints concatenated string

print("\nList Examples\n")

list = ['list_examples', 786, 2.23, 'john', 70.2]
tinylist = [123, 'jane']

print(list)         # Prints complete list
print(list[0])      # Prints first element of the list
print(list[1:3])    # Prints elements starting from 2nd till 3rd
print(list[2:])     # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)  # Prints concatenated lists

print("\nTuple Examples\n")

tuple = ('tuple_examples', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'jane')

print(tuple)               # Prints the complete tuple
print(tuple[0])           # Prints first element of the tuple
print(tuple[1:3])  # Prints elements of the tuple starting from 2nd till 3rd
print(tuple[2:])  # Prints elements of the tuple starting from 3rd element
print(tinytuple * 2)     # Prints the contents of the tuple twice
print(tuple + tinytuple)  # Prints concatenated tuples


print("\nDictionary Examples\n")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}


print(dict['one'])       # Prints value for 'one' key
print(dict[2])          # Prints value for 2 key
# print(dict[1])  # error key =1 not found
print(tinydict)       # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values
