from random import *


def MyBoard(board):
    print(" " + " | " + " " + " | " + " ")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(" " + " | " + " " + " | " + " ")
    print("----------")

    print(" " + " | " + " " + " | " + " ")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(" " + " | " + " " + " | " + " ")
    print("----------")

    print(" " + " | " + " " + " | " + " ")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print(" " + " | " + " " + " | " + " ")


def Place_Maker(board, choice, position):
    board[position] = choice


def Player_Won(board, choice):
    return ((board[1] == choice and board[2] == choice and board[3] == choice) or
            (board[4] == choice and board[5] == choice and board[6] == choice) or
            (board[7] == choice and board[8] == choice and board[9] == choice) or
            (board[1] == choice and board[5] == choice and board[9] == choice) or
            (board[3] == choice and board[5] == choice and board[7] == choice) or
            (board[1] == choice and board[4] == choice and board[7] == choice) or
            (board[2] == choice and board[5] == choice and board[8] == choice) or
            (board[3] == choice and board[6] == choice and board[9] == choice))


def Space_Available(board, position):
    return board[position] == " "


def position_choice():
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not Space_Available(board, int(position)):
        position = input("Choose Your Next Position(1-9 starting from top)")
    return int(position)


def Full_Board_Space(board):
    for i in range(1, 10):
        if Space_Available(board, i):
            return False
    return True


def Chance_Generator():
    ticker = randint(1, 2)
    if ticker == 1:
        return 'player1'
    else:
        return 'player2'


turn = Chance_Generator()
while True:
    if turn == 'player1':
        print("Player 1 goes First: ")
        choiceP1 = str(input("Player1 Choose X or O : ").upper())
        if choiceP1 == 'X':
            choiceP2 = "O"
            print("Player1 is " + choiceP1 + " Player2 is " + choiceP2)
            break
        elif choiceP1 == 'O':
            choiceP2 = 'X'
            print("Player1 is " + choiceP1 + " Player2 is " + choiceP2)
            break
        else:
            print("You Are only suppose to choose either X or O")
            continue

    if turn == 'player2':
        print("Player 2 goes First: ")
        choiceP2 = input("Player2 Choose X or O : ").upper()
        if choiceP2 == 'X':
            choiceP1 = "O"
            print("Player2 is " + choiceP2 + " Player1 is " + choiceP1)
            break
        elif choiceP2 == 'O':
            choiceP1 = 'X'
            print("Player2 is " + choiceP2 + " Player1 is " + choiceP1)
            break
        else:
            print("You Are only suppose to choose either X or O")
            continue

while True:
    board = [" " for n in range(10)]
    while True:
        if turn == 'player1':
            MyBoard(board)
            print('Player 1')
            place = position_choice()
            Place_Maker(board, choiceP1, place)
            if Player_Won(board, choiceP1):
                MyBoard(board)
                print("\n\n*********Player 1 Has Won The Game*********\n\n")
                break
            else:
                if Full_Board_Space(board):
                    MyBoard(board)
                    print("\n\n*********The Game is a Draw*********\n\n")
                    break
                else:
                    turn = 'player2'

        if turn == 'player2':
            MyBoard(board)
            print('Player 2')
            place = position_choice()
            Place_Maker(board, choiceP2, place)
            if Player_Won(board, choiceP2):
                MyBoard(board)
                print("\n\n*********Player 2 Has Won The Game*********\n\n")
                break
            else:
                if Full_Board_Space(board):
                    MyBoard(board)
                    print("\n\n*********The Game is a Draw*********\n\n")
                    break
                else:
                    turn = 'player1'

    play_again = input("Do You want to play the game again ?").lower()
    if not play_again.startswith('y'):
        break
