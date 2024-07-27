
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 
            'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

global playing

class Card: 
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]
        
  def __str__(self):
    return self.rank + " of " + self.suit


class Deck:

  def __init__(self):
    
    self.deck = []

    for suit in suits:
      for rank in ranks:
        created_card = Card(suit,rank)
        self.deck.append(created_card)

  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    single_card = self.deck.pop()
    return single_card
  
  def get_all_cards(self):
    return self.deck
  
  def __str__(self) -> str:
    deck_comp = ''
    for card in self.deck:
       deck_comp += '\n' + card.__str__()
    return "The deck has: " + deck_comp
  


class Hand:
  def __init__(self):
      self.cards = []
      self.value = 0
      self.aces = 0

  def add_card(self, card):
      
      self.cards.append(card)
      self.value += values[card.rank]
      if card.rank == 'Ace':
        self.aces += 1

  def adjust_for_ace(self):
      
      while self.value >  21 and self.aces:
        self.value -= 10
        self.aces -= 1



class Chips:
  def __init__(self):
      self.total = 100  # This can be set to a default value or supplied by a user input
      self.bet = 0
      
  def win_bet(self):
      self.total += self.bet
  
  def lose_bet(self):
      self.total -= self.bet

def take_bet(chips):

  while True:
    try:
      chips.bet = int(input("How many chips would you like to bet? "))

    except ValueError:
      print("Sorry, the bet must be an integer")

    else:
      if chips.bet > chips.total:
        print("Sorry, you do not have enough chips for that bet.")
      else:
        break
          
def hit(deck,hand):
  
  hand.add_card(deck.deal())
  hand.adjust_for_ace()

def hit_or_stand(deck, hand):
  global playing
  
  while True:
    x = input("Hit or Stand? Enter h or s ")
    
    if x[0].lower() == 'h':
        hit(deck,hand)
    
    elif x[0].lower() == 's':
        print("Player stands. Dealers turn")
        playing = False
    
    else:
        print("Sorry, I did not understand that. Please enter h or s only")
        continue
    break

def show_some(player,dealer):
    
  #Show only ONE of the dealers cards and show ALL of the players hand
  print('\nDealers Hand: ')
  print('First card hidden')
  print(dealer.cards[1])

  print('\nPlayers Hand: ')
  for card in player.cards:
      print(card)
    
def show_all(player,dealer):
    
    #Show all cards for dealer and player displaying final values.
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):    
    print("Player Busts")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts. Player wins!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player Tie! PUSH")

#GAME LOGIC
    
while True:

  playing = True
  print("WELCOME TO BLACKJACK")

  deck = Deck()
  deck.shuffle()

  player_hand = Hand()
  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())

  dealer_hand = Hand()
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

  #Setup CHIPS
  player_chips = Chips()
  take_bet(player_chips)

  #Show inital hand of player/dealer
  show_some(player_hand, dealer_hand)

  while playing:
    hit_or_stand(deck,player_hand)

    show_some(player_hand, dealer_hand)

    if player_hand.value > 21:
      player_busts(player_hand,dealer_hand,player_chips)
      break

  if player_hand.value <= 21:
      
    while dealer_hand.value < 17:
      hit(deck,dealer_hand)

    show_all(player_hand, dealer_hand)

    #WIN OR LOSE CONDITIONS
    if dealer_hand.value > player_hand.value:
      dealer_wins(player_hand, dealer_hand, player_chips)

    elif dealer_hand.value < player_hand.value:
      player_wins(player_hand, dealer_hand, player_chips)

    elif dealer_hand.value > 21:
      dealer_busts(player_hand, dealer_hand, player_chips)

    else:
      push(player_hand, dealer_hand,)

  print('\n Player total chips are at: {}'.format(player_chips.total))

  new_game = input("Would you like to play another hand? Please enter y or n")

  if new_game[0].lower() == 'y':
    playing = True
    continue

  else:
    print("Thank you for playing!")
    break


        