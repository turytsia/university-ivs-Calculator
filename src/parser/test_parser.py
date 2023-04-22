import unittest
from ivs_parser import parse, ParserError

class TestFunctions(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(parse("2 + 2"), "4")
        self.assertEqual(parse("2 + 2.95"), "4.95")
        self.assertEqual(parse("0 + 0"), "0")
    
    def test_minus(self):
        self.assertEqual(parse("2 - 2"), "0")
        self.assertEqual(parse("2 - 3"), "-1")
        # TODO add unary -

    def test_mult(self):
        self.assertEqual(parse("2 * 4"), "8")
        self.assertEqual(parse("2 * 1"), "2")
        self.assertEqual(parse("0 * 2"), "0")

    def test_div(self):
        self.assertEqual(parse("2 / 4"), "0.5")
        self.assertRaises(ParserError, parse, "2 / 0")
        self.assertEqual(parse("0 / 2"), "0")

    def test_factorial(self):
        self.assertEqual(parse("2 !"), "2")
        self.assertEqual(parse("5 !"), "120")
        self.assertEqual(parse("0 !"), "1")
        self.assertEqual(parse("2 ! ! ! !"), "2")
        self.assertEqual(parse("5 ! !"), "6.69E+198")

    def test_pow(self):
        self.assertEqual(parse("2 ^ 2"), "4")
        self.assertEqual(parse("2 ^ 2 ^ 2"), "16")
        self.assertEqual(parse("1 ^ 0"), "1")

    def test_priority(self):
        self.assertEqual(parse("2 + 2 * 2"), "6")
        self.assertEqual(parse("2 + 2 + 2 + 2 * 2 + 2 / 2"), "11")
        self.assertEqual(parse("2 * 2 / 2 - 2"), "0")
        self.assertEqual(parse("2 ^ 2 * 2"), "8")
        self.assertEqual(parse("2 + 2 * 2 ^ 2"), "10")
        self.assertEqual(parse("2 ! ^ 2 - 2 * 2"), "0")

    def test_squareroot(self):
        self.assertEqual(parse("√ √ 16"), "2")
        self.assertEqual(parse("√ 4 + √ 4 * √ 4"), "6")
        self.assertEqual(parse("√ √ √ √ 1"), "1")
        self.assertEqual(parse("√ ( ( 2 + 2 ) * 2 - 4 ) / 2"), "1")
        self.assertEqual(parse("√ 4 ^ 2"), "4")
        self.assertEqual(parse("√ 4 ! ^ 2"), "16")
        self.assertEqual(parse("( √ 4 ) ! ^ 2"), "4")

    def test_parentheses(self):
        self.assertEqual(parse("( 2 + 2 ) * 2"), "8")
        self.assertEqual(parse("2 + ( 2 - 3 ) * 5 + ( 1 + 2 )"), "0")
        self.assertEqual(parse("2 * ( 1 + 1 ) ! ^ 2"), "8")
        self.assertEqual(parse("1 + 2 ! + ( 2 ^ ( 2 * ( 2 + 2 ) - 6 ) )"), "7")
        self.assertEqual(parse("( ( 2 + 2 ) / 2 ) / 2 + 2"), "3")
    
    def test_parentheses(self):
        self.assertEqual(parse("( 2 + 2 ) * 2"), "8")
        self.assertEqual(parse("2 + ( 2 - 3 ) * 5 + ( 1 + 2 )"), "0")
        self.assertEqual(parse("2 * ( 1 + 1 ) ! ^ 2"), "8")
        self.assertEqual(parse("1 + 2 ! + ( 2 ^ ( 2 * ( 2 + 2 ) - 6 ) )"), "7")
        self.assertEqual(parse("( ( 2 + 2 ) / 2 ) / 2 + 2"), "3")
    
    def test_mixed_easy(self):
        self.assertEqual(parse("( √ ( ( ( 2 ! ! ! + 2 ! ) * 2 ! ) / 2 ) ) ! ! !"), "2")
        
    



if __name__ == '__main__':
    unittest.main()
