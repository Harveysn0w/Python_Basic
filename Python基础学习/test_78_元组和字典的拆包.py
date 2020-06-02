"""
元组和字典的拆包
在调用带有多值参数的函数时，如果希望：
将一个 元组变量，直接传递给 args
将一个 字典变量，直接传递给 kwargs
就可以使用 拆包，简化参数的传递，拆包 的方式是：
在 元组变量前，增加 一个 *
在 字典变量前，增加 两个 *
"""


def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# demo(gl_nums, gl_dict)
# 拆包语法，简化元组变量/字典变量的传递
demo(*gl_nums, **gl_dict)
# demo(1, 2, 3, name="小明", age=18)
