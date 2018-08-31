'''This exercise is Part 4 of 4 of the Tic Tac Toe exercise series.
In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:
Draw the Tic Tac Toe game board
Checking whether a game board has a winner
Handle a player move from user input
The next step is to put all these three components together to make a two-player Tic Tac Toe game!
Your challenge in this exercise is to use the functions from those previous exercises all together 
in the same program to make a two-player game that you can play with a friend. 
Here are a few things to keep in mind:
You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
If there are no more moves left, don’t ask for the next player’s move!
As a bonus, you can ask the players if they want to play again 
and keep a running tally of who won more - Player 1 or Player 2.'''

import zad26
import zad27

if __name__ == '__main__':
    winnerList = []
    while True:
        boardSizeInt = int(input('Size: '))
        gameBoardList = zad27.makeGameBoardList(boardSizeInt)
        playerInt = 1
        for i in range(boardSizeInt**2):
            zad27.printGameBoard(gameBoardList)   
            zad27.doMove(gameBoardList, playerInt)
            winnerStr = zad26.findWinner(gameBoardList)
            if winnerStr != '0':
                print('The winner is the player %s!' % winnerStr)
                winnerList.append(winnerStr)
                break
            playerInt = zad27.setNextPlayer(playerInt)
        zad27.printGameBoard(gameBoardList)

        nextGame = input('Do you want to play again (y/n)? ').lower()
        if nextGame == 'n':
            print('Player 1: %i wins.\nPlayer 2: %i wins.' % (winnerList.count('1'), winnerList.count('2')))
            break
