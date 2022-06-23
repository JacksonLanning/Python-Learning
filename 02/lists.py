# list
a = [1, 2, 3, 4, 5]

# print(a)

# Lists can contain anything
# strings
a = ["hello", "there"]
# booleans
a = [True, True]
# A mix of datatypes
a = [True, "Jackson", [1, 2, 3]]

# list functions
# length of a list
# print(len([1,2,3,4]))


# access, indexes
my_list = ['a', 'b', 'c', 'd']

# print(my_list[0]) # this gets me a
# print(my_list[3]) # this gets me d


# Iterating over lists
# i is the index
# for i in range(len(my_list)):
#     print(my_list[i])

# # for each loop
# for item in my_list:
#     print(item)




# # These are non mutable ways to change a list
# # empty list
# a = []
# # Add an item to the list
# a = a + [1]
# print(a)

# # # concactinate two lists
# # print([1,2,3]+[4,5,6])



# # Mutable methods
# a = []
# # Add an item to the list
# a.append(1)
# print(a)


# a.extend([1,2])
# print(a)


# scope and mutable methods


# def my_function(var_1, var_2):
#     return var_1 + var_2

# not recommended
# def my_function(var_1, var_2):
#     var_1.extend(var_2)
#     return var_1

# a = [1,2,3]
# b = [4,5,6]

# print(a)
# print(b)
# print(my_function(a, b))
# print(a)
# print(b)

# a = "abc"
# a = a.upper()

# print(a)

# strings, ints, bools, and floats are not mutable "primative data types"
# lists and any other classes/objects can have mutable methods