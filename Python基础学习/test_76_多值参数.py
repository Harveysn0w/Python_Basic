"""
定义支持多值参数的函数
有时可能需要 一个函数 能够处理的参数 个数 是不确定的，这个时候，就可以使用 多值参数
python 中有 两种 多值参数：
参数名前增加 一个 * 可以接收 元组
参数名前增加 两个 * 可以接收 字典
一般在给多值参数命名时，习惯使用以下两个名字
*args —— 存放 元组 参数，前面有一个 *
**kwargs —— 存放 字典 参数，前面有两个 *
args 是 arguments 的缩写，有变量的含义
kw 是 keyword 的缩写，kwargs 可以记忆 键值对参数
"""


def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 3, 6, 9, name="小明", age=18)


