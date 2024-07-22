"""
    函数传参
"""

def fun1(name, age, sex):
    print(f"name: {name}, age: {age}, sex: {sex}")


# 默认参数
def fun2(name, age, sex = "男"):
    print(f"name: {name}, age: {age}, sex: {sex}")


# 不定长参数， 元组容器存储
def fun3(*args):
    print(type(args))
    print(args)

# 关键字传递 ，字典存储
def fun4(**kargs):
    print(type(kargs))
    print(kargs)

# 位置传参
fun1("zhangsan", 12, "男")

# 关键字传参
fun1(age = 22, name = "lisi", sex="女")

# 混用
fun1("wangwu", sex = "男", age = 18)

# 默认参数调用
fun2("wangwu", 12)

# 位置不定长
fun3("zhangsan", 12)

# 关键字不定长
fun4(name = "zhangsan", age = 12)

