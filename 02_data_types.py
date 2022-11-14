'''
Numeric : int, float, complex
Text : str

Sequence :
    list : [] similar to collection in C#
    tuple : init by () but accessed by [index] Tuples can be thought of as read-only lists. (no resize & no change)
    range : x = range(6)

Mapping : 
    dict : init by {} but assigned/accessed by [key]  hash of key-value

Set :
    set: x = {"apple", "banana", "cherry"}  A set is a collection which is unordered, unable to re-assigned but can be add/remove, and unindexed.
    frozenset: x = frozenset({"apple", "banana", "cherry"})

Boolean :
    bool: x = True

Binary :
    bytes: x = b"Hello"
    bytearray: x = bytearray(5)
    memoryview: x = memoryview(bytes(5))

None :
    NoneType: x = None
'''

from my_module import Print, PrintHeader, PrintVar, str2num


def ex_num():
    PrintHeader("Examples of Numeric Types")

    ss = ['', '1', '35656222554887711', '-3255522', '-20.5',
          '35e3', '12E4', '-87.7e100', '3+5j', '-5j']

    for idx, s in enumerate(ss):
        x = str2num(s)
        print("{}) {} ---> {}".format(idx+1,
              PrintVar(s, False), PrintVar(x, False)))


def ex_str():
    PrintHeader("Examples of String Types")

    s = 'Hello Python !'
    PrintVar(s)

    Print("looping through a string ---> ")
    for x in s:
        Print("'{}',".format(x))
    print()

    print(s[0])      # Prints first character of the string
    print(s[2:5])   # Prints characters starting from 3rd to 5th
    print(s[2:])    # Prints string starting from 3rd character
    print(s * 2)    # Prints string two times
    print(s + " concat")  # Prints concatenated string
    print(s.split(" "))
    print('Py' in s)
    print('py' not in s)


def ex_bool():
    PrintHeader("Examples of Boolean Types")
    b = ['', ' ', 1, 0, -1, -12, 44.5, 'true', 'false', True, False]
    for idx, x in enumerate(b):
        print("{}) {} ---> bool= {}".format(idx +
              1, PrintVar(x, False), bool(x)))


def ex_list():
    PrintHeader("Examples of List Types")
    tup_1 = ('1st_members', 786, 2.23, 'john', 70.2)
    list_1 = list(tup_1)  # constructor by a tuple
    list_2 = [123, 'jane']

    PrintVar(tup_1)
    PrintVar(list_1)
    PrintVar(list_2)

    # print(list)         # Prints complete list
    print(list_1[0])      # Prints first element of the list
    print(list_1[1:3])    # Prints elements starting from 2nd till 3rd
    print(list_1[2:])     # Prints elements starting from 3rd element
    print(list_2 * 2)  # Prints list two times
    print(list_1 + list_2)  # Prints concatenated lists


def ex_tuple():
    PrintHeader("Examples of Tuple Types")
    tup_1 = ('1st_members', 786, 2.23, 'john', 70.2)
    tup_2 = tuple(tup_1)  # constructor by a tuple
    tup_3 = (123, 'jane')

    PrintVar(tup_1)
    PrintVar(tup_2)
    PrintVar(tup_3)
    print(tup_1 is tup_2)

    print(tup_2[0])           # Prints first element of the tuple
    # Prints elements of the tuple starting from 2nd till 3rd
    print(tup_2[1:3])
    print(tup_2[2:])  # Prints elements of the tuple starting from 3rd element
    print(tup_3 * 2)     # Prints the contents of the tuple twice
    print(tup_2 + tup_3)  # Prints concatenated tuples


def ex_dict():
    PrintHeader("Examples of Dictionary Types")
    dict_a = {}
    dict_a['one'] = "This is one"
    dict_a[2] = "This is two"

    PrintVar(dict_a)
    print(dict_a['one'])       # Prints value for 'one' key
    print(dict_a[2])          # Prints value for 2 key
    # print(dict[1])  # error key =1 not found

    print()

    dict_b = {'name': 'john', 'code': 6734, 'dept': 'sales'}

    PrintVar(dict_b)
    print(dict_b)       # Prints complete dictionary
    print(dict_b.keys())  # Prints all the keys
    print(dict_b.values())  # Prints all the values
    print(dict_b.items())


def ex_set():
    PrintHeader("Examples of Set Types")
    set_a = {"apple", "banana", "cherry"}
    tup_b = ("abc", 34, True, 40, "male")
    set_b = set(tup_b)  # set() constructor

    PrintVar(set_a)
    PrintVar(tup_b)
    PrintVar(set_b)

    set_a.add("try_add")  # add a member
    set_a.update(set_b)  # add from another set, tuple, list, dict, ...

    for x in set_a:
        Print("{}, ".format(x))
    print()

    set_a.remove("abc")  # remove a member (not exist --> error)
    set_a.discard(True)  # remove a member (not exist --> no error)
    set_a.discard("zzzzzzzzz")

    print(set_a)

    set_a.clear()  # empty the set
    print(set_a)

    del set_a  # delete the set completely


if __name__ == "__main__":
    # ex_num()
    # ex_str()
    # ex_bool()
    # ex_list()
    # ex_tuple()
    # ex_dict()
    ex_set()
