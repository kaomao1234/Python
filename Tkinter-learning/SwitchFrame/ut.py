class Meteorite:
    def __init__(self):
        self.controller = None
        self.destroy = False
        self.atkPoint = 5

    def hit(self):
        self.destroy = True


class SpaceShip:
    def __init__(self):
        self.controller:Game = None
        self.atkPoint = 50
        self.hp = 100

    def attack(self):
        self.controller.score += 1
        print("Attack!")

    def hasAttacked(self):
        self.controller.score -= 5
        print("Spaceship has attack by meteorite!")


class Game:
    def __init__(self):
        self.level = 'normal'
        self.score = 100
        self.spaceShip = SpaceShip()
        self.meteorite = Meteorite()

    def init(self):
        self.spaceShip.controller = self
        self.meteorite.controller = self

    def backToMenu(self):
        self.level = 'normal'
        self.score = 0


game1 = Game()
game1.init()
print(game1.score)
game1.spaceShip.attack()
game1.spaceShip.hasAttacked()
print(game1.score)
