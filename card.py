import itertools
import deck

RANKS = ['A', 'K', 'Q', 'J','10','9','8','7','6','5','4','3','2']
SUIT  = ['C','D', 'H', 'S']

ALL_CARDS = [card[0] + card[1] for card in itertools.product(RANKS,SUIT) ]

assert len(ALL_CARDS) == 52, "standard 52-card deck"

def best_hand(hand_n_deck):
    deck = deck.Deck(hand_n_deck['deck'])

    best_hand_candidates = []

    for num_cards in [1..5]:
        top_cards = deck.serve(num_cards) 
        best_hand_candidates.append(get_best_hand(hand,top_cards))
    
    best_hand_name = choose_best_from_candidates(best_hand_candidates)
       


    return 'straight_flush'

def get_best_hand(hand,top_cards):

