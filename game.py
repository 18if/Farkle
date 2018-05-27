import random
class Farkle:
  
  
  def __init__(self):
    self.rolls = []
    self.gameover = False
    self.players = int(input('How many players? '))
    self.playing = range(self.players)
    self.my_score = 0
    self.scores = {1:100, 2:200, 3:300, 4:400, 5:500, 6:600}

  def move(self):
    for i in range(5):
      self.rolls.append(random.randint(1,6))
      self.my_score += sum(self.scores[a] for a in self.rolls)
  def play(self):
    while self.gameover:
      for player in self.playing:
        self.move()
        print(self.my_score)
        if self.my_score >= 10000:
          self.gameover = True
          print("Player {} wins!".format(player))
          break
a = Farkle()
