import unittest
from cli1 import Player

class TestPlayerPieceAssignment(unittest.TestCase):
    def test_player_piece_assignment(self):
        playerX = Player("X")  # Create a player with X piece
        playerO = Player("O")  # Create another player with O piece

        self.assertEqual(playerX.symbol, "X")  # Check if playerX has been assigned piece X
        self.assertEqual(playerO.symbol, "O")  # Check if playerO has been assigned piece O
        self.assertNotEqual(playerX.symbol, playerO.symbol)  # Ensure both players have unique pieces

if __name__ == '__main__':
    unittest.main()