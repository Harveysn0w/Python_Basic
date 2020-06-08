try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用8初一用户输入的整数并且输出
    result = 8/num

    print(result)

except ValueError:
    print("请输入正确的整数")
# 捕获未知错误
except Exception as result:
    print("未知错误 %s" % result)

