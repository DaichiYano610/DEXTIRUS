#movement.py
import math
import random


class MovePattern:

    def __init__(self):
        self.moveList=[]
        self.flag=0


    def checkDestroy(self):
        if(len(self.moveList)!=0):
            if(self.moveList[0].getDestroy()==1):
                self.moveList.pop(0)

    def getEnemyPattern1(self):

        if(self.flag==0):
            self.moveList.append(Movement())
            self.moveList.append(Movement())
            self.flag=1
        
        self.checkDestroy()
        if(len(self.moveList)==1):
            return self.moveList[0].circle(1.1,1)
        elif(len(self.moveList)==2):
            return self.moveList[0].enemyStart()
        else:
            return 0,0


    def getEnemyBossPattern(self):

        if(self.flag==0):
            self.moveList.append(Movement())
            self.moveList.append(Movement())
            self.flag=1
        
        self.checkDestroy()
        if(len(self.moveList)==1):
            return self.moveList[0].updown(1,2)
        elif(len(self.moveList)==2):
            return self.moveList[0].enemyStart()
        else:
            return 0,0



class Movement:

    def __init__(self):
        self.count=0
        self.destroy=0
        self.flag=0
        

    def setDestroy(self):
        self.destroy=1


    def getDestroy(self):
        return self.destroy

    def random1(self):
        if(random.random()>=0.5):
            self.flag = 1
        else:
            self.flag = -1
        
        
    #無限に動く

    #右移動
    def rightMove(self):
        return 1, 0

    def right1Move(self):
        return 2,0

    def right2Move(self):
        return 4,0
    
    def right3Move(self):
        return 6,0

    #左移動
    def leftMove(self):
        return -1, 0

    def left1Move(self):
        return -2,0

    def left2Move(self):
        return -4,0
    
    def left3Move(self):
        return -6,0

    #上移動
    def upMove(self):
        return 0,1

    def up1Move(self):
        return 0,2
    
    def up2Move(self):
        return 0,4
    
    def up3Move(self):
        return 0,6

    #下移動
    def downMove(self):
        return 0,-1

    def down1Move(self):
        return 0,-2
    
    def down2Move(self):
        return 0,-4

    def down3Move(self):
        return 0,-6

    #右斜め上
    def upper_right_Move(self):
        return 2,1

    #左斜め上
    def upper_left_Move(self):
        return -1,1

    #右斜め下
    def bottomm_right_Move(self):
        return 2,-1

    #左斜め下
    def bottom_left_Move(self):
        return -1,-1

    #上下
    def updown(self,n,t):
        self.count+=1
        if(self.count==360):
            self.count=0

        return 0, n * math.cos(math.radians(self.count * t))


    #円運動
    def circle(self,n,t):
        if(self.flag==0):
            self.random1()
        self.count+=1
        if(self.count==360):
            self.count=0

        return - n * math.sin(math.radians(self.count * t)),self.flag * n * math.cos(math.radians(self.count * t))
    
    
    #一定時間
    
    def enemyStart(self):
        if(self.count==60):
            self.setDestroy()
        else:
            self.count+=1

        return self.leftMove()
            
        

    
