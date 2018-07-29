import itertools
import pprint
import pokerhand 
import pokerdeck
import pokercard
import copy


class BestHandChooser():
    def __init__(self,hand,deck):
        self.hand = hand
        self.deck = deck

    def get_best_hand(self):
        all_possible_cards = []
        all_possible_cards.append(self.hand)
        all_possible_cards.append(pokerhand.Hand(self.deck.cards))

       
        for num_cards_replace in range(1,5):
            for p in itertools.permutations(range(0,5),num_cards_replace):
                new_cards =  list(self.hand.cards)
                for replace_index in range(0,num_cards_replace):
                    new_cards[p[replace_index]] = self.deck.cards[replace_index]

                new_hand = pokerhand.Hand(new_cards)
                all_possible_cards.append(new_hand)

                #print((p))


        all_possible_cards.sort()
        return all_possible_cards[-1]
    

if __name__ == '__main__':
    hand = pokerhand.Hand.from_string("TH JH QC QD QS")
    deck = pokerdeck.Deck("QH KH AH 2S 6S")
    best_hand_chooser = BestHandChooser(hand,deck)
    print(best_hand_chooser.get_best_hand())
