#Blackjack by Bananadine
'''
1.0 - Initial construciton and creation of 'Card' class and objects corresponding to all 52 cards. [1 hour]
1.1 - Introduction of initial __add__ funcition in Card class in attempt to define addition of values. [30 minutes]
1.2 - Testing of new classless varaible method for deck construction. [1 hour]
2.0 - Restructuring program to work with new deck system. [30 minutes]
2.1 - Simple blackjack game working. [1 hour]
2.2 - Harmonized variable names and cleaned up game result messgaes. [30 minutes]
2.3 - Added dealer natural blackjack check. Feature not yet fully functional as game will still proceed. [30 minutes]
2.4 - Added 'deckNumber' variable, updated game result messages, and continued working on dealer blackjack feature. [30 minutes]
2.5 - Successfully implemented dealer blackjack feature. Game complete [15 minutes]
'''
#Deck(s) & Initial Setup
deckNumber = 1
deck = deckNumber * ['Two of Spades','Two of Clubs','Two of Hearts','Two of Diamonds','Three of Spades','Three of Clubs','Three of Hearts','Three of Diamonds','Four of Spades','Four of Clubs','Four of Hearts','Four of Diamonds','Five of Spades','Five of Clubs','Five of Hearts','Five of Diamonds','Six of Spades','Six of Clubs','Six of Hearts','Six of Diamonds','Seven of Spades','Seven of Clubs','Seven of Hearts','Seven of Diamonds','Eight of Spades','Eight of Clubs','Eight of Hearts','Eight of Diamonds','Nine of Spades','Nine of Clubs','Nine of Hearts','Nine of Diamonds','Ten of Spades','Ten of Clubs','Ten of Hearts','Ten of Diamonds','Jack of Spades','Jack of Clubs','Jack of Hearts','Jack of Diamonds','Queen of Spades','Queen of Clubs','Queen of Hearts','Queen of Diamonds','King of Spades','King of Clubs','King of Hearts','King of Diamonds','Ace of Spades','Ace of Clubs','Ace of Hearts','Ace of Diamonds']
cardValue = {'Two of Spades':2,'Two of Clubs':2,'Two of Hearts':2,'Two of Diamonds':2,'Three of Spades':3,'Three of Clubs':3,'Three of Hearts':3,'Three of Diamonds':3,'Four of Spades':4,'Four of Clubs':4,'Four of Hearts':4,'Four of Diamonds':4,'Five of Spades':5,'Five of Clubs':5,'Five of Hearts':5,'Five of Diamonds':5,'Six of Spades':6,'Six of Clubs':6,'Six of Hearts':6,'Six of Diamonds':6,'Seven of Spades':7,'Seven of Clubs':7,'Seven of Hearts':7,'Seven of Diamonds':7,'Eight of Spades':8,'Eight of Clubs':8,'Eight of Hearts':8,'Eight of Diamonds':8,'Nine of Spades':9,'Nine of Clubs':9,'Nine of Hearts':9,'Nine of Diamonds':9,'Ten of Spades':10,'Ten of Clubs':10,'Ten of Hearts':10,'Ten of Diamonds':10,'Jack of Spades':10,'Jack of Clubs':10,'Jack of Hearts':10,'Jack of Diamonds':10,'Queen of Spades':10,'Queen of Clubs':10,'Queen of Hearts':10,'Queen of Diamonds':10,'King of Spades':10,'King of Clubs':10,'King of Hearts':10,'King of Diamonds':10,'Ace of Spades': 11,'Ace of Clubs': 11,'Ace of Hearts': 11,'Ace of Diamonds': 11,}
import random
random.shuffle(deck)
dealerBlackjack = False

#Dealing
def deal_card(deck):
    return deck.pop()

#Value calculation
def calculate_total(hand):
    total = sum(cardValue[card] for card in hand)
    for card in hand:
        if card == 'Ace of Spades' and total > 21:
            total -= 10
        elif card == 'Ace of Clubs'and total > 21:
            total -= 10
        elif card == 'Ace of Hearts'and total > 21:
            total -= 10
        elif card == 'Ace of Diamonds'and total > 21:
            total -= 10
    return total

#Player input
def player_turn(deck, playerHand):
    while (dealerBlackjack == False):
        playerChoice = input("Hit or stand?")
        if playerChoice == 'hit':
            playerHand.append(deal_card(deck))
            total = calculate_total(playerHand)
            print("Your hand:", playerHand, "Total:", total)
            if total > 21:
                print("You bust!")
                return False
        elif playerChoice == 'stand':
            return True

#Dealer logic
def dealer_turn(deck, dealerHand):
    while calculate_total(dealerHand) < 17:
            dealerHand.append(deal_card(deck))
    return dealerHand

#Game Loop
while True:
    playerHand = [deal_card(deck), deal_card(deck)]
    dealerHand = [deal_card(deck), deal_card(deck)]
    if calculate_total(dealerHand) == 21:
        print("Your hand:", playerHand, "Total:", calculate_total(playerHand))
        print("Dealer has blackjack. You lose")
        dealerBlackjack = True
        break
    else:
        print("Your hand:", playerHand, "Total:", calculate_total(playerHand))
        print("Dealer's hand: One unknown card and a", dealerHand[1])
        break

#Player turn
if player_turn(deck, playerHand):
       dealerHand = dealer_turn(deck, dealerHand)
       print("Dealer's hand:", dealerHand, "Total:", calculate_total(dealerHand))
       
#Determine winner
playerTotal = calculate_total(playerHand)
dealerTotal = calculate_total(dealerHand)
if dealerBlackjack == True:
    pass
elif dealerTotal > 21:
    print("Dealer busts.\nYou win!")
elif playerTotal < 21 and playerTotal > dealerTotal:
    print("You win!")
else:
    print("Dealer wins.")