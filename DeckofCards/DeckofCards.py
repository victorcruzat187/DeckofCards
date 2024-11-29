# Victor Cruzat CIS 261 Deck of Cards

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __repr__(self):
        return(f"{self.rank} of {self.suit}")
    
class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "A"]
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]
                     
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self, num_cards):
        dealt_cards = []
        for _ in range(num_cards):
            if self.deck:
                dealt_cards.append(self.deck.pop())
            else:
                print("Nomore cards left to deal!")
                break
        return dealt_cards    
    
    def count(self):
        return len(self.deck)
    
#Main Program
if __name__ == "__main__":
    deck = Deck()
    print("Card Dealer \n")
    print(f"I have a shuffled deck of {deck.count()} cards. \n")
    
    #Shuffle the deck
    deck.shuffle()
    
    while True:
        try:
            #Ask the user how many cards to deal
            num_to_deal = int(input("How many cards would you like?: "))
            if num_to_deal <= 0:
                print("Please enter a positive number.")
                continue
            
            #Deal the cards
            dealt_cards = deck.deal(num_to_deal)
            if dealt_cards:
                print ("\nHere are your cards: ")
                for card in dealt_cards:
                    print(f"{card}")
              
            #Show how many cards are left
            print(f"\nThere are {deck.count()} left in the deck.")
            
            print(f"\nGood luck!")
            
            #Check if the deck is empty
            if deck.count() == 0:
                print("The deck is now empty.")
                break
            
        except ValueError:
            print("Please enter a valid number.")