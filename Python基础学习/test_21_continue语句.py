i = 0
while i < 10:
    # continue 某一条件满足时，不执行后续重复的代码  i == 3
    if i == 3:
        # 在循环中使用continue这个关键字，一定要确认是否修改了循环次数，否则导致死循环
        i += 1
        continue
    print(i)
    i += 1
print("over")
