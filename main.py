import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Game")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls.create_army(screen, enemies)
    stats = Stats()


    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, gun, enemies, bullets)
            controls.update_bullets(screen, bullets, enemies)
            controls.update_enemies(stats, screen, gun, enemies, bullets)

run()