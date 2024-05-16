#player.py
from frame import *
from graphics import *
from movement import *
from bullet import *

class Player(Frame):

    def __init__(self,x,y,win):
        super().__init__(x,y,win)
        self.width=5
        self.length=15
        
        self.hp=30
        self.speed=10
        self.fireRate=15
        self.fireType=0


        self.img=Image(Point(self.x,self.y),"playerImage.jpg") 
        self.img.draw(self.win)

        #弾のインスタンスを格納するリスト
        self.pBulletList=[]


    def move(self,Key):
   
        if(Key == "w" and self.y <575): 
               self.img.move(0, self.speed)
               self.y += (self.speed)

        elif(Key == "a" and self.x > 25):
               self.img.move(-self.speed, 0)
               self.x += (-self.speed)

        elif(Key == "d" and self.x <1000):
               self.img.move(self.speed, 0)
               self.x += (self.speed)

        elif(Key == "s" and self.y > 25):
               self.img.move(0, -self.speed)
               self.y += (-self.speed)

    def getHP(self):
        return self.hp

    def getPBulletList(self):
        return self.pBulletList

    def setFireRate(self,rate):
        self.fireRate=rate

    #PlayerBulletのインスタンスの生成
    def fire(self,key):
        if(key=="e" and self.fireType!=0):
            self.fireType=0
        if(self.count % self.fireRate ==0 and self.fireType==0):
            self.pBulletList.append(PlayerBullet(self.x +20, self.y, self.win))


        if(key=="q" and self.fireType!=1):
            self.fireType=1
        if(self.count % (self.fireRate*2) ==0 and self.fireType==1):
            self.pBulletList.append(PlayerUpBullet(self.x +20, self.y, self.win))
            self.pBulletList.append(PlayerDownBullet(self.x +20, self.y, self.win))
            self.pBulletList.append(PlayerBullet(self.x +20, self.y, self.win))

        

    #pBulletListにあるPlayerBulletの移動
    def bulletMove(self):
        for pBullet in self.pBulletList:
            pBullet.move()

    #pBulletListにあるPlayerBulletのdestroyをチェックし削除
    def checkBullet(self):
        for pBullet in self.pBulletList[:]:
            if(pBullet.checkDestroy()):
                self.pBulletList.remove(pBullet)


    def updateCount(self):
        super().updateCount()
        for pBullet in self.pBulletList[:]:
            pBullet.updateCount()
        
