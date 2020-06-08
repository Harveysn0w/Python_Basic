class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1.判断类属性是否是空对象
        if cls.instance is None:

            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance


# 创建多个对象
p1 = MusicPlayer()
print(p1)

p2 = MusicPlayer()
print(p2)
