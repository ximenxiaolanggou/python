"""
    文件操作
"""

def open_file(file_path):
     file = open(file_path, "r", encoding="UTF-8")
     return file

file = open_file("D:/test.txt")
print(file)

# 读取文件, 传递的参数表示读取的字节数，如果不传递参数表示读取全部内容，需要注意的是如果对一个文件对象多长读取操作，每次读取会从上一次读取位置进行读取
print(file.read(3))
print(file.read())

# 关闭文件
file.close()

file = open_file("D:/test.txt")

#  readlines 会将读取的行数据存放到列表中
lines = file.readlines()
print(type(lines))
print(lines)