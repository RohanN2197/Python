#class Tuna:
#    def __init__(self):
#        print('blblabla')

#    def swim(self):
#        print('I am eating')

#tuna = Tuna()
#tuna.swim()

class Enemy:
    def __init__(self,x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

DarthVader = Enemy(5) #DathVader Object with 5 energy
SithTrooper = Enemy(3)

DarthVader.get_energy()
SithTrooper.get_energy()

