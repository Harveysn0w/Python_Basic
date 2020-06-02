# 定义字符串name，输出我的名字叫小明，请多多关照！
name = "小明"
print("我的名字叫%s，请多多关照！" % name)

# 定义整数变量student_num,输出我的学号是0001
student_num = 1
print("我的学号是%04d" % student_num)
# %d %04d  位数不全补0，不到四位前面补0

# 0.2f 表示只只显示小数点后两位
price = 2.5
weight = 2
money = price * weight
print("苹果单价%0.2f元，买了%0.2f斤，一共花了%0.2f元" % (price, weight, money))

# 定义一个小数scale，输出数据比例是10.00%
# %%,输出%
scale = 0.25
# scale = 0.25*100
print("数据比例是%.f%%" % (scale * 100))
print("数据比例是%.2f%%" % (scale * 100))

# %s   字符串
# %d   输出整数
# %f   输出小数
# %%   输出%
# print("格式化字符串"%变量)
# print("格式化字符串"%（变量1，变量2，变量3）)
