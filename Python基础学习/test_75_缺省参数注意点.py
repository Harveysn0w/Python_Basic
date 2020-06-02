# 必须保证 带有默认值的缺省参数 在参数列表末尾
def print_info(name, title="职工", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生  False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s] %s 是 %s" % (title, name, gender_text))


# 假设班上的同学，男生多
print_info("小明")
print_info("老王")
# 如果有多个缺省参数，需要制定参数名，这样py解释器才能知道它的对应关系
print_info("小美", gender=False)
