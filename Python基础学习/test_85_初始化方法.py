class Cat():

    def __init__(self):
        # __init__方法是专门用来定义一个类具有有哪些属性的方法
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用 类名() 创建对象的时候，会自动调用初始化方法__init__
tom = Cat()
tom.eat()

print(tom.name)

