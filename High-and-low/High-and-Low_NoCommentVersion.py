# ( . w .) coding: utf-8 (- * - )
import random as rnd
import time as t
import sys

TRUMP_LIST = ["\033[31mハート\033[0m", "\033[30mスペード\033[0m", "\033[30mクローバー\033[0m", "\033[31mダイヤ\033[0m"]
answer = 0 
win_count: int = 0

print("\033[33m _   _ _       _                       _   _\n"
      "| | | (_) __ _| |__     __ _ _ __   __| | | | _____      __\n"
      "| |_| | |/ _  |  _ \\   / _  |  _ \\ / _  | | |/ _ \\ \\ /\\ / /\n"
      "|  _  | | |_| | | | | | |_| | | | | |_| | | | (_) \\ V  V /\n"
      "|_| |_|_|\\__  |_| |_|  \\__ _|_| |_|\\__ _| |_|\\___/ \\_/\\_/\n        |___/\n"
      "\nWelcome to High and low!\033[0m\nハイ&ローにようこそ。\n")

while True:
    user_answer = input("ルール説明は必要ですか？ y/n >> ")
    if user_answer == "y":
        while True:
            print("ではルール説明をします。")
            while True:
                t.sleep(1.0)
                print("\n最初にトランプの山札の中から一枚カードを引きます。\nそして、もう一枚山札の中から引きます。\n"
                      "あなたは最初に引いたトランプよりもあとに引いたトランプの数字のほうが大きいか小さいか当ててください。\n"
                      "最初に引くトランプとあとに引くトランプの数が同じになることもありません。\n""\n説明は以上です。")
                question_again = input("もう一度聞きますか？ y/n >> ")
                if question_again == "y":
                    print("\nもう一度説明します。")
                    t.sleep(0.3)
                elif question_again == "n":
                    print("\nそれでは開始します。")
                    break
                else:
                    pass
            break
        break
    elif user_answer == "n":
        print("\nそれでは開始します。")
        break
    else:
        print("半角の \"y\" か \"n\" で答えてください。")

t.sleep(1.0)

while True:
    base_num = rnd.randint(1, 11)
    base_type = rnd.randint(0, 3)
    base_num = base_num + 1

    print("\n引かれたのはは\033[1m", TRUMP_LIST[base_type], "\033[0mの\033[1m", int(base_num), "\033[0mです。\nでは、もう一枚トランプを引きます。")

    after_num = rnd.randint(1, 13)
    after_type = rnd.randint(0, 3)

    if base_num == after_num:
        after_num = 1

    print("\nさて、これは\033[1m", TRUMP_LIST[base_type], "\033[0mの\033[1m", int(base_num), "\033[0mより大きいでしょうか？小さいでしょうか？")

    while True:
        answer = input("大きいと思うなら1、小さいと思うなら2を入力>> ")
        if answer == "1":
            print("\n予想が完了しました。結果は...?")
            break
        elif answer == "2":
            print("\n予想が完了しました。結果は...?")
            break
        else:
            print("半角の \"1\" か \"2\" で答えてください。")

    print("\n引かれたカードは\033[1m", TRUMP_LIST[after_type], "\033[0mの\033[1m", after_num, "\033[0mでした!")

    if base_num < after_num:
        if answer == "1":
            win_count += 1
            question_continue = input("正解!続けますか？ y or type any key >> ")
            if question_continue == "y":
                print("続行します。")
            else:
                print("終了します。結果は\033[36m{}\033[0m勝でした。".format(win_count))
                sys.exit(1)
        elif answer == "2":
            print("\033[31mゲームオーバー!\033[0m結果は\033[36m{}\033[0m勝でした。".format(win_count))
            sys.exit(1)

    if after_num < base_num:
        if answer == "1":
            print("\033[31mゲームオーバー!\033[0m結果は\033[36m", win_count, "\033[0m勝でした。")
            sys.exit(1)
        elif answer == "2":
            win_count += 1
            question_continue = input("正解!続けますか？ y or type any key >> ")
            if question_continue == "y":
                print("続行します。")
            else:
                print("終了します。結果は\033[36m{}\033[0m勝でした。".format(win_count))
                sys.exit(1)
