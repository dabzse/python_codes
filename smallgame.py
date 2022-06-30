import pygame
import sys
from random import randint


# CONSTANTS
SCREEN_SIZE = WIDTH, HEIGHT = (1280, 720)
NUMBER_OF_OBJECTS = 27
OBJECT_SPEED = 16
OBJECT_COLOR_CLEAR = (226, 148, 168)
OBJECT_COLOR_INFECTED = (200, 0, 0)
OBJECT_COLOR_IMMUNE = (0, 226, 0)
OBJECT_RADIUS = 20
ILLNESS_TIME = 500
IMMUNE_TIME = 750
INFECTION_MASK_ON = 50
INFECTION_MASK_OFF = 4
FIRST_CONTACT = 1
BUDGET = 2000
VACCINE_PRICE = 75
MASK_PRICE = 10
FPS = 60


# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PY :: SmallGame")
fps = pygame.time.Clock()
time = 0
pause = False


# MObject class
class MObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = randint(-1, 1)
        self.dy = randint(-1, 1)
        self.illness = 0
        self.immune = 0
        self.mask = False
    
    def move(self):
        if randint(1, 30) == 1:
            self.dx = randint(-1, 1)
        if randint(1, 30) == 1:
            self.dy = randint(-1, 1)

        if OBJECT_RADIUS < self.x + self.dx < WIDTH - OBJECT_RADIUS:
            self.x += self.dx
        if OBJECT_RADIUS + 50 < self.y + self.dy < HEIGHT - OBJECT_RADIUS:
            self.y += self.dy
        
    def cure(self):
        if self.illness > 0:
            self.illness -= 1
            if self.illness == 0:
                self.immune = IMMUNE_TIME
        if self.immune > 0:
            self.immune -= 1


def vaccine(nobj, pos):
    global BUDGET
    for nobj in main_list:
        if nobj.x - OBJECT_RADIUS < pos[0] < nobj.x + OBJECT_RADIUS \
                and nobj.y - OBJECT_RADIUS < pos[1] < nobj.y + OBJECT_RADIUS:
            if nobj.illness == 0 and nobj.immune == 0:
                if BUDGET >= VACCINE_PRICE:
                    nobj.immune = IMMUNE_TIME
                    BUDGET -= VACCINE_PRICE


def add_mask(nobj, pos):
    global BUDGET
    for nobj in main_list:
        if nobj.x - OBJECT_RADIUS < pos[0] < nobj.x + OBJECT_RADIUS \
                and nobj.y - OBJECT_RADIUS < pos[1] < nobj.y + OBJECT_RADIUS:
            if not nobj.mask and BUDGET >= MASK_PRICE:
                nobj.mask = True
                BUDGET -= MASK_PRICE
            else:
                nobj.mask = False



def pos_move(object_list):
    for nobj in object_list:
        nobj.move()
        nobj.cure()

        for other in object_list:
            if id(nobj) != id(other):
                if other.x - 2 * OBJECT_RADIUS < nobj.x < other.x + 2 * OBJECT_RADIUS \
                        and other.y - 2 * OBJECT_RADIUS < nobj.y < other.y + 2 * OBJECT_RADIUS:
                    if other.illness > 0 and nobj.illness == 0 and nobj.immune == 0:
                        if nobj.mask == True or other.mask == True:
                            if randint(1, INFECTION_MASK_ON) == 1:
                                nobj.illness = ILLNESS_TIME
                        else:
                            if randint(1, INFECTION_MASK_OFF) == 1:
                                nobj.illness = ILLNESS_TIME


def draw(object_list):
    global pause
    _count_infected = 0
    screen.fill(color="#1982e4")

    for nobj in object_list:
        _mask = 0
        if nobj.illness > 0:
            _color = OBJECT_COLOR_INFECTED
            if nobj.mask:
                _mask = 5
        elif nobj.immune > 0:
            _color = OBJECT_COLOR_IMMUNE
            if nobj.mask:
                _mask = 5
        else:
            _color = OBJECT_COLOR_CLEAR
            if nobj.mask:
                _mask = 5

        pygame.draw.circle(screen, _color, (nobj.x, nobj.y), OBJECT_RADIUS, _mask)

        if nobj.illness > 0:
            _count_infected += 1
    
    if _count_infected == 0:
        pause = True
    
    font = pygame.font.SysFont("FreeSerif", 27)

    text = font.render("Active cases: " + str(_count_infected), True, (82, 85, 31))
    text_rect = text.get_rect()
    text_rect.left = 10
    text_rect.top = 10
    screen.blit(text, text_rect)

    text = font.render("Time: " + str(time), True, (82, 85, 31))
    text_rect = text.get_rect()
    text_rect.left = 189
    text_rect.top = 10
    screen.blit(text, text_rect)

    text = font.render("Budget: " + str(BUDGET), True, (82, 85, 31))
    text_rect = text.get_rect()
    text_rect.left = 316
    text_rect.top = 10
    screen.blit(text, text_rect)

    text = font.render("Clear:        Infected:        Immune:        Mask:        ", True, (82, 85, 31))
    text_rect = text.get_rect()
    text_rect.left = 613
    text_rect.top = 10
    screen.blit(text, text_rect)


    # notations
    pygame.draw.circle(screen, OBJECT_COLOR_CLEAR, (705, 23), OBJECT_RADIUS, 0)
    pygame.draw.circle(screen, OBJECT_COLOR_INFECTED, (850, 23), OBJECT_RADIUS, 0)
    pygame.draw.circle(screen, OBJECT_COLOR_IMMUNE, (1010, 23), OBJECT_RADIUS, 0)
    pygame.draw.circle(screen, OBJECT_COLOR_CLEAR, (1124, 23), OBJECT_RADIUS, 5)

    pygame.display.update()
    fps.tick(OBJECT_SPEED)


# objects
main_list = [MObject(randint(50, WIDTH - 50), randint(50, HEIGHT - 50)) for _ in range(NUMBER_OF_OBJECTS)]


# trouble starting here
for i in range(FIRST_CONTACT):
    main_list[i].illness = ILLNESS_TIME

# run
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys-exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause = not pause

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                vaccine(main_list, pygame.mouse.get_pos())
            if event.button == pygame.BUTTON_RIGHT:
                add_mask(main_list, pygame.mouse.get_pos())


    if not pause:
        pos_move(main_list)
        draw(main_list)
        time += 1
