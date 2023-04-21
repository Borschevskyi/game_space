import pygame, sys
from bullet import Bullet
from enemy import Enemy
import time

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

def update_bullets(screen, bullets, enemies):
    "обновлять позиции пуль"
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions =  pygame.sprite.groupcollide(bullets, enemies, True, True)
    if len(enemies) == 0:
        bullets.empty()
        create_army(screen, enemies)


def gun_kill(stats, screen, gun, enemies, bullets):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        enemies.empty()
        bullets.empty()
        create_army(screen, enemies)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_enemies(stats, screen, gun, enemies, bullets):
    "обновляет позицию жуликов"
    enemies.update()
    if pygame.sprite.spritecollideany(gun, enemies):
        gun_kill(stats, screen, gun, enemies, bullets)

    enemies_check(stats, screen, gun, enemies, bullets)


def enemies_check(stats, screen, gun, enemies, bullets):
    #проверка жуликов у края экрана
    screen_rect = screen.get_rect()
    for enemу in enemies.sprites():
        if enemу.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, enemies, bullets)
            break



def create_army(screen, enemies):
    "создание армии жуликов"
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    # ширина жуликов
    nubmer_enemy_x = int((700 - 8 * enemy_width) / enemy_width) # колличество жуликов в ряду
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 400 * 1) / enemy_height)

    for row_number in range (number_enemy_y - 1):# жулики по высоте
        for enemy_nubmer in range(nubmer_enemy_x):
            enemy = Enemy(screen)
            enemy.x = (enemy_width * 1.6) + ((enemy_width * 1.4) * enemy_nubmer) #Расстояние между жуликами
            enemy.y = enemy_height + ((enemy_height * 1.5) * row_number) #Расстояние между жуликами вертикально
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * row_number)
            enemies.add(enemy)