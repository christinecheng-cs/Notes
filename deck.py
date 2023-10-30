import collections


Cards = collections.namedtuple('Cards', ['rank', 'suit'])

class Deck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
                   
  def __getitem__(self, position):
    return self._cards[position]
    
  def __len__(self):
    pass


