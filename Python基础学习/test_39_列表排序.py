name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 9, 3, 5, 0, 2, 1]

# 升序
name_list.sort()   # =     name_list.sort(reverse=False)
num_list.sort()    # =     num_list.sort(reverse=False)

# 降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)

# 逆序（反转）
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)