import unittest
import ivs_math as m

class TestFunctions(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(m.sum(2,3), 5)
        self.assertEqual(m.sum(0,0), 0)
        self.assertEqual(m.sum(-2,5), 3)

    def test_sub(self):
        self.assertEqual(m.sub(5,2), 3)
        self.assertEqual(m.sub(0,0), 0)
        self.assertEqual(m.sub(-2,-5), 3)

    def test_mult(self):
        self.assertEqual(m.mult(2,3), 6)
        self.assertEqual(m.mult(0,0), 0)
        self.assertEqual(m.mult(-2,5), -10)

    def test_div(self):
        self.assertEqual(m.div(6,2), 3)
        self.assertEqual(m.div(0,5), 0)
        self.assertEqual(m.div(-10,-2), 5)

    def test_fac(self):
        self.assertEqual(m.fac(5), 120)
        self.assertEqual(m.fac(0), 1)
        self.assertEqual(m.fac(1), 1)

    def test_exp(self):
        self.assertEqual(m.exp(2,3), 8)
        self.assertEqual(m.exp(0,0), 1)
        self.assertEqual(m.exp(-2,5), -32)
    def test_square_root(self):    
        self.assertEqual(m.square_root(9), 3)
        self.assertEqual(m.square_root(4), 2)
        self.assertEqual(m.square_root(1), 1)
        self.assertEqual(m.square_root(16), 4)
        self.assertEqual(m.square_root(0), 0)
        self.assertEqual(m.square_root(25), 5)
        self.assertEqual(m.square_root(100), 10)
        with self.assertRaises(ValueError):
            m.square_root(-1)
        
        


if __name__ == '__main__':
    unittest.main()