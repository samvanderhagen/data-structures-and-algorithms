# Linear Search algorithm 
# input: hidden cards 
# input example: list = [1, 2, 3, 4, 5], item = 2
# output: find the card 
# output examples: index=1
from jovian.pythondsa import evaluate_test_cases

tests = []

tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 2, 0],
            'query': 7
        },
        'output': 3
})
tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
})

tests.append({
        'input': {
            'cards': [4, 2, 1, -1],
            'query': 4
        },
        'output': 0
})

tests.append({
        'input': {
            'cards': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
})

tests.append({
        'input': {
            'cards': [6],
            'query': 6
        },
        'output': 0
})

tests.append({
        'input': {
            'cards': [],
            'query': 7
        },
        'output': -1
})

tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
        },
    'output': -1
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
        },
    'output': 7
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

def locate_card(cards, query):
    for card in cards:
        if card == query:
            return cards.index(card)
    else:
        return -1
evaluate_test_cases(locate_card, tests)

