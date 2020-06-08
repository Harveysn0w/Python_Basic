# 1.打开
file_read = open("test_137_Readme")
file_copy = open("test_137_ReadmeCopy[附件]", "w")

# 2.读、写
text = file_read.read()
file_copy.write(text)

# 3.关闭文件
file_read.close()
file_copy.close()
