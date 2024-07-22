"""
    lambda
"""



def fun(compute_fun, x, y):
    res = compute_fun(x,y)
    print(res)


fun(lambda x,y: x + y, 1, 2)