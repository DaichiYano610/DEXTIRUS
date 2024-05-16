#collision.py
import winsound as ws


class Collision:

    def judge(self,s,t):
        if not (((s.getY() - s.getLength() / 2) >= (t.getY() + t.getLength() / 2)) or ((s.getY() + s.getLength() / 2) <=(t.getY() - t.getLength() / 2))):
            if not (((s.getX() - s.getWidth() / 2) >= (t.getX() + t.getWidth() / 2)) or ((s.getX() + s.getWidth() / 2) <=(t.getX() - t.getWidth() / 2))):
                return True
            else:
                return False

        else:
            return False


    def on(self,player,enemyList):
        
        for enemy in enemyList:

            #playerとenemyの判定
            if (self.judge(player,enemy)):
                    player.addHP(-1)
                    enemy.addHP(-1)


            for eBullet in enemy.getEBulletList():
                 #playerとeBulletの判定
                    if  (self.judge(player,eBullet)):
                            player.addHP(-1)
                            eBullet.addHP(-1)
                            
                    '''
                    for pBullet in player.getPBulletList():
                        #pbulletとeBulletの判定
                        if (self.judge(pBullet,eBullet)):
                                pBullet.addHP(-1)
                                eBullet.addHP(-1)

                    '''



        for enemy in enemyList:
            for pBullet in player.getPBulletList():
                #pBulletとenemyの判定
                        if (self.judge(pBullet,enemy)):
                                pBullet.addHP(-1)
                                enemy.addHP(-1)

                
                
                        



                
                
                    
            
            
                
            
        
        
    
