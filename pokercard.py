import itertools
import pokerdeck

RANKS = ['A', 'K', 'Q', 'J','T','9','8','7','6','5','4','3','2']
SUITS = ['C','D', 'H', 'S']

RANK_NUMERIC = {'A':14, 'K':13, 'Q':12, 'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2 }

NUMERIC_RANK = {v: k for k, v in RANK_NUMERIC.items()}

deck52 = [card[0] + card[1] for card in itertools.product(RANKS,SUITS) ]

assert len(deck52) == 52, "standard 52-card deck"

class Card():
    def __init__(self,card_str):
        self.card_str = card_str.upper()
        assert self.card_str in deck52, "a card must be in a deck"
        self.rank = self.card_str[0]
        self.numeric_rank = RANK_NUMERIC[self.rank]
        self.suit = self.card_str[1]

    def __repr__(self):
        return self.card_str
   

