#ui.py
from graphics import *

class UI:
    def __init__(self,win,playerHP,destroyCount):
        self.win=win
        self.playerHP=playerHP
        self.hpUI=Text(Point(60,570),"HP:"+str(playerHP))
        self.hpUI.setSize(30)
        self.hpUI.setTextColor("white")
        self.hpUI.draw(self.win)
        
        self.count=0
        self.time=0
        self.timeUI=Text(Point(500,570),"{:0>2d}:{:0>2d}".format(int(self.time/60),self.time%60))
        self.timeUI.setSize(30)
        self.timeUI.setTextColor("white")
        self.timeUI.draw(self.win)

        self.destroyCount=destroyCount
        self.destroyCountUI=Text(Point(940,570),"×{:0>2d}".format(self.destroyCount))
        self.destroyCountUI.setSize(30)
        self.destroyCountUI.setTextColor("white")
        self.destroyCountUI.draw(self.win)

        self.gameEndUI=Text(Point(500,400),"")
        self.gameEndUI.setSize(30)
        

        self.gameReplayUI=Text(Point(500,200),"")
        self.gameReplayUI.setSize(30)
        self.gameReplayUI.setTextColor("white")
        
        
        

    def update(self,playerHP,destroyCount):
        if(self.playerHP != playerHP):
            self.hpUI.setText("HP:"+str(playerHP))
            
        self.count+=1
        if(self.count==60):
            self.count=0
            self.time+=1
            self.timeUI.setText("{:0>2d}:{:0>2d}".format(int(self.time/60),self.time%60))


        if(self.destroyCount != destroyCount):
            self.destroyCountUI.setText("×{:0>2d}".format(destroyCount))


    def setGameOver(self):
        self.gameEndUI.setTextColor("red")
        self.gameEndUI.setText("GAME OVER")
        self.gameEndUI.draw(self.win)


    def setGameClear(self):
        self.gameEndUI.setTextColor("yellow")
        self.gameEndUI.setText("CLEAR")
        self.gameEndUI.draw(self.win)


    def setGameReplay(self):
        self.gameReplayUI.setText("Press {o} key to end \nPress {r} key to retry")
        self.gameReplayUI.draw(self.win)
        
        
