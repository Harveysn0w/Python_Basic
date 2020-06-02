info_tuple = ("张三", "5", "9.9", "张三")

# 取值和取索引
print(info_tuple[1])              # 取值，想知道一个索引内具体的值
print(info_tuple.index("9.9"))    # 取索引，已经知道数据的内容，希望知道该数据在元组中的索引

# 统计计数
print(info_tuple.count("张三"))    # 统计一个元素出现的次数
print(len(info_tuple))             # 统计元组中包含元素的个数
