import pygame, controls
from gun import Gun
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Game")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls.create_army(screen, enemies)


    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, enemies, bullets)
        controls.update_bullets(bullets)
        controls.update_enemies(enemies)

run()