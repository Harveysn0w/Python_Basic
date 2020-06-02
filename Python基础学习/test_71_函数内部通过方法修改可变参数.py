# 函数内部使用方法，修改可变参数，会影响外部实参
def demo(num_list):

    print("函数内部的代码")

    # 使用方法修改列表的内容
    num_list.append(9)

    print(num_list)

    print("函数执行完成")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
