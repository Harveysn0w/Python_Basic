# 顺序且居中对齐输入以下内容
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]


for poem_str in poem:
    # print("｜%s｜" % poem_str.ljust(10, "　"))   # 左对齐
    # print("｜%s｜" % poem_str.rjust(10, "　"))   # 右对齐
    print("｜%s｜" % poem_str.center(10, "　"))    # 居中



