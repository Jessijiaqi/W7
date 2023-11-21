import unittest
from cli1 import Board, Game, Player
from logic import check_winner

class TestGameWinnerDetection(unittest.TestCase):
    def test_game_winner_detection(self):
        # Set up the game with an existing board state where there's a winner
        existing_board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['X', None, 'X'],
        ]
        game_board = Board()
        game_board._board = existing_board

        playerX = Player('X')
        playerO = Player('O')
        game = Game(playerX, playerO)

        # Set the game board for the test
        game._board = game_board
        
        # Retrieve the winner using the get_board() method
        winner = check_winner(game_board.get_board())
        
        # Define the expected winner based on the existing_board state
        expected_winner = 'X'  # Assuming 'X' is the expected winner based on the existing_board state
        
        # Assert that the winner detected matches the expected winner
        self.assertEqual(winner, expected_winner)

if __name__ == '__main__':
    unittest.main()