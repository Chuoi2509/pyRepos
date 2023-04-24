import re
# import builtins

import pandas as pd
import numpy as np 
from tabulate import tabulate
import pycodestyle
import timeit
# from IPython.display import display
# import types

import supplementary as spl







# df = pd.read_csv('customer_shopping_data.csv', nrows = 1000).head(20)
# with open('test.html', 'w') as f:
    # f.write(html)
# html = tabulate(df, headers='keys', tablefmt='html')

# print(tabulate(df, headers='keys', tablefmt="fancy_grid"))

# class BaseClass:
    # CONS = 'hi there!'
    # def __init__(self, p1, p2, p3 = 0, p4 = None):
#         self.p1 = p1
#         self.p2 = p2 
#         self.p3 = p3
#         self.p4 = p4
#         print(self.p1, self.p2, self.p3, self.p4, sep = '\n')
# class MyClass(BaseClass):
#     def __init__(self, *args, **kwargs):
#         BaseClass.__init__(self, *args, **kwargs)
#         print(list(args))
#         # print({k: v for (k, v) in kwargs})
#         print(kwargs)
#         self.extra = 'this was added'
#         print(self.extra)
# obj = MyClass(1, 5, p4 = 5)

# postgres = """
# SELECT * FROM banana;
# """
# output = spl.execute_sql(postgres, True)
# head = output[0]
# my_data = output[1:]


def median(lst):
    midpoint = int(len(lst) / 2)
    if len(lst) % 2 == 0:
        median = (lst[midpoint - 1] + lst[midpoint]) / 2
        # since list is zero-based
    else:
        median = lst[midpoint]
    return median

# print(median([1, 2, 3, 4]))


def raise_val_alt(n, vals=None):
    if vals == None:
        vals = []
    result = []
    for val in vals:  
        val_n = val ** n
        result.append(val_n)
    return result

# print(raise_val_alt(2, vals = [1, 2, 3]))

# print(get_all_methods(builtins))


def fibonacci_generator(limit = 255):
    if limit < 1:
        raise ValueError("Limit must be greater than or equal to 1.")
    fibo_list = [0, 1]
    while fibo_list[-1] + fibo_list[-2] <= limit:
        fibo_list.append(fibo_list[-1] +  fibo_list[-2])
    print(fibo_list)


def fibonacci(limit):
    """
    Generates a Fibonacci sequence up to a given limit.
    Args:
        limit (int): The maximum value of the Fibonacci sequence.
    Returns:
        list: A list containing the Fibonacci sequence up to the given limit.
    """
    fib = [0, 1]
    while fib[-1] <= limit:
        fib.append(fib[-1] + fib[-2])
    # this will make last fib always greater than limit
    # so we can safely exclude it
    return fib[:-1]