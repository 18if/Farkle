import random
class Farkle:
  
  
  def __init__(self, playing = 2):
    self.SCORES = {1:100, 2:20, 3:30, 4:40, 5:50, 6:60}
    self.scores = [0 for player in range(playing)]
    self.rolls = [random.randint(1,6) for n in range(6)]

  def move(self, player):
    print('Player {} Rolled: {}'.format(player+1, self.rolls))
    roll_values = [self.SCORES[roll] for roll in self.rolls]
    print('Score this turn: {}\n'.format(sum(roll_values)))
    self.scores[player] += sum(roll_values)
  
  def take_from_list(self, source, indexes):
    """ Given a source list, create a new list from a list of indexes, returning the new list and what remains from the old list 
    
    Example:
    take_from_list([1, 2, 3, 4, 5], [0, 2])
    >>([1, 3], [2, 4, 5])
    """
    new_list = []
    remaining = []

    for idx, val in enumerate(source):
      if idx in indexes:
        new_list.append(val)
      else:
        remaining.append(val)

    
    return new_list, remaining
  
  def complicated_Scores(self, player):
    indexes = input("Pick the indices you wish to extract separated by spaces(remember to start from 0)").split(' ')
    indexes = [int(n) for n in indexes]
    new_list = take_from_list(self.rolls, indexes)[0]
    new_list = [self.SCORES[die] for die in new_list]
    self.scores[player] += sum(new_list)

  def play(self, player):
    self.move(player)
