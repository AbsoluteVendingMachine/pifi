#import sys, pygame, os
import sys
import pygame
import os
pygame.init()
#reference 1415920
#1, 2, 3, 4, 5, 9, 0
size = width, height = 160, 120
flags = pygame.SCALED
background = 0, 200, 50
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
player_position_x : float
player_position_y : float
player_walk_cycle : float
player_vectors = [False, False, False, False]
enemy_data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,] #value 1; type. value 2; hp. value 3 & 4; position. value 5 & 6; velocity. value 7; is the enemy hurt
player_idle_left = pygame.image.load(os.path.abspath('sprites/pi1.png'))
player_walk_left = [pygame.image.load(os.path.abspath('sprites/pi2.png')),
                pygame.image.load(os.path.abspath('sprites/pi1.png')),
                pygame.image.load(os.path.abspath('sprites/pi3.png')),
                pygame.image.load(os.path.abspath('sprites/pi1.png')),]
player_damaged_left = [pygame.image.load(os.path.abspath('sprites/pi4.png')),
                  pygame.image.load(os.path.abspath('sprites/blank.png'))]
player_idle_right = pygame.image.load(os.path.abspath('sprites/pi5.png'))
player_walk_right = [pygame.image.load(os.path.abspath('sprites/pi6.png')),
               pygame.image.load(os.path.abspath('sprites/pi5.png')),
               pygame.image.load(os.path.abspath('sprites/pi7.png')),
               pygame.image.load(os.path.abspath('sprites/pi5.png'))]
player_damaged_right = [pygame.image.load(os.path.abspath('sprites/pi8.png')),
                  pygame.image.load(os.path.abspath('sprites/blank.png'))]
enemy_hurt = [pygame.image.load(os.path.abspath('sprites/blank.png'))]
one_left = [pygame.image.load(os.path.abspath('sprites/numbers1.png')),
            pygame.image.load(os.path.abspath('sprites/numbers2.png')),
            pygame.image.load(os.path.abspath('sprites/numbers3.png')),
            pygame.image.load(os.path.abspath('sprites/numbers2.png'))]
two_left = [pygame.image.load(os.path.abspath('sprites/numbers4.png')),
            pygame.image.load(os.path.abspath('sprites/numbers5.png')),
            pygame.image.load(os.path.abspath('sprites/numbers6.png')),
            pygame.image.load(os.path.abspath('sprites/numbers5.png'))]
three_left = [pygame.image.load(os.path.abspath('sprites/numbers7.png')),
              pygame.image.load(os.path.abspath('sprites/numbers8.png'))]
four_left = [pygame.image.load(os.path.abspath('sprites/numbers9.png')),
             pygame.image.load(os.path.abspath('sprites/numbers10.png'))]
five_left = [pygame.image.load(os.path.abspath('sprites/numbers11.png')),
             pygame.image.load(os.path.abspath('sprites/numbers12.png'))]
nine_left = [pygame.image.load(os.path.abspath('sprites/numbers13.png')),
             pygame.image.load(os.path.abspath('sprites/numbers14.png')),
             pygame.image.load(os.path.abspath('sprites/numbers15.png')),
             pygame.image.load(os.path.abspath('sprites/numbers14.png'))]
one_right = [pygame.image.load(os.path.abspath('sprites/numbers19.png')),
            pygame.image.load(os.path.abspath('sprites/numbers20.png')),
            pygame.image.load(os.path.abspath('sprites/numbers21.png')),
            pygame.image.load(os.path.abspath('sprites/numbers20.png'))]
two_right = [pygame.image.load(os.path.abspath('sprites/numbers22.png')),
            pygame.image.load(os.path.abspath('sprites/numbers23.png')),
            pygame.image.load(os.path.abspath('sprites/numbers24.png')),
            pygame.image.load(os.path.abspath('sprites/numbers23.png'))]
three_right = [pygame.image.load(os.path.abspath('sprites/numbers25.png')),
              pygame.image.load(os.path.abspath('sprites/numbers26.png'))]
four_right = [pygame.image.load(os.path.abspath('sprites/numbers27.png')),
             pygame.image.load(os.path.abspath('sprites/numbers28.png'))]
five_right = [pygame.image.load(os.path.abspath('sprites/numbers29.png')),
             pygame.image.load(os.path.abspath('sprites/numbers30.png'))]
nine_right = [pygame.image.load(os.path.abspath('sprites/numbers31.png')),
             pygame.image.load(os.path.abspath('sprites/numbers32.png')),
             pygame.image.load(os.path.abspath('sprites/numbers33.png')),
             pygame.image.load(os.path.abspath('sprites/numbers32.png'))]
one_hurt = [pygame.image.load(os.path.abspath('sprites/hurt1.png')),
            pygame.image.load(os.path.abspath('sprites/hurt2.png'))]
two_hurt = [pygame.image.load(os.path.abspath('sprites/hurt3.png')),
            pygame.image.load(os.path.abspath('sprites/hurt2.png'))]
three_hurt = [pygame.image.load(os.path.abspath('sprites/hurt4.png')),
            pygame.image.load(os.path.abspath('sprites/hurt2.png'))]
four_hurt = [pygame.image.load(os.path.abspath('sprites/hurt5.png')),
            pygame.image.load(os.path.abspath('sprites/hurt2.png'))]
