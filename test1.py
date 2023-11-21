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