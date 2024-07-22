"""
   dict
   字典
"""

# 定义 dict = {} 定义方式被集合占用了
dict2 = dict()
dict3 = {"name": "zhangsan", "age": 12}
print(dict3)

# key 重复定义会覆盖原先的 val

# 获取数据
print(dict3["name"])
print(dict3["age"])

# 添加,如果key存在就是修改操作
dict3["sex"] = "男"
print(dict3)

# 删除元素
print(dict3.pop("sex"))
print(dict3)

# 获取全部 key
keys = dict3.keys()
print(type(keys))
print(keys)

# 循环
for key in dict3:
    print(f"key:{key}, val: {dict3[key]}")

# 统计元素数量
print(len(dict3))


# 清空
dict3.clear()
print(dict3)