# eval()函数 将字符串当成有效的表达式来求值并返回计算结果
input_str = input("请输入算术题：")

print(eval(input_str))

# 不要滥用eval 等价代码 可以使用终端命令
# 请输入算术题：__import__('os').system('ls')
