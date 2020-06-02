# 注意：在开发时，应该把模块中的所有全局变量
# 都定义在所有函数的上方，以保证都可以正常访问到全局变量
num = 999


def demo():

    print("%d" % num)
    print("%s" % title)
    # print("%s" % name)


# 再定义一个全局变量
title = "hello"

demo()

# 第三个全局变量
# name = "nu1l404"

