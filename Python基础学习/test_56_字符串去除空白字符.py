# 顺序且居中对齐输入以下内容
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流\t\n",
        "欲穷千里目",
        "更上一层楼"]

# 先使用strip方法去除空白字符，在使用center方法居中
for poem_str in poem:

    print("｜%s｜" % poem_str.strip().center(10, "　"))    # 居中