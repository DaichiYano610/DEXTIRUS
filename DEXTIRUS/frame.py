#frame.py

class Frame:
    def __init__(self,x,y,win):
        self.hp=1
        self.x=x
        self.y=y
        self.speed=10
        self.width=50 #横
        self.length=50 #縦
        self.destroy=0
        self.win=win
        self.count=0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getLength(self):
        return self.length

    def setDestroy(self):
        self.destroy=1

    def addHP(self,n):
        self.hp+=n


    #画面外での削除
    def checkPos(self):
        if(self.x<-300 or 1300<self.x or self.y<-300 or self.y>900):
            self.setDestroy()

    #HPの確認
    def checkHP(self):
        if(self.hp<=0):
            self.setDestroy()

    
    #destroy=1のとき，画像消し，Trueを返す
    def checkDestroy(self):
        self.checkPos()
        self.checkHP()
        if(self.destroy==1):
            self.img.undraw()
            return True
        else:
            return False

    def selfUndraw(self):
        self.img.undraw()


    #self.countの更新 
    def updateCount(self):
        self.count+=1
        if(self.count==3600):
            self==0
