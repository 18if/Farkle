import random
class Farkle:
  
  
  def __init__(self):
    self.rolls = []
    self.gameover = False
    self.players = int(input('How many players? '))
    self.playing = range(1,self.players)
    self.my_score = 0
    self.scores = {1:100, 2:20, 3:30, 4:40, 5:50, 6:60}

  def move(self):
    for i in range(5):
      self.rolls.append(random.randint(1,6))
      self.my_score += sum(self.scores[a] for a in self.rolls)
  def play(self):
    while not self.gameover:
      for player in self.playing:
        self.move()
        print(self.my_score)
        if self.my_score >= 10000:
          print("Player {} wins!".format(player))
          self.gameover = True
          break
