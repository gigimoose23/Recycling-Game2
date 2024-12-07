import pygame,math,random,sys,time,os
pygame.init()
WIDTH = 700
HEIGHT = 500
RecycableImages = ["box", "binbag"]
NonRecycableImages = ["pencil", "soldier", "woodbox"]
Score = 0
ScoreText = pygame.font.SysFont("Times New Roman",30,True)
RecycableGroup = pygame.sprite.Group()
NonRecycableGroup = pygame.sprite.Group()
AllItems = pygame.sprite.Group()
Bine = pygame.sprite.Group()
TimeLeft = 60
OrigTim = TimeLeft
TimeSinceLastTakenClock = 0
mainTextDis = False
mainTextDisT = ""
clock = pygame.time.Clock()

    
class Bin(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/bin.png")
        self.image = pygame.transform.scale(self.image,(70,90))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]
class Recycable(pygame.sprite.Sprite):
    
    def __init__(self,imgName):
        pygame.sprite.Sprite.__init__(self)
        self.howLongInter = random.randrange(3,7) - random.randrange(1,2)
        self.image = pygame.image.load("images/"+imgName+ ".png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        
    def update(self):
        if DrawMe:
            self.rect.y += self.howLongInter

class NonRecycable(pygame.sprite.Sprite):
    
    def __init__(self,imgName):
        pygame.sprite.Sprite.__init__(self)
        self.howLongInter = random.randrange(3,7) - random.randrange(1,2)
        self.image = pygame.image.load("images/"+imgName+ ".png")
        self.image = pygame.transform.scale(self.image,(55,55))
        self.rect = self.image.get_rect()
        
    def update(self):
        if DrawMe:
            self.rect.y += self.howLongInter
        


BinMain = Bin(300,400)
Bine.add(BinMain)
AllItems.add(BinMain)
doGenTimer = 0
def doGen():
    for i in range(10):
        Temp = Recycable(RecycableImages[random.randint(0,len(RecycableImages)-1)])
        Temp.rect.x = random.randint(0,WIDTH)
        RecycableGroup.add(Temp)
        AllItems.add(Temp)

    for i in range(10):
        Temp = NonRecycable(NonRecycableImages[random.randint(0,len(NonRecycableImages)-1)])
        Temp.rect.x = random.randint(0,WIDTH)
        NonRecycableGroup.add(Temp)
        AllItems.add(Temp)
doGen()

suc = pygame.mixer.Sound("suc.wav")
err = pygame.mixer.Sound("err.wav")
bgImg = pygame.image.load("images/background.png")
bgImg = pygame.transform.scale(bgImg, (WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
def draw():
    global Score,doGenTimer
    doGenTimer+=1
    if doGenTimer == 150:
        doGen()
        doGenTimer = 0
    screen.blit(bgImg,(0,0))
    AllItems.draw(screen)
    AllItems.update()
    Main = ScoreText.render("Score: " + str(Score),True,(255,255,255),(0,0,0))
    screen.blit(Main, (0,0))
    Maind = None
    if mainTextDis == False:
        Maind = ScoreText.render("Score above 15 in the time to win!",True,(255,255,255))
    else:
        Maind = ScoreText.render(mainTextDisT,True,(255,255,255))
    
    screen.blit(Maind, (0,466))
    Maine = ScoreText.render("" + str(TimeLeft),True,(255,255,255),(0,0,0))
    screen.blit(Maine, (650,0))
    if pygame.sprite.groupcollide(Bine,RecycableGroup,False,True):
        Score+=1
        
        suc.play()

    if pygame.sprite.groupcollide(Bine,NonRecycableGroup,False,True):
        if Score != 0:
            Score-=1
        
        
        err.play()
    
fps = 30
clock = pygame.time.Clock()
gameRunning = True
DrawMe = True
movingRight = False
movingLeft = False
while gameRunning:
    
    if DrawMe == True:
        draw()
        if movingRight == True:
            pass
            #BinMain.rect.x+=3
        elif movingLeft == True:
            pass
            #BinMain.rect.x-=3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                
                    movingRight = True
                elif event.key == pygame.K_LEFT:
                    movingLeft = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    movingRight = False
                elif event.key == pygame.K_LEFT:
                    movingLeft = False

        dt = clock.tick() 

        TimeSinceLastTakenClock += dt
    
        if TimeSinceLastTakenClock > 100:
            if TimeLeft != 0:
                TimeLeft -=1
                TimeSinceLastTakenClock =0
            else:
                mainTextDis = True
                if Score >= 15:
                    mainTextDisT = "You won! Press E to try again."
                else:
                    mainTextDisT = "You lost. Press E to try again."
                
                draw()
                DrawMe = False


        clock.tick(fps)
        pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    for sprite in RecycableGroup.sprites():
                        sprite.kill()
                        del sprite

                    for sprite in NonRecycableGroup.sprites():
                        sprite.kill()
                        del sprite
                    TimeLeft = OrigTim+1
                    doGenTimer = 0
                    doGen()
                    DrawMe = True
                    TimeSinceLastTakenClock = 100
                    Score = 0
                    mainTextDis = False
        clock.tick(fps)
        pygame.display.flip()