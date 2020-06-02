name_list = ["zhangsan", "lisi", "wangwu"]

# 1、取值和取索引
print(name_list[0])               # list index out of range  --- 列表索引超出范围会报错
print(name_list.index("lisi"))    # 知道数据的内容，想确定数据在列表中的位置 --- 取索引
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！

# 2、修改
name_list[0] = "张三"             # 修改指定索引的数据 --- 列表[索引]=数据
# name_list[3] = "王小二"          列表指定的索引超出范围，程序会报错

# 3、增加
name_list.append("王小二")        # append方法可以向列表末尾追加数据---列表.append(数据)
name_list.insert(1, "小美女")     # insert方法在指定位置插入数据---列表.insert(索引，数据)

temp_list = ["孙悟空", "少时地", "大马哈", "白龙"]
name_list.extend(temp_list)      # extend将列表2的数据追加到列表---列表.extend(列表2)


# 4、删除
name_list.remove("王小二")        # remove删除指定列表中的数据---列表.remove(数据)
name_list.pop(1)                 # pop删除指定索引的数据---列表.pop(索引)
name_list.pop()                  # pop默认删除列表中最后一个元素---列表.pop()
name_list.clear()                # clear 清空列表---列表.clear()

print(name_list)