
import pygame, sys
from settings import *
from level import Level
from message_screen import *



pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
area = 3
start_screen = StartScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
typing_screen = TypingTextScreen(SCREEN_WIDTH, SCREEN_HEIGHT, START_TEXT)
level = Level(screen,area)
game_over = GameOver(SCREEN_WIDTH, SCREEN_HEIGHT,  60, (255, 255, 255))
image = pygame.image.load('./Assets/map_files/map_1/map_1.png')

def background_load(image):
    screen.blit(image, (0,0))




while True:
    delta_time = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    if level.start_text:
        typing_screen.run(screen, delta_time)
        pygame.display.flip()

        if typing_screen.is_typing_complete():
            break
    elif not level.started:
        if not level.start_text:
            start_screen.run(screen)
    else:
        if not level.over:
            level.run()
            
        elif level.over:
            game_over.run(screen)

    
    if level.next_lv:
        area += 1
        level = Level(screen,area)
        level.next_lv = False

   
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if level.over:
            level = Level(screen,area)

    if keys[pygame.K_f]:
        if not level.start_text:
            level.start_text = True

    if keys[pygame.K_RETURN]:
        if not level.started:
            level.started = True
            level.start_text = False
            del typing_screen
        

    pygame.display.update()
    clock.tick(60)