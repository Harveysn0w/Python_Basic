a = 99
b = 999

# Plan~a 使用其他变量
# c = a
# a = b
# b = c

# Plan~b 不使用其他变量
# a = a + b
# b = a - b
# a = a - b

# Plan~c Python 专属
# a, b = (b, a)
a, b = b, a

print(a)
print(b)
