import pygame


class Enemy(pygame.sprite.Sprite):
    "Класс одного жулика"
    def __init__(self, screen):
        """инициализация и начальная позиция жуликов"""
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод жулика на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещает жуликов"""
        self.y += 0.12
        self.rect.y = self.y
