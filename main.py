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
