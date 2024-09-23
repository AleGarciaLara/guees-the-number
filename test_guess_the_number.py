import unittest 
from helpers import random_number
from user import user_guess
from computer import computer_guess
from unittest.mock import patch, call

class TestRandomNumber(unittest.TestCase):
  def test_random_number_in_range(self):
    result = random_number(1, 100)
    self.assertGreaterEqual(result, 1)
    self.assertLessEqual(result, 100)
    
  def test_user_guess(self):
    number = 33
    name = "Ale"
    self.assertTrue(user_guess(number, name))
    
  '''def test_computer_guess_in_range(self):
    number = 50  # Número objetivo de prueba
    guess = computer_guess(number)
    self.assertIsInstance(guess, bool) '''
  

  @patch('random.randint')
  def test_guess_correct(self, mock_randint):
    mock_randint.side_effect = [42]
        
    result = computer_guess(42)
        
    self.assertTrue(result)
    mock_randint.assert_called_once_with(1, 100)
        
    
if __name__ == '__main__':
  unittest.main()    
    
