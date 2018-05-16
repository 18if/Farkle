# wins when has 10,000 points
# scoring die will be in scoring sheet
"""
Questions:
  mentioning roll twice. not sure if necessary
  help wiht play and move functions
  need help cleaning up my code. Specifically play, move, and die
  how to store roll to use it's values later. pop?
"""
import math
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
      # need to store it somehow in order to use it later to score
  def scoring_sheet(self):
    thousand = 1,1,1
    two_hundred = 2,2,2
    three_hundred = 3,3,3
    four_hundred = 4,4,4
    five_hundred = 5,5,5
    six_hundred = 6,6,6
    all_dice = 1,2,3,4,5,6
    scores = {1:100, 5:50, thousand:1000, two_hundred:200, three_hundred:300,four_hundred:400, five_hundred:500, six_hundred:600, all_dice:3000}
          roll = random.randint(1,6)
    my_score = my_score += scores[roll]
    pass
      
  def move(self):
    for player in self.playing:
      self.die()
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
    
