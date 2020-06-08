# 1.打开文件
file = open("test_137_Readme")

# 2.读取文件
while True:
    # 一行一行读取内容
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    # print(text)
    print(text, end="")

# 3.关闭文件
file.close()
