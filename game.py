import print_board
import player
import main

player_1_frame_list = []
player_2_frame_list = []

for j in range(64):
    if print_board.board[j] == "⚫️":
        player_1_frame_list.append(j)
    elif print_board.board[j] == "⚪️":
        player_2_frame_list.append(j)

print_board.print_board()

game_continue = True
pass_count = 0
i = 0

while "⬜︎" in print_board.board and game_continue:

    if i == 0:
        player_frame = "⚫️"
    else:
        player_frame = "⚪️"

    if main.check_can_put(player_frame) == False:
        print("プレイヤー", i + 1, player_frame, "は置ける場所がないためパスします。")
        pass_count += 1

        if pass_count == 2:
            break

        if i == 0:
            i = 1
        else:
            i = 0
        continue

    pass_count = 0

    while True:

        player.check_input(i + 1, player_frame)

        reverse_frame_list = main.check_reverse_frames(player.selected_place, player_frame)

        if not reverse_frame_list:
            print("その場所では相手のコマを裏返せません。場所を変えて下さい。")
            continue

        break

    print_board.board[player.selected_place] = player_frame

    for j in reverse_frame_list:
        print_board.board[j] = player_frame

    player_1_frame_list = []
    player_2_frame_list = []

    for j in range(64):
        if print_board.board[j] == "⚫️":
            player_1_frame_list.append(j)
        elif print_board.board[j] == "⚪️":
            player_2_frame_list.append(j)

    print_board.print_board()

    if main.check_for_matches("⚪️") == True or main.check_for_matches("⚫️") == True:
        game_continue = False
        break

    if i == 0:
        i = 1
    else:
        i = 0

main.show_results()