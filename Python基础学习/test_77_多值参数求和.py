# 1、定义一个函数 sum_numbers，可以接收的 任意多个整数 将传递的 所有数字累加 并且返回累加结果
def sum_numbers(*args):
    # def sum_numbers(args):

    num = 0

    print(args)

    # 循环遍历 args 元组顺序求和
    for n in args:
        num += n

    return num


result = sum_numbers(1, 2, 3, 4, 99, 999)
# result = sum_numbers((1, 2, 3, 4, 99, 999))
print(result)
