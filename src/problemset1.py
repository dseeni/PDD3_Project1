
# # ----------------------------------------------------------------------------
# Excercise 1:

# Write a Python function that will create and return a dictionary from
# another dictionary, but sorted by value. You can assume the values are all
# comparable and have a natural sort order.
# # ----------------------------------------------------------------------------
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
# items() is a view of the composers dictionary, sorted by lambda value access
composers_dict = dict(sorted(composers.items(), key=lambda kv: kv[1]))
print(composers_dict)

