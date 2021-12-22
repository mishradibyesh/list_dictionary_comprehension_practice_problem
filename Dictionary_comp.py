"""
@author: Dibyesh Mishra
@date: 23-12-2021 00:38
"""
# Dictionary comprehension is an elegant and concise way to create dictionaries.

# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')for (k, v) in original_dict.items()}
print(new_dict_1)