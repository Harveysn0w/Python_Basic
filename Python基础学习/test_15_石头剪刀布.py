# 导入随机数工具包
import random
# 从控制台输入要输出的拳，1、石头 2、剪刀 3、布
# 电脑随机出拳  //--先假设电脑只会出石头，完成整体代码功能
# 比较胜负 石头胜剪刀，剪刀胜布，布胜石头   if（）or（）or（）
player = int(input("请输入您要出得拳：石头（1）剪刀（2）布（3）—— "))
# computer = 3
computer = random.randint(1, 3)
print("玩家出的拳头是 %d - 电脑出的拳头是 %d" % (player, computer))
if (player == 1 and computer == 2) \
        or (player == 2 and computer == 3) \
        or (player == 3 and computer == 1):
    print("欧耶，电脑弱爆了")
# 平局
elif player == computer:
    print("真是心有灵犀啊，再来一局")
# 其他情况，就是电脑赢了
else:
    print("不服气，我们决战🔪")
