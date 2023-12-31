# ( . w .) coding: utf-8 (- * - )
from random import choice  # リストなどからランダムに選ぶrandom.choiceを使用。choiceのみをimport。
from time import sleep as sl  # 動作を停止できるtime.sleepを使用。sleepのみをimport。slと省略。ホントならslなんて略してはいけない
import sys  # 一部環境でexit()が動作しなかったためこちらを使用。


def main(win_count: int):  # win_countを引数に指定、そこに0を入れて初期化。関数を始めると同時に初期化までできるのだ
    # 2つのサイコロの目を1~6でランダムに決める
    print("\n宜しいですか？では入りますよ。")
    dice1 = choice(DICE)
    dice2 = choice(DICE)

    dice_sum = dice1 + dice2

    sl(1)  # 1秒停止

    # 丁半予想フェーズ
    guess = input("丁半コマ揃いました。 丁=1/半=2 >> ")

    # 結果を表示する
    if dice_sum % 2 == 0:
        answer = "丁"
    elif dice_sum % 2 == 1:
        answer = "半"

    print("目は\033[1m{}\033[0mと\033[1m{}\033[0mで\033[1m{}\033[0mです。".format(dice1, dice2, answer))
    if guess == "1" and dice_sum % 2 == 0:  # 丁　→　出目の合計÷2 = 0
        print("\n勝ちました！")
        win_count += 1
        print(win_show(win_count))
    elif guess == "2" and dice_sum % 2 == 1:  # 半 → 出目の合計÷2 = 1
        print("\n勝ちました！")
        win_count += 1
        print(win_show(win_count))
    else:
        print("\n負けました...")
        win_count = 0
        question_end = input("終了しますか？ y/n >> ")  # 負けたときは終了するかどうか聞く
        if question_end == "y":
            sys.exit(1)
        else:
            pass

    main(win_count)  # 関数の終わりに関数を自分自身で使用。無限ループさせる方法の一つ。


def win_show(win_count):  # ここで関数を定義することで、二回書いていた処理を一回で済ませられる
    return "連勝回数は\033[31m{}\033[0m回です。".format(win_count)


print("-----------------\n--   丁半博打   --\n-----------------\n"
      "\033[32m予想や y/n の質問の回答には半角を使うことをお忘れなく。\033[0m")  # ゲームスタートを知らせる
DICE = [1, 2, 3, 4, 5, 6]  # サイコロの出目の変数

main(0)