five_hurt = [pygame.image.load(os.path.abspath('sprites/hurt6.png')),
            pygame.image.load(os.path.abspath('sprites/hurt2.png'))]
nine_hurt = [pygame.image.load(os.path.abspath('sprites/hurt7.png')),
            pygame.image.load(os.path.abspath('sprites/hurt2.png'))]
zero_hurt = [pygame.image.load(os.path.abspath('sprites/hurt8.png')),
            pygame.image.load(os.path.abspath('sprites/hurt2.png'))]
zero = [pygame.image.load(os.path.abspath('sprites/numbers34.png')),
        pygame.image.load(os.path.abspath('sprites/numbers35.png')),
        pygame.image.load(os.path.abspath('sprites/numbers36.png'))]
grass = pygame.image.load(os.path.abspath('sprites/grass.png'))
pi_font = pygame.Font(os.path.abspath('x12y16pxMaruMonica.ttf'), 12)
pi_font2 = pygame.Font(os.path.abspath('x12y16pxMaruMonica.ttf'), 12)
#test_text = pi_font.render("testing hello world", False, (255, 255, 255), (0, 0, 0))
screen = pygame.display.set_mode(size, flags)
player_position_x = 0
player_position_y = 0
player_walk_cycle = 0
player_hurt_cycle = 0
enemy_fours = 0
enemy_twos = 0
attack_fours = 0
attack_twos = 0
player_state = 0
player_direction = 0
hud_selection = 0
hud_sprites = [pygame.image.load(os.path.abspath('sprites/hud1.png')),
               pygame.image.load(os.path.abspath('sprites/hud2.png')),
               pygame.image.load(os.path.abspath('sprites/hud3.png')),
               pygame.image.load(os.path.abspath('sprites/hud4.png')),]
weapon = [0, 0.0, 0.0, 0.0, 0, 0]
particles = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
subtraction = [pygame.image.load(os.path.abspath('sprites/weapon1.png')),
            pygame.image.load(os.path.abspath('sprites/weapon2.png')),
            pygame.image.load(os.path.abspath('sprites/weapon3.png')),
            pygame.image.load(os.path.abspath('sprites/weapon4.png'))]
addition = [pygame.image.load(os.path.abspath('sprites/weapon5.png')),
            pygame.image.load(os.path.abspath('sprites/weapon6.png'))]
multiplication = [pygame.image.load(os.path.abspath('sprites/weapon6.png')),
                  pygame.image.load(os.path.abspath('sprites/weapon5.png'))]
division = [pygame.image.load(os.path.abspath('sprites/weapon7.png')),
            pygame.image.load(os.path.abspath('sprites/weapon8.png')),
            pygame.image.load(os.path.abspath('sprites/weapon9.png')),
            pygame.image.load(os.path.abspath('sprites/weapon10.png'))]
particle = [pygame.image.load(os.path.abspath('sprites/hit4.png')),
            pygame.image.load(os.path.abspath('sprites/hit3.png')),
            pygame.image.load(os.path.abspath('sprites/hit2.png')),
            pygame.image.load(os.path.abspath('sprites/hit1.png'))]
three_direction = 0.0
game_state = 0
titlescreen = pi_font.render("pifi", False, (255, 255, 255), (0, 0, 0))
to_start = pi_font.render("press x to start", False, (255, 255, 255), (0, 0, 0))
instructions_one = pi_font.render("you play as pi", False, (255, 255, 255), (0, 0, 0))
instructions_two = pi_font.render("move with the arrow keys", False, (255, 255, 255), (0, 0, 0))
instructions_three = pi_font.render("attack with WASD keys", False, (255, 255, 255), (0, 0, 0))
instructions_four = pi_font.render("use your math to win", False, (255, 255, 255), (0, 0, 0))
instructions_five = pi_font.render("change your math with Q & E", False, (255, 255, 255), (0, 0, 0))
instructions_six = pi_font.render("press x to start game", False, (255, 255, 255), (0, 0, 0))
level = 0
enemy_threshold = 0
player_hit = 0
transition_to_next_level = 0
score = 5077
ticks = 0
respawn = [pygame.image.load(os.path.abspath('sprites/respawn1.png')),
           pygame.image.load(os.path.abspath('sprites/respawn2.png')),
           pygame.image.load(os.path.abspath('sprites/respawn3.png')),
           pygame.image.load(os.path.abspath('sprites/respawn4.png')),
           pygame.image.load(os.path.abspath('sprites/respawn5.png')),
           pygame.image.load(os.path.abspath('sprites/respawn6.png'))]
zero_anim = 0
attack_sfx = pygame.mixer.Sound(os.path.abspath('sfx/attack.wav'))
hurt_sfx = pygame.mixer.Sound(os.path.abspath('sfx/death.wav'))
enemy_sfx = pygame.mixer.Sound(os.path.abspath('sfx/kill.wav'))
#ingame_music = pygame.mixer.music.load(os.path.abspath('music/pifi_ingame.ogg'))
#title_music = pygame.mixer.music.load(os.path.abspath('music/pifi_title.ogg'))

