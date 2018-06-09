import random
from collections import Counter
class Farkle:
  
  
  def __init__(self, playing = 2):
    self.SCORES = {
      1: {1: 100, 2: 200, 3: 300, 4: 2000, 5: 2100, 6: 2200},
      2: {1: 0, 2: 0, 3: 200, 4: 400, 5: 500, 6: 600},
      3: {1: 30, 2: 60, 3: 300, 4: 600, 5: 1000, 6: 2000},
      4: {1: 40, 2: 80, 3: 400, 4: 800, 5: 2000, 6: 2500},
      5: {1: 50, 2: 100, 3: 500, 4: 1000, 5: 1050, 6: 1100},
      6: {1: 60, 2: 120, 3: 600, 4: 1200, 5: 2000, 6: 3000}}
    self.scores = [0 for player in range(playing)]

  def move(self, player):
    self.rolls = [random.randint(1,6) for n in range(6)]
    print('Player {} Rolled: {}'.format(player+1, self.rolls))
    while True:
      indexes = input("Pick the indices you wish to extract separated by spaces(remember to start from 0)").split(' ')
      indexes = [int(n) for n in indexes]
      self.take_from_list(player, self.rolls, indexes)
      question = str(input('Roll again? (y/n)'))
      if question == 'y':
        die_num = self.new_list[0]
        c = Counter(self.new_list)
        b = c[die_num]
        die_score = self.SCORES[die_num][b]
        self.scores[player] += die_score
        print("Score last move: {}".format(die_score))    
        self.rolls = [random.randint(1,6) for n in self.remaining]
        print('Player {} Rolled: {}'.format(player+1, self.rolls))
        if self.rolls == []:
          self.rolls = [random.randint(1,6) for n in range(6)]
      if question == 'n':
        print('ok')
        return False
  
  def take_from_list(self, player, source, indexes):
    """ Given a source list, create a new list from a list of indexes, returning the new list and what remains from the old list 
    
    Example:
    take_from_list([1, 2, 3, 4, 5], [0, 2])
    >>([1, 3], [2, 4, 5])
    """
    self.new_list = []
    self.remaining = []

    for idx, val in enumerate(source):
      if idx in indexes:
        self.new_list.append(val)
      else:
        self.remaining.append(val)

    print(self.new_list, self.remaining)

      



  def play(self, player):
    self.move(player)
    print(self.scores)
    

class Die:
  
  def __init__(self, sides=6):
    self.value = 1
    self.sides = sides
  
  def __str__(self):
    return str(self.value)

  def roll(self):
    self.value = random.randint(1, self.sides)
