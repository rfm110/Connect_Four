import random
from Connect_Four import play_connect4, player_won, update_game_state
import numpy as np


def change_player(player):
    if player == 1:
        return 2
    else:
        return 1


def recursive_choose_next_step(game_state, me=1, turns=2):

    prefix = '\t'*(2-turns)

    if turns == 0:
        return [], None
        #set termination condition for the recursive function (to avoid an infinitely running function)

    winning_moves = []
    print prefix, 'initial winning moves are %s' % winning_moves
    loosing_moves = []
    print prefix, 'initial losing moves are',  loosing_moves
    #initialize lists that collect winning moves and losing moves

    possible_moves = np.arange(0, 7, 1)
    qualifying_mask = game_state[0, :] == 0
    possible_moves = possible_moves[qualifying_mask].tolist()
    print prefix, 'possible moves with applied qualifying mask %s' % possible_moves

    #test for available columns(columns that have at least one empty space)
    #add available columns to the possible moves, convert possible_moves to list

    for column_number in possible_moves:
        #iterate through possible_moves_ ist
        game_state_after_move = update_game_state(game_state, me, column_number)
        #update game state based on the the column we're iterating through

        if player_won(game_state_after_move) == me:
            winning_moves.append(column_number)
            print prefix, "column %s" % column_number
            print prefix, 'winning moves are %s' % winning_moves
            #if the columns we're iterating produces a winning condition for the player whose turn it is (me), append
            #column number to the winning_moves list

    if winning_moves != []:
        return winning_moves, random.choice(winning_moves)
        #after collecting all possible immediate winning moves, randomly select a winning column
        #this condition is only executed when the winning_moves list is not empty

    else:

        # this condition is executed if the winning_moves list is empty

        for column_number in possible_moves:
            #iterate through column_numbers in possible_moves
            game_state_after_move = update_game_state(game_state, me, column_number)
            print prefix, 'column number:', column_number
            print prefix, "game state after the move is %s" % game_state_after_move
            #update game_state_state using the column_number from the possible moves list
            print
            winning_moves, random_choice = recursive_choose_next_step(game_state_after_move, me=change_player(me), turns=turns-1)
            print prefix, 'winning move', winning_moves
            # recursively apply function with changed player, reduce turns by one

            if winning_moves != []:
                #if winning move is not "empty"/ produces winning condition for the other player
                loosing_moves.append(column_number)
                print prefix, 'losing moves', loosing_moves
                #append the columns number to losing_moves

    possible_moves = set(possible_moves)-set(loosing_moves)
    print prefix, 'possible moves = possible - losing', possible_moves
    #subtract unfavorable losing moves from possible moves
    return winning_moves, random.choice(list(possible_moves))
    #randomly choose a a column number from the possible_moves list
    # how to distinguish if the column is chosen from random moves or from possible moves


    



