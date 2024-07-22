"""
 字符串操作

 使用反斜杠标识转义字符
"""

# 字符串定义方式
# " 或者 “” 或者 “”“”“”
str_1 = '张三'
str_2 = "李四"
str_3 = """
王
五
"""

print(type(str_1))
print(str_1)
print(type(str_2))
print(str_2)
print(type(str_3))
print(str_3)

str_4 = "\"hello\""
print(type(str_4))
print(str_4)

# 字符串拼接
print("name：" + "张三")
print("name：" + str_1)

# 字符串无法通过 +号和整形拼接 [err]
# print("age:" + 12)

"""
 字符串格式化
"""
name = "张三"
age = 12
money = 13.141
message = "姓名：%s, 年龄：%d, money: %f" % (name, age, money)
print(message)

message = "姓名：%s, 年龄：%d, money: %7.2f" % (name, age, money)
print(message)

print(f"name:{name}, age:{age}, money: {money + 10 }")
