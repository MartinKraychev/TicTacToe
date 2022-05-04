def create_matrix_from_console(empty_symbol):
    collection = []
    row = int(input('Enter the size of the TicTacToe: '))

    for r in range(row):
        line = list(row * empty_symbol)
        collection.append(line)

    return collection


def print_game(game):
    result = ''

    for row in range(len(game)):

        for col in range(len(game[row])):
            result += game[row][col] + ' '
        result += f'\n'

    return result


def player_turn(player, max_size):
    turn_x = int(input(f'Player {player["id"]}, select your row: '))
    turn_y = int(input(f'Player {player["id"]}, select your column: '))

    if turn_x not in range(0, max_size) or turn_y not in range(0, max_size):
        print('Out of range of the game limits, try again')
        return player_turn(player, max_size)

    return turn_x, turn_y


def calculate_empty_slots(game):
    return sum([game[r].count('-') for r in range(len(game))])


def check_winning_combinations(game, players, empty_symbol):
    winning_combinations = []

    # adds the rows
    winning_combinations.extend(game)
    # adds the columns
    winning_combinations.extend(get_columns_combinations(game))
    # adds the diagonals
    winning_combinations.extend(get_primary_diagonal_combination(game))
    winning_combinations.extend(get_secondary_diagonal_combination(game))

    for combination in winning_combinations:
        if empty_symbol not in combination:
            if len(set(combination)) == 1:
                winning_symbol = set(combination).pop()
                winning_player = [player for player in players if player['sign'] == winning_symbol][0]

                return True, winning_player

    return False, None


def get_columns_combinations(game):
    return list(map(list, zip(*game)))


def get_primary_diagonal_combination(game):
    return [[game[ind][ind] for ind in range(len(game))]]


def get_secondary_diagonal_combination(game):
    return [[game[i][len(game) - i - 1] for i in range(len(game))]]
