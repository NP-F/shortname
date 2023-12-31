# ( . w .) coding: utf-8 (- * - )
from random import choice
import sys


def main(win_count: int):
    dice1 = choice(DICE)
    dice2 = choice(DICE)

    dice_sum = dice1 + dice2

    guess = input("\n丁半コマ揃いました。 丁=1/半=2 >> ")

    print("目は{}と{}です。".format(dice1, dice2))
    if guess == "1" and dice_sum % 2 == 0:
        print("勝ちました！")
        win_count += 1
        print("連勝回数は\033[31m{}\033[0m回です。".format(win_count))
    elif guess == "2" and dice_sum % 2 == 1:
        print("勝ちました！")
        win_count += 1
        print("連勝回数は\033[31m{}\033[0m回です。".format(win_count))
    else:
        print("負けました...")
        win_count = 0
        question_end = input("終了しますか？ y/n >>")
        if question_end == "y":
            sys.exit(1)
        else:
            pass

    main(win_count)


print("丁半博打")
DICE = [1, 2, 3, 4, 5, 6]

main(0)
