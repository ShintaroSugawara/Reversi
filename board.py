BLACK = "⚫️"
WHITE = "⚪️"
EMPTY = "⬜︎"

board = [EMPTY] * 64

board[27] = WHITE
board[28] = BLACK
board[35] = BLACK
board[36] = WHITE


def print_board():
    print("  1 2 3 4 5 6 7 8")
    for i in range(0, 64, 8):
        print((i // 8) + 1, "".join(board[i:i+8]))


def check_reverse(selected_place, player_frame):

    if player_frame == BLACK:
        opponent_frame = WHITE
    else:
        opponent_frame = BLACK

    reverse_frame_list = []

    row = selected_place // 8
    column = selected_place % 8

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for row_move, column_move in directions:

        check_frame_list = []

        check_row = row + row_move
        check_column = column + column_move

        while 0 <= check_row < 8 and 0 <= check_column < 8:

            check_place = check_row * 8 + check_column

            if board[check_place] == opponent_frame:
                check_frame_list.append(check_place)

            elif board[check_place] == player_frame:
                if check_frame_list != []:
                    reverse_frame_list += check_frame_list
                break

            else:
                break

            check_row += row_move
            check_column += column_move

    return reverse_frame_list


def check_place(player_frame):

    for i in range(64):
        if board[i] == EMPTY:
            if check_reverse(i, player_frame) != []:
                return True

    return False


def put_frame(selected_place, player_frame, reverse_frame_list):

    board[selected_place] = player_frame

    for j in reverse_frame_list:
        board[j] = player_frame


def check_for_matches(player_frame):

    if player_frame not in board:
        return True

    return False
