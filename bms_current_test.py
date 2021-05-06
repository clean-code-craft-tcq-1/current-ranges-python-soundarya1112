import unittest
import bms_current_ranges

class test_empty_current_ranges(unittest.TestCase):
  def test_failing_current_ranges(self):
    current_input = []
    self.assertTrue(bms_current_ranges.check_empty_input(current_input) == "Empty_Input")
    
  def test_is_nan_current_ranges(self):
    current_valid_input = [4,3,math.nan,1]
    self.assertEqual(bms_current_ranges.check_is_nan(current_valid_input) == "Invalid Input")
    
    
if __name__ == '__main__':
  unittest.main()
