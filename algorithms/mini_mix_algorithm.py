import copy
import json

from functions.main_functions import calculate_empty_slots
from functions.mini_max_functions import calculate_score
import operator

player = 'X'
opponent = '0'
# Saving all scenarios in dictionary to implement memoization
CACHE = {}


def scan_game(game):
    """
    Scans the game for the best possible move, calling recursively minimax algorithm.
    Using Caching to improve performance
    """
    current_state = json.dumps(game)
    # checks if the current scenario is saved in dictionary. Returns True on the second calling
    if current_state in CACHE:
        return CACHE[current_state]

    best_move = (-1, -1)
    best_value = -1

    for row in range(len(game)):
        for col in range(len(game[row])):
            if game[row][col] == '-':
                game_copy = copy.deepcopy(game)
                game_copy[row][col] = opponent
                score = minimax(game_copy, 0, False)

                if score > best_value:
                    best_value = score
                    best_move = (row, col)

    return best_move


def minimax(game, depth, is_maximising):
    """
    Recursive algorithm going through all the scenarios in the game tree and returning the optimal move,
    assuming that the opponent is also playing optimally
    """
    score = calculate_score(game)
    if score:
        return score - depth

    if calculate_empty_slots(game) == 0:
        return 0

    best_value = -1 if is_maximising else 1
    next_to_play = opponent if is_maximising else player
    comperator = operator.gt if is_maximising else operator.lt
    next_max_or_min = False if is_maximising else True
    current_state = None

    for row in range(len(game)):
        for col in range(len(game[row])):
            if game[row][col] == '-':
                game_copy = copy.deepcopy(game)
                if is_maximising:
                    current_state = json.dumps(game_copy)
                    # Keeps all the states of the game in a cache
                    if current_state not in CACHE:
                        CACHE[current_state] = 0
                game_copy[row][col] = next_to_play

                score = minimax(game_copy, depth + 1, next_max_or_min)
                if comperator(score, best_value):
                    # if the score is bigger, replaces the value of the state
                    if is_maximising:
                        CACHE[current_state] = (row, col)
                    best_value = score

    return best_value
