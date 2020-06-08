class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XTQ(Dog):

    def game(self):
        print("%s 在神界玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):

        print("%s 和 %s 愉快的玩耍" % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1.创建狗对象
# wc = Dog("旺财")
wc = XTQ("飞天神犬")

# 2.创建小明对象
xm = Person("小明")

# 3.让小明和狗玩的方法
xm.game_with_dog(wc)
