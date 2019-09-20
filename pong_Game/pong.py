import pygame
import random

pygame.init()

clock = pygame.time.Clock()
screen_width = 600

screen_height = 400
win = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Pong Game")
hitSound = pygame.mixer.Sound('sound/hit.wav')

class paddle(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.hitbox = (self.x  , self.y , self.width  , self.height )
    
    def draw(self, win):
        pygame.draw.rect(win, (160,150,100), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x  , self.y , self.width  , self.height )
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 1 )

class cpuPlay(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x  , self.y , self.width  , self.height )
        self.vely = 3
        self.velx = 3        



    
    def move (self):
        self.ballX , self.ballY = ball.retPos()
        if self.width == 10 and self.y >= self.vely + 15  and self.y + 15 <= screen_height - self.height - self.vely and self.ballX < 300:

                      if self.y < self.ballY :
                           if self.y < 320: 
                                self.y += self.vely
                           else: 
                                self.y -= self.vely
                      elif self.y > self.ballY : 
                           if self.y > 20:
                              self.y -= self.vely
                           else: 
                              self.y += self.vely
                      else:  
                           pass
        else:         
             if self.x >= self.velx + 15 and  self.x <= 240 and self.ballX < 300 :
                      
                      if self.x < self.ballX :
                           if self.x < 230: 
                                self.x += self.velx
                           else: 
                                self.x -= self.velx
                      elif self.x > self.ballX: 
                           if self.x > 20:
                              self.x -= self.velx
                           else:     
                              self.x += self.velx
                      else:  
                           pass

    def draw(self, win):
        pygame.draw.rect(win, (160,150,100), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x  , self.y , self.width  , self.height )
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 1 )
        self.move()
        
    
     
        
         

class ball (object):
    def __init__(self,x , y , radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = (random.randint(-4,4), random.randint(1,8) )
        self.hitVer = False
        self.hitHor= False 
        self.velX = self.vel[0]
        self.velY = self.vel[1]
        self.score = 0
        self.scoreCpu = 0 
        

    
    def direction(self,hitVer,hitHor):
        if self.hitVer :  
              self.velX  = -self.velX
              self.velY  =  self.velY
        elif self.hitHor :
              self.velX  =  self.velX
              self.velY  = -self.velY
        else: 
              self.velX  = self.velX
              self.velY  = self.velY
        
    def move(self ):
        if   self.x > screen_width  or self.x < 0  or self.y > screen_height or self.y < 0  : 
              if self.x < 300:
                 self.score += 1 
              elif self.x > 300:
                 self.scoreCpu += 1
              else: 
                 pass

              self.x = 300
              self.y = 200
              self.vel = (random.randint(-4,4), random.randint(1,8) )
              self.velX = self.vel[0]
              self.velY = self.vel[1]
  
        else: 
              self.x += self.velX
              self.y += self.velY
          
    def retPos (self):
        return self.x,self.y
 
    def draw(self, win):
        pygame.draw.circle(win, (0, 255, 85), [self.x, self.y], self.radius)
        self.direction(self.hitVer,self.hitHor)
        self.move()
    def retScores (self):
        return  self.score,self.scoreCpu 

def redrawGameWindow():
    win.fill((0,0,0))
    vertical.draw(win)
    horizental1.draw(win)
    horizental2.draw(win)
    verticalCPU.draw(win)
    horizental1CPU.draw(win)
    horizental2CPU.draw(win)
    horizental2CPU.draw(win)
    ball.draw(win)
    pygame.draw.line(win, (0, 0, 255), (300, 0), (300, 400))
    text1 = font.render('Score: ' + str(score), 1, (0,150,0))
    text2 = font.render('cpu Score: ' + str(cpuScore), 1, (0,150,0))
    win.blit(text1, (310,10))
    win.blit(text2, (200,10))
    pygame.display.update()
   

#main loop
font = pygame.font.SysFont('comicsans' , 20 , True, True)
ball = ball(300,200,10)
vertical = paddle(590, 150, 10,60)
horizental1 = paddle(500, 0, 60,10)
horizental2 = paddle(500, 390, 60,10)

score = 0 
cpuScore = 0  
verticalCPU = cpuPlay(0, 150, 10,60)
horizental1CPU = cpuPlay(100, 0, 60,10)
horizental2CPU = cpuPlay(100, 390, 60,10)


run = True
while run: 
      clock.tick(35)


      score, cpuScore  = ball.retScores()


      if (ball.y - ball.radius < vertical.hitbox[1] + vertical.hitbox[3] and ball.y + ball.radius > vertical.hitbox[1] and ball.x + ball.radius  > vertical.hitbox[0] and ball.x - ball.radius < vertical.hitbox[0] + vertical.hitbox [2] ) or (ball.y - ball.radius < verticalCPU.hitbox[1] + verticalCPU.hitbox[3] and ball.y + ball.radius > verticalCPU.hitbox[1] and ball.x - ball.radius  > verticalCPU.hitbox[0] and ball.x - ball.radius < verticalCPU.hitbox[0] + verticalCPU.hitbox [2] ):
                  ball.hitVer = True  
                  ball.hitHor = False
                  hitSound.play()
      elif( ball.x - ball.radius  < horizental1.hitbox[0] + horizental1.hitbox[2]  and ball.x + ball.radius > horizental1.hitbox[0] ) and (ball.y - ball.radius < horizental1.hitbox[1] + horizental1.hitbox[3]  and ball.y + ball.radius > horizental1.hitbox[1]) or ( (ball.x - ball.radius  < horizental2.hitbox[0] + horizental2.hitbox[2] ) and (ball.x + ball.radius > horizental2.hitbox[0]) and (ball.y + ball.radius > horizental2.hitbox[1]) and (ball.y - ball.radius < horizental2.hitbox[1] +  horizental2.hitbox[3] ) ) or    ( ball.x - ball.radius  < horizental1CPU.hitbox[0] + horizental1CPU.hitbox[2]  and ball.x + ball.radius > horizental1CPU.hitbox[0] ) and (ball.y - ball.radius < horizental1CPU.hitbox[1] + horizental1CPU.hitbox[3]  and ball.y + ball.radius > horizental1CPU.hitbox[1]) or ( (ball.x - ball.radius  < horizental2CPU.hitbox[0] + horizental2CPU.hitbox[2] ) and (ball.x + ball.radius > horizental2CPU.hitbox[0]) and (ball.y + ball.radius > horizental2CPU.hitbox[1]) and (ball.y - ball.radius < horizental2CPU.hitbox[1] +  horizental2CPU.hitbox[3] ) ):
                  ball.hitHor = True
                  ball.hitVer = False
                  hitSound.play()
      else: 
                  ball.hitHor = False
                  ball.hitVer = False
      
      for event in pygame.event.get():
          if event.type == pygame.QUIT: 
             run = False

      Keys = pygame.key.get_pressed()

      if Keys[pygame.K_LEFT] and horizental1.x > horizental1.vel and  horizental1.x > 312 :
         horizental1.x -= horizental1.vel
         horizental2.x -= horizental2.vel
      if Keys[pygame.K_RIGHT] and horizental1.x < screen_width - horizental1.width - horizental1.vel:
         horizental1.x += horizental1.vel
         horizental2.x += horizental2.vel 
      if Keys[pygame.K_UP] and vertical.y > vertical.vel:
         vertical.y -= vertical.vel
      if Keys[pygame.K_DOWN] and vertical.y < screen_height - vertical.height - vertical.vel:
	      vertical.y += vertical.vel
      redrawGameWindow()

pygame.quit()

