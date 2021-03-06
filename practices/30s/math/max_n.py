"""
Returns the n maximum elements from the provided list. If n is greater than or equal to the provided list's length, then return the original list(sorted in descending order).

Use list.sort() combined with the deepcopy function from the inbuilt copy module to create a shallow clone of the list and sort it in ascending order and then use list.reverse() reverse it to make it descending order. Use [:n] to get the specified number of elements. Omit the second argument, n, to get a one-element list
"""


def max_n(lst, n=1, reverse=True):
    return sorted(lst, reverse=reverse)[:n]


if __name__ == '__main__':
    print(max_n([1, 2, 3]))
    print(max_n([1, 2, 3, 4, 5, 6], 2))
