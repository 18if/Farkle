import random
class Farkle:
  
  
  def __init__(self, playing = 2):
    self.SCORES = {1:100, 2:20, 3:30, 4:40, 5:50, 6:60}
    self.scores = [0 for player in range(num_players)]

  def move(self, player):
    rolls = [random.randint(1,6) for n in range(6)]
    print('Player {}: {}'.format(player+1, rolls))
    roll_values = [self.SCORES[roll] for roll in rolls]
    print('Score this turn: {}\n'.format(sum(roll_values)))
    self.scores[player] += sum(roll_values)
