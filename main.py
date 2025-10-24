def create_matrix():
    return [['-' for _ in range(10)] for _ in range(10)]

player1_matrix = create_matrix()
player2_matrix = create_matrix()

print("Player 1 matrix:")
for row in player1_matrix:
    print(" ".join(row))

print("\nPlayer 2 matrix:")
for row in player2_matrix:
    print(" ".join(row))
print("Hello from Yuliya")

