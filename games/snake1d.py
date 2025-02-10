from game1d import Game1d
from random import randrange
from machine import Timer

class Snake(Game1d):
    def gameInit(self):
        self.state = 0 #0 - attract mode, 1 - playing, 2 - game over
        self.goingRight = True
        self.player = 10
        self.tail = [9,8,7]
        self.fruit = randrange(300)
        self.wall = randrange(300)
        self.gameOverCounter = 0
        self.timer = Timer(-1)
        self.timerPeriod = 5000
        self.timer.init(mode=Timer.ONE_SHOT,period=self.timerPeriod,callback=self.wallTimerInterrupt)

    def draw(self,buttons,display):
        if(self.state == 2):
            return self.drawGameOver(display)
        if(self.state == 0): #attract mode
            if(buttons['R'] or buttons['L'] or buttons['U'] or buttons['D'] or buttons['A'] or buttons['B'] or buttons['X'] or buttons['Y']):
                self.state = 1 #start game
                self.player = randrange(300)
                self.tail = []
            return self.drawAttract(display)

        display = [(0,0,0) for i in range(len(display))] #clear entire display

        #Move player
        if(self.goingRight):
            self.player +=1
        else:
            self.player -=1
        self.player = self.player % len(display) #wrap around
        self.tail.append(self.player)
        self.tail.pop(0)
        
        if(buttons['R']):
            self.goingRight = True
        if(buttons['L']):
            self.goingRight = False

        if(self.player==self.fruit):
            
            self.fruit = randrange(300)
            self.tail.insert(0,self.player)

        if(self.player == self.wall):
            self.state=2

        display[self.player] = (125,0,125)
        for i in range(len(self.tail)):
            mod = max(120 - (10*i),40) #fade tail out to a minimum brightness
            display[self.tail[len(self.tail) -i -1]] = (mod,0,mod)
        display[self.fruit] = (0,125,0)
        display[self.wall] = (125,0,0)
        return display

    #called whenever timer expires, to reset location of the wall and decrement time left
    def wallTimerInterrupt(self,t):
        safe = False #Safe zone to spawn wall
        while(not safe):
            safe = True
            newWall = randrange(300)
            if self.distanceToPlayer(newWall) < 12:
                safe = False
        self.wall = newWall
        self.timerPeriod = max(self.timerPeriod-150,500)
        self.timer.init(mode=Timer.ONE_SHOT,period=self.timerPeriod,callback=self.wallTimerInterrupt)

    
    def distanceToPlayer(self,into):
        if(into==self.player):
            return 0
        if(self.player>into) :
            inner = self.player - into
            outer = (300 - self.player)+into
        else:
            inner = into - self.player
            outer = (300 - into)+self.player
        if (inner>=outer):
            return outer
        else:
            return inner

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
            self.gameInit()
        return display

    # Draws attract mode
    def drawAttract(self,display):
        display = [(0,0,0) for i in range(len(display))] #clear entire display
        self.player +=1
        self.player = self.player % len(display) #wrap around
        self.tail.append(self.player)
        self.tail.pop(0)
        display[self.player] = (125,125,0)
        for i in range(len(self.tail)):
            mod = max(120 - (10*i),40) #fade tail out to a minimum brightness
            display[self.tail[len(self.tail) -i -1]] = (mod,mod,0)
        return display