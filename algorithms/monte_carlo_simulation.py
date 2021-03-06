import copy
import random

from functions.main_functions import check_winning_combinations
from functions.monte_carlo_functions import create_initial_data, create_choices, get_ai_best_choice


def simulation(game, empty_symbol):
    """
    Replays the current state of the game certain amount of times using random picks
    Returns the turn with highest probability to win
    """
    repeat_simulation = 5000
    choices_data = create_initial_data(game, empty_symbol)
    choices = create_choices(game)

    for rep in range(repeat_simulation):

        game_copy = copy.deepcopy(game)
        choices_copy = copy.deepcopy(choices)

        all_turns = []
        players = ['0', 'X']

        while choices_copy:

            current_player = players[0]
            turn = random.choice(choices_copy)
            row, col = turn
            game_copy[row][col] = current_player
            all_turns.append(turn)
            choices_copy.remove(turn)
            players.reverse()

            winner = check_winning_combinations(game_copy, empty_symbol)

            if winner:
                first_turn = all_turns[0]
                data_row = first_turn[0]
                data_col = first_turn[1]

                if winner == '0':
                    choices_data[data_row][data_col] += 1
                else:
                    choices_data[data_row][data_col] -= 1
                break

    ai_row_choice, ai_col_choice = get_ai_best_choice(choices_data)

    return ai_row_choice, ai_col_choice
