# Разработай свою игру в этом файле!
from pygame import *
window = display.set_mode((900, 700))
clock = time.Clock()

font.init()
shrift = font.SysFont('Comic Sans MS', 30)

game = 1
hp = 3
collect_coins = 0


#класс героя~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Hero(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


    def control(self):
        global hp, game, collect_coins
        keyboard = key.get_pressed()
        
        if keyboard[K_w]:
            self.rect.y -= 2
            if sprite.spritecollide(self, walls, False):
                self.rect.y += 2
        if keyboard[K_a]:
            self.rect.x -= 2
            if sprite.spritecollide(self, walls, False):
                self.rect.x += 2
        if keyboard[K_s]:
            self.rect.y += 2
            if sprite.spritecollide(self, walls, False):
                self.rect.y -= 2
        if keyboard[K_d]:
            self.rect.x += 2
            if sprite.spritecollide(self, walls, False):
                self.rect.x -= 2
        if self.rect.x >= 670:
            self.rect.x = 670
        if self.rect.x <= 45:
            self.rect.x = 45
        if self.rect.y >= 670:
            self.rect.y = 670
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.colliderect(vrag.rect):
            hp -= 1
            if hp == 0:
                game = 0
            self.rect.x = 50
            self.rect.y = 315
            heal.rect.x = 180
        if self.rect.colliderect(vrag1.rect):
            hp -= 1
            if hp == 0:
                game = 0
            self.rect.x = 50
            self.rect.y = 315
            heal.rect.x = 70
            heal.rect.y = 600
        if self.rect.colliderect(vrag2.rect):
            hp -= 1
            if hp == 0:
                game = 0
            self.rect.x = 50
            self.rect.y = 315
            heal.rect.x = 580
            heal.rect.y = 190
        if self.rect.colliderect(vrag3.rect):
            hp -= 1
            if hp == 0:
                game = 0
            self.rect.x = 50
            self.rect.y = 315
            heal.rect.x = 400
            heal.rect.y = 450
        if self.rect.colliderect(vrag4.rect):
            hp -= 1
            if hp == 0:
                game = 0
            self.rect.x = 50
            self.rect.y = 315
            heal.rect.x = 350
            heal.rect.y = 640
        if self.rect.colliderect(vrag5.rect):
            hp -= 1
            if hp == 0:
                game = 0
            self.rect.x = 50
            self.rect.y = 315
            heal.rect.x = 600
            heal.rect.y = 580
        if self.rect.colliderect(vrag6.rect):
            hp -= 1
            if hp == 0:
                game = 0
            self.rect.x = 50
            self.rect.y = 315
            heal.rect.x = 500
            heal.rect.y = 315
        if self.rect.colliderect(heal.rect):
            hp += 1
            heal.rect.x = -1000
            if hp > 3:
                hp -= 1
        for i in coins.sprites():
            if self.rect.colliderect(i.rect):
                i.rect.x = -10000
                collect_coins += 1

    def resize(self, w, h):
        self.image = transform.scale(self.image, (w,h))
        x, y = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
#класс врага~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Enemy(Hero):
    def __init__(self, img, x, y, steps, steps2, speed):
        super().__init__(img, x, y)
        self.steps = steps
        self.steps2 = steps2
        self.distance = 0
        self.side = 1
        self.speed = speed

    def move(self):
        self.rect.y += self.side*self.speed
        self.distance += 1*self.speed
        if self.distance == self.steps:
            self.distance = 0
            self.side = -self.side
    def move2(self):
        self.rect.x += self.side*self.speed
        self.distance += 1*self.speed
        if self.distance == self.steps2:
            self.distance = 0
            self.side = -self.side

#~~~~~герой~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

