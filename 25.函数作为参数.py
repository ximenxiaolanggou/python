"""
    函数作为参数传递
"""

def compute(x, y):
    return x + y


def fun(compute_fun, x, y):
    res = compute_fun(x,y)
    print(res)


fun(compute, 1, 2)