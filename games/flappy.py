from game1d import Game1d
from random import randrange,random
from machine import Timer
from lib.hsv_to_rgb import hsv_to_rgb

class Flappy(Game1d):
    def gameInit(self):
        self.state = 0 #0 - attract mode, 1 - playing, 2 - game over
        self.gap = 0 
        self.gapSize = 20
        self.player=0
        self.gameOverCounter = 0
        self.attractCounter = 0
        
        self.timer = Timer(-1)
        self.timerPeriod = 3000
        

    def draw(self,buttons,display):
       
        if(self.state == 2):
            return self.drawGameOver(display)
        if(self.state == 0): #attract mode
            if(self.player != buttons['pot']): #moved, so start game
                print("starting game")
                self.gap = 10
                self.gapSize = 20
                self.timerPeriod = 3000
                self.attractCounter = 0
                self.state=1
                self.timer.init(period=self.timerPeriod,callback=self.wallTimerInterrupt)
            else:
                return self.drawAttract(display)
        if(self.state==1):
            display = [(0,0,0) for i in range(len(display))] #clear entire display
        
        #show gap
        for i in range(self.gap,(self.gap+self.gapSize)):
            display[i] = (0,125,0)
        #Move player
        self.player = buttons['pot']
        display[self.player] = (200,0,200)
        
        return display

    #called whenever timer expires, to reset location of the wall and decrement time left
    def wallTimerInterrupt(self,t):
        if(self.player >= self.gap and self.player <= (self.gap+self.gapSize)):
            #safe
            if(self.gapSize>2):
                self.gapSize-=1
            else:
                #gap is only 2 big, start changing timer period....
                if(self.timerPeriod>1000):
                    self.timerPeriod -= 300
                self.timer.init(period=self.timerPeriod,callback=self.wallTimerInterrupt)

            self.gap = randrange(0,144-self.gapSize)

        else:
            #fail
            self.timer.deinit()
            self.state = 2
        return

    # Draws game over flashing red
    def drawGameOver(self,display):
        self.gameOverCounter += 1
        if(self.gameOverCounter % 5 ==0):
            #toggle
            if(display[0][0]==0):
                display = [(100,0,0) for i in range(len(display))]
            else:
                display = [(0,0,0) for i in range(len(display))]
        if(self.gameOverCounter % 100 ==0):#reset
            self.state=0
            display = [(100,0,0) for i in range(len(display))]
        return display

    # Draws attract mode
    def drawAttract(self,display):
        if(self.attractCounter==0):
            display = [(0,0,0) for i in range(len(display))]
            #display[100] = [0,100,0]
        
        if(self.attractCounter % 20 == 0):
            display = [hsv_to_rgb(random(),0.8,0.3) for i in range(len(display))]
            #display = [(randrange(80),randrange(100),randrange(100)) for i in range(len(display))]
        self.attractCounter +=1
        if(self.attractCounter>600):
            self.attractCounter = 0
        
        return display
