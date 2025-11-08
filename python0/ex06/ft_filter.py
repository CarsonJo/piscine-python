import collections.abc as abc
"""like the built in filter"""


def ft_filter(func: abc.Callable, iter: abc.Iterable):
    arr = []
    for i in iter:
        if func(i):
            arr.append(i)
    return arr
