"""
Takes any number of iterable objects or objects with a length property and returns the longest one. If multiple objects have the same length, the first one will be returned.

Use max() with len as the key to return the item with the greatest length.
"""


def longest_item(*args) -> int:
    return max(args, key=len)


print(longest_item('this', 'is', 'a', 'testcase'))
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5])  # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar')  # 'foobar'
