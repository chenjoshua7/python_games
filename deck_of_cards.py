##############################
##                          ##
##       Deck of Card       ##
##      (Hi/Lo/Rd/Blk)      ##
##                          ##
##############################

# After showing my Blackjack game to a couple people, they strongly suggested I
# practice working with classes. Therefore, I decided to make a Card class and
# Deck class to represent a deck of cards. I then used this to make the simple
# High Low Red Black card guessing game

class Card:
    def __init__(self, suit, rank):
        if not isinstance(suit, int) or not isinstance(rank, int):
            raise ValueError("Both suit and rank must be integers")
        
        valid_suits = {1: "Hearts", 2: "Diamonds", 3: "Spades", 4: "Clubs"}
        valid_rank = {14: "Ace", 
                      2: 2,
                      3: 3,
                      4: 4,
                      5: 5,
                      6: 6,
                      7: 7,
                      8: 8,
                      9: 9,
                      10: 10,
                      11: "Jack",
                      12: "Queen",
                      13: "King",
                    }
        
        if rank not in valid_rank:
            raise ValueError(f"Invalid card. Choose from {list(valid_rank.values())}")

        if suit not in valid_suits:
            raise ValueError(f"Invalid suit. Choose from {list(valid_suits.values())}")

        self.rankint = rank

        self.suit = valid_suits[suit]
        self.rank = valid_rank[rank]

        if suit in [1,2]:
            self.color = "Red"
        if suit in [3,4]:
            self.color = "Black"

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def display(self):
        print(f"{self.rank} of {self.suit}")    

class Deck:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
        else:
            print(f"{card} not found in the deck.")

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def display(self, head=None):
        if head is None:
            head = len(self.cards)
        for card in self.cards[:head]:
            print(card)
    
    def random_draw(self, replace = True):
        self.shuffle()
        rand_card = self.cards[-1]
        if replace == False:
            self.remove(rand_card)
        return rand_card

    def count(self):
        return len(self.cards)

    def standard(self):
        for suit in range(1, 5):
            for rank in range(2, 15):
                self.add(Card(suit, rank))

## Hi Low Red Black
                
def playGame():
    deck = Deck()
    deck.standard()
    start = deck.random_draw(replace = False)
    print("Starting card: " + str(start))
    score = 0

    while True:
        print("-" * 45)
        print("||High - 1||Low -  2||Red - 3||Black - 4||")
        guess = int(input("Make your guess: "))
        card = deck.random_draw(replace = False)
        print(f"Draw: " + str(card))
        if guess == 1:
            if card.rankint > start.rankint:
                score += 1
                print(f"Score - {score}")
            if card.rankint == start.rankint:
                score == 0
                print("Same Card - You Lose!")
                break
            if card.rankint < start.rankint:
                score == 0
                print("You Lose!")
                break
        if guess == 2:
            if card.rankint < start.rankint:
                score += 1
                print(f"Score - {score}")
            if card.rankint == start.rankint:
                score == 0
                print("Same Card - You Lose!")
                break
            if card.rankint > start.rankint:
                score == 0
                print("You Lose!")
                break
        if guess == 3:
            if card.color == "Red":
                score += 1
                print(f"Score - {score}")
            else:
                score == 0
                print("You Lose!")
                break
        if guess == 4:
            if card.color == "Black":
                score += 1
                print(f"Score - {score}")
            else:
                score == 0
                print("You Lose!")
                break
        start = card
    
    print("-" * 45)
    print(f"Final Score: {score} Play Again?")
    again = int(input("Yes - 1 || No - 0   "))
    if again == True:
        print("-" * 45)
        print("-" * 45)
        print("-" * 45)
        print("-" * 45)
        print("-" * 45)
        playGame()

playGame()