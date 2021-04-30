import unittest
import calc 

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)

    def test_sub(self):
        result = calc.sub(10,5)
        self.assertEqual(result, 5)

    def test_mult(self):
        result = calc.mult(10,5)
        self.assertEqual(result, 50)

    def test_div(self):
        result = calc.div(10,5)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()