import pygame #підключення основної бібліотеки




clock = pygame.time.Clock() 

pygame.init()
screen = pygame.display.set_mode((452, 260)) #формат екрана
pygame.display.set_caption("Platformer Sprite") #назва гри
icon = pygame.image.load('8541990_ghost_game_icon.png').convert_alpha() #моя іконка
pygame.display.set_icon(icon)




ghost = pygame.image.load('ghost.png').convert_alpha() #додавання ворогів

ghost_list_in_game = []      #створив список в якому будуть елементи(створені копії ворогів)


bg = pygame.image.load('pngtree-d-game-art-natural-landscape-for-games-mobile-applications-and-computers-image_1696197.jpg').convert_alpha() #фон



walk_right = [
    pygame.image.load('1_000.png').convert_alpha(),
    pygame.image.load('1_001.png').convert_alpha(),
    pygame.image.load('1_002.png').convert_alpha(),
    pygame.image.load('1_003.png').convert_alpha(),
    pygame.image.load('1_004.png').convert_alpha(),
    pygame.image.load('1_005.png').convert_alpha(),
    pygame.image.load('1_006.png').convert_alpha(),
    pygame.image.load('1_007.png').convert_alpha(),
    pygame.image.load('1_008.png').convert_alpha(),
    pygame.image.load('1_009.png').convert_alpha(),
    pygame.image.load('1_010.png').convert_alpha(),                       #використання методу conver_alpha() для кращої та зручнішої обробки зображень особисто для pygame 
    pygame.image.load('1_011.png').convert_alpha(),
    pygame.image.load('1_012.png').convert_alpha(),
    pygame.image.load('1_013.png').convert_alpha(),
    pygame.image.load('1_014.png').convert_alpha(),
    pygame.image.load('1_015.png').convert_alpha(),
    pygame.image.load('1_016.png').convert_alpha(),
    pygame.image.load('1_017.png').convert_alpha(),
    pygame.image.load('1_018.png').convert_alpha(),
    pygame.image.load('1_019.png').convert_alpha(),
    pygame.image.load('1_020.png').convert_alpha(),
    pygame.image.load('1_021.png').convert_alpha(),

]                                                                             #анімації
walk_left = [
    pygame.image.load('1_022.png').convert_alpha(),
    pygame.image.load('1_023.png').convert_alpha(),
    pygame.image.load('1_024.png').convert_alpha(),
    pygame.image.load('1_025.png').convert_alpha(),
    pygame.image.load('1_026.png').convert_alpha(),
    pygame.image.load('1_027.png').convert_alpha(),
    pygame.image.load('1_028.png').convert_alpha(),
    pygame.image.load('1_029.png').convert_alpha(),
    pygame.image.load('1_030.png').convert_alpha(),      
    pygame.image.load('1_031.png').convert_alpha(),
    pygame.image.load('1_032.png').convert_alpha(),
    pygame.image.load('1_033.png').convert_alpha(),
    pygame.image.load('1_034.png').convert_alpha(),
    pygame.image.load('1_035.png').convert_alpha(),
    pygame.image.load('1_036.png').convert_alpha(),
    pygame.image.load('1_037.png').convert_alpha(),
    pygame.image.load('1_038.png').convert_alpha(),
    pygame.image.load('1_039.png').convert_alpha(),
    pygame.image.load('1_040.png').convert_alpha(),
    pygame.image.load('1_041.png').convert_alpha(),
    pygame.image.load('1_042.png').convert_alpha(),

]


player_anim_count = 0   #початок анімації

player_speed = 5 #швидкість персонажа
player_x = 0 #початкові координати персонажа
player_y = 45

is_jump = False #стрибок
jump_count = 10

bg_x = 0 #перший фон


bg_sound = pygame.mixer.Sound('space_city_bpm115.mp3') #музика
bg_sound.play()

ghost_timer = pygame.USEREVENT + 1           #створюю таймер щоб періодично(кожні 2500 мілісекунд) з'являлися вороги
pygame.time.set_timer(ghost_timer, 2500)

label = pygame.font.Font('Tektur_SemiCondensed-SemiBold.ttf', 40)
lose_label = label.render('Ви програли!', False, ("White"))
restart_label = label.render('Спробуйте ще раз!', False, ("Green"))
restart_label_rect = restart_label.get_rect(topleft = (65, 200))



bullet = pygame.image.load ('bullet.png').convert_alpha()             #створення патрону для ліквідації ворогів та списку в якому будуть ці пулі перебиратись
bullets = []
bullets_left = 5

gameplay = True                       #змінна яка ілюструє фул гру, якщо значення буде False(коли гравець доторкнеться до ворога) - то game over)

running = True #основний цикл гри
while running:




    
    screen.blit(bg, (bg_x, 0)) #додавання першого фону на екран
    screen.blit(bg, (bg_x + 452, 0)) #додавання другого фону на екран(для переходу)
    
    if gameplay:

        
        
    


        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))     #створюю уявні квадрати за допомогою яких можна відстжувати дотики для гг і ворога
        
        if ghost_list_in_game:
            for (i, el) in enumerate (ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10
                if el.x < -10:                           #якщо ворог за границею екрана - він видаляється
                    ghost_list_in_game.pop(i)

                
                if player_rect.colliderect(el):              #створюю умову завдяки якій якщо гравець доторкнеться до ворога то він програє 
                    gameplay = False
                    
            

        






        keys = pygame.key.get_pressed()  
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:                                                                                  #основа пересування вліво та вправо
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        


    
        if keys[pygame.K_LEFT] and player_x > 1:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 380:                 #границі пересування персонажа з лівого та правого боку екрану
            player_x += player_speed
        
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
                if jump_count >= -10:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:                                            #система стрибків
                        player_y += (jump_count ** 2) / 2
                    jump_count -=1
                else:
                    is_jump = False
                    jump_count = 10


        
        if player_anim_count == 20:
            player_anim_count = 0
        else:
            player_anim_count += 1    #цикл анімації

        bg_x -= 2
        if bg_x == -452:     #цикл фону
            bg_x = 0


                    
                                                                                                 
        if bullets:                                                                                #додаю опцію завдяки якій створюється і випускається пуля
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4

                if el.x > 454:                                                #коли пуля за границею екрана вона зникає
                    bullets.pop(i)
                
                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):          #створення методу зникання ворога та самої пулі при зіткненні
                        if el.colliderect(ghost_el):
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)






    else: 
        screen.fill(("Black"))
        screen.blit(lose_label, (110, 100))                       #виведення екрану програшу в випадку дотику до ворога
        screen.blit(restart_label, (restart_label_rect))
        
        
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed() [0]:               #додаю зону для взаємодії мишки з текстом і завдяки цьому гра перезапускаєтсья
            gameplay = True
            player_x = 0
            player_y = 45
            ghost_list_in_game.clear()
            bullets.clear()
        



        
    
    
    


    
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:     #умова виходу з гри
            running = False
            pygame.quit()
        if event.type == ghost_timer:                                                 #коли таймер стосовно ворога запускається - список оновлюється елементами
            ghost_list_in_game.append(ghost.get_rect(topleft=(453, 45)))


        if gameplay and event.type  == pygame.KEYUP and event.key == pygame.K_b and bullets_left >0:                   #створення можливості при натисненні клавіші B випускати лише один патрон 
            bullets.append(bullet.get_rect(topleft = (player_x + 30, player_y + 10)))  
            bullets_left -= 1


    clock.tick(40)        #FPS
    
