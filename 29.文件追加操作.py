"""
    文件追加操作
    文件存在，会清空文件数据
    文件不存，在会创建文件
"""

def open_file(file_path):
     file = open(file_path, "a", encoding="UTF-8")
     return file

file = open_file("D:/test.txt")
print(file)

file.write("hello java\n")
file.write("hello scala")

# 将内存中数据写入磁盘
file.flush()

# close方法也会将内存中数据写入磁盘
file.close()
