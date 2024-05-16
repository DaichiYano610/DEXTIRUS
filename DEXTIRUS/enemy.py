#enemy.py
import random
from frame import *
from graphics import *
from movement import *
from bullet import *


class EnemyManage:

    def __init__(self,win):
        self.enemyList = []
        self.win=win
        self.count=0
        self.time=0
        self.destroyCount=0
        self.flag=0
        

    def getEnemyList(self):
        return self.enemyList

    def getDestroyCount(self):
        return self.destroyCount

    def getGameClear(self):
        if(self.flag==1 and len(self.enemyList)==0):
            return True
        else:
            return False


    def spawn(self):
        if(self.time <= 20 or (self.time >= 40 and self.time <= 60)):
            self.randomNormalEnemySpawn()
        if(( self.time >= 20 and self.time<=40) or (self.time >= 40 and self.time <= 60)):
            self.randomQuickEnemySpawn()

        if(self.time > 60 and len(self.enemyList)==0 and self.flag==0):
            self.BossSpawn()
            self.flag=1

    def BossSpawn(self):
        self.enemyList.append(EnemyBoss(1020, 300,self.win))
        

    def randomQuickEnemySpawn(self):
        if(self.count % 240 ==0 and len(self.enemyList)<8):
            self.enemyList.append(QuickEnemy(1100, random.randint(100,500),self.win))
            self.enemyList.append(QuickEnemy(1100, random.randint(100,500),self.win))

    def randomNormalEnemySpawn(self):
        if(self.count % 240 ==0 and len(self.enemyList)<8):
            self.enemyList.append(NormalEnemy(1100, random.randint(100,500),self.win))
            self.enemyList.append(NormalEnemy(1100, random.randint(100,500),self.win))
            

    def enemyFire(self):
        for enemy in self.enemyList:
            enemy.fire()
    
    def move(self):
        for enemy in self.enemyList:
            enemy.move()
            enemy.bulletMove()

    def checkBullet(self):
        for enemy in self.enemyList:
            enemy.checkBullet()

        

    def checkEnemy(self):
        for enemy in self.enemyList[:]:
            if(enemy.checkDestroy()):
                enemy.allBulletRemove()
                self.enemyList.remove(enemy)
                self.destroyCount+=1

    def updateCount(self):
        self.count+=1
        if(self.count % 60==0):
            self.time+=1
        if(self.count==3600):
            self.count==0
            
        for enemy in self.enemyList[:]:
            enemy.updateCount()
    

class Enemy(Frame):

    def __init__(self,x,y,win):
        super().__init__(x,y,win)
        self.fireRate=240
        self.eBulletList=[]
        self.movePattern = MovePattern()
        self.movement=Movement()


    def getEBulletList(self):
        return self.eBulletList


    #弾の発射する時間間隔の変更
    def setFireRate(self,rate):
        self.fireRate = rate


    #eBulletListにあるEnemyBulletの移動
    def bulletMove(self):
        for eBullet in self.eBulletList[:]:
            eBullet.move()

    def allBulletRemove(self):
        for eBullet in self.eBulletList[:]:
            eBullet.selfUndraw()
        self.eBulletList.clear()
        

    #eBulletsにあるEnemyBulletのdestroyをチェックし削除
    def checkBullet(self):
        for eBullet in self.eBulletList[:]:
            if(eBullet.checkDestroy()):
                self.eBulletList.remove(eBullet)


    def updateCount(self):
        super().updateCount()
        for eBullet in self.eBulletList[:]:
            eBullet.updateCount()


class NormalEnemy(Enemy):

    def __init__(self,x,y,win):
        super().__init__(x,y,win)
        self.width=80
        self.length=60
        
        self.hp=5
        self.speed=2
        self.fireRate=60
        self.img=Image(Point(self.x,self.y),"enemy1Image.jpg") 
        self.img.draw(self.win)
        

    #動かす
    def move(self):
        dx, dy = self.movePattern.getEnemyPattern1()
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.img.move(dx * self.speed,dy * self.speed)


    def fire(self):
        if(self.count % self.fireRate == 0):
            self.eBulletList.append(EnemyBullet(self.x,self.y +15,self.win))
            

        if((self.count + 30) % int(self.fireRate *1.8) == 0 ):
            self.eBulletList.append(EnemyReflectBullet(self.x,self.y +15,self.win))
        


class QuickEnemy(Enemy):

    def __init__(self,x,y,win):
        super().__init__(x,y,win)
        self.width=80
        self.length=60
        
        self.hp=5
        self.speed=2
        self.fireRate=30
        self.img=Image(Point(self.x,self.y),"enemy2Image.jpg") 
        self.img.draw(self.win)

    #動かす
    def move(self):
        dx, dy = self.movePattern.getEnemyPattern1()
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.img.move(dx * self.speed,dy * self.speed)


    def fire(self):
        if(self.count % self.fireRate == 0 ):
            self.eBulletList.append(EnemyQuickBullet(self.x,self.y,self.win))

        '''
        if(self.count % (self.fireRate * 6) == 0 ):
            self.eBulletList.append(EnemyReflectBullet(self.x,self.y +15,self.win))
        '''


class EnemyBoss(Enemy):

    def __init__(self,x,y,win):
        super().__init__(x,y,win)
        self.width=200
        self.length=500
        
        self.hp=300
        self.speed=4
        self.fireRate=93
        self.img=Image(Point(self.x,self.y),"enemyBossImage.jpg") 
        self.img.draw(self.win)


    #動かす
    def move(self):
        dx, dy = self.movePattern.getEnemyBossPattern()
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.img.move(dx * self.speed,dy * self.speed)


    def fire(self):
        if(self.count % self.fireRate == 0 or (self.count - 10)% self.fireRate ==0 or (self.count - 20)% self.fireRate ==0):
            self.eBulletList.append(EnemyBossBullet(self.x - 100, self.y +75,self.win))
            self.eBulletList.append(EnemyBossBullet(self.x - 100, self.y -70,self.win))

        if((self.count-30) % self.fireRate == 0 or (self.count - 40)% self.fireRate ==0 or (self.count - 50)% self.fireRate ==0):
            self.eBulletList.append(EnemyBossBullet(self.x - 100, self.y +170,self.win))
            self.eBulletList.append(EnemyBossBullet(self.x - 100, self.y -170,self.win))

        if(self.count % (self.fireRate * 4)  == 0):
            self.eBulletList.append(EnemyReflectBullet(self.x - 50, self.y +100,self.win))

        if(self.count % (self.fireRate * 4)  == 0):
            self.eBulletList.append(EnemyReflectBullet(self.x - 50, self.y -120,self.win))

        if((self.count - 30) % (self.fireRate * 4)  == 0):
            self.eBulletList.append(EnemyReflectBullet(self.x - 80, self.y +170,self.win))

        if((self.count - 30) % (self.fireRate * 4) == 0):
            self.eBulletList.append(EnemyReflectBullet(self.x - 80, self.y -170,self.win))

        
            



    

    

    
