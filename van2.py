import random

class Stud:
    def __init__(self, name):
        self.name = name
        self.deadinside = 50
        self.prog = 0
        self.dengi = 100
        self.life = True
    def sell_organs(self):
        print("You have sold your organs")
        self.deadinside -= 10
        self.dengi += 100
    def stud(self):
        print("Studying")
        self.deadinside -= 5
        self.prog += 1
    def suck(self):
        print("Sleeping")
        self.deadinside += 5
    def celebrate(self):
        print("VIETNAM FLASHBACKS")
        self.deadinside += 20
        self.prog -= 0.1
        self.dengi -= 5
    def alive(self):
        if self.dengi < 10:
            print("You have obtained POMOYKA")
            self.alive = False
        if self.deadinside < 0:
            print("suicide")
            self.alive = False
        if self.deadinside > 400:
            print("You have obtained Heaven")
            self.alive = False
        if self.prog < -0.1:
            print("Your parents have killed you")
            self.alive = False
        if self.prog > 70:
            print("You study nicely")
    def day_end(self):
        print(f"Moral health = {self.deadinside}/390")
        print(f"Progress = {self.prog}")
        print(f"Money = {self.dengi} UAH")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + "`s life."
        print(f"{day:=^50}")
        if self.prog < 10:
            self.stud()
            self.alive()
        elif self.deadinside < 10:
            self.celebrate()
            self.alive()
        elif self.dengi < 20:
            self.sell_organs()
            self.alive()
        deb = random.randint(1, 4)
        if deb == 1:
            self.deadinside -= 1
        if deb == 2:
            self.dengi -= 1
        if deb == 3:
            self.prog -= 1
        if deb == 4:
            self.prog += 1
            self.deadinside += 1
            self.dengi += 1
        self.day_end()


nick = Stud(name = "Dead inside")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
if nick.prog > 70 and nick.life == True:
    print("You have obtained university")
elif nick.prog < 70 and nick.life == True:
    print("You finished school")
