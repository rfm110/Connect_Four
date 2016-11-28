import random
import numpy as np
from scipy.signal import convolve2d
import random


def update_game_state(initial_grid, color, column_number):
    # color = 1. 2
    # column_number = 1..7
    active_column = initial_grid[:, column_number]
    zeros_within_column = active_column == 0
    nonzero_coordinates = np.nonzero(zeros_within_column)
    line_number = np.max(nonzero_coordinates)

    final_grid = initial_grid.copy()
    final_grid[line_number, column_number] = color
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
            return 1

        player_2_score = convolve2d(player_2_pattern, pattern, 'valid')
        if np.max(player_2_score) == 4:
            return 2

    if np.any(game_grid==0):
        return 0

    else:
        return -1

def choose_next_step(game_state, player_number):

    """
    picks the best options for plays by the computer using artificial intelligence
    :param game_state:
    :param player_number:
    :return:
    """

    #initialize lists for preferred moves(possible moves and winning moves)
    possible_moves = []
    winning_moves = []


    me = player_number

    #set player number
    if player_number == 1:
        #"me" is player 1
       other_player = 2
        #remaining player is player 2
    else:
        other_player = 1
        #when player number is 2, make other player 1

    #begin for loop that iterates through the columns on the grid
    qualifying_column_level_1 = np.arange(0, 7, 1)
    #build vector starting at 0, ending at 7, with step size 1 (for the 7 columns)
    qualifying_mask = game_state[0, :] == 0
    #uses game state from row zero all the way to the end for columns that contains zero
    qualifying_column_level_1 = qualifying_column_level_1[qualifying_mask].tolist()
    #applies qualifying mask to qualifying_column_level_1: all columns that contain 0

    for column_number in qualifying_column_level_1:
        #begin for loop to iterate through column)number in qualifying_column_level_1
        other_player_wins = False
        #condition does not let other player win
        main_grid = update_game_state(game_state, me, column_number)
        #update main grid, using possible column numbers from qualifying_column-level_!

        if player_won(main_grid) == me:
            #if the column produces a winning condition for me, append the column number to the winning moves list
            winning_moves.append(column_number)
        else:
            qualifying_mask = main_grid[0, :] == 0
            #new qualifying mask based on the updated main grid
            qualifying_column_level_2 = np.arange(0, 7, 1)
            #build vector starting at 0, ending at 7, with step size 1 (for the 7 columns)
            qualifying_column_level_2 = qualifying_column_level_2[qualifying_mask].tolist()
            #apply qualifying mask to qualifying_column_level_2, all columns that contain zero

            for possible_column in qualifying_column_level_2:
            #for possible_column in range(0, 7):
                current_grid = update_game_state(main_grid, other_player, possible_column)
                #new game grid using with using qualifying_column_level_2

                if player_won(current_grid) == other_player:
                    #if this produces a winning condition for the other player, other_player_wins = 0, break out of loop
                    other_player_wins = True
                    break

            if other_player_wins == False:
                #if it does not produce a winning condition for the other player, append column number to possible_moves
                possible_moves.append(column_number)

    if winning_moves != []:
        return random.choice(winning_moves)
    #if winning moves is not empty, randomly pick a column number that produces a winning condition for "me"

    if winning_moves == [] and possible_moves == []:
        return random.choice(qualifying_column_level_1)
    #if winning moves is empty and possible moves is empty, randomly select a column using qualifying_column_level_1
    #which will provide a column number that is not completely full

    return random.choice(possible_moves)
    #if possible moves is not empty, randomly pick a column number from possible moves



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
                    player_turn = choose_next_step(game_grid, 1)
                print 'turn chosen %s' % player_turn

            if player_number == 2:
                print 'player 2',
                if human_player2 == True:
                    print 'human player'
                    player_turn = int(raw_input('column number - between 1 and 7 \n')) - 1
                else:
                    print 'AI player'
                    player_turn = choose_next_step(game_grid, 2)
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
    print play_connect4(human_player2=False) #call function to start the game
