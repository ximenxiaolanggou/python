"""
    列表
    1、元素类型可以不一样
"""

# 列表创建
list1 = ["zhangsan", 12, 13.14]
print(type(list1))
print(list1)

# 嵌套列表
list2 = ["zhangsan", [12,"hehe", True], 13.14]
print(type(list2))
print(list2)

list3 = []
list4 = list()

# 列表数据获取
print(list2[0])
print(list2[1][2])
print(list2[-1]) # -1 最后一个元素，-2，-3...
print(list2[1][-1])

# 列表操作
print("------------------------ 列表操作 ------------------------")

# 查询列表中某个元素的下标，找不到会抛异常
list = ["zhangsan", "lisi", "wangwu"]
print(list.index("lisi"))
# print(list.index("lisi1")) # 元素不存在抛出ValueError异常

# 修改元素值
list[1] = "lisi666"
print(list[1])

# 插入元素，如果下标超出元素个数就会插入在最后面
list.insert(1, "zhaoliu")
print(list)

# 元素追加 1
list.append("xiaocai")
print(list)

# 追加元素2
list.extend(["libai", "tang"])
print(list)

# del 删除元素
del list[0]
print(list)

# pop 删除元素
ele = list.pop(1)
print(ele)
print(list)

# renove 删除某个元素在列表中的第一个匹配项, 如果元素不存在会抛出异常
list.remove("libai")
print(list)

# count 统计某个元素个数
count = list.count("tang")
print(count)

# len 统计列表中元素个数
len = len(list)
print(len)

# 列表遍历 while
index = 0
while index < len:
    print(list[index])
    index += 1

# 列表遍历 for
for ele in list:
    print(ele)

# clear 清空列表
list.clear()
print(list)