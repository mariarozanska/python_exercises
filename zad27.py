'''This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. 
In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, 
to know whether player 1 or player 2 (or whoever is X and O won).
When a player (say player 1, who is X) wants to place an X on the screen, 
they can’t just click on a terminal. So we are going to approximate this clicking simply by asking 
the user for a coordinate of where they want to place their piece.
As a reminder, our tic tac toe game is really a list of lists. 
The game starts out with an empty game board like this:
game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3.
Then the game would print out:
game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]
And ask Player 2 for their move, printing an O in that place.
Things to note:
For this exercise, assume that player 1 (the first player to move) will always be X 
and player 2 (the second player) will always be O.
Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). 
Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
Then you can use your Python skills to figure out which row and column they want their piece to be in.
Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position 
where there already is another piece, do not allow the piece to go there.

Bonus:
For the “standard” exercise, don’t worry about “ending” the game - 
no need to keep track of how many squares are full. 
In a bonus version, keep track of how many squares are full 
and automatically stop asking for moves when there are no more valid moves.'''

def makeGameBoardList(board_size_int):
    return [['0'] * board_size_int for i in range(board_size_int)]

def printGameBoard(game_board_list):
    board_size_int = len(game_board_list)
    # icons_dict = {'0': '-', '1': 'X', '2': 'O'}
    replace_num_to_icon = lambda x: ' | '.join(x).replace('1', 'X').replace('2', 'O').replace('0', '-')
    game_board_icon_list = list(map(replace_num_to_icon, game_board_list))
    for i in range(board_size_int):
        print(' ---' * board_size_int)
        print('| ' + game_board_icon_list[i] + ' |')
    print(' ---' * board_size_int)

def doMove(game_board_list, player_int):
    row_int, col_int = map(int, input('Player %i: row, col ' % player_int).split(','))
    while game_board_list[row_int - 1][col_int - 1] != '0':
        print('There already is another piece.')
        row_int, col_int = map(int, input('Player %i: row, col ' % player_int).split(','))        
    game_board_list[row_int - 1][col_int - 1] = str(player_int)

def setNextPlayer(current_player_int):
    if current_player_int == 1:
        return 2
    else:
        return 1
    
if __name__ == '__main__':
    boardSizeInt = 3
    gameBoardList = makeGameBoardList(boardSizeInt)
    playerInt = 1
    for i in range(boardSizeInt**2):
        printGameBoard(gameBoardList)   
        doMove(gameBoardList, playerInt)
        playerInt = setNextPlayer(playerInt)
    printGameBoard(gameBoardList)
        
