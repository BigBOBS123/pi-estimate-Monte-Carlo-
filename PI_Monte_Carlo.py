import random; import pygame

#variables for later
Left_dot_location_1 = 45
Left_dot_location_2 = 550
out_answer = 0
in_answer = 0
IN = (124, 252, 0)
OUT = (255, 0, 0)
CLEAR_SCREEN = 590
run = True; GOING = True; END = True; NEW_POINT = True

#how many points do we need
sample_points = 1

#other things
pygame.init()
win = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

def END(): 
    print('in:  ' + str(in_answer))
    print('out:  ' + str(out_answer))
    print('total:  ' + str(in_answer + out_answer))
    clock.tick(10)



#main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pressed = pygame.key.get_pressed()
    if not pressed[pygame.K_SPACE]:
        GOING = True
        
    if pressed[pygame.K_RETURN]:
        END()
        IN_SCREEN = font.render('in ' + str(in_answer), True, (0, 0, 0))
        OUT_SCREEN = font.render('out ' + str(out_answer), True, (0, 0, 0))
        TOTAL_SCREEN = font.render('total ' + str(out_answer + in_answer), True, (0, 0, 0))
        pygame.draw.rect(win, (255, 255, 255), [230, 12, 350, 20], 20)
        
        win.blit(IN_SCREEN, (232, 14))
        win.blit(OUT_SCREEN, (350, 14))
        win.blit(TOTAL_SCREEN, (468, 14))
        pygame.display.update()
    
    
    if pressed[pygame.K_BACKSPACE]:
        for i in range(0, 9): 
            CLEAR_SCREEN = CLEAR_SCREEN - 50
            pygame.draw.rect(win, (0, 0, 0), [630, 30, CLEAR_SCREEN, CLEAR_SCREEN], 160)
        CLEAR_SCREEN = 590
        clock.tick(5)
        
    pygame.draw.rect(win, (255, 255, 255), [630, 30, 540, 540], 1)
    pygame.draw.circle(win, (255, 255, 255), (900, 300), 270, 1)
    pygame.display.update()
    
    while GOING:
        for i in range(0, int(sample_points)):
            random_x_coordinate = random.randint(1, 540)
            red_dot_x = random_x_coordinate + 630
            random_y_coordinate = random.randint(1, 540)
            red_dot_y = random_y_coordinate + 30
            pygame.draw.circle(win, (255, 0, 0), (red_dot_x, red_dot_y), 1)
        
            if (random_x_coordinate - 270) ** 2 + (random_y_coordinate - 270) ** 2 < 270 ** 2:
                IN_or_OUT = IN
            elif (random_x_coordinate - 270) ** 2 + (random_y_coordinate - 270) ** 2 > 270 ** 2:
                IN_or_OUT = OUT

            Left_dot_location_1 = Left_dot_location_1 + 9

            if Left_dot_location_1 >= 550:
                Left_dot_location_2 = Left_dot_location_2 - 9
                Left_dot_location_1 = 50
                
            if Left_dot_location_2 <= 30:
                Left_dot_location_1 = 45
                Left_dot_location_2 = 550
            pygame.draw.circle(win, IN_or_OUT, (Left_dot_location_1, Left_dot_location_2), 6)
            pygame.draw.circle(win, IN_or_OUT, (10, 8), 6)
            if IN_or_OUT == OUT:
                out_answer = out_answer + 1
            if IN_or_OUT == IN:
                in_answer = in_answer + 1
            
            PI = in_answer / int(in_answer + out_answer) * 4
            PI_SCREEN = font.render(str(PI), True, (0, 0, 0))
            
            pygame.display.update()
            pygame.draw.rect(win, (255, 255, 255), [20, 12, 180, 20], 20)
            win.blit(PI_SCREEN, (22, 14))
            
            print(str(PI))
            if int(in_answer) + int(out_answer) >= int(sample_points):
                GOING = False     
    
    
   
pygame.quit()
