import pygame,math,random,sys
pygame.init()
WIDTH = 700
HEIGHT = 500
RecycableImages = ["box", "binbag"]
NonRecycableImages = ["pencil", "soldier", "woodbox"]

RecycableGroup = pygame.sprite.Group()
NonRecycableGroup = pygame.sprite.Group()
AllItems = pygame.sprite.Group()
class Bin(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/bin.png")
        self.image = pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()
        
    def update():
        pass
class Recycable(pygame.sprite.Sprite):
    
    def __init__(self,imgName):
        pygame.sprite.Sprite.__init__(self)
       
        self.image = pygame.image.load("images/"+imgName+ ".png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()

    def update():
        pass

class NonRecycable(pygame.sprite.Sprite):
    
    def __init__(self,imgName):
        pygame.sprite.Sprite.__init__(self)
       
        self.image = pygame.image.load("images/"+imgName+ ".png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        
    def update():
        pass


BinMain = Bin("12332wrgfwwf","does this even matter")
AllItems.add(BinMain)
for i in range(20):
    Temp = Recycable(RecycableImages[random.randint(0,len(RecycableImages)-1)])
    Temp.rect.x = random.randint(0,WIDTH)
    RecycableGroup.add(Temp)
    AllItems.add(Temp)

for i in range(20):
    Temp = NonRecycable(NonRecycableImages[random.randint(0,len(NonRecycableImages)-1)])
    Temp.rect.x = random.randint(0,WIDTH)
    RecycableGroup.add(Temp)
    AllItems.add(Temp)


bgImg = pygame.image.load("images/background.png")
bgImg = pygame.transform.scale(bgImg, (WIDTH,HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
def draw():
    screen.blit(bgImg,(0,0))
    AllItems.draw(screen)
    
fps = 30
clock = pygame.time.Clock()
gameRunning = True
movingRight = False
movingLeft = False
while gameRunning:
    draw()
    if movingRight == True:
        BinMain.rect.x+=3
    elif movingLeft == True:
        BinMain.rect.x-=3
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
            
      

    clock.tick(fps)
    pygame.display.flip()