def load_level(value):
    if value == 0:
        spawn_enemy(1, 1, 32, 65, 0, 0, 0)
        spawn_enemy(1, 1, 70, 65, 0, 0, 0)
        spawn_enemy(1, 1, 55, 100, 0, 0, 0)
    
    elif value == 1:
        spawn_enemy(2, 2, 0, 64, 0, 0, 0)
        spawn_enemy(2, 2, 120, 64, 0, 0, 0)
    
    elif value == 2:
        spawn_enemy(1, 1, 18, 29, 0, 0, 0)
        spawn_enemy(2, 2, 80, 100, 0, 0, 0)
        spawn_enemy(3, 3, 120, 0, 0, 0, 0)

    elif value == 3:
        spawn_enemy(2, 2, 38, 100, 0, 0, 0)
        spawn_enemy(3, 3, 140, 100, 0, 0, 0)
        spawn_enemy(2, 2, 140, 0, 0, 0, 0)
    
    elif value == 4:
        spawn_enemy(4, 4, 0, 80, 0, 0, 0)
        spawn_enemy(4, 4, 50, 80, 0, 0, 0)
        spawn_enemy(4, 4, 30, 30, 0, 0, 0)
        spawn_enemy(4, 4, 80, 30, 0, 0, 0)
    
    elif value == 5:
        spawn_enemy(1, 1, 0, 0, 0, 0, 0)
        spawn_enemy(2, 2, 50, 0, 0, 0, 0)
        spawn_enemy(3, 3, 100, 0, 0, 0, 0)
        spawn_enemy(4, 4, 25, 0, 0, 0, 0)
        spawn_enemy(5, 5, 75, 0, 0, 0, 0)
    
    elif value == 6:
        spawn_enemy(5, 5, 40, 40, 0, 0, 0)
        spawn_enemy(5, 5, 120, 40, 0, 0, 0)
    
    elif value == 7:
        spawn_enemy(4, 4, 60, 60, 0, 0, 0)
        spawn_enemy(4, 4, 100, 60, 0, 0, 0)
        spawn_enemy(4, 4, 80, 80, 0, 0, 0)
        spawn_enemy(4, 4, 80, 40, 0, 0, 0)
        spawn_enemy(5, 5, 0, 0, 0, 0, 0)
    
    elif value == 8:
        spawn_enemy(2, 2, 60, 60, 0, 0, 0)
        spawn_enemy(2, 2, 100, 60, 0, 0, 0)
        spawn_enemy(2, 2, 80, 80, 0, 0, 0)
        spawn_enemy(2, 2, 80, 40, 0, 0, 0)
    
    elif value == 9:
        spawn_enemy(3, 3, 60, 60, 0, 0, 0)
        spawn_enemy(3, 3, 100, 60, 0, 0, 0)
    
    elif value == 10:
        spawn_enemy(5, 5, 60, 0, 0, 0, 0)
    
    elif value == 11:
        spawn_enemy(9, 9, 0, 0, 0, 0, 0)
    
    elif value == 12:
        spawn_enemy(1, 1, 60, 60, 0, 0, 0)
        spawn_enemy(1, 1, 100, 60, 0, 0, 0)
        spawn_enemy(9, 9, 80, 0, 0, 0, 0)
    
    elif value == 13:
        spawn_enemy(9, 9, 20, 60, 0, 0, 0)
        spawn_enemy(9, 9, 140, 60, 0, 0, 0)
        spawn_enemy(9, 9, 80, 120, 0, 0, 0)
        spawn_enemy(9, 9, 80, 0, 0, 0, 0)
    
    elif value == 14:
        spawn_enemy(3, 3, 20, 60, 0, 0, 0)
        spawn_enemy(2, 2, 140, 60, 0, 0, 0)
        spawn_enemy(4, 4, 80, 120, 0, 0, 0)
        spawn_enemy(9, 9, 80, 0, 0, 0, 0)
    
    elif value == 15:
        spawn_enemy(5, 5, 100, 60, 0, 0, 0)
        spawn_enemy(5, 5, 60, 60, 0, 0, 0)
        spawn_enemy(9, 9, 80, 140, 0, 0, 0)
    
    elif value == 16:
        spawn_enemy(1, 1, 0, 0, 0, 0, 0)
    
    elif value == 17:
        spawn_enemy(9, 9, 0, 0, 0, 0, 0)
        spawn_enemy(4, 4, 50, 0, 0, 0, 0)
        spawn_enemy(2, 2, 100, 0, 0, 0, 0)
        spawn_enemy(4, 4, 25, 0, 0, 0, 0)
        spawn_enemy(9, 9, 75, 0, 0, 0, 0)
    
    elif value == 18:
        spawn_enemy(4, 4, 80, 80, 0, 0, 0)
        spawn_enemy(1, 1, 80, 40, 0, 0, 0)
    
    elif value == 19:
        spawn_enemy(1, 1, 39, 100, 0, 0, 0)
        spawn_enemy(9, 9, 230, 100, 0, 0, 0)
    
    elif value == 20:
        spawn_enemy(2, 2, 0, 0, 0, 0, 0)
        spawn_enemy(4, 4, 0, 0, 0, 0, 0)
        spawn_enemy(9, 9, 0, 0, 0, 0, 0)
    
    elif value == 21:
        spawn_enemy(9, 9, 160, 120, 0, 0, 0)
        spawn_enemy(9, 9, 0, 0, 0, 0, 0)
    
    elif value == 22:
        spawn_enemy(9, 9, 0, 0, 0, 0, 0)
        spawn_enemy(1, 1, 0, 0, 0, 0, 0)
        spawn_enemy(1, 1, 0, 0, 0, 0, 0)
        
    elif value == 23:
        spawn_enemy(1, 1, 60, 60, 0, 0, 0)
        spawn_enemy(1, 1, 100, 60, 0, 0, 0)
        spawn_enemy(1, 1, 80, 80, 0, 0, 0)
        spawn_enemy(1, 1, 80, 40, 0, 0, 0)
    
    elif value == 24:
        spawn_enemy(3, 3, 60, 60, 0, 0, 0)
        spawn_enemy(3, 3, 100, 60, 0, 0, 0)
        spawn_enemy(3, 3, 80, 80, 0, 0, 0)
        spawn_enemy(3, 3, 80, 40, 0, 0, 0)
    
    elif value == 25:
        spawn_enemy(5, 5, 60, 60, 0, 0, 0)
        spawn_enemy(5, 5, 100, 60, 0, 0, 0)
        spawn_enemy(5, 5, 80, 80, 0, 0, 0)
        spawn_enemy(5, 5, 80, 40, 0, 0, 0)
    
    elif value == 26:
        spawn_enemy(4, 4, 160, 120, 0, 0, 0)
    
    elif value == 27:
        spawn_enemy(5, 5, 80, 80, 0, 0, 0)
        spawn_enemy(2, 2, 80, 80, 0, 0, 0)
        spawn_enemy(2, 2, 80, 80, 0, 0, 0)
        spawn_enemy(9, 9, 80, 80, 0, 0, 0)
    
    elif value == 28:
        spawn_enemy(9, 9, 100, 60, 5, 0, 0)
        spawn_enemy(9, 9, 60, 60, -5, 0, 0)
    
    elif value == 29:
        spawn_enemy(1, 1, 0, 0, 0, 0, 0)
        spawn_enemy(1, 1, 140, 0, 0, 0, 0)
        spawn_enemy(1, 1, 140, 100, 0, 0, 0)
        spawn_enemy(1, 1, 0, 100, 0, 0, 0)
    
    elif value == 30:
        spawn_enemy(1, 1, 140, 100, 0, 0, 0)
    
    elif value == 31:
        spawn_enemy(9, 9, 0, 0, 0, 0, 0)
        spawn_enemy(9, 9, 50, 0, 0, 0, 0)
        spawn_enemy(9, 9, 100, 0, 0, 0, 0)
        spawn_enemy(9, 9, 25, 0, 0, 0, 0)
        spawn_enemy(9, 9, 75, 0, 0, 0, 0)
    
    elif value == 32:
        value = 32

