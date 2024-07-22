"""
   json 模块

"""

import json

data = [
    {"name": "张三", "age": 12},
    {"name": "lisi", "age": 13},
    {"name": "wangwu", "age": 14}
]

# ensure_ascii 不使用 ascii来转换中文
str = json.dumps(data, ensure_ascii=False)
print(type(str))
print(str)

new_data = json.loads(str)
print(type(new_data))
print(new_data)
