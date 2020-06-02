Harvey_str = "Hello Harvey"
print(Harvey_str)

# 1、判断是否以指定字符串开始
print(Harvey_str.startswith("Hello"))
print(Harvey_str.startswith("hello"))

# 2、判断是否以指定字符串结束
print(Harvey_str.endswith("Harvey"))
print(Harvey_str.endswith("harvey"))

# 3、查找指定字符串~索引位置  ~  index方法如果指定的字符串不存在会报错-find则是返回-1
print(Harvey_str.find("llo"))
print(Harvey_str.find("abc"))

# 4、替换字符串
print(Harvey_str.replace("Harvey", "Python"))
# replace方法执行完成以后，会返回一个新的字符串
# 注意：不会修改原有字符串的内容

print(Harvey_str)

