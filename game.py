import random
from collections import Counter
class Farkle:
  
  
  def __init__(self, playing = 2):
    self.SCORES = {
      1: {1: 100, 2: 200, 3: 300, 4: 2000, 5: 2200, 6: 2300},
      2: {1: 20, 2: 40, 3: 200, 4: 400, 5: 440, 6: 600},
      3: {1: 30, 2: 60, 3: 300, 4: 600, 5: 660, 6: 900},
      4: {1: 40, 2: 80, 3: 400, 4: 800, 5: 880, 6: 1200},
      5: {1: 50, 2: 100, 3: 500, 4: 1000, 5: 1100, 6: 1500},
      6: {1: 60, 2: 120, 3: 600, 4: 1200, 5: 1420, 6: 2020}}
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
          return False
      if question == 'n':
        die_num = self.new_list[0]
        c = Counter(self.new_list)
        b = c[die_num]
        die_score = self.SCORES[die_num][b]
        self.scores[player] += die_score
        print("Score last move: {}".format(die_score))
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
    if self.scores >= 10000:
      print("Player {} wins!".format(player))
