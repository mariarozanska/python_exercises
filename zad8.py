'''Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock'''

game = 'y'
while game == 'y':
    player1 = input('Player 1 (rock/scissors/paper): ').lower()
    player2 = input('Player 2 (rock/scissors/paper): ').lower()

    if player1 == player2:
        print('The match ended in a draw.')
    elif (player1, player2) in [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]:
        print('Player 1 is a winner.')
    else:
        print('Player 2 is a winner.')

    game = input('Do you want to play again? (y/n): ').lower()