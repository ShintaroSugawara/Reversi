import board
import player


def show_results():

    board.update_frame_list()

    player_1_count = len(board.player_1_frame_list)
    player_2_count = len(board.player_2_frame_list)

    print("プレイヤー 1 ⚫️ は", player_1_count, "個です。")
    print("プレイヤー 2 ⚪️ は", player_2_count, "個です。")

    if player_1_count > player_2_count:
        print("プレイヤー 1 ⚫️ の勝ちです！おめでとうございます！🎉")
    elif player_2_count > player_1_count:
        print("プレイヤー 2 ⚪️ の勝ちです！おめでとうございます！🎉")
    else:
        print("同じコマ数のため、引き分けです。")


def main():

    board.print_board()

    game_continue = True
    i = 0
    pass_count = 0

    while "⬜︎" in board.board and game_continue:

        if i == 0:
            player_frame = "⚫️"
        else:
            player_frame = "⚪️"

        if board.check_place(player_frame) == False:
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

            reverse_frame_list = board.check_reverse(player.selected_place, player_frame)

            if reverse_frame_list == []:
                print("そこにはコマを置けません。場所を変えて下さい。")
                continue

            break

        board.put_frame(player.selected_place, player_frame, reverse_frame_list)
        board.update_frame_list()
        board.print_board()

        if board.check_for_matches("⚪️") == True or board.check_for_matches("⚫️") == True:
            game_continue = False
            break

        if i == 0:
            i = 1
        else:
            i = 0

    show_results()


if __name__ == "__main__":
    main()