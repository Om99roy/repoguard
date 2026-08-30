import unittest
from app import calculate_total

## calculate the false test case 

class TestCalculateTotal(unittest.TestCase):
    def test_total_includes_tax(self):
       result = calculate_total(100,1,0.10)
       self.assertEqual(result, 110)


if __name__ == '__main__':
    unittest.main()