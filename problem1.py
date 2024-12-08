# Poblem 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
# input: hidden cards 
# input example: list = [1, 2, 3, 4, 5], item = 2
# output: find the card 
# output examples: index=1
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

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

# Linear Binary Search
def locate_card_linear_research(cards, query):
    for card in cards:
        if card == query:
            return cards.index(card)
    else:
        return -1

# Logarithmic Binary Search
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        before_mid = cards[mid-1]

        if mid_number == query:
            if before_mid == mid_number and (mid-1) > -1:
                hi = mid - 1
                continue
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1

evaluate_test_cases(locate_card, tests)

