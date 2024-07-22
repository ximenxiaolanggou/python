"""
   set
   元素不重复，无序
"""

# 定义
set1 = {"zhangsan", "lisi", "wangwu", "lisi"}
set2 = {}
set3 = set()

print(type(set1))
print(set1)

# 操作
set = set()

# 添加元素
set.add("zhangsan")
set.add("lisi")
set.add("wangwu")
set.add("lisi")
print(set)

# 删除元素
set.remove("lisi")
print(set)

# pop 去除元素并去除
print(set.pop())
print(set)

# difference 取两个集合的差集，会生成新的集合，不会影响原两个集合
set_one = {1,2,3}
set_two = {2,3,4}
print(set_one.difference(set_two))

# difference_update 去除set_one中与set_two相同的元素
set_one = {1,2,3}
set_two = {2,3,4}
set_one.difference_update(set_two)
print(set_one)

# union 合并
set_one = {1,2,3}
set_two = {2,3,4}
print(set_one.union(set_two))

# 遍历
set_one = {1,2,3}
for ele in set_one:
    print(ele)

# clear 清空
set.clear()
print(set)