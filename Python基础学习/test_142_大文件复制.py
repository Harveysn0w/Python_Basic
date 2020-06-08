# 1.打开
file_read = open("test_137_Readme")
file_copy = open("test_137_ReadmeCopy[大的附件哦]", "w")

# 2.读、写
while True:
    # 读取一行内容
    text = file_read.readline()

    # 判断是否读取到内容
    if not text:
        break

    file_copy.write(text)

# 3.关闭文件
file_read.close()
file_copy.close()
