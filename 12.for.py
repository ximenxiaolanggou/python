"""
    for
"""

# 基础语法

for ch in "zhangsan":
    print(ch == "a") # ch为字符类型


# range 语法一 从0开始计五个数，所以不包含5
for num in range(5):
    print(num)


# range 语法二 不包含15
for num in range(10, 15):
    print(num)

# range 语法三 不包含16
for num in range(10, 16, 2):
    print(num)

# 不建议使用，但是能访问到，可以在外面定义一个变量num这样，在每次循环中会被rang中的数据覆盖
print(num)