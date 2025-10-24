def create_matrix():
    return [['-' for _ in range(10)] for _ in range(10)]

def print_matrix_with_coords(matrix):
    print("   " + " ".join(str(i) for i in range(10)))
    i = 0
    for row in matrix:
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        letter = letters[i]
        print(f"{letter}  " + " ".join(row))
        i += 1


def parse_coordinates(coord):

    row_letter = coord[0].upper()
    col_number = coord[1]

    row_index = ord(row_letter) - ord('A')
    col_index = int(col_number)

    return row_index, col_index



def check_if_ship_killed(move_row, move_column, matrix, ship_coordinates):
    intact = []
    hit = []

    for row, col in ship_coordinates:
        cell = matrix[row][col]
        if cell == '1' or cell == 'H':
            intact.append((row, col))
        elif cell == 'X':
            hit.append((row, col))

    if (move_row, move_column) in intact:
        intact.remove((move_row, move_column))
        hit.append((move_row, move_column))

    if intact:
        return False
    else:
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

# Обновление карты противника по координате
def enemy_card(matrix_1, matrix_2, number_y, number_x):
    match matrix_2[number_y][number_x]:
        case '-':
            matrix_1[number_y][number_x] = '-'
        case 'X':
            matrix_1[number_y][number_x] = 'X'
        case 'R':
            matrix_1[number_y][number_x] = 'R'
    for row in matrix_1:
        print(row)
    return matrix_1

# Горизонтальное размещение корабля
def filling_ship_hor(matrix, number_y_first, number_x_first, number_x_second):
    if number_x_first < number_x_second:
        for number_x in range(number_x_first, number_x_second + 1):
            matrix[number_y_first][number_x] = 1
    else:
        for number_x in range(number_x_second, number_x_first + 1):
            matrix[number_y_first][number_x] = 1
    return matrix

# Вертикальное размещение корабля
def filling_ship_ver(matrix, number_y_first, number_y_second, number_x_first):
    if number_y_first < number_y_second:
        for number_y in range(number_y_first, number_y_second + 1):
            matrix[number_y][number_x_first] = 1
    else:
        for number_y in range(number_y_second, number_y_first + 1):
            matrix[number_y][number_x_first] = 1
    return matrix

player1_matrix = create_matrix()
player2_matrix = create_matrix()

print("Initial matrix Player 1:")
print_matrix_with_coords(player1_matrix)

print("\nInitial matrix player 2:")
print_matrix_with_coords(player2_matrix)