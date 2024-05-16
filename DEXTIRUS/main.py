#test.py
from graphics import *
import winsound as ws
from frame import *
from player import *
from enemy import *
from bullet import *
from movement import *
from collision import *
from ui import *


def main():
    #ウィンドウ表示
    win = GraphWin("game",1000,600,autoflush=False)
    win.setCoords(0,0,1000,600)

    replayFlag=1
    key0=""


    #入力用変数
    key1=""

    try:

        background=Image(Point(501,300),"title.png")
        background.draw(win)

        #音声
        ws.PlaySound("GameMusic.wav",ws.SND_LOOP | ws.SND_ASYNC )

        #タイトル処理
        
        while(1):
            key1=win.getKey()
            if(key1=="s"):
                break

    
        while(replayFlag):
                
    
            #背景
            background=Image(Point(501,300),"background.png")
            background.draw(win)
            
            #Playerインスタンス
            player=Player(300,300,win)

            #EnemyManageインスタンス
            enemyM=EnemyManage(win)

            #Collisionインスタンス
            collision=Collision()

            #UIのインスタンス
            ui=UI(win,player.getHP(),enemyM.getDestroyCount())

            #ゲームの繰り返し処理
            while(1): 
                #キー入力    
                key1=win.checkKey()


                #playerの移動
                player.move(key1)

                #playerの弾の生成
                player.fire(key1)

                #playerの弾の移動
                player.bulletMove()
                
                #enemyの生成
                enemyM.spawn() 
                
                #enemyの弾の生成
                enemyM.enemyFire()

                #enemyとenemyの弾の移動
                enemyM.move()

                #衝突判定
                collision.on(player,enemyM.getEnemyList())


                #playerの必要のなくなった弾のデータ削除
                player.checkBullet()

                #ememyの必要のなくなった弾のデータ削除
                enemyM.checkBullet()

                #enemyの必要のなくなったデータ削除
                enemyM.checkEnemy()

                player.updateCount()
                enemyM.updateCount()
                

                ui.update(player.getHP(),enemyM.getDestroyCount())

                #"o"を入力すると終了する
                if(key1=="o"):
                    break

                if(player.getHP()<=0):
                    ui.setGameOver()
                    break

                if(enemyM.getGameClear()):
                    ui.setGameClear()
                    break
                
                update(60)

            ui.setGameReplay() 
            while(1):
                key0=win.getKey()
                if(key0=="r"):
                    break
                if(key0=="o"):
                    replayFlag=0
                    break
        


    finally:
        ws.PlaySound("*",ws.SND_PURGE)
        win.close()

main()
