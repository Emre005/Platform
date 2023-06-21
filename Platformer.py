import pygame
import sys

# Pygame'ı başlat
pygame.init()

# Ekranın boyutlarını belirle
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Karakterin özelliklerini ayarla
x, y, width, height = 50, 500, 64, 64
vel = 5
isJump = False
jumpCount = 10
gravity = 5


class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)


# Platformları oluştur
platforms = [Platform(350, 500, 200, 10), Platform(150, 400, 200, 10), Platform(550, 300, 200, 10)]

# Arka plan görüntüsünü yükle
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Karakter resimlerini yükle ve ölçekle
character_right = pygame.image.load('character_right.png')
character_right = pygame.transform.scale(character_right, (width, height))

character_left = pygame.image.load('character_left.png')
character_left = pygame.transform.scale(character_left, (width, height))

# Karakterin başlangıç yönünü belirle
direction = 'right'

# Ana oyun döngüsü
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        direction = 'left'
    if keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel
        direction = 'right'
    if not isJump:  # Karakter zıplamıyorsa
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    on_ground = False
    for platform in platforms:
        if y + height < platform.rect.y or y > platform.rect.y + platform.rect.height or x > platform.rect.x + platform.rect.width or x + width < platform.rect.x:
            continue
        else:
            y = platform.rect.y - height
            if not isJump:
                jumpCount = 10
            on_ground = True
            break
    if not on_ground:
        y += gravity

    screen.blit(background, (0, 0))  # Arka planı çiz

    # Karakteri çiz
    if direction == 'right':
        screen.blit(character_right, (x, y))
    elif direction == 'left':
        screen.blit(character_left, (x, y))

    # Platformları çiz
    for platform in platforms:
        platform.draw(screen)

    pygame.display.update()  # Ekranı güncelle

pygame.quit()
