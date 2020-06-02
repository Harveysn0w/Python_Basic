def demo1():

    # 定义一个局部变量
    num = 10

    print("在demo1函数内部的变量是 %d" % num)


# 全局变量，在外面
num = 1
print("%d" % num)


# 在不同函数内部，可以定义相同名字的局部变量，彼此之间不冲突
def demo2():
    num = 99
    print("在demo2函数内部的变量是 %d" % num)


# 调用局部变量
demo1()
demo2()
