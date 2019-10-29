
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
keys_intersection = d1.keys() & d2.keys()
d3 = {key: (d1[key], d2[key]) for key in keys_intersection}
# print(d3)


# # ----------------------------------------------------------------------------
# Exercise 3
# You have text data spread across multiple servers. Each server is able to
# analyze this data and return a dictionary that contains words and their
# frequency.
#
# Your job is to combine this data to create a single dictionary that contains
# all the words and their combined frequencies from all these data sources.
#
# Bonus points if you can make your dictionary sorted by frequency
# (highest to lowest).
# For example, you may have three servers that each return these dictionaries:
# # ----------------------------------------------------------------------------

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
final_dict = dict(d1)
for key in d2.keys():
    try:
        final_dict[key] = d2[key] + final_dict[key]
    except KeyError:
        final_dict[key] = d2[key]
for key in d3.keys():
    try:
        final_dict[key] = d3[key] + final_dict[key]
    except KeyError:
        final_dict[key] = d3[key]

# use .get() for the default value and bypass this junk:
def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v

    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))

# # ----------------------------------------------------------------------------
# Exercise 4
# For this exercise suppose you have a web API load balanced across multiple
# nodes. This API receives various requests for resources and logs each request
# to some local storage. Each instance of the API is able to return a dictionary
# containing the resource that was accessed (the dictionary key) and the number
# of times it was requested (the associated value).
#
# Your task here is to identify resources that have been requested on some, but
# not all the servers, so you can determine if you have an issue with your load
# balancer not distributing certain resource requests across all nodes.
#
# For simplicity, we will assume that there are exactly 3 nodes in the cluster.
#
# You should write a function that takes 3 dictionaries as arguments for node 1,
#     node 2, and node 3, and returns a dictionary that contains only keys that
#     are not found in all of the dictionaries. The value should be a list
#     containing the number of times it was requested in each node (the node
#     order should match the dictionary (node) order passed to your function).
#     Use 0 if the resource was not requested from the corresponding node.
#
# Suppose your dictionaries are for logs of all the GET requests on each node:
# # ----------------------------------------------------------------------------


n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}


def uncommon_dict_keys(*args):
    d_list = [d for d in args]
    uncommon_keys = d_list[0].keys() - d_list[1].keys()
    for i in range(1, len(d_list)):
        if i == len(d_list)-1:
            new_uncommon = d_list[i].keys() ^ d_list[0].keys()
        else:
            new_uncommon = d_list[i].keys() ^ d_list[i+1].keys()
        uncommon_keys = uncommon_keys | new_uncommon
    return uncommon_keys

def uncommon_dict_kv(*args):
    uncommon_keys = uncommon_dict_keys(*args)
    print('116:', 'uncommon_keys ''='' ', uncommon_keys)
    uncommon_dict = {}
    for d in args:
        for k in uncommon_keys:
            # if key already exists in uncommon_dict:
            if uncommon_dict.get(k) is not None:
                try:
                    uncommon_dict[k] = *uncommon_dict.get(k, 0), d.get(k, 0)

                except TypeError:
                    uncommon_dict[k] = uncommon_dict.get(k, 0), d.get(k, 0)
                except KeyError:
                    continue
            # if key doesnt exist in uncommon_dict:
            else:
                uncommon_dict[k] = d.get(k, 0)
    return uncommon_dict

# print(uncommon_dict_keys(n1,n2,n3))

print(uncommon_dict_kv(n1, n2, n3))
