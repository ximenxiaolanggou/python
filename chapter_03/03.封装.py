"""
    封装
     - 私有成员变量 成员变量前面添加__
     - 私有成员方法 成员方法前面添加__
"""

class Dog:
    __name: None
    __age: None

    def get_name(self):
        return self.__name

    def __action(self):
        print("汪汪 ~~~")

    def __init__(self, name, age):
        self.__name = name
        self.__age = age





if __name__ == '__main__':
    dog = Dog("阿花", 8);
    print(dog.get_name())
