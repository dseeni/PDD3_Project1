
# # ----------------------------------------------------------------------------
# Excercise 1:
# Write a Python function that will create and return a dictionary from
# another dictionary, but sorted by value. You can assume the values are all
# comparable and have a natural sort order.
# # ----------------------------------------------------------------------------
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
# items() is a view of the composers dictionary, sorted by lambda value access
composers_dict = dict(sorted(composers.items(), key=lambda kv: kv[1]))
# print(composers_dict)


# # ----------------------------------------------------------------------------
# Exercise 2:
# Given two dictionaries, d1 and d2, write a function that creates a dictionary
# that contains only the keys common to both dictionaries, with values being a
# tuple containg the values from d1 and d2. (Order of keys is not important).
# # ----------------------------------------------------------------------------
# def intersect(d1, d2):
#     d1_keys = d1.keys()
#     d2_keys = d2.keys()
#     keys = d1_keys & d2_keys
#     d = {k: (d1[k], d2[k]) for k in keys}
#     return d
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
d_tup = (d1, d2)
keys_difference = d1.keys() & d2.keys()
d3 = {key: (d1[key], d2[key]) for key in keys_difference}
print(d3)


