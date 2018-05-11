# wins when has 10,000 points
# scoring die will be in scoring sheet
import math
import random
class Farkle:
  
  
  def __init__(self):
    self.gameover = False
    self.players = int(input('How many players? '))
    self.playing = range(self.players)
    self.score = # no idea how to do this
    
  def scoring_sheet(self):
# scoring die are:
# 1	100 points
# 5	50 points
# Three 1's	1,000 points
# Three 2's	200 points
# Three 3's	300 points
# Three 4's	400 points
# Three 5's	500 points
# Three 6's	600 points
# 1-2-3-4-5-6 	3000 jnhpoints
# 3 Pairs	1500 points (including 4-of-a-kind and a pair)
# ideas: use "math" to add and multiplt the dice
    pass
  def die(self):
    for i in range(6):
      roll = random.randint(1,6)
      print(roll)
      
  def move(self):
    for player in self.playing:
      
    # player moves
    # player puts aside whatever die they want
    # player moves untill all die are aside or fail to roll scoring die
     pass
    

  def play(self):
    for player in self.playing:
      self.move(player)
      if self.score >= 10,000:
        print("Player {} wins!".format(player))
      
      pass
    