player = Hero('pacman.png', 50, 315)
player.resize(32, 32)
#~~~враги~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
vrag = Enemy('blue.png', 300, 120, 310, 310, 1)
vrag.resize(32, 32)
vrag1 = Enemy('orange.png', 510, 200, 250, 250, 1)
vrag1.resize(32, 32)
vrag2 = Enemy('pink.png', 60, 445, 250, 250,  2)
vrag2.resize(32, 32)
vrag3 = Enemy('red.png', 60, 40, 150,100,  1)
vrag3.resize(32, 32)
vrag4 = Enemy('green.png', 60, 640, 550, 550, 2)
vrag4.resize(32, 32)
vrag5 = Enemy('yellow.png', 240, 250, 200, 200,  2)
vrag5.resize(32, 32)
vrag6 = Enemy('violet.png', 240, 380, 0, 200, 1)
vrag6.resize(32, 32)
#~~~здоровье~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
heal = Hero('strabbery.png', 180, 400)
heal.resize(30, 30)
#~~~~жизни~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cherry = image.load('cherry.png')
cherry = transform.scale(cherry, (40, 40))
#~~~~~стены~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
st1 = Hero('st_centr.png', 278, 288)
st2 = Hero('st2.png', 213, 163)
st3 = Hero('st2.png', 481, 163)
st4 = Hero('st3.png', 210, 73)
st5 = Hero('st3.png', 405, 73)
st6 = Hero('st4.png', 98, 73)
st7 = Hero('st4.png', 542, 73)
st8 = Hero('st5.png', 275, 160)
st9 = Hero('st5.png', 275, 418)
st10 = Hero('st5.png', 275, 545)
st11 = Hero('st6.png', 213, 352)
st12 = Hero('st6.png', 480, 352)
st13 = Hero('st7.png', 345, 38 )
st14 = Hero('st7.png', 345, 169 )
st15 = Hero('st7.png', 345, 425 )
st16 = Hero('st7.png', 345, 555 )
st17 = Hero('st7.png', 211, 548 )
st18 = Hero('st7.png', 545, 488 )
st19 = Hero('st7.png', 478, 548 )
st20 = Hero('st7.png', 145, 488 )
st21 = Hero('st8.png', 98, 160)
st22 = Hero('st8.png', 545, 160)
st23 = Hero('st8.png', 98, 480)
st24 = Hero('st8.png', 545, 480)
st25 = Hero('st8.png', 235, 225)
st26 = Hero('st8.png', 410, 225)
st27 = Hero('st9.png', 213, 482)
st28 = Hero('st9.png', 412, 481)
st29 = Hero('st10.png', 45, 545)
st30 = Hero('st10.png', 610, 545)
st31 = Hero('st11.png', 50, 348)
st32 = Hero('st11.png', 50, 220)
st33 = Hero('st11.png', 550, 348)
st34 = Hero('st11.png', 550, 220)
st35 = Hero('st12.png', 104, 610)
st36 = Hero('st12.png', 416, 610)
st37 = Hero('stena_verh.png', 54, 20)
st38 = Hero('stena_verh.png', 54, 670)
st39 = Hero('stenka_bok.png', 47, 20)
st40 = Hero('stenka_bok.png', 654, 20)
st41 = Hero('stenka_bok.png', 47, 445)
st42 = Hero('stenka_bok.png', 654,445)

walls = sprite.Group()
walls.add(st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11, st12, st13, st14, st15, st16, st17, st18, st19, st20, st21, st22, st23, st24, st25, st26, st27, st28, st29, st30, st31, st32, st33, st34, st35, st36, st37, st38, st39, st40, st41, st42)
#~~~монетки~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
c1 = Hero('coin.png', 200, 315)
c2 = Hero('coin.png', 400, 515)
c3 = Hero('coin.png', 510, 400)
c4 = Hero('coin.png', 400, 120)
c5 = Hero('coin.png', 60, 40)
c6 = Hero('coin.png', 150, 580)
c7 = Hero('coin.png', 60, 640)
c8 = Hero('coin.png', 380, 190)
c9 = Hero('coin.png', 470, 640)
c10 = Hero('coin.png', 590, 40)
c11 = Hero('coin.png', 180, 120)
c12 = Hero('coin.png', 300, 450)
coins = sprite.Group()
coins.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12)
for i in coins.sprites():
    i.resize(30,30)
