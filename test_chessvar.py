import unittest
from ChessVar import ChessVar

class TestChessVar(unittest.TestCase):

    def setUp(self):
        """Set up a new ChessVar game before each test."""
        self.game = ChessVar()

    def test_initial_state(self):
        """Test that the initial game state is 'UNFINISHED'."""
        self.assertEqual(self.game.get_game_state(), 'UNFINISHED')
    
    def test_valid_move(self):
        """Test a valid move."""
        self.assertTrue(self.game.make_move('e2', 'e4'))  # Pawn move for White

    def test_invalid_move(self):
        """Test an invalid move."""
        self.assertFalse(self.game.make_move('e2', 'e5'))  # Invalid pawn move

    def test_capture_king(self):
        """Test game ends when a king is captured."""
        self.game.make_move('e2', 'e4')  # White moves
        self.game.make_move('e7', 'e5')  # Black moves
        # Simulate capturing Black's king (assume Black's king is on e8)
        self.assertTrue(self.game.make_move('e4', 'e8'))
        self.assertEqual(self.game.get_game_state(), 'WHITE_WON')

    def test_enter_fairy_piece_valid(self):
        """Test entering a valid Falcon or Hunter."""
        # Simulate losing a piece (game logic should allow for this)
        self.assertTrue(self.game.enter_fairy_piece('Falcon', 'd1'))

    def test_enter_fairy_piece_invalid(self):
        """Test entering a Falcon or Hunter in an invalid square."""
        self.assertFalse(self.game.enter_fairy_piece('Falcon', 'z9'))  # Invalid square

    def test_game_already_won(self):
        """Test no moves are allowed after the game is won."""
        # Simulate a game where Black's king is captured
        self.game.make_move('e2', 'e4')
        self.game.make_move('e7', 'e5')
        self.game.make_move('e4', 'e8')  # White captures Black's king
        self.assertEqual(self.game.get_game_state(), 'WHITE_WON')
        # Try making a move after the game is over
        self.assertFalse(self.game.make_move('a2', 'a3'))

if __name__ == '__main__':
    unittest.main()
