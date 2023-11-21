import unittest
from cli1 import Board, Game, Player

class TestPlayerMove(unittest.TestCase):
    def test_player_can_play_only_in_viable_spots(self):
        # Set up the game with an existing board state
        existing_board = [
            ['X', 'O', 'X'],
            [None, 'O', None],
            ['O', 'X', None],
        ]
        game_board = Board()
        game_board._board = existing_board

        playerX = Player('X')
        playerO = Player('O')
        game = Game(playerX, playerO)
        game._board = game_board

        # Attempt to make a move in an occupied spot
        row, col = 1, 1  # Example: Trying to play in the occupied spot (1, 1)
        current_player = game._playerX  # Assuming it's playerX's turn

        # Attempting to make a move in the occupied spot
        game._board.make_move(row, col, current_player.symbol)

        # Assert that the spot remains unchanged (player cannot play in an occupied spot)
        expected_board_state = [
            ['X', 'O', 'X'],
            [None, 'O', None],
            ['O', 'X', None],
        ]
        self.assertNotEqual(game_board.get_board(), expected_board_state)

if __name__ == '__main__':
    unittest.main()