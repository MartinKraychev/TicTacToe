from functions import create_matrix_from_console, calculate_empty_slots, player_turn, check_winning_combinations, \
    print_game

players = [{'id': '1',
            'sign': 'X'},

           {'id': '2',
            'sign': '0'}]

winner = None
empty_symbol = '-'

game = create_matrix_from_console(empty_symbol)
empty_slots = calculate_empty_slots(game)

while empty_slots:

    current_player = players[0]
    row, col = player_turn(current_player, len(game))

    if game[row][col] == empty_symbol:
        game[row][col] = current_player['sign']

        # swap the players after successful turn
        players.reverse()

        # recalculate empty slots after each successful turn
        empty_slots = calculate_empty_slots(game)

        print(print_game(game))

        game_finished, winner = check_winning_combinations(game, players, empty_symbol)

        if game_finished:
            print(f'The winner is Player {winner["id"]}')
            break

    else:
        print('This slot is already taken, try again.')

if not winner:
    print('The game finished and it is a draw!')
