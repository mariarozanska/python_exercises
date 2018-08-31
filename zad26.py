'''This exercise is Part 2 of 4 of the Tic Tac Toe exercise series.
As you may have guessed, we are trying to build up to a full tic-tac-toe board. 
Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, 
not worrying about how the moves were made.
If a game of Tic Tac Toe is represented as a list of lists, like so:
game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token in that space, 
and a 2 means that player 2 put their token in that space.
Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, 
tell me whether anyone has won, and tell me which player won, if any. 
A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. 
Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.'''

def findWinner(game_board_list):
    board_size_int = len(game_board_list)
    winner_list = [[str(i + 1)] * board_size_int for i in range(2)]
    diagr_list = []
    diagl_list = []
    for i in range(board_size_int):
        if game_board_list[i] in winner_list:
            return game_board_list[i][0]
        elif [row[i] for row in game_board_list] in winner_list:
            return game_board_list[0][i]
        diagr_list.append(game_board_list[i][i])
        diagl_list.append(game_board_list[i][-i - 1])
    if diagr_list in winner_list:
        return game_board_list[0][0]
    elif diagl_list in winner_list:
        return game_board_list[0][-1]
    return '0'


if __name__ == '__main__':
    gameBoardList = [['1', '2', '2'],
	             ['2', '2', '0'],
	             ['2', '1', '0']]
    winnerStr = findWinner(gameBoardList)
    print(winnerStr)