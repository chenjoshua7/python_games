######################### 
##                     ##
##      BLACKJACK      ##
##                     ##
#########################

# Coded from scratch. Most complicated game I have coded to date. Implemented a simple betting system.
# Lets of room for improvement
#
# Ideas including
# 1. Insurance
# 2. Splitting
# 3. Doubling Down
# 4. Multiple Players
# 5. Cards including sutis
# 6. Multiple decks 

import random

# GLOBAL VARIABLES

SUITS = ["C", "H", "S", "D"] #unused
CARDS = [2,3,4,5,6,7,8,10,'J','Q','K','A'] * 4
NEW_DECK = CARDS.copy()

VALUE_10 = ["J","Q","K"]

PLAYER_HAND = []
DEALER_HAND = []

PLAYER_SCORE = 0
DEALER_SCORE = 0
BUST = False

MONEY = 1000
BET = 0

# Pause function for UI
def pause():
    pause = input("Press <ENTER> to continue...")
    

def deal_cards():
    global PLAYER_HAND, DEALER_HAND, CARDS
    PLAYER_HAND = CARDS[-2:]
    CARDS = CARDS[:-2]
    DEALER_HAND = CARDS[-2:]
    CARDS = CARDS[:-2]
    if check_blackjack(PLAYER_HAND) == check_blackjack(DEALER_HAND) == True:
        print("Both have Blackjack - Tie Game")
    elif check_blackjack(PLAYER_HAND):
        print(f'Your have a {PLAYER_HAND[0]} and {PLAYER_HAND[1]}')
        print('You have blackjack! Lucky lucky')
    elif check_blackjack(DEALER_HAND):
        print(f'Your have a {PLAYER_HAND[0]} and {PLAYER_HAND[1]}')
        print("Unlucky, Dealer got Blackjack")
    else:
        print(f'Your cards are a {PLAYER_HAND[0]} and {PLAYER_HAND[1]}')
        print(f'The Dealer shows a {DEALER_HAND[0]}')

def calculate_score(hand, score):
    score = 0
    for card in hand:
        if type(card) == int:
            score += card
        elif card in ["J", "Q", "K"]:
            score += 10

    if "A" in hand:
        if score + 11 <= 21:
            return score + 11
        else:
            return score + 1
    else:
        return score
        

def check_blackjack(hand):
    global VALUE_10
    if "A" not in hand:
        return False
    else:
        if any(card in hand for card in VALUE_10):
            return True
        else:
            return False

def playerChoice():
    global PLAYER_SCORE, PLAYER_HAND, CARDS, BUST
    PLAYER_SCORE = calculate_score(PLAYER_HAND, PLAYER_SCORE)
    print(f'Your score right now is {PLAYER_SCORE}')
    print("------------------------------------------")
    choice = int(input("Enter 1 to hit - Enter 0 to stay: "))
    print("------------------------------------------")
    if choice == 1:
        PLAYER_HAND.append(CARDS[-1])
        print(f'You drew a {CARDS[-1]}')
        CARDS = CARDS[:-1]
        PLAYER_SCORE = calculate_score(PLAYER_HAND, PLAYER_SCORE)
        if PLAYER_SCORE > 21:
            print('BUST!!')
            PLAYER_SCORE = 0
            BUST = True
            return
        if PLAYER_SCORE == 21:
            print('Nice! You got 21')
            return
        if PLAYER_SCORE < 21:
            playerChoice()
    else:
        return


def dealerMove():
    global PLAYER_SCORE, DEALER_SCORE, DEALER_HAND, CARDS, BUST
    if BUST == True:
        return
    DEALER_SCORE = calculate_score(DEALER_HAND, DEALER_SCORE)
    if DEALER_SCORE < 16:
        DEALER_HAND.append(CARDS[-1])
        print(f'Dealer drew a {CARDS[-1]}')
        CARDS = CARDS[:-1]
        DEALER_SCORE = calculate_score(DEALER_HAND, DEALER_SCORE)
        if DEALER_SCORE > 21:
            print('Dealer bust')
            DEALER_SCORE = 0
            return
        elif DEALER_SCORE > 16 or DEALER_SCORE > PLAYER_SCORE:
            return
        else:
            stop = input('...')
            dealerMove()
    
def winner():
    global DEALER_SCORE, PLAYER_SCORE, MONEY, BET
    print("------------------------------------------")
    pause()
    print("------------------------------------------")
    if DEALER_SCORE != 0 and PLAYER_SCORE != 0:
        print(f"Player: {PLAYER_SCORE} - Dealer: {DEALER_SCORE}")
    elif PLAYER_SCORE == 0:
        print('Player busted... Too bad :(')
        MONEY -= BET
        return
    elif DEALER_SCORE == 0:
        print('Dealer Buster - Player Wins!')
        MONEY += BET
        return
    if DEALER_SCORE > PLAYER_SCORE:
        print("Dealer wins")
        MONEY -= BET
    if PLAYER_SCORE > DEALER_SCORE:
        print("YOU WIN!")
        MONEY += BET
    if PLAYER_SCORE == DEALER_SCORE:
        print("Tie")

def getBet():
    global MONEY
    while True:
        try:
            bet = int(input("Bet amount: "))
            if bet <= MONEY and bet > 0:
                return bet
            else:
                print(f"Invalid bet amount. Please enter a bet less than or equal to your available money of ${MONEY}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def testing():
    global DEALER_HAND, PLAYER_HAND, BET, MONEY, CARDS
    playAgain = True
    print("Welcome to Chen's Casino - Good Luck!")
    print("------------------------------------------")
    while playAgain == 1:
        MONEY = 1000
        BUST = False
        CARDS = NEW_DECK.copy()
        print(f"You have ${MONEY}")
        BET = getBet()
        print("------------------------------------------")
        random.shuffle(CARDS)
        deal_cards()
        if check_blackjack(PLAYER_HAND) or check_blackjack(DEALER_HAND) == True:
            print("------------------------------------------")
            pause()
            print("------------------------------------------")
        else:
            playerChoice()
            if PLAYER_SCORE == 0:
                BUST = True
            pause()
            print("------------------------------------------")
            if BUST == True:
                print("Bad luck... Try again")
                MONEY -= BET
            if BUST == False:  
                print(f"The dealer needs to beat {PLAYER_SCORE}")
                print(f"Dealer has a {DEALER_HAND[0]} and {DEALER_HAND[1]}")
                dealerMove()
                winner()
        if MONEY == 0:
            print("Looks like you're broke. Better luck next time!")
            return
        print(f"You now have ${MONEY}")
        playAgain = int(input("Enter 1 to play again - Enter 0 to quit: "))
    print("------------------------------------------")
    print(f"Bye bye now - Come back soon to Chen's Casino")


testing()

