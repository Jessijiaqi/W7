import unittest
from cli1 import check_winner, Board, Game, Player

class TestGameOutcome(unittest.TestCase):
    def test_game_outcome(self):
        # Create a board where 'X' wins
        win_board_X = [
            ['X', 'X', 'X'],
            ['O', 'O', None],
            [None, None, None],
        ]
        
        # Create a board where 'O' wins
        win_board_O = [
            ['O', 'X', None],
            ['O', 'X', None],
            ['O', None, None],
        ]

        # Create a board where the game is a draw
        draw_board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]

        # Check if 'X' wins
        self.assertEqual(check_winner(win_board_X), 'X')

        # Check if 'O' wins
        self.assertEqual(check_winner(win_board_O), 'O')

        # Check if it's a draw
        self.assertEqual(check_winner(draw_board), 'draw')

if __name__ == '__main__':
    unittest.main()