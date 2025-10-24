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


player1_matrix = create_matrix()
player2_matrix = create_matrix()

print("Initial matrix Player 1:")
print_matrix_with_coords(player1_matrix)

print("\nInitial matrix player 2:")
print_matrix_with_coords(player2_matrix)


def parse_coordinates(coord):
    if len(coord) < 2 or len(coord) > 3:
        raise ValueError("Неверный формат. Пример: B5 или J0")

    row_letter = coord[0].upper()
    col_number = coord[1:]

    if not row_letter.isalpha() or not col_number.isdigit():
        raise ValueError("Координата должна содержать букву и цифру")

    row_index = ord(row_letter) - ord('A')
    col_index = int(col_number)

    if not (0 <= row_index < 10 and 0 <= col_index < 10):
        raise ValueError("Координата вне допустимого диапазона (A–J, 0–9)")
    return row_index, col_index




def place_ship(matrix, coords):
    ship_cells = []
    for coord in coords:
        row = ord(coord[0].upper()) - ord('A')
        col = int(coord[1:])
        if not (0 <= row < 10 and 0 <= col < 10):
            return f"Координата вне поля: {coord}"
        if matrix[row][col] != '-':
            return f"Клетка уже занята: {coord}"
        ship_cells.append((row, col))

    # Размещение
    for row, col in ship_cells:
        matrix[row][col] = '1'
    return "Корабль размещён", ship_cells


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