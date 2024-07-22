
class Animal:

    def sound(self):
        pass  # 空，让语法不产生错误


class Cat(Animal):

    def sound(self):
        print("miao ~~")

class Dog(Animal):

    def sound(self):
        print("wang ~~")

def fun(animal:Animal):
    animal.sound()
if __name__ == '__main__':
    fun(Cat())
    fun(Dog())