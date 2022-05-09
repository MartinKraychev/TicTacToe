from algorithms.mini_mix_algorithm import scan_game
from functions.main_functions import create_matrix_from_console, calculate_empty_slots, player_turn, \
    check_winning_combinations, \
    show_game
from algorithms.monte_carlo_simulation import simulation


def start_game():
    """
    Starts a game of Tic Tac Toe.
    The player is playing with X while the AI is playing with 0.The AI uses monte carlo simulation to predict his moves.
    """

    players = ['X', '0']

    winner = None
    empty_symbol = '-'

    game = create_matrix_from_console(empty_symbol)
    empty_slots = calculate_empty_slots(game)

    while empty_slots:

        current_player = players[0]
        if current_player == '0':
            # AI turn to pick

            # monte carlo simulation below
            # row, col = simulation(game, empty_symbol)

            #  minimax algorithm below
            row, col = scan_game(game)

        else:
            # real player turn to pick
            row, col = player_turn(current_player, len(game))

        if game[row][col] == empty_symbol:
            game[row][col] = current_player

            # swap the players after successful turn
            players.reverse()

            # recalculate empty slots after each successful turn
            empty_slots = calculate_empty_slots(game)

            print(show_game(game))

            winner = check_winning_combinations(game, empty_symbol)

            if winner:
                print(f'The winner is Player {winner}')
                break

        else:
            print('This slot is already taken, try again.')

    if not winner:
        print('The game finished and it is a draw!')


start_game()
