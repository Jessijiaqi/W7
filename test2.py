import unittest
from cli1 import Game, Player  # Import necessary classes from cli1 file

class TestGameInitialization(unittest.TestCase):
    def test_two_human_players(self):
        playerX = Player("X")  # Create a human player
        playerO = Player("O")  # Create another human player
        game = Game(playerX, playerO)  # Initialize the game with two human players

        self.assertIsInstance(game._playerX, Player)  # Check if playerX is an instance of Player
        self.assertIsInstance(game._playerO, Player)  # Check if playerO is an instance of Player

    def test_one_human_one_bot(self):
        human_player = Player("X")  # Create a human player
        bot_player = Player("O", is_human=False)  # Create a bot player
        game = Game(human_player, bot_player)  # Initialize the game with one human and one bot player

        self.assertIsInstance(game._playerX, Player)  # Check if playerX is an instance of Player
        self.assertIsInstance(game._playerO, Player)  # Check if playerO is an instance of Player
        self.assertFalse(game._playerO.is_human)  # Check if playerO is a bot

if __name__ == '__main__':
    unittest.main()