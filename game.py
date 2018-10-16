import pygame
import time
import random

############################################################

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))        #Display
pygame.display.set_caption('A bit Racey')       #Title

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

clock = pygame.time.Clock()             #Game clock

carImg = pygame.image.load('racecar.png')
car_width = 73

#############################################################

def car(x,y):
    gameDisplay.blit(carImg, (x,y))
    
    
    
def obstacles(obsta_x, obsta_y, obsta_width, obsta_height, color):    pygame.draw.rect(gameDisplay, color, [obsta_x, obsta_y, obsta_width, obsta_height])
    
    
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
    
    
def message_display(text):
    textFont = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = (display_width/2 , display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()

    
def crash():
    message_display('You Crashed')
    time.sleep(2)
    game_loop()
    

    
def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    gameExit = False #If true, game finished
    
    x_change = 0
    
    obsta_x_start = random.randrange(0, display_width)
    obsta_y_start = -600
    obsta_speed = 7
    obsta_width = 100
    obsta_height = 100
    
    
    while not gameExit:      #Game loop
        
        for event in pygame.event.get():    #Get the events (keys, ...)
            if event.type == pygame.QUIT:   #Quit the game
                pygame.quit()
                quit()
                
            ####################### 
            
            if event.type == pygame.KEYDOWN:    #key pressed
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    
            if event.type == pygame.KEYUP: #key released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            #######################
             
        x += x_change
            
        gameDisplay.fill(white)
        
        obstacles(obsta_x_start, obsta_y_start, obsta_width, obsta_height, black)
        obsta_y_start += obsta_speed
        
        car(x,y)        #Draw the car (update)
        
        if x > (display_width - car_width) or x < 0:
            crash()
        if obsta_y_start > (display_height + obsta_height):
            obsta_y_start = 0 - obsta_height
            obsta_x_start = random.randrange(0, display_width)
            
            
        pygame.display.update()         #pygame.display.flip
        clock.tick(60)      #Fps
        

##################################################################

if __name__ == "__main__":
    game_loop()
    pygame.quit()  #Stop pygame
    quit()
