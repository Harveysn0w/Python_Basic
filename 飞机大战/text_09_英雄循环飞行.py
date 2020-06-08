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
scree.blit(hero, (150, 300))

# 创建时钟对象
clock = pygame.time.Clock()

# 1-1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环~意味着游戏正式开始！
while True:
    # 可以指定循环体内部的代码执行的频率
    clock.tick(60)

    # 1-2.修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置~循环飞行
    # 判断飞机身体和y值都在外面在重复  bottom=y+height
    # if hero_rect.y + hero_rect.height <= 0:
    if hero_rect.bottom <= 0:
        hero_rect.y = 700

    # 1-3.调用blit方法绘制图像
    scree.blit(bg, (0, 0))
    scree.blit(hero, hero_rect)

    # 1-4.使用update方法更新显示
    pygame.display.update()

    # 解决 Mac-pygame 卡顿
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()


# 游戏结束
pygame.quit()


