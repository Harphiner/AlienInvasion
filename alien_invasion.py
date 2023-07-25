import sys

import pygame

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init();
        # 让pygame.display.set_mode()生成的屏幕成为类的成员screen，方便以后直接通过这个成员来设置屏幕
        # screen本质上是一个pygame的surface，而pygame.diaplay.set_mode()返回的surface是整个游戏窗口
        # 这也是为什么后面不能直接self.screen.set_caption("Alien Invasion")和pygame.display.fill((230,230,230))的原因
        # 因为screen的级别是窗口，颜色填充（fill）的也是窗口，而caption对应的是整个游戏（个人理解）
        self.screen = pygame.display.set_mode((1200,800))
        # 设置窗口标题
        # 不能用self.screen.set_caption("Alien Invasion")替换
        pygame.display.set_caption("Alien Invasion")
        # 设置背景颜色
        self.bg_color = (230,230,230)
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件。
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()                   
            # 填充颜色
            # 不能用pygame.display.fill((230,230,230))替换
            self.screen.fill(self.bg_color)
            # 让最近绘制的屏幕可见，不断擦除旧屏幕，显示新屏幕       
            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()
