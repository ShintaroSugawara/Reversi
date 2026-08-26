board = ["⬜︎"] * 64

board[27] = "⚪️"
board[28] = "⚫️"
board[35] = "⚫️"
board[36] = "⚪️"

def print_board():
    print("  1 2 3 4 5 6 7 8")
    for i in range(0, 64, 8):
        print((i // 8) + 1, "".join(board[i:i+8]))