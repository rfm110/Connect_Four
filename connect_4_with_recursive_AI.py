
from Recursive_connect4 import recursive_choose_next_step

import random
import numpy as np
from scipy.signal import convolve2d


def update_game_state(initial_grid, color, column_number):
    active_column = initial_grid[:, column_number]
    zeros_within_column = active_column == 0
    nonzero_coordinates = np.nonzero(zeros_within_column)
    line_number = np.max(nonzero_coordinates)

    final_grid = initial_grid.copy()
    final_grid[line_number, column_number] = color
    return final_grid


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
            return 1

        player_2_score = convolve2d(player_2_pattern, pattern, 'valid')
        if np.max(player_2_score) == 4:
            return 2

    if np.any(game_grid==0):
        return 0

    else:
        return -1

def play_connect4(player1_steps=[], player2_steps=[], human_player1 = True, human_player2 = True):


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



        if player1_steps != [] and player_number == 1:
            player_turn = player1_steps.pop()
            if player1_steps == [] and player2_steps == []:
                print 'force quit flag set'
                force_end_game = True
            #not manually entered moves, player can be either artificial or real

        if player2_steps != [] and player_number == 2:
            player_turn = player2_steps.pop()
            if player2_steps == [] and player1_steps == []:
                print 'force quit flag set'
                force_end_game = True


        if player_turn is None:
           # print 'player turn demanded'
            if player_number == 1:
                print 'player 1',
                if human_player1 == True:
                    print 'human player'
                    player_turn = int(raw_input('column number - between 1 and 7 \n')) - 1
                else:
                    print 'AI player'
                    player_turn = recursive_choose_next_step(game_grid, me=1, turns=2)[1]
                print 'turn chosen %s' % player_turn

            if player_number == 2:
                print 'player 2',
                if human_player2 == True:
                    print 'human player'
                    player_turn = int(raw_input('column number - between 1 and 7 \n')) - 1
                else:
                    print 'AI player'
                    player_turn = recursive_choose_next_step(game_grid, me=2, turns=2)[1]
                print 'turn chosen %s' % player_turn

        #player picks a column and we subtract one since indexing starts at o

        game_grid = update_game_state(game_grid, player_number, player_turn)
        #this function is what allows the chip to be dropped with the proper number depending on which player is playing, 1 or 2
        result = player_won(game_grid)
        if result:
            if result == -1:
                print "it's a draw"
            else:
                print 'player %s won' % result
        else:
            'continue game'

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
    print play_connect4( [0,1,2,4,5,6], human_player2=False) #call function to start the game
