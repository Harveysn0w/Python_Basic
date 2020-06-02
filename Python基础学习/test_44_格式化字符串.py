# 格式化字符串后面的（）本质上就是一个元组
info_tuple = ("张三", 18, 1.75)
print("%s 年龄是 %d 身高是 %.2f 米" % info_tuple)

# 使用格式化字符串同样可以生成一个新的字符串
info_str = "%s 年龄是 %d 身高是 %.2f 米" % info_tuple
print(info_str)
