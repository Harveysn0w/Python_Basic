# 在开发是，不要起和系统模块一样的名字，否则导致出错。
import random

# 查看模块具体路径
print(random.__file__)

# 生成一个0-10的随机数
rand = random.randint(0, 10)

print(rand)

