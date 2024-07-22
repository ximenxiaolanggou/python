"""
    魔术方法
"""
class Person:
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 字符串,如果不重写代表输出就是对象的内存地址
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    # 两个对象比较大小 只能用于 < 、>
    def __lt__(self, other):
        return self.age < other.age

    # 两个对象比较大小 只能用于 <= 、>=
    def __le__(self, other):
        return self.age < other.age

    # 相等比较，如果不重写就是比较两个对象的内存地址
    def __le__(self, other):
        return self.age == other.age


if __name__ == '__main__':
    person1 = Person("zhangsan", 12)
    person2 = Person("zhangsan", 13)
    print(person1 < person2)
    print(person1 <= person2)
    print(person1 == person2)