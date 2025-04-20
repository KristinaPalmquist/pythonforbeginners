import random

# class Dice:
#     def __init__(self):
#         self.numbers = (1, 2, 3, 4, 5, 6)
#     def roll(self):
#         return random.choice(self.numbers)

class Dice:
    def roll(self):
       first = random.randint(1, 6)
       second = random.randint(1, 6)
       return first, second


