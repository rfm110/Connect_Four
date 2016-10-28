import random
import numpy as np
from scipy.signal import convolve2d
import random



# game_grid = np.zeros((6, 7))

def update_game_state(initial_grid, color, column_number):
    # color = 1. 2
    # column_number = 1..7
    active_column = initial_grid[:, column_number]
    zeros_within_column = active_column == 0
    nonzero_coordinates = np.nonzero(zeros_within_column)
    line_number = np.max(nonzero_coordinates)

    final_grid = initial_grid.copy()
    final_grid[line_number, column_number] = color
    print final_grid
    return  final_grid


def player_won(game_grid):
    pattern_1 = np.array([[1, 1, 1, 1]])

    pattern_2 = np.array([[1],
                          [1],
                          [1],
                          [1]])

    pattern_3 = np.array([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])

    pattern_4 = np.array([[0, 0, 0, 1],
                          [0, 0, 1, 0],
                          [0, 1, 0, 0],
                          [1, 0, 0, 0]])

    pattern_list = [pattern_1, pattern_2, pattern_3, pattern_4]

    player_1_pattern = (game_grid == 1).astype(np.int)
    player_2_pattern = (game_grid == 2).astype(np.int)

    for pattern in pattern_list:
        player_1_score = convolve2d(player_1_pattern, pattern, 'valid')
        if np.max(player_1_score) == 4:
            print 'Player 1 won!'
            return 1

        player_2_score = convolve2d(player_2_pattern, pattern, 'valid')
        if np.max(player_2_score) == 4:
            print 'Player 2 won!'
            return 2

    if np.any(game_grid==0):
        print 'Next turn'
        return 0

    else:
        print "It's a draw!"
        return -1

#define function to start game, no arguments
#number_of_players = raw_input("please enter the number of players")
def play_connect4(player1_steps=[], player2_steps=[]):
    #transfer function
    #reset game grid to contain all zeroes
    game_grid = np.zeros((6,7))

    result = 0 #initialize result of game to zero to set while loop

    player_number = 1 #this should be altered in every iteration through thw while loop

    force_end_game = False

#use while loop instead of for loop to since there is no set range, only a condition (result == 0)
    while result == 0:
    #result will only change when a player wins

        print("player %s plays now" % player_number)
        #print which player's turn it is

        print game_grid  # will recognize winning patterns

        player_turn = None



        if player1_steps and player_number == 1:
            player_turn = player1_steps.pop()
            if player1_steps == [] and player2_steps == []:
                print 'force quit flag set'
                force_end_game = True

        if player2_steps and player_number == 2:
            player_turn = player2_steps.pop()
            if player2_steps == [] and player1_steps == []:
                print 'force quit flag set'
                force_end_game = True


        if player_turn is None:
            print 'player turn demanded'
            player_turn = int(raw_input('column number - between 1 and 7 \n')) - 1
        #player picks a column and we subtract one since indexing starts at o



        game_grid = update_game_state(game_grid, player_number, player_turn)
        print 'game grid updated'
        #this function is what allows the chip to be dropped with the proper number depending on which player is playing, 1 or 2
        result = player_won(game_grid)
        print 'win determined'
        #change the value of result once someone wins to exit out of the while loop



        if force_end_game:
            print 'force quit forced'
            break

        if player_number == 1:
            player_number = 2
            #switch turns
        else:
            player_number = 1



    return game_grid


if __name__ == "__main__":
    play_connect4() #call function to start the game



# player_A = int(raw_input("Pick a position from 1 to 7, starting from the left, in which to drop your disk")) - 1
#
#
# try:
#     player = int(player_A)
# except:
#     print "your input is invalid"


# random.randint(1, 7)

#if __name__ == "__main__":
    # test_grid_1 = np.zeros((6, 7))
    # out_grid_1 = game_state(test_grid_1, 1, 5)
    # print out_grid_1
    # out_grid_2 = game_state(out_grid_1, 2, 5)
    # print out_grid_2
    #
    # test_grid_2a = np.zeros((6, 7))
    # test_grid_2a[5,[0, 1, 2, 3]]=1
    # test_grid_2b = np.zeros((6, 7))
    # test_grid_2b[5,[0, 1, 2, 3]]=2
    #
    #
    # #testing for column pattern
    # test_grid_3a = np.zeros((6, 7))
    # test_grid_3a[[0, 1, 2, 3],[0]]=1
    # test_grid_3b = np.zeros((6, 7))
    # test_grid_3b[[0, 1, 2, 3],[0]]=2
    #
    #
    # #test for diagonals
    # test_grid_4a = np.zeros((6, 7))
    # #np.fill_diagonal(test_grid_4a, 1)
    # #test_grid_4a[0,0]=0
    # #test_grid_4a[1,1]=0
    # #test_grid_4b = np.zeros((6, 7))
    # #np.fill_diagonal(test_grid_4b, 2)
    # #test_grid_4b[0,0]=0
    # #test_grid_4b[1,1]=0
    # d1 = np.ones((4, 4))
    # d2 = np.diag(d1)
    # d2 = np.diag(d2)
    # d3 = np.rot90(d2)
    # d2 = np.pad(d2, ((2,0), (0,3)), 'constant', constant_values=0)
    # print d2
    # test_grid_4a = test_grid_4a + d2
    # print test_grid_4a
    #
    # test_grid_4b = np.zeros((6, 7))
    #
    #
    # d3 = np.pad(d3, ((2,0), (0,3)), 'constant', constant_values=0)
    # test_grid_4b = test_grid_4b + d3
    #
    # print test_grid_2a
    # print test_grid_2b
    # print test_grid_3a
    # print test_grid_3b
    # print test_grid_4a
    # print test_grid_4b
    #
    # player_won(test_grid_2a)
    # player_won(test_grid_2b)
    # player_won(test_grid_3a)
    # player_won(test_grid_3b)
    # player_won(test_grid_4a)
    # player_won(test_grid_4b)
    #
