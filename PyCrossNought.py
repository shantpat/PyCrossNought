import random

def print_board():
    global board

    print(board[0],' || ',board[1],' || ',board[2] )
    print('===============')
    print(board[3],' || ',board[4],' || ',board[5] )
    print('===============')
    print(board[6],' || ',board[7],' || ',board[8] )
    print('')

def tie_algorithm():
    global board
    eboard = []
    for element in board:
        if element in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            eboard.append('E')
        else:
            eboard.append(element)

    r1 = [(eboard[0], 0), (eboard[1], 1), (eboard[2], 2)]
    r2 = [(eboard[3], 3), (eboard[4], 4), (eboard[5], 5)]
    r3 = [(eboard[6], 6), (eboard[7], 7), (eboard[8], 8)]
    r1.sort()
    r2.sort()
    r3.sort()

    c1 = [(eboard[0], 0), (eboard[3], 3), (eboard[6], 6)]
    c2 = [(eboard[1], 1), (eboard[4], 4), (eboard[7], 7)]
    c3 = [(eboard[2], 2), (eboard[5], 5), (eboard[8], 8)]
    c1.sort()
    c2.sort()
    c3.sort()

    d1 = [(eboard[0], 0), (eboard[4], 4), (eboard[8], 8)]
    d2 = [(eboard[2], 2), (eboard[4], 4), (eboard[6], 6)]
    d1.sort()
    d2.sort()
    if [r1[0][0], r1[1][0], r1[2][0]] == ['E', 'X', 'X']:
        board[r1[0][1]] = 'X'
        return 2

    elif [r2[0][0], r2[1][0], r2[2][0]] == ['E', 'X', 'X']:
        board[r2[0][1]] = 'X'
        return 2

    elif [r3[0][0], r3[1][0], r3[2][0]] == ['E', 'X', 'X']:
        board[r3[0][1]] = 'X'
        return 2

    elif [c1[0][0], c1[1][0], c1[2][0]] == ['E', 'X', 'X']:
        board[c1[0][1]] = 'X'
        return 2

    elif [c2[0][0], c2[1][0], c2[2][0]] == ['E', 'X', 'X']:
        board[c2[0][1]] = 'X'
        return 2

    elif [c3[0][0], c3[1][0], c3[2][0]] == ['E', 'X', 'X']:
        board[c3[0][1]] = 'X'
        return 2

    elif [d1[0][0], d1[1][0], d1[2][0]] == ['E', 'X', 'X']:
        board[d1[0][1]] = 'X'
        return 2

    elif [d2[0][0], d2[1][0], d2[2][0]] == ['E', 'X', 'X']:
        board[d2[0][1]] = 'X'
        return 2

    elif [r1[0][0], r1[1][0], r1[2][0]] == ['E', 'O', 'O']:
        board[r1[0][1]] = 'X'

    elif [r2[0][0], r2[1][0], r2[2][0]] == ['E', 'O', 'O']:
        board[r2[0][1]] = 'X'

    elif [r3[0][0], r3[1][0], r3[2][0]] == ['E', 'O', 'O']:
        board[r3[0][1]] = 'X'

    elif [c1[0][0], c1[1][0], c1[2][0]] == ['E', 'O', 'O']:
        board[c1[0][1]] = 'X'

    elif [c2[0][0], c2[1][0], c2[2][0]] == ['E', 'O', 'O']:
        board[c2[0][1]] = 'X'

    elif [c3[0][0], c3[1][0], c3[2][0]] == ['E', 'O', 'O']:
        board[c3[0][1]] = 'X'

    elif [d1[0][0], d1[1][0], d1[2][0]] == ['E', 'O', 'O']:
        board[d1[0][1]] = 'X'

    elif [d2[0][0], d2[1][0], d2[2][0]] == ['E', 'O', 'O']:
        board[d2[0][1]] = 'X'

    else:
        for i in range(9):
            if eboard[i] == 'E':
                board[i] = 'X'
                break
            else:
                return 1

    return 0

def ask_to_play():
    global board
    move = int(input())
    while True:
        if board[move - 1] == 'X' :
            print("Please enter a valid move!")
            move = int(input())

        elif board[move - 1] == 'O':
            print("Please enter a valid move!")
            move = int(input())
        else:
            break
    return move


board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

print_board()
p1_moves = []
p2_moves = []
start_game = True

