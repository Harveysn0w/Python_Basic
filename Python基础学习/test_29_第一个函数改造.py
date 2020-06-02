name = "小明"
# python 解释器只知道下方定义一个函数，只有在程序中主动调用函数，才会让函数执行
# 函数def 需要上下保持两行空格


def say_hello():
    """打招呼 — — 函数的文档注释"""
    print("Hello 1")
    print("Hello 2")
    print("Hello 3")


print(name)

say_hello()

print(name)
