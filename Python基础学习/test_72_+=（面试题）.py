# 在py中，列表变量调用+=本质上实在执行列表变量的extend方法，不会修改变量的引用
def demo(num, num_list):

    print("函数开始")

    # num = num + num
    num += num
    # num_list = num_list + num_list
    # 列表变量使用+=不会做先加在赋值的操作，本质上是调用列表extend的方法
    # num_list.extend(num_list)
    num_list += num_list

    print(num)
    print(num_list)

    print("函数完成")


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
