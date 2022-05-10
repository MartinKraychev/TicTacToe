import copy

from functions.main_functions import calculate_empty_slots
from functions.mini_max_functions import calculate_score

player = 'X'
opponent = '0'


def scan_game(game):
    """
    Scans the game for the best possible move, calling recursively minimax algorithm
    """
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

    if is_maximising:
        best_value = -100

        for row in range(len(game)):
            for col in range(len(game[row])):
                if game[row][col] == '-':
                    game_copy = copy.deepcopy(game)

                    game_copy[row][col] = opponent
                    best_value = max(best_value, minimax(game_copy, depth + 1, False))

        return best_value

    else:
        best_value = 100

        for row in range(len(game)):
            for col in range(len(game[row])):
                if game[row][col] == '-':
                    game_copy = copy.deepcopy(game)
                    game_copy[row][col] = player
                    best_value = min(best_value, minimax(game_copy, depth + 1, True))

        return best_value


