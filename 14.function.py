"""
    函数
"""
num = 100
# 定义函数 如果未写返回值，会有默认返回值为None,类型为NoneType
def len(str):
    count = 0
    for ele in str:
        count += 1
    return count


str1 = "hello python"

# 调用函数并打印统计信息，
print(f"字符串长度：{len(str1)}")


def len2():
    print("len2")

print(len2() == None) # True

print(not len2()) # true  not进行反转
