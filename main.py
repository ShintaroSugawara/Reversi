import print_board
import player


def check_for_matches(player_X_frame):

    if player_X_frame not in print_board.board:
        return True


def check_reverse_frames(selected_place, player_frame):

    if player_frame == "⚫️":
        opponent_frame = "⚪️"
    else:
        opponent_frame = "⚫️"

    reverse_frame_list = []

    selected_row = selected_place // 8
    selected_column = selected_place % 8

    checking_frame_list = []
    for j in range(1, 8):
        row = selected_row - j
        column = selected_column

        if row < 0:
            break

        place = row * 8 + column

        if print_board.board[place] == opponent_frame:
            checking_frame_list.append(place)
        elif print_board.board[place] == player_frame:
            if checking_frame_list:
                reverse_frame_list += checking_frame_list
            break
        else:
            break

    checking_frame_list = []
    for j in range(1, 8):
        row = selected_row + j
        column = selected_column

        if row > 7:
            break

        place = row * 8 + column

        if print_board.board[place] == opponent_frame:
            checking_frame_list.append(place)
        elif print_board.board[place] == player_frame:
            if checking_frame_list:
                reverse_frame_list += checking_frame_list
            break
        else:
            break

    checking_frame_list = []
    for j in range(1, 8):
        row = selected_row
        column = selected_column - j

        if column < 0:
            break

        place = row * 8 + column

        if print_board.board[place] == opponent_frame:
            checking_frame_list.append(place)
        elif print_board.board[place] == player_frame:
            if checking_frame_list:
                reverse_frame_list += checking_frame_list
            break
        else:
            break

    checking_frame_list = []
    for j in range(1, 8):
        row = selected_row
        column = selected_column + j

        if column > 7:
            break

        place = row * 8 + column

        if print_board.board[place] == opponent_frame:
            checking_frame_list.append(place)
        elif print_board.board[place] == player_frame:
            if checking_frame_list:
                reverse_frame_list += checking_frame_list
            break
        else:
            break

    checking_frame_list = []
    for j in range(1, 8):
        row = selected_row - j
        column = selected_column - j

        if row < 0 or column < 0:
            break

        place = row * 8 + column

        if print_board.board[place] == opponent_frame:
            checking_frame_list.append(place)
        elif print_board.board[place] == player_frame:
            if checking_frame_list:
                reverse_frame_list += checking_frame_list
            break
        else:
            break

    checking_frame_list = []
    for j in range(1, 8):
        row = selected_row - j
        column = selected_column + j

        if row < 0 or column > 7:
            break

        place = row * 8 + column

        if print_board.board[place] == opponent_frame:
            checking_frame_list.append(place)
        elif print_board.board[place] == player_frame:
            if checking_frame_list:
                reverse_frame_list += checking_frame_list
            break
        else:
            break

    checking_frame_list = []
    for j in range(1, 8):
        row = selected_row + j
        column = selected_column - j

        if row > 7 or column < 0:
            break

        place = row * 8 + column

        if print_board.board[place] == opponent_frame:
            checking_frame_list.append(place)
        elif print_board.board[place] == player_frame:
            if checking_frame_list:
                reverse_frame_list += checking_frame_list
            break
        else:
            break

    checking_frame_list = []
    for j in range(1, 8):
        row = selected_row + j
        column = selected_column + j

        if row > 7 or column > 7:
            break

        place = row * 8 + column

        if print_board.board[place] == opponent_frame:
            checking_frame_list.append(place)
        elif print_board.board[place] == player_frame:
            if checking_frame_list:
                reverse_frame_list += checking_frame_list
            break
        else:
            break

    return reverse_frame_list


def check_can_put(player_frame):

    for i in range(64):
        if print_board.board[i] == "⬜︎":
            if check_reverse_frames(i, player_frame):
                return True

    return False


def show_results():

    player_1_count = print_board.board.count("⚫️")
    player_2_count = print_board.board.count("⚪️")

    print("プレイヤー 1 ⚫️ は", player_1_count, "個、プレイヤー 2 ⚪️ は", player_2_count, "個でした。")

    if player_1_count > player_2_count:
        print("プレイヤー 1 ⚫️ の勝ちです！おめでとうございます！🎉")
    elif player_2_count > player_1_count:
        print("プレイヤー 2 ⚪️ の勝ちです！おめでとうございます！🎉")
    else:
        print("両者同じコマ数のため、引き分けとなります。")