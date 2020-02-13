class Enemy:
    life = 3

    def attack(self):
        print('ouch!')
        self.life -=1

    def checkLife(self):
        if self.life <=0:
            print('dead')
        else:
            print(str(self.life) + "life left")


enemy1 = Enemy() #creating enemy1 object from class Enemy
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy2.checkLife()
