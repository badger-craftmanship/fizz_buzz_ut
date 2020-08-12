import unittest
from fizz_buzz import is_fizz , is_buzz, fizzBuzzString

class IsFizzBuzz(unittest.TestCase):
  """Testing fizz buzz functionallity"""

  def test_is_3_fizz (self):
    """Is 3 a fizz number"""
    number = 3
    self.assertTrue(is_fizz(number))

  def test_is_5_fizz (self):
    """Is 5 a fizz number"""
    self.assertTrue(is_buzz(5))

  def test_is_15_fizz_buzz (self):
    """Is 15 a fizz and buzz number """
    self.assertTrue(is_fizz(15))
    self.assertTrue(is_buzz(15))

  def test_is_13_not_fizz_not_buzz(self):
    """Is 13 not fizz nor buzz a number"""
    number = 13
    self.assertFalse(is_fizz(number))
    self.assertFalse(is_buzz(number))

  def test_is_3_fizz_text(self):
    """Is 3 returning fizz text"""
    self.assertEqual("Fizz",fizzBuzzString(3))

if __name__ == '__main__':
  unittest.main()
