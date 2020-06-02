# 全局变量名前，应该加g_或者gl_的前缀
g_num = 999
# 再定义一个全局变量
g_name = "nu1l404"


def demo():
    # 如果局部变量和全局变量名称相同时，会在局部变量下面有灰色的虚线
    num = 99
    print("%d" % num)
    print("%s" % g_title)
    print("%s" % g_name)


# 再定义一个全局变量
g_title = "hello"

demo()




