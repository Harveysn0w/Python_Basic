def print_info(name, gender=True):
    """
    
    :param name: 班上同学的姓名
    :param gender: True 男生  False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


# 假设班上的同学，男生多
print_info("小明")
print_info("老王")
print_info("小美", False)
