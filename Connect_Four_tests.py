from Connect_Four import update_game_state, player_won, play_connect4, choose_next_step
import numpy as np
import unittest
import Recursive_connect4

class ConnectFourTester(unittest.TestCase):

    def test_game_sate_moidification_1(self):
        #test for stacked 1 and 2
        test_grid = np.zeros((6, 7))

        actual_result = update_game_state(test_grid, 1, 5)
        actual_result = update_game_state(actual_result, 2, 5)

        expected_result = np.zeros((6, 7))
        expected_result[5, 5] = 1
        expected_result[4, 5] = 2

        print actual_result
        print expected_result

        self.assertTrue(np.all((actual_result-expected_result)==0))

    def test_game_state_modification_2(self):
        #test for winning situation by 4 in a row
        test_grid = np.zeros((6, 7))
        actual_result = update_game_state(test_grid, 1, 0)
        actual_result = update_game_state(actual_result, 1, 1)
        actual_result = update_game_state(actual_result, 1, 2)
        actual_result = update_game_state(actual_result, 1, 3)

        expected_result = np.zeros((6, 7))
        expected_result[5, [0, 1, 2, 3]] = 1

        print actual_result
        print expected_result
        self.assertTrue(np.all((actual_result - expected_result) == 0))

    def test_game_state_modification_3(self):
        test_grid = np.zeros((6, 7))
        test_grid[0, 6] = 1
        test_grid[1, 6] = 1
        test_grid[2, 6] = 1
        test_grid[3, 6] = 1
        actual_result = player_won(test_grid)
        expected_result = np.array([[1, 1, 1, 1]])
        print actual_result
        print expected_result
        self.assertTrue(np.all((actual_result - expected_result) == 0))

    def test_game_state_modification_4(self):
        player_1_steps = [1, 2, 3, 4]
        player_2_steps = [1, 2, 3, 4]

        actual_result = play_connect4(player_1_steps, player_2_steps)
        print 'deebug 1', actual_result
        expected_result = np.zeros((6, 7))
        expected_result[5, 1] = 1
        expected_result[5, 2] = 1
        expected_result[5, 3] = 1
        expected_result[5, 4] = 1
        expected_result[4, 4] = 2
        expected_result[4, 3] = 2
        expected_result[4, 2] = 2
        print 'debug 2', expected_result
        self.assertTrue(np.all((actual_result - expected_result) == 0))

        print actual_result


    def test_artifical_intelligence(self):
        player_1_steps = [1, 2, 3]
        player_2_steps = [1, 2, 3]
        print 1, 'starting a new game!'
        actual_result = play_connect4(player_1_steps, player_2_steps)
        print "result 1"
        print actual_result
        # actual_result = choose_next_step(actual_result, 1)
        actual_result = Recursive_connect4.recursive_choose_next_step(actual_result, 1, 2)
        print "result 2"
        print("artificial intelligence" , actual_result)
        expected_results = [0, 4]
        self.assertTrue(actual_result in expected_results)

    def test_artifical_intelligence_non_losing_condition(self):
        player_1_steps = [0, 1, 2]
        player_2_steps = [5, 6, 3]
        actual_result = play_connect4(player_1_steps, player_2_steps)
        actual_result = Recursive_connect4.recursive_choose_next_step(actual_result, 1, 2)[1]
        #actual result should be the winning move which is [4]
        print(actual_result)
        expected_result = [4]
        self.assertTrue(actual_result in expected_result)





if __name__ == "__main__":

    unittest.main()




#
#     test_grid_1 = np.zeros((6, 7))
#     out_grid_1 = game_state(test_grid_1, 1, 5)
#     print out_grid_1
#     out_grid_2 = game_state(out_grid_1, 2, 5)
#     print out_grid_2
#     #
#     test_grid_2a = np.zeros((6, 7))
#     test_grid_2a[5, [0, 1, 2, 3]] = 1
#     test_grid_2b = np.zeros((6, 7))
#     test_grid_2b[5, [0, 1, 2, 3]] = 2
#
#     # testing for column pattern
#     test_grid_3a = np.zeros((6, 7))
#     test_grid_3a[[0, 1, 2, 3], [0]] = 1
#     test_grid_3b = np.zeros((6, 7))
#     test_grid_3b[[0, 1, 2, 3], [0]] = 2
#     #
#     #
#     # #test for diagonals
#     test_grid_4a = np.zeros((6, 7))
#     np.fill_diagonal(test_grid_4a, 1)
#     test_grid_4a[0, 0] = 0
#     test_grid_4a[1, 1] = 0
#     test_grid_4b = np.zeros((6, 7))
#     np.fill_diagonal(test_grid_4b, 2)
#     test_grid_4b[0, 0] = 0
#     test_grid_4b[1, 1] = 0
#     d1 = np.ones((4, 4))
#     d2 = np.diag(d1)
#     d2 = np.diag(d2)
#     d3 = np.rot90(d2)
#     d2 = np.pad(d2, ((2, 0), (0, 3)), 'constant', constant_values=0)
#     print d2
#     test_grid_4a = test_grid_4a + d2
#     print test_grid_4a
#     #
#     test_grid_4b = np.zeros((6, 7))
#     #
#     #
#     d3 = np.pad(d3, ((2, 0), (0, 3)), 'constant', constant_values=0)
#     test_grid_4b = test_grid_4b + d3
#     #
#     print test_grid_2a
#     print test_grid_2b
#     print test_grid_3a
#     print test_grid_3b
#     print test_grid_4a
#     print test_grid_4b
#     #
#     player_won(test_grid_2a)
#     player_won(test_grid_2b)
#     player_won(test_grid_3a)
#     player_won(test_grid_3b)
#     player_won(test_grid_4a)
#     player_won(test_grid_4b)
#
#
# class connect4game(unittest):
#     def test1(self):
#         self.assert(test_grid_2a, 1)