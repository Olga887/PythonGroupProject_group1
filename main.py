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

def enemy_card(enemy_matrix, matrix, number_y, number_x):
    match matrix[number_y][number_x]:
        case '-':
            enemy_matrix[number_y][number_x] = 'O'
        case 'X':
            enemy_matrix[number_y][number_x] = 'X'
        case 'R':
            enemy_matrix[number_y][number_x] = 'R'
    for row in enemy_matrix:
        print(row)
    return enemy_matrix


def filling_ship_hor(matrix, number_y_first, number_x_first, number_x_second):
    if number_x_first < number_x_second:
        for number_x in range(number_x_first, number_x_second + 1):
            if not matrix[number_y_first][number_x]:
                matrix[number_y_first][number_x] = '1'
    else:
        for number_x in range(number_x_second, number_x_first + 1):
            matrix[number_y_first][number_x] = '1'
    return matrix


def filling_ship_ver(matrix, number_y_first, number_y_second, number_x_first):
    if number_y_first < number_y_second:
        for number_y in range(number_y_first, number_y_second + 1):
            matrix[number_y][number_x_first] = '1'
    else:
        for number_y in range(number_y_second, number_y_first + 1):
            matrix[number_y][number_x_first] = '1'
    return matrix



def cells_ship(matrix, number_y_first, number_x_first, number_y_second, number_x_second):
    is_correct_coord = True
    start_x = 0
    start_y = 0
    stop_y = 0
    if number_y_first | number_y_second | number_x_first | number_x_second not in range(0, 10):
        is_correct_coord = False
    else:
        if number_y_first == number_y_second:
            cells_count = abs(number_x_first - number_x_second)
            if number_y_first == 0:
                start_y = 0
                stop_y = 2
            elif number_y_first == 9:
                start_y = 8
                stop_y = 10
            else:
                start_y = number_y_first - 1
                stop_y = number_y_first + 2
            if number_x_first <= number_x_second:
                start_x = number_x_first
            else:
                start_x = number_x_second
            for i in range(start_y, stop_y):
                    for j in range(start_x, start_x + cells_count):
                        if matrix[i][j] == '1':
                            is_correct_coord = False
                        else:
                            filling_ship_hor(matrix, number_y_first, number_x_first, number_x_second)
        elif number_x_first == number_x_second:
            cells_count = abs(number_y_first - number_y_second)
            if number_x_first == 0:
                start_x = 0
                stop_x = 2
            elif number_x_first == 9:
                start_x = 8
                stop_x = 10
            else:
                start_x = number_x_first - 1
                stop_x = number_x_first + 2
            if number_y_first <= number_y_second:
                start_y = number_y_first
            else:
                start_y = number_y_second
            for i in range(start_x, stop_x):
                    for j in range(start_y, start_y + cells_count):
                        if matrix[j][i] == '1':
                            is_correct_coord = False
                        else:
                            filling_ship_ver(matrix, number_y_first, number_y_second, number_x_first)
        else:
            is_correct_coord = False
    return is_correct_coord, matrix


player1_matrix = create_matrix()
player2_matrix = create_matrix()

print("Initial matrix Player 1:")
print_matrix_with_coords(player1_matrix)

print("\nInitial matrix player 2:")
print_matrix_with_coords(player2_matrix)