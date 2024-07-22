"""
   容器通用操作
"""

my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = (1,2,3,4,5)
my_dict = {"key1": 1,"key2": 2,"key3": 3,"key4": 4,"key5": 5}

# len
print(len(my_list))
print(len(my_tuple))
print(len(my_str))
print(len(my_set))
print(len(my_dict))


# max
print(max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))

# len
print(min(my_list))
print(min(my_tuple))
print(min(my_str))
print(min(my_set))
print(min(my_dict))

# 容器转列表
print(list(my_list))
print(list(my_tuple))
print(list(my_str))
print(list(my_set))
print(list(my_dict)) # 字典会抛弃val ，只有key存放到列表中

# 容器转元组
print(tuple(my_list))
print(tuple(my_tuple))
print(tuple(my_str))
print(tuple(my_set))
print(tuple(my_dict)) # 字典会抛弃val ，只有key存放到列表中

# 容器转字符串
print(str(my_list))
print(str(my_tuple))
print(str(my_str))
print(str(my_set))
print(str(my_dict)) # key val 都保留


# 容器转集合
print(set(my_list))
print(set(my_tuple))
print(set(my_str))
print(set(my_set))
print(set(my_dict)) # 字典会抛弃val ，只有key存放到列表中


# 排序
print(f"类型：{type(sorted(my_list))}，数据为：{sorted(my_list)}")
print(f"类型：{type(sorted(my_tuple))}，数据为：{sorted(my_tuple)}")
print(f"类型：{type(sorted(my_str))}，数据为：{sorted(my_str)}")
print(f"类型：{type(sorted(my_set))}，数据为：{sorted(my_set)}")
print(f"类型：{type(sorted(my_dict))}，数据为：{sorted(my_dict)}")

# 倒序
print(f"类型：{type(sorted(my_list, reverse=True))}，数据为：{sorted(my_list, reverse=True)}")
print(f"类型：{type(sorted(my_tuple, reverse=True))}，数据为：{sorted(my_tuple, reverse=True)}")
print(f"类型：{type(sorted(my_str, reverse=True))}，数据为：{sorted(my_str, reverse=True)}")
print(f"类型：{type(sorted(my_set, reverse=True))}，数据为：{sorted(my_set, reverse=True)}")
print(f"类型：{type(sorted(my_dict, reverse=True))}，数据为：{sorted(my_dict, reverse=True)}")