def render_grass():
    screen.blit(grass, (113, 23))
    screen.blit(grass, (81, 67))
    screen.blit(grass, (20, 100))
    screen.blit(grass, (30, 43))

def render_particles(value : int):
    particle_value = value * 3
    if particles[2 + particle_value] > 0:
        screen.blit(particle[int(particles[2 + particle_value])], (particles[0 + particle_value], particles[1 + particle_value]))
        particles[2 + particle_value] -= 0.2

def spawn_particle(x, y):
    if particles[2] <= 0:
        particles[2] = 3
        particles[0] = x
        particles[1] = y
    
    elif particles[5] <= 0:
        particles[5] = 3
        particles[3] = x
        particles[4] = y
    
    elif particles[8] <= 0:
        particles[8] = 3
        particles[6] = x
        particles[7] = y
    
    elif particles[11] <= 0:
        particles[11] = 3
        particles[9] = x
        particles[10] = y
    
    elif particles[14] <= 0:
        particles[14] = 3
        particles[12] = x
        particles[13] = y

def attack(weapon_type : int, x_vector : float, y_vector: float):
    attack_sfx.play()
    weapon[0] = weapon_type
    weapon[4] = x_vector
    weapon[5] = y_vector
    weapon[3] = 3
    weapon[1] = player_position_x
    weapon[2] = player_position_y

def attack_logic():
    if weapon[3] > 0:
        weapon[1] += weapon[4]
        weapon[2] += weapon[5]
        weapon[3] -= 0.2
        
        if weapon[0] == 0:
            screen.blit(subtraction[int(attack_fours)], (int(weapon[1]), int(weapon[2])))

        elif weapon[0] == 1:
            screen.blit(addition[int(attack_twos)], (int(weapon[1]), int(weapon[2])))

        elif weapon[0] == 2:
            screen.blit(multiplication[int(attack_twos)], (int(weapon[1]), int(weapon[2])))

        else:
            screen.blit(division[int(attack_fours)], (int(weapon[1]), int(weapon[2])))
    
    else:
        weapon[1] = -500
        weapon[2] = -500

def render_hud():
    screen.blit(hud_sprites[hud_selection], (111, -2))

