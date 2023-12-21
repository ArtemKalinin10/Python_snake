import random
import pygame
import sys

pygame.init()

LENGHT = 1000
WIDHT = 1000
pygame.display.set_caption('Змейка')
screen = pygame.display.set_mode((LENGHT, WIDHT))
x = LENGHT // 2 - 20
y = WIDHT // 2 - 20
move_direction = ''
x_yab = random.randrange(0, LENGHT, 40)
y_yab = random.randrange(0, WIDHT, 40)
cnt = 0
color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
coords = [(x, y, 1, color)]
f1 = pygame.font.Font(None, 38)
game = True
FPS = 6
clock = pygame.time.Clock()
def setka():
    for i in range(0, LENGHT + 1, 40):
        for j in range(0, WIDHT + 1, 40):
            pygame.draw.rect(screen, (211, 211, 211), pygame.Rect(i, j, 40, 40), 1)
    text1 = f1.render(f'Счет: {cnt}', 1, (180, 0, 0))
    screen.blit(text1, (5, 5))
    pygame.display.flip()

def teleport():
    global x
    global y
    global game
    if y <= -40 or y >= WIDHT or x <= -40 or x >= LENGHT:
        game = False

def telo_zmei():
    global x 
    global y 
    global coords
    global move_direction
    global random_spisok
    global color
    
    if random_spisok != []:
        move_direction = random_spisok[0]
    if move_direction == 'x_-y':
        y -= 40
        coords.pop(0)
        coords.append((x, y, move_direction, color))
    elif move_direction == '-x_y':
        x -= 40
        coords.pop(0)
        coords.append((x, y, move_direction, color))
    elif move_direction == 'x_+y':
        y += 40
        coords.pop(0)
        coords.append((x, y, move_direction, color))
    elif move_direction == '+x_y':
        x += 40
        coords.pop(0)
        coords.append((x, y, move_direction, color))

def otrisovka():
    global coords
    for i in coords:
        pygame.draw.rect(screen, i[3], pygame.Rect(i[0], i[1], 40, 40))
def poedanye():
    global coords
    global x_yab
    global y_yab
    global cnt
    global color

    if coords[-1][0] == x_yab and coords[-1][1] == y_yab:
        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        if coords[0][2] == 'x_-y':
            coords.insert(0, (coords[0][0], coords[0][1] + 40, 'x_-y', color))
        elif coords[0][2] == '-x_y':
            coords.insert(0, (coords[0][0] + 40, coords[0][1], '-x_y', color))
        elif coords[0][2] == 'x_+y':
            coords.insert(0, (coords[0][0], coords[0][1] - 40, 'x_+y', color))
        elif coords[0][2] == '+x_y':
            coords.insert(0, (coords[0][0] - 40, coords[0][1], '+x_y', color))
        x_yab = random.randrange(0, LENGHT, 40)
        y_yab = random.randrange(0, WIDHT, 40)
        while True:
            flag = True
            for i in coords:
                if (i[0], i[1]) == (x_yab, y_yab):
                    x_yab = random.randrange(0, LENGHT, 40)
                    y_yab = random.randrange(0, WIDHT, 40)
                    flag = False
            if flag:
                break
        cnt += 1
    else:
        pygame.draw.circle(screen, 'RED', (x_yab + 20, y_yab + 20), 17)
        pygame.display.flip()

def konech():
    global coords
    global game
    for i in coords[:-1]:
        if i[0] == coords[-1][0] and i[1] == coords[-1][1]:
            game = False
            break
while game:
    random_spisok = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and move_direction != 'x_+y':
                move_direction = 'x_-y'
            elif event.key == pygame.K_a and move_direction != '+x_y':
                move_direction = '-x_y'
            elif event.key == pygame.K_s and move_direction != 'x_-y':
                move_direction = 'x_+y'
            elif event.key == pygame.K_d and move_direction != '-x_y':
                move_direction = '+x_y'
            random_spisok.append(move_direction)
            
    telo_zmei()
    teleport()
    otrisovka()
    setka()
    poedanye()
    konech()
    pygame.display.flip()
    screen.fill('BLACK')
    clock.tick(FPS)


while not game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('BLACK')
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('Вы проиграли!', 1, (180, 0, 0))
        screen.blit(text1, (LENGHT / 2 - 100, WIDHT / 2 - 300))
        text1 = f1.render(f'Ваш итоговый счет: {cnt}', 1, (180, 0, 0))
        screen.blit(text1, (LENGHT / 2 - 140, WIDHT / 2 - 200))
        pygame.display.flip()