import random
import os


def calc_hand(hand):
    sum = 0
    non_aces = [card for card in hand if card != 'A']
    aces = [card for card in hand if card == 'A']
    for card in non_aces:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)
    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum


cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
]

random.shuffle(cards)

player = []
dealer = []

player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    player_score = calc_hand(player)
    dealer_score = calc_hand(dealer)
    print('Dealer Cards: [{}][?]'.format(dealer[0]))
    print('Your Cards: [{}] ({})'.format(']['.join(player), player_score))
    print('')
    print('What would you like to do?')
    print('[1]  Hit')
    print('[2]  Stand')
    print('')
    choice = input('Your Choice: ')
    print('')
    if choice == '1':
        player.append(cards.pop())
    elif choice == '2':
        while calc_hand(dealer) <= 16:
            dealer.append(cards.pop())
            
