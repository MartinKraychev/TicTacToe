def create_matrix_from_console(empty_symbol):
    """
    Create the initial state of the game depending on user input
    """
    collection = []
    row = ensure_int_value_from_console('Enter the size of the TicTacToe: ')

    for r in range(row):
        line = list(row * empty_symbol)
        collection.append(line)

    return collection


def show_game(game):
    """
    returns the current state of the game
    """
    result = ''

    for row in range(len(game)):

        for col in range(len(game[row])):
            result += game[row][col] + ' '
        result += f'\n'

    return result


def player_turn(player, max_size):
    """
    Receives, check and returns the coordinates the player picks
    """
    turn_x = ensure_int_value_from_console(f'Player {player}, select your row: ')
    turn_y = ensure_int_value_from_console(f'Player {player}, select your column: ')

    if 0 <= turn_x < max_size and 0 <= turn_y < max_size:
        return turn_x, turn_y

    print('Out of range of the game limits, try again')
    return player_turn(player, max_size)


def calculate_empty_slots(game):
    """
    Returns the count of empty slots in the game
    """
    return sum([game[r].count('-') for r in range(len(game))])


def check_winning_combinations(game, empty_symbol):
    """
    Collects all the possible winning combinations and checks if there is a valid one
    """

    def get_columns_combinations(data):
        return list(map(list, zip(*data)))

    def get_primary_diagonal_combination(data):
        return [[data[ind][ind] for ind in range(len(data))]]

    def get_secondary_diagonal_combination(data):
        return [[data[i][len(game) - i - 1] for i in range(len(data))]]

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
            combi_set = set(combination)
            if len(combi_set) == 1:
                winning_symbol = combi_set.pop()
                winning_player = winning_symbol

                return True, winning_player

    return False, None


def ensure_int_value_from_console(message):
    """
    ensures that the player gives valid value
    """
    result = input(message)
    try:
        value = int(result)
    except ValueError:
        print('Please use integer value')
        return ensure_int_value_from_console(message)

    return value


