# 1、判断空白字符
space_str = " \t\n\r"
print(space_str.isspace())

# 2、判断字符串中是否只包含数字
num_str = "⑴"              # 1  1.1  (1)  \u26  一千  "⑴"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
# 都不能判断小数，判断范围越来越大
