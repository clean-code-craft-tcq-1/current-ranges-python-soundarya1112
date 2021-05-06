import unittest
import bms_current_ranges

class test_battery_current_ranges(unittest.TestCase):
  def test_failing_current_ranges(self):
    current_input = []
    self.assertTrue(bms_current_ranges.current_ranges(current_input) == "Invalid Input")
    
if __name__ == '__main__':
  unittest.main()
