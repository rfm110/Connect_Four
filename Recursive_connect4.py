import random
from Connect_Four import play_connect4, player_won, update_game_state
import numpy as np


def change_player(player):
    if player == 1:
        return 2
    else:
        return 1


def recursive_choose_next_step(game_state, me=1, turns=2):

    if turns == 0:
        return [], None

    winning_moves = []
    loosing_moves = []

    possible_moves = np.arange(0, 7, 1)
    qualifying_mask = game_state[0, :] == 0
    possible_moves = possible_moves[qualifying_mask].tolist()

    for column_number in possible_moves:
        game_state_after_move = update_game_state(game_state, me, column_number)

        if player_won(game_state_after_move) == me:
            winning_moves.append(column_number)

    if winning_moves != []:
        return winning_moves, random.choice(winning_moves)

    else:
        for column_number in possible_moves:
            game_state_after_move = update_game_state(game_state, me, column_number)
            winning_moves, random_choice = recursive_choose_next_step(game_state_after_move, me=change_player(me), turns=turns-1)

            if winning_moves != []:
                loosing_moves.append(column_number)


    if set(possible_moves) == set(loosing_moves):
        return possible_moves, random.choice(list(possible_moves))
    else:
        possible_moves = set(possible_moves)-set(loosing_moves)
        return winning_moves, random.choice(list(possible_moves))



    



