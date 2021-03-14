#platypus's weekend

import os
import random
import pygame
import sys

WIDTH = 480
HEIGHT = 720
FPS = 60

WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platypus\'s weekend")
clock = pygame.time.Clock()

#загрузка изображений и музыки
game_folder = os.path.dirname('C:/Coding/Platypus/')
img_folder = os.path.join (game_folder, 'img')
sound_folder = os.path.join (game_folder, 'sound')
fon = pygame.image.load (os.path.join(img_folder, 'fon.png'))
zast = pygame.image.load (os.path.join(img_folder, 'zast.png'))
keyy = pygame.image.load (os.path.join(img_folder, 'key.png'))
end = pygame.image.load (os.path.join(img_folder, 'end.png'))
cocoimg = pygame.image.load (os.path.join(img_folder, 'coco.png'))
drinksimg = pygame.image.load (os.path.join(img_folder, 'drinks.png'))
iceimg = pygame.image.load (os.path.join(img_folder, 'ice.png'))
orangeimg = pygame.image.load (os.path.join(img_folder, 'orange.png'))
platy = pygame.image.load (os.path.join(img_folder, 'platy.png'))
rainimg = pygame.image.load (os.path.join(img_folder, 'rain.png'))
skiimg = pygame.image.load (os.path.join(img_folder, 'ski.png'))
sunimg = pygame.image.load (os.path.join(img_folder, 'sun.png'))
seedimg = pygame.image.load (os.path.join(img_folder, 'seed.png'))
pygame.mixer.music.load (os.path.join (sound_folder, 'doctor_dreamchip.wav'))
pygame.mixer.music.set_volume(0.4)


pubs=0 #очки
days=2 #жизни
pips = 0 #пули
speed = 0 #текущая скорость
line = 1 #текущая сторона

#функция для текста
font_name = pygame.font.match_font('PerfectDOSVGA437.ttf')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#кнопки и значения иконок
def key():
    screen.blit (keyy, (0,0))
    draw_text (screen, 'Arrow key - move', 35, WIDTH/2, 30)
    draw_text (screen, 'Space key - fire', 35, WIDTH/2, 50)
    draw_text (screen, 'Today is friday!', 35, 300, 100)
    draw_text (screen, 'So let\'s party start!', 35, 300, 120)
    draw_text (screen, 'Collect cocktails to score', 35, 270, 200)
    draw_text (screen, 'Plus to your days', 35, 240, 260)
    draw_text (screen, 'Very bad point', 35, 220, 320)
    draw_text (screen, 'Be faster and carefull', 35, 250, 380)
    draw_text (screen, 'Calm down, dude!', 35, 240, 450)
    draw_text (screen, 'FIRE!', 35, 160, 520)
    draw_text (screen, 'Get mix up with side', 35, 250, 580)
    draw_text (screen, 'Press any key to continue', 35, 250, 670)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False
                start = True

#авторство и благодарности
def credit():
    screen.blit (fon, (0,0))
    draw_text (screen, 'Idea & Coding & Drawing by:', 35, 250, 170)
    draw_text (screen, 'Dotokbit', 35, 250, 200)
    draw_text (screen, 'Music by:', 35, 250, 300)
    draw_text (screen, 'Doctor_Dreamchip', 35, 250, 330)
    draw_text (screen, '(freesound.org)', 35, 250, 360)
    draw_text (screen, 'Press any key to continue', 35, 250, 670)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False
                start = True

#конечный экран
def gover():
    pygame.mixer.music.stop()
    running = False
    over = True
    while over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                sys.exit()
        screen.blit (end, (0,0))
        draw_text (screen, 'It\'s seems monday coming!', 40, 210, 30)
        draw_text (screen, 'Press any key to exit!', 40, 250, 670)
        pygame.display.flip()

# начальный экран
start = True
while start:
    clock.tick(FPS)
    screen.blit (zast, (0,0))
    draw_text (screen, 'Press S to START', 50, WIDTH/2, 270)
    draw_text (screen, 'Press K to KEY', 50, WIDTH/2, 340)
    draw_text (screen, 'Press C to CREDIT', 50, WIDTH/2, 410)
    draw_text (screen, 'Press E to EXIT', 50, WIDTH/2, 480)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                start = False
                key = False
                credit = False
                running = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_k:
                key()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                credit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                sys.exit()
             
