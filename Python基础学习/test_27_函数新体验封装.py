# 将九九乘法表封装在函数中
def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("✨", end="")     乘法表和小星星相似       \t 转义字符
            print("%d * %d = %d" % (col, row, col * row), end="\t")
            col += 1
        print("")
        row += 1
# multiple_table()