#~~фон и логотип~~~~~~~~~~~~~~~~~~~~~~~~~
logo = Hero('logo.png', 710, 20)
logo.image = transform.scale(logo.image, (180, 50))


fon = image.load('fon.jpg')
fon = transform.scale(fon, (700, 800))
fon2 = image.load('fonfon.png')
fon3 = image.load('black.png')
fon3 = transform.scale(fon3, (1000, 1000))
fon4 = image.load('game_over.png')
fon4 = transform.scale(fon4, (300, 130))

#~~~~~сам игровой цикл~~~~~~~~~~~~~~~~~~~~~~~
while game == 1:
    keyboard = key.get_pressed()
    fon_start = image.load('start.jpg')
    fon_start = transform.scale(fon_start, (900, 700))
    fon_logo = image.load('logo.png')
    fon_logo = transform.scale(fon_logo, (400, 100))
    window.blit(fon_start, (0, 0))
    window.blit(fon_logo, (250, 60))
    start_text = shrift.render('Press any button to start', True, (255,255,255))
    window.blit(start_text, (270, 510))
    for e in event.get():
        if e.type == QUIT:
            exit()
        if e.type == KEYDOWN:
            if game == 1:
                start = time.get_ticks()
            game = 2
            while game == 2:
                window.blit(fon, (0, 0))
                window.blit(fon2, (700, 0))
                for e in event.get():
                    if e.type == QUIT:
                        game = 7
                
                player.control()
                player.show()
                coins.draw(window)
                    
                vrag.move2()
                vrag.show()
                vrag1.move()
                vrag1.show()
                vrag2.move2()
                vrag2.show()
                vrag3.move()
                vrag3.show()
                vrag4.move2()
                vrag4.show()
                vrag5.move2()
                vrag5.show()
                vrag6.move2()
                vrag6.show()
                heal.show()
                logo.show()
                if collect_coins == 12:
                    portal = Hero('portal.png', 650, 315)
                    portal.show()
                    if player.rect.colliderect(portal.rect):
                        game = 3
                    
                    
                for i in range(hp):
                    window.blit(cherry, (730 + 50*i, 90))
                    
                score_text = shrift.render('Your score:'+str(collect_coins), True, (255, 255, 255))
                window.blit(score_text, (710, 160))
                time_time = shrift.render('Your time:'+str((time.get_ticks()-start)//1000), True, (255, 255, 255))
                window.blit(time_time, (720,200))

                display.update()
                clock.tick(70)

        if game == 3:
            window.blit(fon3, (0, -150))
            window.blit(fon4, (300, 70))
            win_text = shrift.render('You won!!! Press any button to exit', True, (255,255,255))
            window.blit(time_time, (370,320))
            window.blit(score_text, (365, 360))
            window.blit(win_text, (210, 280))
            display.update()
            while True:
                keyboard = key.get_pressed()
                for e in event.get():
                    if e.type == QUIT:
                        exit()
                    if e.type == KEYDOWN:
                        exit()
                clock.tick(70)
        if game == 0:
            window.blit(fon3, (0, -150))
            window.blit(fon4, (300, 70))
            lose_text = shrift.render('You lose!!! Press any button to exit', True, (255,255,255))
            window.blit(time_time, (370,320))
            window.blit(score_text, (365, 360))
            window.blit(lose_text, (210, 280))
            display.update()
            while True:
                keyboard = key.get_pressed()
                for e in event.get():
                    if e.type == QUIT:
                        exit()
                    if e.type == KEYDOWN:
                        exit()
                clock.tick(70)

        display.update()
        clock.tick(70)