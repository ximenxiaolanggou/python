
# Student 类名
class Student:
    # 类的属性 成员变量
    name = None
    gender = None
    age:int = None

    # 必须携带 self
    def say(self):
        import winsound
        winsound.Beep(2000, 3000)
        # 必须使用 self 才能访问成员变量
        self.name
        print("say hello")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("创建Student对象~~")



if __name__ == '__main__':
    stu = Student("王五", 12)
    stu.say()
    print(stu)