import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("飞机大战")

# 设置颜色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        # 防止飞机移出屏幕
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

# 创建玩家飞机实例
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 更新所有精灵的位置
    all_sprites.update()
    
    # 清屏
    screen.fill(WHITE)
    
    # 绘制所有精灵
    all_sprites.draw(screen)
    
    # 更新显示
    pygame.display.flip()

# 退出游戏
pygame.quit()
sys.exit()