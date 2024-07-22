"""
    字符串
"""

# 定义
str = "hello java scala python java"

str1 = str[1]
str2 = str[-1]
print(type(str1)) # 字符串类型
print(str1)
print(str2)

# count 统计字符串出现的次数
print(str.count("java"))

# 字符串替换
new_str = str.replace("java", "go")
print(str)
print(new_str)

list = str.split(" ")
print(str)
print(list)

# strip 去除前后空格

str = "  java  "
print(str)
print(str.strip()) # 默认去除首位空格

str = "12java21"
print(str.strip("12")) # 输出为 java strip函数会将12分成 1和2