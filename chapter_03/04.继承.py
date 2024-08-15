
class Animal:
    __age: 0

    def action(self):
        print("动物默认行为")

    def sound(self):
        pass  # 空，让语法不产生错误


# 单继承
# 多继承，如果属性或者方法有重复，以第一个为准，后续不可覆盖
class Cat(Animal):


    def eat_fish(self):
        print("猫喜欢吃鱼")

    def  sound(self):
        # 调用父类方法
        super().action()
        # Animal.action(self)
        print("miao ~~")


if __name__ == '__main__':
    cat = Cat()
    cat.action()
    cat.sound()