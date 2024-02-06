"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = 0;
    numY = 0;
    for idx in board:
        for itor in idx:
            if itor == 'X':
                numX += 1;
            if itor == 'O':
                numY += 1;
    if numX == numY:
        return 'X';
    return 'O';



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set();
    for idx in range(3):
        for itor in range(3):
            if(board[idx][itor] == None):
                possibleActions.add((idx, itor));
    return possibleActions;


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    value = player(board);
    if(action[0] > 2 or action[0] < 0 or action[1] > 2 or action[1] < 0):
        raise Exception("Invalid Move, out of bounds");
    if(board[action[0]][action[1]] != None):
        raise Exception("Invalid Move, square already taken");
    deepBoard = copy.deepcopy(board);
    deepBoard[action[0]][action[1]] = value;
    return deepBoard;


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for idx in board:
        if(len(set(idx)) == 1 and idx[0] != None):
            return idx[0];
    for idx in range(len(board)):
        if(board[0][idx] != None and board[0][idx] == board[1][idx] and board[1][idx] == board[2][idx]):
            return board[0][idx];
    if(board[1][1] != None):
        if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            return board[0][0];
        if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            return board[0][2];
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None):
        return True;
    if(None not in board[0] and None not in board[1] and None not in board[2]):
        return True;
    return False;


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerGame = winner(board);
    if(winnerGame != None):
        return 1 if winnerGame == 'X' else -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None;
    return minimaxHelper(board, float('-inf'), float('inf'), (-1, -1))[1];


def minimaxHelper(board, alpha, beta, prevMove):
    if(terminal(board)):
        return (utility(board), prevMove);
    if(player(board) == 'X'):
        return maximize(board, alpha, beta, prevMove);
    else:
        return minimize(board, alpha, beta, prevMove);


def maximize(board, alpha, beta, prevMove):
    tempMax = (float('-inf'), (-1, -1));
    for idx in actions(board):
        value = minimaxHelper(result(board, idx), alpha, beta, idx);
        if(value[0] > tempMax[0]):
            tempMax = value;
        alpha = max(alpha, tempMax[0]);
        if(beta <= alpha):
            break;
    if(prevMove[0] != -1):
        return (tempMax[0], prevMove);
    return (tempMax[0], tempMax[1]);


def minimize(board, alpha, beta, prevMove):
    tempMin = (float('inf'), (-1, -1))
    for idx in actions(board):
        value = minimaxHelper(result(board, idx), alpha, beta, idx);
        if(value[0] < tempMin[0]):
            tempMin = value;
        beta = min(beta, tempMin[0]);
        if(beta < alpha):
            break;
    if(prevMove[0] != -1):
        return (tempMin[0], prevMove);
    return (tempMin[0], tempMin[1]);