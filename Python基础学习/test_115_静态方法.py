class Dog(object):

    @staticmethod
    def run():

        # 不访问实例属性，也不访问类属性，就可以定义静态方法

        print("小狗跑跑跑")


# 通过类名.调用静态方法 ~ 不需要创建对象
Dog.run()
