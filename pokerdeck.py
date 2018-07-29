import pokercard

class Deck():
    def __init__(self, top_5_cards):
        self.cards = top_5_cards

    # constructs from string
    @classmethod
    def from_string(cls, cards_string):
        cards = []
        for card_str in cards_string.split(' '):
            cards.append(pokercard.Card(card_str))

        return cls(cards)

    def __repr__(self):
        repr = 'Decks top cards : ' + ' '.join([str(x) for x in self.cards]) + "\n"
        return repr

    def serve_cards_from_top(self,num_cards):
        return self.cards[0:num_cards]

     
