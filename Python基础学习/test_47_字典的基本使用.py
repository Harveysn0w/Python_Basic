xiaoming_dict = {"name": "小明"}

# 1、取值
print(xiaoming_dict["name"])         # 在取值时，如果指定的key不存在，程序会报错

# 2、增加/修改
xiaoming_dict["age"] = 18            # 如果key不存在，会新增键值对
xiaoming_dict["name"] = "李四"        # 如果key存在，会修改已经存在键值对

# 3、删除
xiaoming_dict.pop("age")             # 使用pop方法，指定要删除的key，如果key不存在则报错
xiaoming_dict.clear()                # clear方法清空字典


print(xiaoming_dict)
