"""
    元组：
    不可修改
    but
    元组中嵌套list，list元素可以修改
"""

# 定义
tp1 = (1, "hello", 13.2, (2, "world", 56.56))
tp2 = ()
tp3 = tuple()

print(type(tp1))
print(tp1)

# 如果是单个元素，需要加上逗号，不然就不是元组类型，而是字符串类型
print(type(("hello")))
print(type(("hello",)))

# 获取元素
word = tp1[-1][1]
print(word)

# 元组操作

# index 获取元素下标
tp = ("java", "python", "scala", "java")
print(tp.index("scala"))

# count 统计某个元素个数
print(tp.count("java"))

# len 统计元素个数
print(len(tp))

# 遍历
index = 0
while index < len(tp):
    print(tp[index])
    index += 1

for ele in tp:
    print(ele)