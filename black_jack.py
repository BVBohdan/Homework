import random

def get_deck():
    '''Возвращает лист карт'''
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'T']
    return deck


def shuffle_deck(deck):
    '''Возвращает перемешанную колоду.'''
    return random.sample(deck, len(deck))


def calculate(hand):
    '''Считает очки карт на руке. Возвращает сумму очков'''
    cards_cost = {
        '2' : 2,    'J' : 2,
        '3' : 3,    'Q' : 3,
        '4' : 4,    'K' : 4,
        '5' : 5,    'T' : 11,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        '10': 10
    }
    players_points = 0
    for h in hand:
        if h == 'T' and players_points > 10:
            players_points += 1
        else:
            players_points += cards_cost[h]
    return players_points


def want_more():
    ask = input('Need more cards?(Y/N) ').strip().lower()
    if ask == 'y':
        return True
    return False


def user_lose():
    print('You lose(')
    print(f'Your points: {calculate(players_cards)}')
    print(f'PCs points: {calculate(pc_cards)}')


def user_won():
    print('Congradulations, you won!')
    print(f'Your points: {calculate(players_cards)}')
    print(f'PCs points: {calculate(pc_cards)}')

deck = shuffle_deck(get_deck())
players_cards = []
pc_cards = []

start = True if input('Enter "start" to start a game: ') == 'start' else False

players_cards.append(random.choice(deck))
players_cards.append(random.choice(deck))


while start:
    print('\n' * 100)
    print(f'Your cards: {players_cards}')
    print(f'Your points: {calculate(players_cards)}')


    if want_more():
        players_cards.append(random.choice(deck))
        if calculate(players_cards) <= 21:
            continue
        print('\n' * 100)
        user_lose()
        break

    while calculate(pc_cards) < 15:
        pc_cards.append(random.choice(deck))

    if calculate(pc_cards) > 21:
        user_won()
        break
    elif calculate(players_cards) > calculate(pc_cards):
        user_won()
        break
    elif calculate(players_cards) == calculate(pc_cards):
        print('Draw this time)')
        print(f'Your points: {calculate(players_cards)}')
        print(f'PCs points: {calculate(pc_cards)}')
        break

    user_lose()
    break