import sys
import board


def check_input(player, frame):

    global selected_place, selected_place_row, selected_place_column

    while True:

        try:
            print("【 プレイヤー", player, frame, "のターンです。 】")
            selected_place_row, selected_place_column = input("コマを置きたい位置(行と列)をスペースを開けて入力して下さい:").split()
            selected_place_row = int(selected_place_row)
            selected_place_column = int(selected_place_column)

        except ValueError:
            print("数字をスペースを開けて入力して下さい。")
            continue

        except KeyboardInterrupt:
            print("ゲームを中断します。")
            sys.exit()

        if not (1 <= selected_place_row <= 8 and 1 <= selected_place_column <= 8):
            print("行と列は1～8で入力してください。")
            continue

        selected_place = ((selected_place_row) - 1) * 8 + ((selected_place_column) - 1)

        if board.board[selected_place] != board.ENPTY:
            print("そのマスはすでに埋まっています。場所を変えて下さい。")
            continue

        break