def spawn_enemy(enemy_type, hp, position_x, position_y, velocity_x, velocity_y, hurt):
    if enemy_data[0] < 1:
        enemy_data[0] = enemy_type
        enemy_data[1] = hp
        enemy_data[2] = position_x
        enemy_data[3] = position_y
        enemy_data[4] = velocity_x
        enemy_data[5] = velocity_y
        enemy_data[6] = hurt
    
    elif enemy_data[7] < 1:
        enemy_data[7] = enemy_type
        enemy_data[8] = hp
        enemy_data[9] = position_x
        enemy_data[10] = position_y
        enemy_data[11] = velocity_x
        enemy_data[12] = velocity_y
        enemy_data[13] = hurt
    
    elif enemy_data[14] < 1:
        enemy_data[14] = enemy_type
        enemy_data[15] = hp
        enemy_data[16] = position_x
        enemy_data[17] = position_y
        enemy_data[18] = velocity_x
        enemy_data[19] = velocity_y
        enemy_data[20] = hurt
    
    elif enemy_data[21] < 1:
        enemy_data[21] = enemy_type
        enemy_data[22] = hp
        enemy_data[23] = position_x
        enemy_data[24] = position_y
        enemy_data[25] = velocity_x
        enemy_data[26] = velocity_y
        enemy_data[27] = hurt
    
    elif enemy_data[28] < 1:
        enemy_data[28] = enemy_type
        enemy_data[29] = hp
        enemy_data[30] = position_x
        enemy_data[31] = position_y
        enemy_data[32] = velocity_x
        enemy_data[33] = velocity_y
        enemy_data[34] = hurt

