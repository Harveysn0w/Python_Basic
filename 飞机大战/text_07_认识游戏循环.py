import pygame

# 游戏的初始化
pygame.init()

# 创建游戏的窗口 480*700
scree = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
scree.blit(bg, (0, 0))

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
scree.blit(hero, (200, 500))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环~意味着游戏正式开始！
# i = 0
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)
    # 解决 Mac-pygame 卡顿
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    # print(i)
    # i += 1

# 游戏结束
pygame.quit()


