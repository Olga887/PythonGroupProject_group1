import random

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))


def get_random_matrix():
    size = 10
    symbols = ['-', 'O', '1', 'X', 'H']

    matrix = [[random.choice(symbols) for _ in range(size)] for _ in range(size)]
    return matrix

def check_if_ship_killed(move_row, move_column, matrix, ship_coordinates):
    return True


def make_move(matrix, move_row, move_column, ship_coordinates):
    result = []
    #hit = matrix[move_row][move_column]
    #print(hit)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == move_row and j == move_column:
                if matrix[i][j] == '-':
                    matrix[i][j] = 'O'
                    result.append(True)
                elif matrix[i][j] == '1':
                    is_killed = check_if_ship_killed(move_row, move_column, matrix, ship_coordinates)
                    if is_killed:
                        matrix[i][j] = 'X'
                        result.append(False)
                    else:
                        matrix[i][j] = 'H'
                        result.append(False)
                elif matrix[i][j] == 'H':
                    matrix[i][j] = 'H'
                    result.append(True)
                elif matrix[i][j] == 'X':
                    matrix[i][j] = 'X'
                    result.append(True)
    result.append(matrix)
    return result


matrix = get_random_matrix()
print_matrix(matrix)
print('\n\n')
ship_coordinates = ""
result = make_move(matrix, 0, 3, ship_coordinates)
print(result[0])
print_matrix(result[1])
