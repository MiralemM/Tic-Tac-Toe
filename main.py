
table2 = "   |   |   \n___|___|___\n   |   |   \n___|___|___\n   |   |   "


def list_to_string(list_table):
    table3 = ""
    return print(table3.join(list_table))


def put_place():
    global game_over

    putt_place = {1: 1, 2: 5, 3: 9, 4: 25, 5: 29, 6: 33, 7: 49, 8: 53, 9: 57}

    list_table = list(table2)

    turns = 10
    for turn in range(1, turns):
        print(f"Turn: {turn}")
        if turn % 2 != 0:
            user1_input = int(input("Player 'X' turn. Please input a number between 1-9: "))
            if list_table[putt_place[user1_input]] != " ":
                print("That place in board is not available. You lost your turn. Pay attention next time.")
            else:
                list_table[putt_place[user1_input]] = "X"
        if turn % 2 == 0:
            user2_input = int(input("Player 'O' turn. Please input a number between 1-9: "))
            if list_table[putt_place[user2_input]] != " ":
                print("That place in board is not available. You lost your turn. Pay attention next time.")
            else:
                list_table[putt_place[user2_input]] = "O"
        new_list = list_table
        list_to_string(new_list)
        if (new_list[putt_place[1]], new_list[putt_place[2]], new_list[putt_place[3]]) == ("X", "X", "X"):
            print("Congrats")
            print("Player 'X' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[1]], new_list[putt_place[2]], new_list[putt_place[3]]) == ("O", "O", "O"):
            print("Congrats")
            print("Player 'O' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[4]], new_list[putt_place[5]], new_list[putt_place[6]]) == ("X", "X", "X"):
            print("Congrats")
            print("Player 'X' is winner!!")
            game_over = False
        elif (new_list[putt_place[4]], new_list[putt_place[5]], new_list[putt_place[6]]) == ("O", "O", "O"):
            print("Congrats")
            print("Player 'O' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[7]], new_list[putt_place[8]], new_list[putt_place[9]]) == ("X", "X", "X"):
            print("Congrats")
            print("Player 'X' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[7]], new_list[putt_place[8]], new_list[putt_place[9]]) == ("O", "O", "O"):
            print("Congrats")
            print("Player 'O' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[1]], new_list[putt_place[4]], new_list[putt_place[7]]) == ("X", "X", "X"):
            print("Congrats")
            print("Player 'X' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[1]], new_list[putt_place[4]], new_list[putt_place[7]]) == ("O", "O", "O"):
            print("Congrats")
            print("Player 'O' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[2]], new_list[putt_place[5]], new_list[putt_place[8]]) == ("X", "X", "X"):
            print("Congrats")
            print("Player 'X' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[2]], new_list[putt_place[5]], new_list[putt_place[8]]) == ("O", "O", "O"):
            print("Congrats")
            print("Player 'O' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[3]], new_list[putt_place[6]], new_list[putt_place[9]]) == ("X", "X", "X"):
            print("Congrats")
            print("Player 'X' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[3]], new_list[putt_place[6]], new_list[putt_place[9]]) == ("O", "O", "O"):
            print("Congrats")
            print("Player 'O' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[1]], new_list[putt_place[5]], new_list[putt_place[9]]) == ("X", "X", "X"):
            print("Congrats")
            print("Player 'X' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[1]], new_list[putt_place[5]], new_list[putt_place[9]]) == ("O", "O", "O"):
            print("Congrats")
            print("Player 'O' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[3]], new_list[putt_place[5]], new_list[putt_place[7]]) == ("X", "X", "X"):
            print("Congrats")
            print("Player 'X' is winner!!")
            game_over = False
            break
        elif (new_list[putt_place[3]], new_list[putt_place[5]], new_list[putt_place[7]]) == ("O", "O", "O"):
            print("Congrats")
            print("Player 'O' is winner!!")
            game_over = False
            break
        if turn == 9:
            print("Draw. Game Over!")
            game_over = False


game_over = True

while game_over:
    put_place()
