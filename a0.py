#!/usr/bin/env python2

import sys;
import random;
import copy;
import Queue;
import math;
import datetime;

def queen_attack_check(temp_board,row,col,N):
    #cannnot place a queen if a queen is already present or that position is unavilable/restricted
    if(temp_board[row][col]=='Q ' or temp_board[row][col]=='X '):
        return False;

    #to check if the placing queen is attacked by any other queen in the same row
    row_condition_check=check_row(temp_board,N,row,col)
    if row_condition_check is False:
        return False;

    #to check if the placing queen is attacked by any other queen in the same column
    column_condition_check=check_column(temp_board,N,row,col)
    if column_condition_check is False:
        return False;

    #to check if the queen is attacked from the left diagonal
    left_diagonal_condition_check=check_left_diagonal(temp_board,N,row,col)
    if left_diagonal_condition_check is False:
        return False;

    #to check if the queen is attacked from the right diagonal
    right_diagonal_condition_check=check_right_diagonal(temp_board,N,row,col)
    if right_diagonal_condition_check is False:
        return False;

    #if all the conditions are satisifed we place the queen on that block
    return True;

def check_row(temp_board,N,row,col):
    if col != 0:
        for xx in range(col-1,-1,-1):
            if (temp_board[row][xx]=='Q '):#keeping the row constant and traversing the entire column
                return False; # return false if theres a queen in the row that can attack
            else:
                continue
        return True
    else:
        return True


def check_column(temp_board,N,row,col):
    if row != 0:
        for xx in range(row-1,-1,-1):
            if(temp_board[xx][col]=='X '):
                return True
            elif(temp_board[xx][col]=='Q ') :
                return False
            else:
                continue
        return True
    else:
        return True

def check_left_diagonal(temp_board,N,row,col):
    while row-1 >= 0 and col-1 >=0:
        if(temp_board[row-1][col-1]=='X '):
            return True;
        elif (temp_board[row-1][col-1]=='Q '):
            return False;
        else:
            row= row-1;
            col= col-1;
            continue;
    return True;

def check_right_diagonal(temp_board,N,row,col):
    while row-1 >= 0 and col+1 < N:
        if(temp_board[row-1][col+1]=='X '):
            return True;
        elif(temp_board[row-1][col+1]=='Q '):
            return False;
        else:
            row=row-1;
            col=col+1;
            continue;
    return True;

#https://github.com/pjhanwar/N-Queens-with-Obstacles/blob/master/Nqueens.py
def DFS(row, column, liz_cnt, board,N):
    n = N
    l = N
    cnt = liz_cnt
    board_copy = [k[:] for k in board]
    flg = 0
    for i in range(column,n):
        cnt = liz_cnt
        board_copy = [k[:] for k in board]
        if queen_attack_check(board_copy,row,i,N):
            flg=1
            board_copy[row][i] = 'Q '
            cnt += 1

            if cnt == l:
                print_square_board(board_copy, N);
                return True

            for col in range(i + 1, n):
                if board_copy[row][col] == 'X ':
                    if DFS(row, col + 1, cnt, board_copy,N):
                        return True

            if row < n - 1:
                if DFS(row + 1, 0, cnt, board_copy,N):
                    return True

            if row == n - 1 and i == n - 1:
                return False

    if flg == 0 and row < n - 1:
        if DFS(row + 1, 0, cnt, board_copy,N):
            return True
#https://github.com/pjhanwar/N-Queens-with-Obstacles/blob/master/Nqueens.py

#function to print the square boards in proper given output format
def print_square_board(square_board,N):
    for x in range(N):
        for y in range(N):
            sys.stdout.write(square_board[x][y]);
        print ("");

def initializing_the_square_board():
    square_board = [];
    # print "Welcome to nRooks:";
    co_ordinate_list = co_ordinate_function(*sys.argv);
    #print co_ordinate_list;
    # starting the search algorithm
    N = 0;
    p_counter = 0;
    # loop to get the value of N
    for p in sys.argv:
        p_counter = p_counter + 1;
        if (p_counter == 3):
            N = int(str(p));
        elif (p_counter > 3):
            break;

    # creating the square board
    for number_of_rooks1 in range(N):
        square_board.append([]);
        for number_of_rooks2 in range(N):
            square_board[number_of_rooks1].append("_ ");

    # marking x on the prohibited square zones
    for number_of_rooks1 in range(len(co_ordinate_list)):
        square_board[co_ordinate_list[number_of_rooks1][0] - 1][co_ordinate_list[number_of_rooks1][1] - 1] = 'X ';

    #print square_board;
    return N, square_board;

def nrooks():
    N,square_board=initializing_the_square_board();

    # start placing the rooks to the left most column
    for number_of_rooks1 in range(N):

        # place the rook on this row number in the first column if the block is empty
        error_counter = 0;
        for number_of_rooks2 in range(N):
            # print square_board[number_of_rooks2][number_of_rooks1];
            if (square_board[number_of_rooks2][number_of_rooks1] == '_ '):
                # now check if that row does not have a rook on it
                status = "true";
                for number_of_rooks3 in range(N):
                    if (square_board[number_of_rooks2][number_of_rooks3] == "R "):
                        status = "false";

                # now check if that column does not have a rook on it
                for number_of_rooks3 in range(N):
                    if (square_board[number_of_rooks3][number_of_rooks1] == "R "):
                        status = "false";

                if (status == "true"):
                    square_board[number_of_rooks2][number_of_rooks1] = "R ";
                    break;
            else:
                error_counter = error_counter + 1;
        if (error_counter == N):
            print ("No solution");
            sys.exit(1);

    counter_N = 0;
    for n1 in range(N):
        for n2 in range(N):
            if (square_board[n1][n2] == 'R '):
                counter_N = counter_N + 1;
    if (counter_N < N):
        print ("No solution");
        sys.exit(1);
    else:
        print_square_board(square_board, N);
	
def co_ordinate_function(*array_of_args):
    counter=0;
    arr=[];

    for p in array_of_args:
        counter=counter+1;
        if(counter==4):
            unavailable_blanks=int(str(p));
            x=counter;
            y=x+1;
            main_counter=0;
            for xx in range(unavailable_blanks):
                #print "here"
                arr.append([]);
                arr[main_counter].append(int(array_of_args[x]));
                arr[main_counter].append(int(array_of_args[y]));
                x=x+2;
                y=y+2;
                main_counter=main_counter+1;
        elif(counter>4):
            break;
    return arr;

if(sys.argv[1]=='nrooks'):
    nrooks();

if(sys.argv[1]=='nqueens'):
    N, square_board = initializing_the_square_board();
    #print("Original board:");
    #print_square_board(square_board,N);
    #print("");
    #print("Modified Board:");

    #send the initial board
    if(DFS(0,0,0,square_board,N)):
        #do nothing
        print("");
    else:
        print("No solution");
