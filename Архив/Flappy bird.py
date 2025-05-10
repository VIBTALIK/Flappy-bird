import random
import sys
import pygame
from pygame.locals import *


FPS = 32
scr_width = 289
scr_height = 511
display_screen_window = pygame.display.set_mode((scr_width, scr_height))
play_ground = scr_height * 0.8
game_image = {}
game_audio_sound = {}
player = 'images/bird.png'
bcg_image = 'images/background.png'
pipe_image = 'image/pipe.png'

def welcome_main_screen():
    p_x = int(scr_width / 5)
    p_y = int((scr_height - game_image['player'].get_height()) / 2)
    msgx = int((scr_width - game_image['message'].get_width()) / 2)
    msgy = int(scr_height * 0.13)
    b_x = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                display_screen_window.blit(game_image['background'], (0,0))
                display_screen_window.blit(game_image['player'], (p_x, p_y))
                display_screen_window.blit(game_image['message'], (msgx, msgy))
                display_screen_window.blit(game_image['base'], (b_x, play_ground))
                pygame.display.update()
                time_clock.tick(FPS)

def main_gameplay():
    score = 0
    p_x = int(scr_width / 5)
    p_y = int(scr_width / 2)
    b_x = 0

    n_pip1 = get_Random_Pipes()
    n_pip2 = get_Random_Pipes()

    up_pips = [
        {'x': scr_width + 200, 'y': n_pip1[0]['y']},
        {'x': scr_width + 200 + (scr_width / 2), 'y': n_pip2[0]['y']}
    ]

    low_pips = [
        {'x': scr_width + 200, 'y': n_pip1[1]['y']},
        {'x': scr_width + 200 + (scr_width / 2), 'y': n_pip2[1]['y']}
    ]

    pip_Vx = -4

    p_vx = -9
    p_mvx = 10
    p_mvy = -8
    p_accuracy = 1

    p_flap_accuracy = -8
    p_flap = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if p_y > 0:
                    p_vx = p_flap_accuracy
                    p_flap = True
                    game_audio_sound['wing'].play()
        
        cr_tst = is_Colliding(p_x, p_y, up_pips, low_pips)

        if cr_tst:
            return

        p_middle_positions = p_x + game_image['player'].get_width() / 2

        for pipe in up_pips:
            pip_middle_positions = pipe['x'] + game_image['pipe'][0].get_width() / 2
            if pip_middle_positions <= p_middle_positions < pip_middle_positions + 4:
                score += 1
                print('Ваши очки {score}')
                game_audio_sound['point'].play()


