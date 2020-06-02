name_list = ["张三", "李四", "王武"]

# 使用del 关键字，删除指定列表索引的元素 ---- del列表[索引]
# 在日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]

# del 关键字本质上是将一个变量从内存中删除
#     name = "小明"
#     del name
#     print(name)
# 注意：如果使用del关键字将变量从内存中删除，后续代码就不能在使用这个变量了


print(name_list)