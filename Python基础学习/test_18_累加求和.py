# 计算0-100之间所有数字累计求和结果
# 定义最终结果的变量
result = 0
# 定义一个整数变量记录循环次数
i = 0
# 开始循环
while i <= 100:
    print(i)
    # 每一次循环，都让result这个变量和i这个计数器详加
    result += i
    # 处理计数器
    i += 1
print("0-100之间相加的结果 = %d" % result)
