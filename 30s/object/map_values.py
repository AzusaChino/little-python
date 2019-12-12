"""

Creates an object with the same keys as the provided object and values generated by running the provided function for each value.

Use dict.keys() to iterate over the object's keys, assigning the values produced by fn to each key of a new object.
"""


def map_values(obj, fn):
    ret = {}
    for key in obj.keys():
        ret[key] = fn(obj[key])
    return ret


users = {
    'fred': {'user': 'fred', 'age': 40},
    'pebbles': {'user': 'pebbles', 'age': 1}
}

map_values(users, lambda u: u['age'])