def enemy_logic(value : int):
    enemy_value = 7 * value
    if enemy_data[1 + enemy_value] >= 1 and enemy_data[1 + enemy_value] < 10:
        if enemy_data[6 + enemy_value] > 0:
            if enemy_data[0 + enemy_value] == 1:
                screen.blit(one_hurt[int(enemy_data[6 + enemy_value])], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
            
            elif enemy_data[0 + enemy_value] == 2:
                screen.blit(two_hurt[int(enemy_data[6 + enemy_value])], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
            
            elif enemy_data[0 + enemy_value] == 3:
                screen.blit(three_hurt[int(enemy_data[6 + enemy_value])], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
            
            elif enemy_data[0 + enemy_value] == 4:
                screen.blit(four_hurt[int(enemy_data[6 + enemy_value])], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
            
            elif enemy_data[0 + enemy_value] == 5:
                screen.blit(five_hurt[int(enemy_data[6 + enemy_value])], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
            
            elif enemy_data[0 + enemy_value] == 9:
                screen.blit(nine_hurt[int(enemy_data[6 + enemy_value])], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))

            enemy_data[6 + enemy_value] -= 0.5
        
        elif enemy_data[6 + enemy_value] <= 0:
            if abs(enemy_data[2 + enemy_value] - weapon[1]) < 8 and abs(enemy_data[3 + enemy_value] - weapon[2]) < 8:
                enemy_sfx.play()
                weapon[1] = -500
                weapon[2] = -500
                weapon[3] = 0
                weapon[4] = 0
                weapon[5] = 0
                enemy_data[6] = 1

                if enemy_data[0 + enemy_value] < 10:
                    if weapon[0] == 0:
                        enemy_data[1 + enemy_value] -= 1
                    
                    elif weapon[0] == 1:
                        enemy_data[1 + enemy_value] += 1
                    
                    elif weapon[0] == 2:
                        enemy_data[1 + enemy_value] *= 2
                
                    elif weapon[0] == 3:
                        enemy_data[1 + enemy_value] /= 2
                        if enemy_data[0 + enemy_value] == 10:
                            enemy_data[1 + enemy_value] -= 100
                
                #if enemy_data[1 + enemy_value] < 1 or enemy_data[1 + enemy_value] > 10:
                    #spawn_particle(2 + enemy_value, 3 + enemy_value)
                
                
    else:
        enemy_data[0 + enemy_value] = 0.0
        enemy_data[1 + enemy_value] = 0.0
        enemy_data[2 + enemy_value] = 0.0
        enemy_data[3 + enemy_value] = 0.0
        enemy_data[4 + enemy_value] = 0.0
        enemy_data[5 + enemy_value] = 0.0
        enemy_data[6 + enemy_value] = 0.0

    if enemy_data[1 + enemy_value] >= 1 and enemy_data[1 + enemy_value] < 10:
        if enemy_data[0 + enemy_value] == 1:
            if enemy_data[2 + enemy_value] < player_position_x:
                enemy_data[4 + enemy_value] = 0.25

            elif enemy_data[2 + enemy_value] > player_position_x:
                enemy_data[4 + enemy_value] = -0.25

            if enemy_data[3 + enemy_value] < player_position_y:
                enemy_data[5 + enemy_value] = 0.25

            elif enemy_data[3 + enemy_value] > player_position_y:
                enemy_data[5 + enemy_value] = -0.25
        
            enemy_data[2 + enemy_value] += enemy_data[4 + enemy_value]
            enemy_data[3 + enemy_value] += enemy_data[5 + enemy_value]

            if not enemy_data[6 + enemy_value] > 0:
                if enemy_data[2 + enemy_value] < player_position_x:
                    screen.blit(one_right[int(enemy_fours)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
                
                else:
                    screen.blit(one_left[int(enemy_fours)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
        
        elif enemy_data[0 + enemy_value] == 2:
            if enemy_data[2 + enemy_value] < player_position_x:
                enemy_data[4 + enemy_value] += 0.05
            
            elif enemy_data[2 + enemy_value] > player_position_x:
                enemy_data[4 + enemy_value] -= 0.05
            
            if enemy_data[3 + enemy_value] > player_position_y:
                enemy_data[5 + enemy_value] -= 0.05
            
            elif enemy_data[3 + enemy_value] < player_position_y:
                enemy_data[5 + enemy_value] += 0.05
            
            if enemy_data[4 + enemy_value] > 0.4:
                enemy_data[4 + enemy_value] = 0.4
            
            if enemy_data[4 + enemy_value] < -0.4:
                enemy_data[4 + enemy_value] = -0.4
            
            if enemy_data[5 + enemy_value] > 0.4:
                enemy_data[5 + enemy_value] = 0.4
            
            if enemy_data[5 + enemy_value] < -0.4:
                enemy_data[5 + enemy_value] = -0.4
            
            enemy_data[2 + enemy_value] += enemy_data[4 + enemy_value]
            enemy_data[3 + enemy_value] += enemy_data[5 + enemy_value]

            if not enemy_data[6 + enemy_value] > 0:
                if enemy_data[2 + enemy_value] < player_position_x:
                    screen.blit(two_right[int(enemy_fours)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
                
                else:
                    screen.blit(two_left[int(enemy_fours)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
        
        elif enemy_data[0 + enemy_value] == 3:
            if three_direction < 3:
                enemy_data[4 + enemy_value] += 0.075

            else:
                enemy_data[4 + enemy_value] -= 0.075
            
            if enemy_data[4 + enemy_value] > 0.4:
                enemy_data[4 + enemy_value] = 0.4

            if enemy_data[4 + enemy_value] < -0.4:
                enemy_data[4 + enemy_value] = -0.4
            
            enemy_data[2 + enemy_value] += enemy_data[4 + enemy_value]
            enemy_data[3 + enemy_value] += enemy_data[5 + enemy_value]

            if not enemy_data[6 + enemy_value] > 0:
                if enemy_data[2 + enemy_value] < player_position_x:
                    screen.blit(three_right[int(enemy_twos)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
                
                else:
                    screen.blit(three_left[int(enemy_twos)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
        
        elif enemy_data[0 + enemy_value] == 4:
            if three_direction == 0 or three_direction == 3:
                if enemy_data[2 + enemy_value] < player_position_x:
                    enemy_data[4 + enemy_value] += 1
                
                elif enemy_data[2 + enemy_value] > player_position_x:
                    enemy_data[4 + enemy_value] -= 1
                
                if enemy_data[3 + enemy_value] > player_position_y:
                    enemy_data[5 + enemy_value] -= 1
                
                elif enemy_data[3 + enemy_value] < player_position_y:
                    enemy_data[5 + enemy_value] += 1
            
            if enemy_data[4 + enemy_value] > 2:
                enemy_data[4 + enemy_value] = 2
            
            if enemy_data[4 + enemy_value] < -2:
                enemy_data[4 + enemy_value] = -2
            
            if enemy_data[5 + enemy_value] > 2:
                enemy_data[5 + enemy_value] = 2
            
            if enemy_data[5 + enemy_value] < -2:
                enemy_data[5 + enemy_value] = -2
            
            enemy_data[2 + enemy_value] += enemy_data[4 + enemy_value]
            enemy_data[3 + enemy_value] += enemy_data[5 + enemy_value]
            enemy_data[4 + enemy_value] *= 0.89
            enemy_data[5 + enemy_value] *= 0.89

            if not enemy_data[6 + enemy_value] > 0:
                if enemy_data[2 + enemy_value] < player_position_x:
                    screen.blit(four_right[int(enemy_twos)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
                
                else:
                    screen.blit(four_left[int(enemy_twos)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
        
        elif enemy_data[0 + enemy_value] == 5:
            if not enemy_data[6 + enemy_value] > 0:
                if enemy_data[2 + enemy_value] < player_position_x:
                    screen.blit(five_right[int(enemy_twos)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
                
                else:
                    screen.blit(five_left[int(enemy_twos)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
        
        elif enemy_data[0 + enemy_value] == 9:
            if enemy_data[2 + enemy_value] < player_position_x:
                enemy_data[4 + enemy_value] += 0.05
            
            elif enemy_data[2 + enemy_value] > player_position_x:
                enemy_data[4 + enemy_value] -= 0.05
            
            if enemy_data[3 + enemy_value] > player_position_y:
                enemy_data[5 + enemy_value] -= 0.05
            
            elif enemy_data[3 + enemy_value] < player_position_y:
                enemy_data[5 + enemy_value] += 0.05
            
            if enemy_data[4 + enemy_value] > 0.8:
                enemy_data[4 + enemy_value] = 0.8
            
            if enemy_data[4 + enemy_value] < -0.8:
                enemy_data[4 + enemy_value] = -0.8
            
            if enemy_data[5 + enemy_value] > 0.8:
                enemy_data[5 + enemy_value] = 0.8
            
            if enemy_data[5 + enemy_value] < -0.8:
                enemy_data[5 + enemy_value] = -0.8
            
            enemy_data[2 + enemy_value] += enemy_data[4 + enemy_value]
            enemy_data[3 + enemy_value] += enemy_data[5 + enemy_value]

            if not enemy_data[6 + enemy_value] > 0:
                if enemy_data[2 + enemy_value] < player_position_x:
                    screen.blit(nine_right[int(enemy_fours)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
                
                else:
                    screen.blit(nine_left[int(enemy_fours)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
        
        elif enemy_data[0 + enemy_value] == 10:
            if enemy_data[2 + enemy_value] < player_position_x:
                enemy_data[4 + enemy_value] = 0.3

            elif enemy_data[2 + enemy_value] > player_position_x:
                enemy_data[4 + enemy_value] = -0.3

            if enemy_data[3 + enemy_value] < player_position_y:
                enemy_data[5 + enemy_value] = 0.3

            elif enemy_data[3 + enemy_value] > player_position_y:
                enemy_data[5 + enemy_value] = -0.3
        
            enemy_data[2 + enemy_value] += enemy_data[4 + enemy_value]
            enemy_data[3 + enemy_value] += enemy_data[5 + enemy_value]

            if not enemy_data[6 + enemy_value] > 0:
                if enemy_data[2 + enemy_value] < player_position_x:
                    screen.blit(zero[int(enemy_fours)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
                
                else:
                    screen.blit(zero[int(enemy_fours)], (enemy_data[2 + enemy_value], enemy_data[3 + enemy_value]))
            
    if enemy_data[2 + enemy_value] > 140:
        enemy_data[2 + enemy_value] = 140
    
    if enemy_data[2 + enemy_value] < 0:
        enemy_data[2 + enemy_value] = 0
    
    if enemy_data[3 + enemy_value] < 10:
        enemy_data[3 + enemy_value] = 10
        
def movement_vector_active(value : int):
    player_vectors[value] = True
    #player_state = 1

def movement_vector_deactive(value : int):
    player_vectors[value] = False

def render_player():
    if player_state == 0:
        if player_direction == 0:
            screen.blit(player_idle_left, (int(player_position_x), int(player_position_y)))

        else:
            screen.blit(player_idle_right, (int(player_position_x), int(player_position_y)))

    elif player_state == 1:
        if player_direction == 0:
            screen.blit(player_walk_left[int(player_walk_cycle)], (int(player_position_x), int(player_position_y)))

        else:
            screen.blit(player_walk_right[int(player_walk_cycle)], (int(player_position_x), int(player_position_y)))

    elif player_state == 2:
        if player_direction == 0:
            screen.blit(player_damaged_left[int(player_hurt_cycle)], (int(player_position_x), int(player_position_y)))

        else:
            screen.blit(player_damaged_right[int(player_hurt_cycle)], (int(player_position_x), int(player_position_y)))

#spawn_enemy(9, 9, 64, 64, 0, 0, 0)
#spawn_enemy(3, 3, 20, 20, 0, 0, 0)
#spawn_enemy(3, 3, 96, 96, 0, 0, 0)
#spawn_enemy(1, 1, 128, 128, 0, 0, 0)
#spawn_enemy(5, 5, 40, 88, 0, 0, 0)

pygame.mixer.music.load(os.path.abspath("music/pifi_title.ogg"))
pygame.mixer.music.play(-1)

while game_state == 0:
    screen.fill(background)
    render_grass()
    screen.blit(titlescreen, (40, 30))
    screen.blit(to_start, (40, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_state = 1

    pygame.display.flip()

while game_state == 1:
    screen.fill(background)
    render_grass()
    screen.blit(instructions_one, (0, 0))
    screen.blit(instructions_two, (0, 12))
    screen.blit(instructions_three, (0, 24))
    screen.blit(instructions_four, (0, 36))
    screen.blit(instructions_five, (0, 48))
    screen.blit(instructions_six, (0, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_state = 2
                level = 0
                player_hit = False
                transition_to_next_level = 1
                player_hit = 0

    pygame.display.flip()


pygame.mixer.music.unload()
pygame.mixer.music.stop()
pygame.mixer.music.load(os.path.abspath('music/pifi_ingame.ogg'))
pygame.mixer.music.play(-1)

while game_state == 2:
    ticks += 0.001

    if level == 33:
        game_state = 3

    if enemy_data[0] > 0:
        if abs(player_position_x - enemy_data[2]) < 2 and abs(player_position_y - enemy_data[3]) < 2:
            player_hit = 1
    
    if enemy_data[7] > 0:
        if abs(player_position_x - enemy_data[9]) < 2 and abs(player_position_y - enemy_data[10]) < 2:
            player_hit = 1
    
    if enemy_data[14] > 0:
        if abs(player_position_x - enemy_data[16]) < 2 and abs(player_position_y - enemy_data[17]) < 2:
            player_hit = 1

    if enemy_data[21] > 0:
        if abs(player_position_x - enemy_data[23]) < 2 and abs(player_position_y - enemy_data[24]) < 2:
            player_hit = 1
    
    if enemy_data[28] > 0:
        if abs(player_position_x - enemy_data[30]) < 2 and abs(player_position_y - enemy_data[31]) < 2:
            player_hit = 1
    
    #elif abs(player_position_x - enemy_data[16]) < 1 and abs(player_position_y - enemy_data[17]) < 1:
    #    player_hit = 1
    
    #elif abs(player_position_x - enemy_data[23]) < 1 and abs(player_position_y - enemy_data[24]) < 1:
    #    player_hit = 1
    
    #elif abs(player_position_x - enemy_data[30]) < 1 and abs(player_position_y - enemy_data[31]) < 1:
    #    player_hit = 1

    if player_hit == 1:
        hurt_sfx.play()
        player_hit = 0
        transition_to_next_level = 1
    
    if transition_to_next_level == 1:
        player_position_x = 80
        player_position_y = 60
        transition_to_next_level = 0
        player_vectors = [False, False, False, False]
        enemy_data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,]
        load_level(level)
    
    if enemy_data[1] < 1 or enemy_data[1] > 10:
        if enemy_data[8] < 1 or enemy_data[7] > 10:
            if enemy_data[15] < 1 or enemy_data[13] > 10:
                if enemy_data[22] < 1 or enemy_data[20] > 10:
                    if enemy_data[29] < 1 or enemy_data[27] > 10:
                        player_hit = 0
                        transition_to_next_level = 1
                        level += 1

    if player_position_x > 140:
        player_position_x = 140
    
    if player_position_x < 0:
        player_position_x = 0
    
    if player_position_y < 10:
        player_position_y = 10
    
    if player_position_y > 110:
        player_position_y = 110

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if weapon[3] <= 0:
                if event.key == pygame.K_d:
                    attack(hud_selection, 1.75, 0)
                
                if event.key == pygame.K_a:
                    attack(hud_selection, -1.75, 0)
                
                if event.key == pygame.K_w:
                    attack(hud_selection, 0, -1.75)
                
                if event.key == pygame.K_s:
                    attack(hud_selection, 0, 1.75)

            if event.key == pygame.K_RIGHT:
                movement_vector_active(1)
                player_state = 1
                player_direction = 1
            
            if event.key == pygame.K_LEFT:
                movement_vector_active(0)
                player_state = 1
                player_direction = 0
            
            if event.key == pygame.K_UP:
                movement_vector_active(2)
                player_state = 1
            
            if event.key == pygame.K_DOWN:
                movement_vector_active(3)
                player_state = 1
            
            if event.key == pygame.K_q:
                hud_selection -= 1
                if hud_selection < 0:
                    hud_selection = 3
            
            if event.key == pygame.K_e:
                hud_selection += 1
                if hud_selection > 3:
                    hud_selection = 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                movement_vector_deactive(1)
            
            if event.key == pygame.K_LEFT:
                movement_vector_deactive(0)
            
            if event.key == pygame.K_UP:
                movement_vector_deactive(2)
            
            if event.key == pygame.K_DOWN:
                movement_vector_deactive(3)

        #if not (event.type == pygame.K_RIGHT and
                #event.type == pygame.K_LEFT and
                #event.type == pygame.K_DOWN and
                #event.type == pygame.K_UP):
            #player_state = "idle"

    enemy_fours += 0.2
    if enemy_fours >= 4:
        enemy_fours = 0
    
    enemy_twos += 0.2
    if enemy_twos >= 2:
        enemy_twos = 0
    
    attack_fours += 0.5
    if attack_fours >= 4:
        attack_fours = 0
    
    attack_twos += 0.4
    if attack_twos >= 2:
        attack_twos = 0
    
    three_direction += 0.1
    if three_direction >= 6:
        three_direction = 0
    
    zero_anim += 0.2
    if zero_anim >= 2:
        zero_anim = 0
    
    if player_vectors[0]:
        player_position_x -= 0.7

    if player_vectors[1]:
        player_position_x += 0.7

    if player_vectors[2]:
        player_position_y -= 0.7

    if player_vectors[3]:
        player_position_y += 0.7

    if (not player_vectors[0] and
        not player_vectors[1] and
        not player_vectors[2] and
        not player_vectors[3]):
        player_state = 0
    
    if player_state == 0:
        player_walk_cycle = 0

    elif player_state == 1:
        player_walk_cycle += 0.2
        if player_walk_cycle >= 4:
            player_walk_cycle = 0
    
    screen.fill(background)
    render_grass()
    render_player()
    enemy_logic(0)
    enemy_logic(1)
    enemy_logic(2)
    enemy_logic(3)
    enemy_logic(4)
    attack_logic()
    render_particles(0)
    render_particles(1)
    render_particles(2)
    render_particles(3)
    render_particles(4)
    render_hud()
    #screen.blit(test_text, (100, 0)) #it works :D
    pygame.display.flip()
    clock.tick(60)

final_text_one = pi_font2.render("you figured it out!", False, (255, 255, 255), (0, 0, 0))
final_text_two = pi_font2.render("thanks for playing.", False, (255, 255, 255), (0, 0, 0))
score_text = pi_font2.render(str("score:") + str(int(score / ticks)), False, (255, 255, 255), (0, 0, 0))
screen.fill(background)
render_grass()
screen.blit(final_text_one, (40, 30))
screen.blit(final_text_two, (40, 50))
screen.blit(score_text, (40, 70))
pygame.display.flip()
pygame.mixer.music.unload()
pygame.mixer.music.stop()
pygame.mixer.music.load(os.path.abspath('music/pifi_title.ogg'))
pygame.mixer.music.play(-1)

while 1 == 1:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()