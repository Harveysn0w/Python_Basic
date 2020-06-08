import pygame

pygame.init()

# 创建游戏的窗口 480*700
scree = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")

# 2.blit 绘制图像
scree.blit(bg, (0, 0))

# 3.update 更新屏幕显示
pygame.display.update()

# 游戏循环
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()


# 游戏结束
pygame.quit()

# pygame 在Mac运行卡顿，解决办法
"""
在mac 上的pygame特别容易卡顿，因此中需要以下代码防止卡顿~方法1

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()   解决程序开启就无响应的问题
        exit()
        
在使用pygame编写界面代码，在程序退出时，
增加相应的pygame.quit指令，强制程序在退出时，
自动退出pygame应用。
"""
"""
在mac 上的pygame特别容易卡顿，因此中需要以下代码防止卡顿~方法2

while True:
    for event in pygame.event.get():
        # 检测窗口上的关闭按钮是否被点击
        if event.type == pygame.QUIT:
            # 退出游戏
            print('关闭按钮点击')
            exit()
            

"""
