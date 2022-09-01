import random
import numpy as np
import time

print("Game started...")

def print_board():
    board=np.array(([["","",""],
        ["","",""],
        ["","",""]]),dtype=str)

    return board

def state(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=="":
                return True



def Possilibity(board):
    l=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=="":
                l.append((i,j))

    return l


def random_place(board,player):
    selection=Possilibity(board)
    current_loc=random.choice(selection)
    board[current_loc]=player
    return board


def winning(board,player):
    for i in range(0,2-1):
        for j in range(i,2+1):
            if board[j][i]==player and board[j][i+1]==player and board[j][i+2]==player:
                print("Winning_Horizontal ",board[j][i]+"||"+board[j][i+1]+"||"+board[j][i+2])
                return True

    #Vertical Wining

    for i in range(0,2):
        for j in range(0,2-1):
            if board[j][i]==player and board[j+1][i]==player and board[j+2][i]==player:
                print("Winning Vertical ",board[j][i]+"||"+board[j+1][i]+"||"+board[j+2][i])
                return True


    for i in range(0,2):
        for j in range(0,2-1):
            if board[i][j+2]==player and board[i+1][j+2]==player and board[i+2][j+2]==player:
                print("Winning Vertical ",board[i][j+2]+"||"+board[i+1][j+2]+"||"+ board[i+2][j+2])
                return True

    #diagonal Winning

    for i in range(0,2-1):
        for j in range(0,2-1):
            if board[i][j]==player and board[i+1][j+1]==player and board[i+2][j+2]==player:
                print("Diagonal Winning ",board[i][j]+"||"+board[i+1][j+1]+"||"+ board[i+2][j+2])
                return True

    for i in range(0,2-1):
        for j in range(0,2-1):
            if board[j][i+2]==player and board[j+1][i+1]==player and board[j+2][i]==player:
                print("Diagonal Winning ",board[j][i+2]+"||"+board[j+1][i+2]+"||"+ board[j+2][i])
                return True




board=print_board()

turn=0
game=False
while not game:
    if turn==0:
        player="X"
        if state(board):
            time.sleep(2)
            random_place(board,player)

            if winning(board,player):
                game=True


    else:
        player="0"
        if state(board):
            time.sleep(2)
            g=random_place(board,player)

            if winning(board,player):
                game=True

    turn+=1
    turn=turn%2
    print(board)

