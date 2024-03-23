from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed


class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 500:
            self.direction = "right"
        if self.rect.x >= 700 - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


win_width = 700
win_height = 500

mixer.init()
mixer.music.load('sound/jungles.ogg')
mixer.music.play()

window = display.set_mode((win_width, win_height))
display.set_caption("Доганялки")
background = transform.scale(image.load("image/background.jpg"), (win_width, win_height))
clock = time.Clock()

player = Player("image/hero.png", 5, win_height - 80, 4)
monster = Enemy("image/cyborg.png", win_width - 120, 280, 2)
final = GameSprite("image/treasure.png", win_width - 120, win_height - 80, 0)

w1 = Wall(154, 205, 50, 100, 20, 590, 10)
w2 = Wall(154, 205, 50, 100, 490, 400, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 110, 10, 380)
w5 = Wall(154, 205, 50, 200, 110, 100, 10)
w6 = Wall(154, 205, 50, 390, 20, 10, 390)
w7 = Wall(154, 205, 50, 300, 210, 100, 10)
w8 = Wall(154, 205, 50, 200, 310, 100, 10)
w9 = Wall(154, 205, 50, 300, 400, 100, 10)
w10 = Wall(154, 205, 50, 490, 110, 10, 380)
w11 = Wall(154, 205, 50, 680, 20, 10, 480)

x1 = 100
x2 = 0
y1 = 100
y2 = 0

game = True
finish = False

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

money = mixer.Sound('sound/money.ogg')
kick = mixer.Sound('sound/kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

    display.update()
    clock.tick(60)
