import pygame, sys
from bullet import Bullet
from enemy import Enemy

def events(screen, gun, bullets):
    "Обработка событий"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:


            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:


            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False



def update(bg_color, screen, gun, enemies, bullets):
    "обновление экрана"
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemies.draw(screen)
    pygame.display.flip()

def update_bullets(bullets, enemies):
    "обновлять позиции пуль"
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions =  pygame.sprite.groupcollide(bullets, enemies, True, True)

def update_enemies(enemies):
    "обновляет позицию жуликов"
    enemies.update()

def create_army(screen, enemies):
    "создание армии жуликов"
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    nubmer_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)

    for row_number in range (number_enemy_y - 3):
        for enemy_nubmer in range(nubmer_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + (enemy_width * enemy_nubmer)
            enemy.y = enemy_height + (enemy_height * row_number)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * row_number)
            enemies.add(enemy)