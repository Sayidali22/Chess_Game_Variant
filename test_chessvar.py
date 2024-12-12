import unittest
from ChessVar import ChessVar

class TestChessVar(unittest.TestCase):

    def setUp(self):
        """Set up a new ChessVar game before each test."""
        self.game = ChessVar()

    def test_initial_state(self):
        """Test that the initial game state is 'UNFINISHED'."""
        self.assertEqual(self.game.get_game_state(), 'UNFINISHED')

if __name__ == '__main__':
    unittest.main()
