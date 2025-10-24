def create_matrix():
    return [['-' for _ in range(10)] for _ in range(10)]

def print_matrix_with_coords(matrix):
    print("   " + " ".join(str(i) for i in range(10)))
    for i, row in enumerate(matrix):
        letter = chr(ord('A') + i)
        print(f"{letter}  " + " ".join(row))

player1_matrix = create_matrix()
player2_matrix = create_matrix()

print("Initial matrix Player 1:")
print_matrix_with_coords(player1_matrix)

print("\nInitial matrix player 2:")
print_matrix_with_coords(player2_matrix)


def parse_coordinates(coord):
    if len(coord) < 2 or len(coord) > 3:
        raise ValueError("Wrong format. Example: B5 or J0")

    row_letter = coord[0].upper()
    col_number = coord[1:]

    if not row_letter.isalpha() or not col_number.isdigit():
        raise ValueError("Coord should have a letter and nuber")

    row_index = ord(row_letter) - ord('A')
    col_index = int(col_number)

    if not (0 <= row_index < 10 and 0 <= col_index < 10):
        raise ValueError("Out of acceptable range (A–J, 0–9)")
    return row_index, col_index
