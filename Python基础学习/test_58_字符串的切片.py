# 字符串切片~字符串[开始索引:结束索引:步长]
num_str = "0123456789"
# 截取从2-5位置的字符串
print(num_str[2:6])
# 截取从2-末尾的字符串
print(num_str[2:])
# 截取开始-5的字符串
print(num_str[:6])
# 截取完整的字符串
print(num_str[:])
# 从开始位置，每隔一个字符，截取字符串
print(num_str[::2])
# 从索引1开始，每隔一个取一个
print(num_str[1::2])
# 截取从2-末尾-1的字符串
print(num_str[2:-1])
# 截取字符串末尾2个字符
print(num_str[-2:])
# 字符串的逆序（面试题）
print(num_str[::-1])
