import pygame

pygame.init()

# 创建游戏的窗口 480*700
scree = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
scree.blit(bg, (0, 0))
pygame.display.update()

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
scree.blit(hero, (200, 500))
pygame.display.update()

# 游戏循环
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

# 游戏结束
pygame.quit()