# класс игрок
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = platy
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 645)
    def update(self):
        if speed >= 0 and line%2 == 1: #при взаимодействиее с "Кокосом" у игрока меняются лево/право
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate [pygame.K_LEFT]:
                self.speedx = -5
            if keystate [pygame.K_RIGHT]:
                self.speedx = 5
        if speed <= -1 and line%2 == 1: #при взаимодействии с "Мороженным" игрок замедляется
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate [pygame.K_LEFT]:
                self.speedx = -1
            if keystate [pygame.K_RIGHT]:
                self.speedx = 1
        if speed >= 0 and line%2 == 0:
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate [pygame.K_LEFT]:
                self.speedx = 5
            if keystate [pygame.K_RIGHT]:
                self.speedx = -5
        if speed <= -1 and line%2 == 0:
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate [pygame.K_LEFT]:
                self.speedx = 1
            if keystate [pygame.K_RIGHT]:
                self.speedx = -1
        self.rect.x += self.speedx
        if self.rect.left < 50:
            self.rect.left = 50
        if self.rect.right > 430:
            self.rect.right = 430
    def shoot(self):
        if pips >= 1:
            seed = Seed(self.rect.centerx, self.rect.top)
            all_sprites.add(seed)
            seeds.add(seed)
         
#класс Иконки - "Коктейль" - дает очки
class Drink (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = drinksimg
        self.rect = self.image.get_rect()
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        self.rect.x = random.randrange(40, 390)
        self.rect.y = random.randrange(-710, -10)       
    def update(self):
        if speed <= 0:
            self.speedy=3
            self.rect.y += self.speedy
        if speed >= 1: #при взаимодействии с "Роликами" скорость спрайтов увеличивается
            self.speedy = 10
            self.rect.y += self.speedy 
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(40, 390)
            self.rect.y = random.randrange(-710, -10)

#класс Икоки - "Солнце" - дает жизнь     
class Sun (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sunimg
        self.rect = self.image.get_rect()
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        self.rect.x = random.randrange(40, 390)
        self.rect.y = random.randrange(-710, -10)       
    def update(self):
        if speed <= 0:
            self.speedy=3
            self.rect.y += self.speedy
        if speed >= 1:
            self.speedy = 10
            self.rect.y += self.speedy
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(40, 390)
            self.rect.y = random.randrange(-710, -10)

#класс Икоки - "Туча" - убирает жизнь 
class Rain (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = rainimg
        self.rect = self.image.get_rect()
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        self.rect.x = random.randrange(40, 390)
        self.rect.y = random.randrange(-710, -10)       
    def update(self):
        if speed <= 0:
            self.speedy=3
            self.rect.y += self.speedy
        if speed >= 1:
            self.speedy = 10
            self.rect.y += self.speedy
        if pubs >= 10: #при росте очков растет скорость "плохих" спрайтов
            self.speedy = 5
            self.rect.y += self.speedy
        if pubs >= 20: 
            self.speedy = 7
            self.rect.y += self.speedy
        if pubs >= 30:
            self.speedy = 15
            self.rect.y += self.speedy
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(40, 390)
            self.rect.y = random.randrange(-710, -10)

#класс Икоки - "Ролики" - увеличивает скорость
class Ski (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = skiimg
        self.rect = self.image.get_rect()
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        self.rect.x = random.randrange(40, 390)
        self.rect.y = random.randrange(-710, -10)      
    def update(self):
        if speed <= 0:
            self.speedy=3
            self.rect.y += self.speedy
        if speed >= 1:
            self.speedy = 10
            self.rect.y += self.speedy
        if pubs >= 10:
            self.speedy = 5
            self.rect.y += self.speedy
        if pubs >= 20:
            self.speedy = 7
        if pubs >= 30:
            self.speedy = 15
            self.rect.y += self.speedy
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(40, 390)
            self.rect.y = random.randrange(-710, -10)

#класс Икоки - "Мороженное" - замедляет скорость
class Ice (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = iceimg
        self.rect = self.image.get_rect()
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        self.rect.x = random.randrange(40, 390)
        self.rect.y = random.randrange(-710, -10)       
    def update(self):
        if speed <= 0:
            self.speedy=3
            self.rect.y += self.speedy
        if speed >= 1:
            self.speedy = 10
            self.rect.y += self.speedy
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(40, 390)
            self.rect.y = random.randrange(-710, -10)

#класс Икоки - "Апельсин" - умеет стрелять семечками
class Orange (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = orangeimg
        self.rect = self.image.get_rect()
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        self.rect.x = random.randrange(40, 390)
        self.rect.y = random.randrange(-710, -10)       
    def update(self):
        if speed <= 0:
            self.speedy=3
            self.rect.y += self.speedy
        if speed >= 1:
            self.speedy = 10
            self.rect.y += self.speedy
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(40, 390)
            self.rect.y = random.randrange(-710, -10)

#класс Икоки - "Кокос" - меняет направления лево/право
class Coco (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cocoimg
        self.rect = self.image.get_rect()
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        self.rect.x = random.randrange(40, 390)
        self.rect.y = random.randrange(-710, -10)       
    def update(self):
        if speed <= 0:
            self.speedy=3
            self.rect.y += self.speedy
        if speed >= 1:
            self.speedy = 10
            self.rect.y += self.speedy
        if pubs >= 10:
            self.speedy = 5
            self.rect.y += self.speedy
        if pubs >= 20:
            self.speedy = 7
        if pubs >= 30:
            self.speedy = 15
            self.rect.y += self.speedy
        self.rect.right != self.rect.left and self.rect.bottom != self.rect.top
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(40, 390)
            self.rect.y = random.randrange(-710, -10)

#класс Икоки - "Семечко" - пуля от апельсина
class Seed (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = seedimg
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speedy = -20  
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill

#запускаем спрайты    
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
drinks = pygame.sprite.Group()
suns = pygame.sprite.Group()
rains = pygame.sprite.Group()
skis = pygame.sprite.Group()
ices = pygame.sprite.Group()
oranges = pygame.sprite.Group()
cocos = pygame.sprite.Group()
player = Player()
seeds = pygame.sprite.Group()
all_sprites.add(player)
for i in range(1):
        d = Drink()
        su = Sun()
        r = Rain()
        s = Ski()
        ic = Ice()
        o = Orange()
        c = Coco()
        all_sprites.add(d, su, r, s, ic, o, c)
        mobs.add(d, su, r, s, ic, o, c)
        drinks.add(d)
        suns.add(su)
        rains.add(r)
        skis.add(s)
        ices.add(ic)
        oranges.add(o)
        cocos.add(c)

#запускаем игру    
pygame.mixer.music.play( loops=-1)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                if pips > 0:
                    pips -=1 
    all_sprites.update()
#взаимодействие со спрайтами
    hits = pygame.sprite.spritecollide(player, drinks, True)
    for hit in hits:
        d = Drink()
        all_sprites.add(d)
        drinks.add(d)
        pubs +=1
    hits1 = pygame.sprite.spritecollide(player, suns, True)
    for hit in hits1:
        su = Sun()
        all_sprites.add(su)
        drinks.add(su)
        days +=1
    hits2 = pygame.sprite.spritecollide(player, rains, True)
    for hit in hits2:
        r = Rain()
        all_sprites.add(r)
        rains.add(r)
        days -=1
    hits3 = pygame.sprite.spritecollide(player, skis, True)
    for hit in hits3:
        s = Ski()
        all_sprites.add(s)
        skis.add(s)
        speed  += 1
    hits4 = pygame.sprite.spritecollide(player, ices, True)
    for hit in hits4:
        ic = Ice()
        all_sprites.add(ic)
        ices.add(ic)
        speed -= 1
    hits5 = pygame.sprite.spritecollide(player, oranges, True)
    for hit in hits5:
        o = Orange()
        all_sprites.add(o)
        oranges.add(o)
        pips += 1
    hits6 = pygame.sprite.spritecollide(player, cocos, True)
    for hit in hits6:
        c = Coco()
        all_sprites.add(c)
        cocos.add(c)
        line +=1
    hits7 = pygame.sprite.groupcollide(drinks, seeds , True, True )
    for hit in hits7:
        d = Drink()
        all_sprites.add(d)
        drinks.add(d)
        pubs += 1
    hits8 = pygame.sprite.groupcollide(suns, seeds , True, True )
    for hit in hits8:
        su = Sun()
        all_sprites.add(su)
        suns.add(su)
        pubs += 1
    hits9 = pygame.sprite.groupcollide(rains, seeds , True, True )
    for hit in hits9:
        r = Rain()
        all_sprites.add(r)
        drinks.add(r)
        pubs += 1
    hits10 = pygame.sprite.groupcollide(skis, seeds , True, True )
    for hit in hits10:
        s = Ski()
        all_sprites.add(s)
        skis.add(s)
        pubs += 1
    hits11 = pygame.sprite.groupcollide(ices, seeds , True, True )
    for hit in hits11:
        ic = Ice()
        all_sprites.add(ic)
        ices.add(ic)
        pubs += 1
    hits12 = pygame.sprite.groupcollide(oranges, seeds , True, True )
    for hit in hits12:
        o = Orange()
        all_sprites.add(o)
        oranges.add(o)
        pubs += 1
    hits13 = pygame.sprite.groupcollide(cocos, seeds , True, True )
    for hit in hits13:
        c = Coco()
        all_sprites.add(c)
        cocos.add(c)
        pubs += 1

#завершение игры
    if days == 0:
        running = False
        gover()
          
#рендеринг
    screen.blit(fon, (0, 0))
    all_sprites.draw(screen)
    draw_text (screen, 'Score:', 25, 110, 10)
    draw_text (screen, str(pubs), 25, 110, 30)
    draw_text (screen, 'Days' , 25, 200, 10)
    draw_text (screen, str(days) , 25, 200, 30)
    draw_text (screen, 'Pips', 25, 290, 10)
    draw_text (screen, str(pips) , 25, 290, 30)
    draw_text (screen, 'Speed', 25, 370, 10)
    draw_text (screen, str(speed) , 25, 370, 30)
    pygame.display.flip()

pygame.quit()