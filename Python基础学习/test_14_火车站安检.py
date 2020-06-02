# 定义布尔型变量has_ticket表示是否有车票
# 定义整型变量knife_length表示刀的长度，单位厘米
# 首先检查是否有车票，如果有才允许进行安检
# 安检时，需要检查刀的长度，判断是否超过20cm
# 如果超过20cm，提示刀的长度，不允许上车
# 如果不超过20cm，安检通过
# 如果没有车票，不允许进门
has_ticket = True
knife_length = 30
if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length >= 20:
        print("兄得，你带🔪太长了,有%d公分长" % knife_length)
        print("安检不通过，不允许上车！")
    else:
        print("安检通过，祝您旅途愉快！")
else:
    print("大哥，请先买票！")
