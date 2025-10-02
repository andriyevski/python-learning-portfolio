# Homework from file tasks/9_13_Dice.md
## Task ## : 9.13
# 9_13_Dice
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self, sides):
        self.sides = sides
        number_rand = randint(1,self.sides)
        return f"Cube have right now a {number_rand} sides!"

    def drop(self, sides, times):
        self.sides = sides
        self.times = times

        times_real = 0
        while self.times > 0:
            self.times-=1
            times_real+=1
            print(f"We drop - {times_real} times : You have a {self.sides} sides!")



new_cube = Die()
print(new_cube.roll_die(100))
print(new_cube.drop(1,100))
print(new_cube.drop(5,20))
