import unittest
from cli1 import Board  

class TestGameInitialization(unittest.TestCase):
    def test_empty_board(self):
        board_instance = Board()  

      
        expected_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(board_instance.get_board(), expected_board)

if __name__ == '__main__':
    unittest.main()

    import unittest
from cli1 import Game, Player  

class TestGameInitialization(unittest.TestCase):
    def test_two_human_players(self):
        playerX = Player("X") 
        playerO = Player("O")  
        game = Game(playerX, playerO)  

        self.assertIsInstance(game._playerX, Player)  
        self.assertIsInstance(game._playerO, Player)  

    def test_one_human_one_bot(self):
        human_player = Player("X")  
        bot_player = Player("O", is_human=False)  
        game = Game(human_player, bot_player)  

        self.assertIsInstance(game._playerX, Player)  
        self.assertIsInstance(game._playerO, Player)  
        self.assertFalse(game._playerO.is_human)  

if __name__ == '__main__':
    unittest.main()

    import unittest
from cli1 import Player

class TestPlayerPieceAssignment(unittest.TestCase):
    def test_player_piece_assignment(self):
        playerX = Player("X") 
        playerO = Player("O") 

        self.assertEqual(playerX.symbol, "X")  
        self.assertEqual(playerO.symbol, "O") 
        self.assertNotEqual(playerX.symbol, playerO.symbol)

if __name__ == '__main__':
    unittest.main()


    import unittest
from cli1 import Game, Player, Board

class TestPlayerTurn(unittest.TestCase):
    def test_player_turn(self):
        playerX = Player("X") 
        playerO = Player("O") 
        game = Game(playerX, playerO)  
        board = Board()
        row, col = 0, 0
        game._board.make_move(row, col, playerX.symbol)
        current_player = game.switch_player(playerX)
        self.assertEqual(current_player, playerO)

if __name__ == '__main__':
    unittest.main()


    import unittest
from cli1 import check_winner, Board, Game, Player

class TestGameOutcome(unittest.TestCase):
    def test_game_outcome(self):
        
        win_board_X = [
            ['X', 'X', 'X'],
            ['O', 'O', None],
            [None, None, None],
        ]
        
        
        win_board_O = [
            ['O', 'X', None],
            ['O', 'X', None],
            ['O', None, None],
        ]

        
        draw_board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]

       
        self.assertEqual(check_winner(win_board_X), 'X')

        
        self.assertEqual(check_winner(win_board_O), 'O')

        
        self.assertEqual(check_winner(draw_board), 'draw')

if __name__ == '__main__':
    unittest.main()

    import unittest
from cli1 import Board, Game, Player

class TestPlayerMove(unittest.TestCase):
    def test_player_can_play_only_in_viable_spots(self):
  
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

       
        row, col = 1, 1  
        current_player = game._playerX  

        
        game._board.make_move(row, col, current_player.symbol)

        
        expected_board_state = [
            ['X', 'O', 'X'],
            [None, 'O', None],
            ['O', 'X', None],
        ]
        self.assertNotEqual(game_board.get_board(), expected_board_state)

if __name__ == '__main__':
    unittest.main()

    import unittest
from cli1 import Board, Game, Player
from logic import check_winner

class TestGameWinnerDetection(unittest.TestCase):
    def test_game_winner_detection(self):
        
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

        
        game._board = game_board
        
        
        winner = check_winner(game_board.get_board())
        
        
        expected_winner = 'X'  
        
       
        self.assertEqual(winner, expected_winner)

if __name__ == '__main__':
    unittest.main()