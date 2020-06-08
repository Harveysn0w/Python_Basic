class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让属类性的值+1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("手枪")

# 2.输出工具对象的总数
# 对象.类属性=值，只会给对象添加一个属性，不会影响类属性的值
tool3.count = 99
print("工具对象的总数 %d" % tool3.count)
print("===>%d" % Tool.count)

