students = [
    {"name": "阿土"},
    {"name": "小美"},
    {"name": "李四"}
]
# 在学员列表中搜索指定的姓名
find_name = "小美"

for stu_dict in students:

    print(stu_dict)

    # 判断当前遍历的字典中姓名是否为find_name
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)

        # 如果已经找到，直接退出循环，就不需要再对后续的数据进行比较
        break

else:
    # 如果希望搜索列表时，所有字典检查完毕，都没有发现搜索的目标，还希望有一个统一的提示可以用else
    print("抱歉没有找到 %s" % find_name)

print("循环结束")
