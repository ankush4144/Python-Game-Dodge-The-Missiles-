#prototypwe with classes
import random
import sys
import pygame
pygame.init()
basicfont = pygame.font.SysFont('comicsansms', 35,True)
clock=pygame.time.Clock()
class displayAndLoading():
    def __init__(self):
        self.overSound = pygame.mixer.Sound("gameover.wav")
        self.crashSound = pygame.mixer.Sound("crash.wav")
        self.rocketSound = pygame.mixer.Sound("rocket.wav")
        self.introMusic = pygame.mixer.Sound("intro.wav")
        self.window=pygame.display.set_mode((490,480))
        pygame.display.set_caption("DODGE THE CAR")
        self.boom=pygame.image.load('boom.png')
        self.boom = pygame.transform.scale(self.boom, (70, 65))
        self.char=pygame.image.load('Car2.png')
        self.char = pygame.transform.scale(self.char, (90, 110))
        self.obs=pygame.image.load('rocket.png')
        self.obs = pygame.transform.scale(self.obs, (75, 75))
        self.bg=pygame.image.load('bg.jpg')
        self.bg = pygame.transform.scale(self.bg, (490, 480))
        self.bg1=pygame.image.load('bg1.jpg')
        self.bg1 = pygame.transform.scale(self.bg1, (490, 480))
        self.exit=pygame.image.load('exit.jpg')
        self.exit = pygame.transform.scale(self.exit, (490, 480))
        self.introCar=pygame.image.load('Car.png')
        self.introCar = pygame.transform.scale(self.introCar, (95, 80))
        self.rocket = pygame.image.load('obstacle2.png')
        self.rocket = pygame.transform.scale(self.rocket, (75, 75))
class calculationAndDrawing(displayAndLoading):
    def __init__(self):
        super().__init__()
        self.score=0
        self.text='YOU CRASHED!'
        
        self.x=0
        self.y=380
        self.width=40
        self.height=60
        self.vel=5 #velocity of car
        self.x2=0
        self.y2=0
        self.velObstacle=2 #velocity of rocket
        self.difficulty=0  #to increase difficulty of game
        
    def randomObstacle(self):
        self.x2=random.randrange(1,450)
    def drawing(self):
        self.window.blit(self.bg, (0,0))
        self.window.blit(self.char,(self.x,self.y))
        #hitbox 1
        #pygame.draw.rect(self.window,(0,255,0),(self.x,self.y+30,84,58),2)
        self.window.blit(self.obs,(self.x2,self.y2))
        if(self.y2<=10):
            pygame.mixer.Sound.play(game.rocketSound)
            pygame.mixer.music.stop()
        #hitbox 2
        #pygame.draw.rect(self.window,(0,0,0),(self.x2+17,self.y2+12,39,60),2)
        self.window.blit(basicfont.render("SCORE: "+str(self.score),1,(0,0,0)),(300,10))
        pygame.display.update()
    def coordsAndScoreCalculation(self):
        if self.x<0:
            self.x=0
        if self.x>400:
            self.x=400
        if(self.y2>440):
            self.randomObstacle()
            self.score+=1
            self.difficulty+=1
            self.y2=0
            
        else:                           
            self.y2+=self.velObstacle
        self.drawing()
          
        if(self.difficulty==10):        #to increase difficulty of game
            self.velObstacle+=1
            self.difficulty=0
        



game=calculationAndDrawing()

def exitScreen():

    game.score=0
    pygame.mixer.Sound.play(game.overSound)
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end=False                
        smallFont=pygame.font.Font('hello.otf', 13)
        
        game.window.blit(game.exit, (0,0))
        pygame.draw.rect(game.window, (255,0,0),(100,300,100,50))
        pygame.draw.rect(game.window, (255,0,0),(300,300,100,50))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 100+100 > mouse[0] > 100 and 300+50 > mouse[1] >300:
            pygame.draw.rect(game.window,(205,0,0),(100,300,100,50))
            if(click[0]==1):
                game.overSound.stop()
                mainGame()
        if 300+100 > mouse[0] > 300 and 300+50 > mouse[1] >300:
            pygame.draw.rect(game.window,(205,0,0),(300,300,100,50))
            if(click[0]==1):
                pygame.quit()
                quit()
        game.window.blit(smallFont.render("PLAY AGAIN",1,(0,0,0)),((52+(100//2)),(295+(50//2))))
        game.window.blit(smallFont.render("QUIT",1,(0,0,0)),((280+(100//2)),(295+(50//2))))
        pygame.display.update()
        clock.tick(15)
    
def mainGame():  
    run=True        
    game=calculationAndDrawing()
    game.randomObstacle()
    while run:
        clock.tick(60)  #generating frames
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                run=False
                quit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            game.x-=game.vel
        elif keys[pygame.K_RIGHT]:
            game.x+=game.vel
        game.coordsAndScoreCalculation()
        if game.x<(game.x2+17+39) and (game.x+84)>(game.x2+17) and (game.y+30)<(game.y2+12+60) and (game.y+30+58)>(game.y2+12):
            print("HIT")
            pygame.mixer.Sound.play(game.crashSound)
            pygame.mixer.music.stop()
            game.window.blit(basicfont.render(game.text,1,(0,0,0)),(120,90))
            game.window.blit(game.boom,(game.x2,game.y2+20))
            pygame.draw.rect(game.window,(205,0,0),(0,0,490,50))
            game.window.blit(basicfont.render('YOUR TOTAL SCORE IS '+str(game.score),1,(255, 0, 0)), (10,0))
            pygame.display.update()
            pygame.time.delay(2500)
            run=False
            exitScreen()
    pygame.quit()


def welcomeScreen():
    xCoords=0          #For car in the intro animation
    yCoords=330
    x=random.randrange(1,300)              #For rocket in the intro animation
    y=0
    pygame.mixer.Sound.play(game.introMusic,-1)
    intro = True
    
    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end=False
                quit()
        smallFont=pygame.font.Font('hello.otf', 15)
        game.window.blit(game.bg1, (0,0))
        pygame.draw.rect(game.window, (30,144,225),(100,200,100,50))
        pygame.draw.rect(game.window, (30,144,225),(300,200,100,50))
        game.window.blit(basicfont.render("DODGING THE MISSILES",1,(102,205,0)),(20,10))
        game.window.blit(game.introCar, (xCoords,yCoords))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        
        if 100+100 > mouse[0] > 100 and 200+50 > mouse[1] >200:
            pygame.draw.rect(game.window,(16,78,139),(100,200,100,50))
            if(click[0]==1):
                game.introMusic.stop()
                mainGame()
        if 300+100 > mouse[0] > 300 and 200+50 > mouse[1] >200:
            pygame.draw.rect(game.window,(16,78,139),(300,200,100,50))
            if(click[0]==1):
                pygame.quit()
                quit()
        game.window.blit(smallFont.render("LET'S GO",1,(255,153,18)),((58+(100//2)),(190+(50//2))))
        game.window.blit(smallFont.render("QUIT",1,(255,153,18)),((279+(100//2)),(190+(50//2))))

        game.window.blit(game.rocket, (x,y))
        pygame.display.update()
        xCoords+=5
        y+=4
        if(xCoords>=490):
            xCoords=0
        if(y>=480):
            y=0
            x=random.randrange(1,300)
        clock.tick(30)
welcome=True

if(welcome==True):
    welcome=False
    welcomeScreen()
    

