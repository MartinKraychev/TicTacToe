from functions.main_functions import check_winning_combinations


def calculate_score(game):
    """
    returns points depending who is the winner, later used from the maximising and minimising player
    """
    empty_symbol = '-'
    winner = check_winning_combinations(game, empty_symbol)

    if winner:
        if winner == '0':
            return 10
        else:
            return -10
