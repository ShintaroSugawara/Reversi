board = ["⬜︎"] * 64

board[27] = "⚪️"
board[28] = "⚫️"
board[35] = "⚫️"
board[36] = "⚪️"

player_1_frame_list = []
player_2_frame_list = []


def print_board():
    print("  1 2 3 4 5 6 7 8")
    for i in range(0, 64, 8):
        print((i // 8) + 1, "".join(board[i:i+8]))


def check_reverse(selected_place, player_frame):

    if player_frame == "⚫️":
        opponent_frame = "⚪️"
    else:
        opponent_frame = "⚫️"

    reverse_frame_list = []

    check_frame_list = []
    row_end = ((selected_place // 8) + 1) * 8
    for j in range(selected_place + 1, row_end):
        if board[j] == opponent_frame:
            check_frame_list.append(j)
        elif board[j] == player_frame:
            if check_frame_list != []:
                reverse_frame_list += check_frame_list
            break
        else:
            break

    check_frame_list = []
    row_start = (selected_place // 8) * 8
    for j in range(selected_place - 1, row_start - 1, -1):
        if board[j] == opponent_frame:
            check_frame_list.append(j)
        elif board[j] == player_frame:
            if check_frame_list != []:
                reverse_frame_list += check_frame_list
            break
        else:
            break

    check_frame_list = []
    for j in range(selected_place + 8, 64, 8):
        if board[j] == opponent_frame:
            check_frame_list.append(j)
        elif board[j] == player_frame:
            if check_frame_list != []:
                reverse_frame_list += check_frame_list
            break
        else:
            break

    check_frame_list = []
    for j in range(selected_place - 8, -1, -8):
        if board[j] == opponent_frame:
            check_frame_list.append(j)
        elif board[j] == player_frame:
            if check_frame_list != []:
                reverse_frame_list += check_frame_list
            break
        else:
            break

    check_frame_list = []
    j = selected_place
    while j % 8 != 7 and j + 9 < 64:
        j += 9
        if board[j] == opponent_frame:
            check_frame_list.append(j)
        elif board[j] == player_frame:
            if check_frame_list != []:
                reverse_frame_list += check_frame_list
            break
        else:
            break

    check_frame_list = []
    j = selected_place
    while j % 8 != 0 and j - 9 >= 0:
        j -= 9
        if board[j] == opponent_frame:
            check_frame_list.append(j)
        elif board[j] == player_frame:
            if check_frame_list != []:
                reverse_frame_list += check_frame_list
            break
        else:
            break

    check_frame_list = []
    j = selected_place
    while j % 8 != 0 and j + 7 < 64:
        j += 7
        if board[j] == opponent_frame:
            check_frame_list.append(j)
        elif board[j] == player_frame:
            if check_frame_list != []:
                reverse_frame_list += check_frame_list
            break
        else:
            break

    check_frame_list = []
    j = selected_place
    while j % 8 != 7 and j - 7 >= 0:
        j -= 7
        if board[j] == opponent_frame:
            check_frame_list.append(j)
        elif board[j] == player_frame:
            if check_frame_list != []:
                reverse_frame_list += check_frame_list
            break
        else:
            break

    return reverse_frame_list


def check_place(player_frame):

    for i in range(64):
        if board[i] == "⬜︎":
            if check_reverse(i, player_frame) != []:
                return True

    return False


def put_frame(selected_place, player_frame, reverse_frame_list):

    board[selected_place] = player_frame

    for j in reverse_frame_list:
        board[j] = player_frame


def update_frame_list():

    player_1_frame_list.clear()
    player_2_frame_list.clear()

    for j in range(64):
        if board[j] == "⚫️":
            player_1_frame_list.append(j)
        elif board[j] == "⚪️":
            player_2_frame_list.append(j)


def check_for_matches(player_frame):

    if player_frame not in board:
        return True

    return False
