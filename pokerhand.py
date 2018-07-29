import pokercard

# class Hand represents  5 cards in the game of poker

rankings = {
 'straight-flush' : 9,
 'four-of-a-kind' : 8,
 'full-house'     : 7,
 'flush'          : 6,
 'straight'       : 5,
 'three-of-a-kind': 4,
 'two-pairs'      : 3,
 'one-pair'       : 2,
 'highest-card'   : 1
}

class Hand():
    def __init__(self,cards):
        self.cards = cards
        assert len(set(self.cards)) == len(self.cards), "hand contains duplicate cards {}".format(cards)
        self.ranking = self._determine_ranking()

    # constructs from string
    @classmethod
    def from_string(cls, cards_string):
        cards = []
        for card_str in cards_string.split(' '):
            cards.append(pokercard.Card(card_str))

        return cls(cards)

    def __getitem__(self,index):
        return self.cards[index]

    def __repr__(self):
        hand_repr = 'Hand : ' + ' '.join([str(x) for x in self.cards]) + "\n"
        hand_repr += 'Ranking : ' +  self.ranking + "\n"
        return hand_repr

    def __lt__(self,other):
        return rankings[self.ranking] < rankings[other.ranking]
        
    def _determine_ranking(self):
        straight_flush = self._is_straight_flush()
        if straight_flush: 
            return 'straight-flush'

        four_of_a_kind = self._is_four_of_a_kind()
        if four_of_a_kind :
            return  'four-of-a-kind' 

        full_house = self._is_full_house()
        if full_house:
            return 'full-house'

        flush = self._is_flush()
        if flush: 
            return 'flush'

        straight = self._is_straight()
        if straight:
            return 'straight' 

        three_of_a_kind = self._is_three_of_a_kind()
        if three_of_a_kind :
            return  'three-of-a-kind' 


        two_pairs = self._is_two_pairs()
        if two_pairs:
            return 'two-pairs'


        one_pair = self._is_one_pair()
        if one_pair:
            return 'one-pair'

        return 'highest-card'

    def _is_straight_flush(self):
        same_suit = self._same_suit() 
        continous_rank = self._continous_rank()
        #print(same_suit,continous_rank)
        return self._same_suit() and self._continous_rank()

    def _is_straight(self):
        return self._continous_rank()

    def _is_flush(self):
        return self._same_suit() 

    def _is_four_of_a_kind(self):
        return self._has_4_same_rank()

    def _is_three_of_a_kind(self):
        return self._has_3_same_rank()

    def _is_two_pairs(self):
        rank_stats = self._get_rank_stats()
        return len(rank_stats) == 3

    def _is_one_pair(self):
        rank_stats = self._get_rank_stats()
        max_key = max(rank_stats.keys(), key=(lambda k: len(rank_stats[k])))
        return len(rank_stats[max_key]) == 2

    def _is_full_house(self):
        rank_stats = self._get_rank_stats()
        if len(rank_stats.keys()) == 2:
            for key in rank_stats:
                if len(rank_stats[key]) == 3:
                    return True
            
        return False
                
    def _continous_rank(self):
        rankings = [None] * (len(pokercard.RANKS) + 2)
        for card in self.cards:
            rankings[card.numeric_rank] = card 

        continous_count = 0
        for i in range(2,14+1):
            if rankings[i] is not None:
                continous_count+=1 
            else:
                continous_count = 0 
            if continous_count == 5:
                return True
        return False


    def _get_rank_stats(self):
        rank_stats = {}
        for card in self.cards:
            if card.rank not in rank_stats:
                rank_stats[card.rank] = []
            rank_stats[card.rank].append(card) 
        return rank_stats


    def _has_4_same_rank(self):
        rank_stats = self._get_rank_stats()
        max_key = max(rank_stats.keys(), key=(lambda k: len(rank_stats[k])))
        return len(rank_stats[max_key]) == 4

    def _has_3_same_rank(self):
        rank_stats = self._get_rank_stats()
        max_key = max(rank_stats.keys(), key=(lambda k: len(rank_stats[k])))
        return len(rank_stats[max_key]) == 3

    def _same_suit(self):
        return len(set([card.suit for card in self.cards])) == 1 

    def _break_into_suits(self):        
        suits = {}

        for suit in pokercard.SUITS:
            suits[suit] = [None] * (len(pokercard.RANKS) + 2)

        for card in self.cards:
            suits[card.suit][card.numeric_rank] = card 

        return suits
   

if __name__ == '__main__':
    hand = Hand.from_string("AH KH QH JH TH")
    print(hand)
    hand = Hand.from_string("KH KS KC KD TH")
    print(hand)
    hand = Hand.from_string("KH KS KC QH QD")
    print(hand)

    hand = Hand.from_string("AH KH QH JH 9H")
    print(hand)
    
    hand = Hand.from_string("TC TD TH 7S 6D")
    print(hand)

    hand = Hand.from_string("TC TD 7H 7S 6D")
    print(hand)
    
    hand = Hand.from_string("TC TD 7H 8S 6D")
    print(hand)

    hand = Hand.from_string("JC 9D 7H 8S 6D")
    print(hand)
    
