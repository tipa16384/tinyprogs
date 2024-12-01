from enum import Enum
from random import shuffle
from collections import defaultdict

class Suits(Enum):
    Masks = 1
    Crows = 2
    Rams = 3
    Tomes = 4,
    JOKERS = 5

class Card:
    def __init__(self, suit: Suits, value: int):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"Card(suit={self.suit.name}, value={self.value})"
    
    def __str__(self):
        if self.suit == Suits.JOKERS:
            return "Black Joker" if self.value == 0 else "Red Joker"
        return f"{self.value} of {self.suit.name}"

def create_deck():
    deck = []
    for suit in Suits:
        if suit == Suits.JOKERS:
            deck.append(Card(suit, 0))  # Black Joker
            deck.append(Card(suit, 14)) # Red Joker
        else:
            for value in range(1, 14):
                deck.append(Card(suit, value))
    return deck

def stone_hand(hand, discard, rest_of_deck):
    # draw two cards and discard the lowest two cards and return the new hand, discard, and deck
    new_hand = hand + rest_of_deck[:2]
    new_hand.sort(key=lambda card: card.value)
    new_discard = discard + hand[:2]
    new_deck = rest_of_deck[2:]
    new_hand = new_hand[2:]
    return (new_hand, new_discard, new_deck)

def draw_hand(extra=False):
    deck = create_deck()
    shuffle(deck)
    
    num_cards_to_draw = 7 if extra else 6
    hand = deck[:num_cards_to_draw]

    discard = []
    rest_of_deck = deck[num_cards_to_draw:]
    hand = hand[2:]
    
    return (hand, discard, rest_of_deck)

def evaluate_hand_strength(hand, w_mean=1, w_median=1, w_sd=0.5):
    """
    Evaluates the strength of a hand of cards based on mean, median, and standard deviation of card values.

    Parameters:
    - hand (list): A list of Card objects, each having at least a 'value' attribute.
    - w_mean (float): Weight for the mean in the hand strength score.
    - w_median (float): Weight for the median in the hand strength score.
    - w_sd (float): Weight for the standard deviation in the hand strength score.

    Returns:
    - hss (float): The calculated hand strength score.
    """
    import statistics

    # Extract the card values
    values = [card.value for card in hand]

    # Calculate mean, median, and standard deviation
    mean_value = statistics.mean(values)
    median_value = statistics.median(values)
    sd_value = statistics.stdev(values) if len(values) > 1 else 0  # Avoid division by zero

    # Compute the Hand Strength Score (HSS)
    hss = w_mean * mean_value + w_median * median_value - w_sd * sd_value

    return hss

def analyze_stoning_improvement():
    # dictionary with key integer from 0..14 and value is a floating point number
    improvement = {}
    trials = 100000
    for _ in range(trials):
        hand, discard, deck = draw_hand()
        sd = evaluate_hand_strength(hand, w_mean=0, w_median=0, w_sd=1)
        median = evaluate_hand_strength(hand, w_mean=0, w_median=1, w_sd=0)
        mean = evaluate_hand_strength(hand, w_mean=1, w_median=0, w_sd=0)
        lowest_card_value = min([card.value for card in hand])
        hand, discard, deck = stone_hand(hand, discard, deck)
        sd_1 = evaluate_hand_strength(hand, w_mean=0, w_median=0, w_sd=1)
        median_1 = evaluate_hand_strength(hand, w_mean=0, w_median=1, w_sd=0)
        mean_1 = evaluate_hand_strength(hand, w_mean=1, w_median=0, w_sd=0)
        if not lowest_card_value in improvement:
            improvement[lowest_card_value] = (sd_1 - sd, median_1 - median, mean_1 - mean)
        else:
            sd_improvement, median_improvement, mean_improvement = improvement[lowest_card_value]
            improvement[lowest_card_value] = (sd_improvement + sd_1 - sd, median_improvement + median_1 - median, mean_improvement + mean_1 - mean)
    # divide each value by the number of trials
    for k in improvement:
        sd, median, mean = improvement[k]
        improvement[k] = (sd/trials, median/trials, mean/trials)

    return improvement

def write_csv(improvement: dict):
    with open('improvement.csv', 'w') as f:
        f.write("Card Value,Delta SD,Delta Median,Delta Mean\n")
        for k, v in improvement.items():
            sd, median, mean = v
            f.write(f"{k},{sd},{median},{mean}\n")

if __name__ == '__main__':
    improvement = analyze_stoning_improvement()
    write_csv(improvement)
    print("Analysis complete. Results written to improvement.csv")

