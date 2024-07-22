"""
   自定义模块
"""
# 只有列表中定义的方法名才可以被外部所导入，但是只限制与 import * ,如果手动导入 form xx import sum2 就可以使用
__all__ = ["sum"]

# 定义求和函数
def sum(*args):
    count = 0;
    for ele in args:
        count += ele
    return count

def sum2(*args):
    count = 0;
    for ele in args:
        count += ele
    return count

if __name__ == '__main__':
    print(sum(1,2,3))

