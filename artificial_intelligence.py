from Connect_Four import player_won, update_game_state
import random


def choose_next_step(game_state, player_number):

    #initialize list for preferred moves
    possible_moves = []
    #winning_moves = []


    me = player_number
    if player_number == 1:
       other_player = 2
    else:
        other_player = 1
    #begin for loop that iterates through the columns on the grid
    for column_number in range(0, 7):
        other_player_wins = False
        main_grid = update_game_state(game_state, me, column_number)

        if player_won(main_grid) == me:
            return column_number
            #winning_moves.append(column_number)
            print main_grid
            #return random.choice(column_number)
        else:

            for possible_column in range(0, 7):
                current_grid = update_game_state(main_grid, other_player, possible_column)
                #new_game_grid = update_game_state(game_grid, 1, possible_column)

                if player_won(current_grid) == other_player:
                    other_player_wins = True
                    break
            if other_player_wins == False:
                possible_moves.append(column_number)


    return random.choice(possible_moves)