if start_game:

    corners = [1,3,7,9]
    p1_move_1 = corners[random.randrange(len(corners))]
    p1_moves.append(p1_move_1)
    board[p1_move_1-1] = 'X'

    print_board()

    p2_move_1 = ask_to_play()
    board[p2_move_1-1] = 'O'

    print_board()

    if p1_move_1 == 1:

        if p2_move_1 == 2:
            p1_move_2 = 7
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2-1] = 'O'

            print_board()

            if p2_move_2 == 4:
                p1_move_3 = 9
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 4:
            p1_move_2 = 3
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 2:
                p1_move_3 = 9
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 6:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 3:
            p1_move_2 = 7
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 4:
                p1_move_3 = 9
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 7:
            p1_move_2 = 3
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 2:
                p1_move_3 = 9
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 6:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 2
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 6:
            p1_move_2 = 3
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 2:
                p1_move_3 = 7
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 4:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 2
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 8:
            p1_move_2 = 7
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 4:
                p1_move_3 = 3
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 2:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 9:
            p1_move_2 = 7
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 4:
                p1_move_3 = 3
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 5:
            p1_move_2 = 9
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 7:
                p1_move_3 = 3
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 2:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 6:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            elif p2_move_2 == 3:
                p1_move_3 = 7
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 4:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                while board.count('X') + board.count('O') < 9:
                    a = tie_algorithm()

                    if board.count('X') + board.count('O') == 9:
                        print('Tie')
                        break
                    if a == 0:
                        print_board()
                        p1_move_4 = ask_to_play()
                        board[p1_move_4 - 1] = 'O'
                        print_board()

                    elif a == 2:
                        print('X wins!')
                        break
                    else:
                        print('Tie')
                        break

    elif p1_move_1 == 3:

        if p2_move_1 == 2:
            p1_move_2 = 9
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 6:
                p1_move_3 = 7
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 6
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 6:
            p1_move_2 = 1
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 2:
                p1_move_3 = 7
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 4:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 2
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 1:
            p1_move_2 = 9
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 6:
                p1_move_3 = 7
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 6
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 9:
            p1_move_2 = 1
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 2:
                p1_move_3 = 7
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 4:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 2
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 4:
            p1_move_2 = 1
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 2:
                p1_move_3 = 9
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 6:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 2
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 7:
            p1_move_2 = 9
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 6:
                p1_move_3 = 1
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 6
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 8:
            p1_move_2 = 9
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 6:
                p1_move_3 = 1
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 2:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 6
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        else:
            while board.count('X') + board.count('O') < 9:
                a = tie_algorithm()

                if board.count('X') + board.count('O') == 9:
                    print('Tie')
                    break
                if a == 0:
                    print_board()
                    p1_move_4 = ask_to_play()
                    board[p1_move_4 - 1] = 'O'
                    print_board()

                elif a == 2:
                    print('X wins!')
                    break
                else:
                    print('Tie')
                    break

    elif p1_move_1 == 7:

        if p2_move_1 == 8:
            p1_move_2 = 1
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 4:
                p1_move_3 = 3
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 2:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 4:
            p1_move_2 = 9
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 8:
                p1_move_3 = 3
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 6:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 8
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 9:
            p1_move_2 = 1
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 4:
                p1_move_3 = 3
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 2:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 1:
            p1_move_2 = 9
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 8:
                p1_move_3 = 3
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 6:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 8
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 6:
            p1_move_2 = 9
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 8:
                p1_move_3 = 1
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 4:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 8
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 2:
            p1_move_2 = 1
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 4:
                p1_move_3 = 9
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 3:
            p1_move_2 = 1
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 4:
                p1_move_3 = 9
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 2:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 4
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        else:
            while board.count('X') + board.count('O') < 9:
                a = tie_algorithm()

                if board.count('X') + board.count('O') == 9:
                    print('Tie')
                    break
                if a == 0:
                    print_board()
                    p1_move_4 = ask_to_play()
                    board[p1_move_4 - 1] = 'O'
                    print_board()

                elif a == 2:
                    print('X wins!')
                    break
                else:
                    print('Tie')
                    break

    elif p1_move_1 == 9:

        if p2_move_1 == 8:
            p1_move_2 = 3
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 6:
                p1_move_3 = 1
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 2:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 6
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 6:
            p1_move_2 = 7
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 8:
                p1_move_3 = 1
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 4:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 8
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 7:
            p1_move_2 = 3
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 6:
                p1_move_3 = 1
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 2:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 6
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 3:
            p1_move_2 = 7
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 8:
                p1_move_3 = 1
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 4:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 4
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 8
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 4:
            p1_move_2 = 7
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 8:
                p1_move_3 = 3
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 6:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 6
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 8
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 2:
            p1_move_2 = 3
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 6:
                p1_move_3 = 7
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 8:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 8
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 6
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        elif p2_move_1 == 1:
            p1_move_2 = 3
            board[p1_move_2 - 1] = 'X'

            print_board()

            p2_move_2 = ask_to_play()
            board[p2_move_2 - 1] = 'O'

            print_board()

            if p2_move_2 == 6:
                p1_move_3 = 7
                board[p1_move_3 - 1] = 'X'

                print_board()

                p2_move_3 = ask_to_play()
                board[p2_move_3 - 1] = 'O'

                print_board()

                if p2_move_3 == 5:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                if p2_move_3 == 2:
                    p1_move_4 = 5
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

                else:
                    p1_move_4 = 2
                    board[p1_move_4 - 1] = 'X'

                    print_board()

                    print('X wins!')

            else:
                p1_move_3 = 6
                board[p1_move_3 - 1] = 'X'

                print_board()

                print("X wins!")

        else:
            while board.count('X') + board.count('O') < 9:
                a = tie_algorithm()

                if board.count('X') + board.count('O') == 9:
                    print('Tie')
                    break
                if a == 0:
                    print_board()
                    p1_move_4 = ask_to_play()
                    board[p1_move_4 - 1] = 'O'
                    print_board()

                elif a == 2:
                    print('X wins!')
                    break
                else:
                    print('Tie')
                    break








