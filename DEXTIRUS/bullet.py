#bullet.py
from graphics import *
from movement import *
from frame import *
import random


class Bullet(Frame):

        def __init__(self,x,y,win):
                super().__init__(x,y,win)
                self.movement=Movement()
                self.width=30  #横
                self.length=20 #縦


        #画面外での削除
        def checkPos(self):
                if(self.x<-50 or 1050<self.x or self.y<-50 or self.y>650):
                    self.setDestroy()


        def move(self):
                dx, dy = self.movement.leftMove()
                self.x += dx *self.speed
                self.y += dy *self.speed
                self.img.move(dx *self.speed, dy *self.speed)


class PlayerBullet(Bullet):

        def __init__(self,x,y,win):
                super().__init__(x,y,win)
                  
                self.img = Image(Point(self.x,self.y),"playerBulletImage.jpg")
                self.img.draw(self.win)
                

        def move(self):
                dx, dy = self.movement.rightMove()
                self.x += dx *self.speed
                self.y += dy *self.speed
                self.img.move(dx *self.speed,dy *self.speed)


class PlayerUpBullet(PlayerBullet):

        def __init__(self,x,y,win):
                super().__init__(x,y,win)
                self.speed=5

        def move(self):
                dx, dy = self.movement.upper_right_Move()
                self.x += dx *self.speed
                self.y += dy *self.speed
                self.img.move(dx *self.speed,dy *self.speed)
                
                

class PlayerDownBullet(PlayerBullet):

        def __init__(self,x,y,win):
                super().__init__(x,y,win)
                self.speed=5

        def move(self):
                dx, dy = self.movement.bottomm_right_Move()
                self.x += dx *self.speed
                self.y += dy *self.speed
                self.img.move(dx *self.speed,dy *self.speed)
                


class EnemyBullet(Bullet):

        def __init__(self,x,y,win):
                super().__init__(x,y,win)
                self.width=20
                self.length=20
                
                self.speed=4

                self.img = Image(Point(self.x,self.y),"enemyBulletImage.jpg")
                self.img.draw(self.win)


class EnemyQuickBullet(Bullet):

        def __init__(self,x,y,win):
                super().__init__(x,y,win)
                self.width=30
                self.length=20
                
                self.speed=7

                self.img = Image(Point(self.x,self.y),"enemyQuickBulletImage.jpg")
                self.img.draw(self.win)
                



class EnemyReflectBullet(Bullet):

        def __init__(self,x,y,win):
                super().__init__(x,y,win)
                self.width=20
                self.length=20
                
                self.speed=3

                self.img = Image(Point(self.x,self.y),"enemyReflectBulletImage.jpg")
                self.img.draw(self.win)
                
                self.flagY=random.randint(0,1)
                self.flagX=0


        def move(self):
                if(self.y >= 600):
                        self.flagY=0
                if(self.flagY==0):
                        dx, dy = self.movement.downMove()
                        self.x += dx *self.speed
                        self.y += dy *self.speed
                        self.img.move(dx *self.speed, dy *self.speed)


                if(self.y <= 0):
                        self.flagY=1
                if(self.flagY==1):
                        dx, dy = self.movement.upMove()
                        self.x += dx *self.speed
                        self.y += dy *self.speed
                        self.img.move(dx *self.speed, dy *self.speed)


                if(self.x >= 1000):
                        self.flagX=0
                if(self.flagX==0):
                        dx, dy = self.movement.leftMove()
                        self.x += dx *self.speed
                        self.y += dy *self.speed
                        self.img.move(dx *self.speed, dy *self.speed)


                if(self.x <= 0):
                        self.flagX=1
                if(self.flagX==1):
                        dx, dy = self.movement.rightMove()
                        self.x += dx *self.speed
                        self.y += dy *self.speed
                        self.img.move(dx *self.speed, dy *self.speed)

                if(self.count==420):
                        self.setDestroy()


class EnemyBossBullet(Bullet):

        def __init__(self,x,y,win):
                super().__init__(x,y,win)
                self.hp=2
                self.width=100
                
                self.img = Image(Point(self.x,self.y),"enemyBossBulletImage.jpg")
                self.img.draw(self.win)
                



                


                

                
                        
                        
                         
                        
                
                


        



