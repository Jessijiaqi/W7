import unittest
from cli1 import Game, Player, Board

class TestPlayerTurn(unittest.TestCase):
    def test_player_turn(self):
        playerX = Player("X")  # Create a player with symbol X
        playerO = Player("O")  # Create another player with symbol O
        game = Game(playerX, playerO)  # Initialize the game with the two players

        # Set up the board as needed for your implementation
        # For example, create an empty board:
        board = Board()

        # Perform a mock move (you'll need to adjust this based on your game logic)
        row, col = 0, 0
        game._board.make_move(row, col, playerX.symbol)

        # Check if after playerX's turn, it's playerO's turn
        current_player = game.switch_player(playerX)
        self.assertEqual(current_player, playerO)

if __name__ == '__main__':
    unittest.main()