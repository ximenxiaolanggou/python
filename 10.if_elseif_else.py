"""
    if elif else
"""

bool_1 = True
bool_2 = False

print(bool_1 == bool_2)
print(10 > 5)
print(10 < 5)

name = "张三"
age = 12

# if判断
if age > 5:
    print(True)

# if else
if age > 18 | age > 20:
    print("成年")
else:
    print("未成年")

# if elif else

if age > 18:
    print("成年")
elif age > 12:
    print("少年")
else:
    print("小孩")


# if嵌套
if True:
    if False:
        print(False)
    else:
        print(True)
else:
    print(False)
