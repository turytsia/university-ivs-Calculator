import unittest
from ivs_parser import parse, ParserError, ValueTooLongError

class TestFunctions(unittest.TestCase):
    def test_general(self):
        self.assertEqual(parse(""), "")
        self.assertEqual(parse("245.34546"), "245.34546")
        self.assertRaises(ParserError, parse, "n1 + 2")
        self.assertRaises(ParserError, parse, "TEXT")
        self.assertRaises(ParserError, parse, " ")
        self.assertRaises(ParserError, parse, "\\")

    def test_plus(self):
        self.assertEqual(parse("2 + 2"), "4")
        self.assertEqual(parse("2 + 2.95"), "4.95")
        self.assertEqual(parse("0 + 0"), "0")
        self.assertRaises(ParserError, parse, "2 + + 2")
        self.assertRaises(ParserError, parse, "2 + 2 +")
    
    def test_minus(self):
        self.assertEqual(parse("- 2"), "-2")
        self.assertEqual(parse("2 - 2"), "0")
        self.assertEqual(parse("2 - 3"), "-1")
        self.assertEqual(parse("- 2 - 2"), "-4")
        self.assertEqual(parse("- - ( 2 - 2 )"), "0")
        self.assertEqual(parse("( - 2 - - 2 )"), "0")
        self.assertEqual(parse("- ( - ( - ( 2 - 2 ) - 2 ) )"), "-2")
        self.assertRaises(ParserError, parse, "-")
        self.assertRaises(ParserError, parse, "- + 2")

    def test_mult(self):
        self.assertEqual(parse("2 * 4"), "8")
        self.assertEqual(parse("2 * 1"), "2")
        self.assertEqual(parse("0 * 2"), "0")
        self.assertEqual(parse("-5 * 2"), "-10")
        self.assertEqual(parse("2.5 * 2"), "5")
        self.assertRaises(ParserError, parse, "2 *")
        self.assertRaises(ParserError, parse, "2 * *")
        self.assertRaises(ParserError, parse, "*")

    def test_div(self):
        self.assertEqual(parse("2 / 4"), "0.5")
        self.assertEqual(parse("0 / 2"), "0")
        self.assertRaises(ParserError, parse, "2 / 0")

    def test_factorial(self):
        self.assertEqual(parse("2 !"), "2")
        self.assertEqual(parse("5 !"), "120")
        self.assertEqual(parse("0 !"), "1")
        self.assertEqual(parse("2 ! ! ! !"), "2")
        self.assertEqual(parse("5 ! !"), "6.69E+198")
        self.assertRaises(ValueTooLongError, parse, "5 ! ! !")
        self.assertRaises(ParserError, parse, "2.5 !")
        self.assertRaises(ParserError, parse, "- 1 !")
        self.assertRaises(ParserError, parse, "(2 - 3) !")
        self.assertRaises(ParserError, parse, "- (2 - 3) !")

    def test_pow(self):
        self.assertEqual(parse("2 ^ 2"), "4")
        self.assertEqual(parse("2 ^ 2 ^ 2"), "16")
        self.assertEqual(parse("1 ^ 0"), "1")
        self.assertRaises(ParserError, parse, "2 ^ - 3")
        self.assertRaises(ParserError, parse, "2 ^ 0.5")
        # self.assertRaises(ParserError, parse, "0 ^ 0")

    def test_priority(self):
        self.assertEqual(parse("2 + 2 * 2"), "6")
        self.assertEqual(parse("2 + 2 + 2 + 2 * 2 + 2 / 2"), "11")
        self.assertEqual(parse("2 * 2 / 2 - 2"), "0")
        self.assertEqual(parse("2 ^ 2 * 2"), "8")
        self.assertEqual(parse("2 + 2 * 2 ^ 2"), "10")
        self.assertEqual(parse("2 ! ^ 2 - 2 * 2"), "0")

    def test_squareroot(self):
        self.assertEqual(parse("1 √ 4"), "4")
        self.assertEqual(parse("2 √ 16"), "4")
        self.assertEqual(parse("2 √ 4 + 2 √ 4 * 2 √ 4"), "6")
        self.assertEqual(parse("2 √ ( ( 2 + 2 ) * 2 - 4 ) / 2"), "1")
        self.assertEqual(parse("2 √ 4 ^ 2"), "4")
        self.assertEqual(parse("2 √ ( 4 ! ) ^ 2"), "24.0000000003")
        self.assertEqual(parse("( 2 √ 4 ) ! ^ 2"), "4")
        self.assertRaises(ParserError, parse, "2 √ - 3")
        self.assertRaises(ParserError, parse, "2.5 √ 2")
        self.assertRaises(ParserError, parse, "√ 2")
        self.assertRaises(ParserError, parse, "√")

    def test_parentheses(self):
        self.assertEqual(parse("( 2 + 2 ) * 2"), "8")
        self.assertEqual(parse("2 + ( 2 - 3 ) * 5 + ( 1 + 2 )"), "0")
        self.assertEqual(parse("2 * ( 1 + 1 ) ! ^ 2"), "8")
        self.assertEqual(parse("1 + 2 ! + ( 2 ^ ( 2 * ( 2 + 2 ) - 6 ) )"), "7")
        self.assertEqual(parse("( ( 2 + 2 ) / 2 ) / 2 + 2"), "3")
        self.assertRaises(ParserError, parse, "( 2 + 2 * ( 2 )")
        self.assertRaises(ParserError, parse, "(")
        self.assertRaises(ParserError, parse, "()")
    
    def test_mixed(self):
        self.assertEqual(parse("( 2 √ ( ( ( 2 ! ! ! + 2 ! ) * 2 ! ) / 2 ) ) ! ! !"), "2")
        
    



if __name__ == '__main__':
    unittest.main()
