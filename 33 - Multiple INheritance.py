class Mario():
    def move(self):
        print('I am Mario movin')

class Mushroom():
    def eat(self):
        print('Now i am big')


class BigMario(Mario,Mushroom):
    pass

bigMario = BigMario()
bigMario.move()
bigMario.eat()
