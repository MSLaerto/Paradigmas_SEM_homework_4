import functools
def custom_reducer(x, y):
    return x * y 
numbers = [1, 2, 3, 4, 5]
result = functools.reduce(custom_reducer, numbers)
print("Result:", result)