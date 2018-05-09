import random
class Farkle:
  
  
    def __init__(self):
      self.gameover = False
      self.players = int(input('How many players? '))
      self.playing = range(self.players)
    def die(self):
      for i in range(6):
        roll = random.randint(1,6)
        print(roll)
    def play(self):
      for player in self.playing:
        self.die
