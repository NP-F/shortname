# ( . w .) coding: utf-8 (- * - )
import random as rnd  # 指定範囲の整数の乱数を生成する"random.randint"のみを使用。rndと省略。
import time as t  # "time.sleep"という処理を一定時間止める関数を使用。ただの時間停止なのでなかったとしてもゲームにはなる。tと省略。
import sys  # 一部環境でexit()が動作しなかったためこちらを使用。

TRUMP_LIST = ["\033[31mハート\033[0m", "\033[30mスペード\033[0m", "\033[30mクローバー\033[0m", "\033[31mダイヤ\033[0m"]  # マークのリスト。定数。
answer = 0  # 大きいと思うか小さいと思うかを答えるときの変数。敢えてstring型に。
win_count: int = 0  # ゲームオーバー時に出る勝利数のための変数。
# **コメント多くてごめん**
print("\033[33m _   _ _       _                       _   _\n"
      "| | | (_) __ _| |__     __ _ _ __   __| | | | _____      __\n"
      "| |_| | |/ _  |  _ \\   / _  |  _ \\ / _  | | |/ _ \\ \\ /\\ / /\n"
      "|  _  | | |_| | | | | | |_| | | | | |_| | | | (_) \\ V  V /\n"
      "|_| |_|_|\\__  |_| |_|  \\__ _|_| |_|\\__ _| |_|\\___/ \\_/\\_/\n        |___/\n"
      "\nWelcome to High and low!\033[0m\nハイ&ローにようこそ。\n")  # \を表示するために\\とする必要がある

while True:  # while_01と命名 yかn以外を入力したときに使う
    user_answer = input("ルール説明は必要ですか？ y/n >> ")
    if user_answer == "y":
        while True:  # while_02と命名
            print("ではルール説明をします。")
            while True:   # while_03と命名
                t.sleep(1.0)
                print("\n最初にトランプの山札の中から一枚カードを引きます。\nそして、もう一枚山札の中から引きます。\n"
                      "あなたは最初に引いたトランプよりもあとに引いたトランプの数字のほうが大きいか小さいか当ててください。\n"
                      "最初に引くトランプとあとに引くトランプの数が同じになることもありません。\n""\n説明は以上です。")
                question_again = input("もう一度聞きますか？ y/n >> ")
                if question_again == "y":
                    print("\nもう一度説明します。")  # これって僕の感想なんですけどもう一回聞く必要あります？説明上に残ってるからもう一回聞かなくても...
                    t.sleep(0.3)
                elif question_again == "n":
                    print("\nそれでは開始します。")
                    break  # breakくんと命名
                else:
                    pass
            break  # breakちゃんと命名
        break  # breakくんがwhile_03を止め、breakくんがwhile_02を止め、ここのbreakがwhile_01を止める
    elif user_answer == "n":  # nだったときはwhile_01を止める
        print("\nそれでは開始します。")
        break
    else:  # elseの場合はpassして、line19に帰る
        print("半角の \"y\" か \"n\" で答えてください。")

t.sleep(1.0)

while True:  # ゲームオーバーにならない限り繰り返すことができる
    base_num = rnd.randint(1, 11)  # base_numは生成した段階では1~11までしかない line49を見たら1~13にしない理由がわかる
    base_type = rnd.randint(0, 3)  # TRUMP_LIST用。0~3の4つのうちのどれかを作成
    base_num = base_num + 1  # base_numが1にならないように管理している 1が出てきたら1を足して2になるため1は出ない

    print("\n引かれたのはは\033[1m", TRUMP_LIST[base_type], "\033[0mの\033[1m", int(base_num), "\033[0mです。\nでは、もう一枚トランプを引きます。")

    after_num = rnd.randint(1, 13)
    after_type = rnd.randint(0, 3)

    if base_num == after_num:  # base_numとafter_numが同じ値の場合めんどいため、その時はafter_numを1にする。base_numは1にならないため1にする。
        after_num = 1

    print("\nさて、これは\033[1m", TRUMP_LIST[base_type], "\033[0mの\033[1m", int(base_num), "\033[0mより大きいでしょうか？小さいでしょうか？")

    while True:  # while_04と命名。1、2以外を入力したときにやり直す処理
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

    if base_num < after_num:  # あとの方が大きいとき
        if answer == "1":
            win_count += 1  # 勝利数を計算するインクリメント処理。インクリメントとは繰り返すたびに1ずつ足していくこと。
            question_continue = input("正解!続けますか？ y or type any key >> ")
            if question_continue == "y":
                print("続行します。")
            else:  # 処理が長くなるのでy以外は強制終了にする
                print("終了します。結果は\033[36m{}\033[0m勝でした。".format(win_count))
                sys.exit(1)()
        elif answer == "2":
            print("\033[31mゲームオーバー!\033[0m結果は\033[36m{}\033[0m勝でした。".format(win_count))
            sys.exit(1)()

    if after_num < base_num:  # 先のほうが大きいとき
        if answer == "1":
            print("\033[31mゲームオーバー!\033[0m結果は\033[36m", win_count, "\033[0m勝でした。")
            sys.exit(1)()
        elif answer == "2":
            win_count += 1  # line77を参照
            question_continue = input("正解!続けますか？ y or type any key >> ")
            if question_continue == "y":
                print("続行します。")
            else:  # line81を参照
                print("終了します。結果は\033[36m{}\033[0m勝でした。".format(win_count))
                sys.exit(1)()
