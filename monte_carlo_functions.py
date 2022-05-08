def create_initial_data(game, empty_symbol):
    """
   creates a data structure containing 0's and N's
   after every repetition we increase or decrease the value of the next possible turn
   """
    not_available_symbol = 'N'

    data = []
    for row in range(len(game)):
        data.append([0 if symbol == empty_symbol else not_available_symbol for symbol in game[row]])

    return data


def create_choices(game):
    """
    creates a list of tuples with all the possible choices the AI can make in his next turn
    """
    choices = []

    for row in range(len(game)):
        for col in range(len(game[row])):
            if game[row][col] == '-':
                choices.append(tuple([row, col]))

    return choices


def get_ai_best_choice(data):
    """
    find the best selected (max picked) choice from the data and returns the row and col indexes of it
    """
    only_numbers = [data[r][c] for r in range(len(data)) for c in range(len(data[r])) if isinstance(data[r][c], int)]
    max_number = max(only_numbers)

    for row in range(len(data)):
        if max_number in data[row]:
            for col in range(len(data[row])):
                if max_number == data[row][col]:
                    data_best_choice_row = row
                    data_best_choice_col = col
                    print(f'The AI player 0 chooses {data_best_choice_row} row and {data_best_choice_col} col')
                    print(data)
                    return data_best_choice_row, data_best_choice_col

