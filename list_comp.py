"""
@author: Dibyesh Mishra
@date: 23-12-2021 00:32
"""

#List comprehension offers a shorter syntax when you want to create a new list
# based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if "a" in x]
new_list2 = ['hello' for x in fruits]

print(new_list)
print(new_list2)