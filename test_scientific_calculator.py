import unittest
import math
from scientific_calulator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):


    def setUp(self):
        self.calc = ScientificCalculator()

    def test_sin(self):
        sin_90, sin_neg_90, sin_0 = self.calc.sin(90), self.calc.sin(-90), self.calc.sin(0)
        self.assertAlmostEqual(sin_90, 1.0)
        self.assertAlmostEqual(sin_neg_90, -1.0)
        self.assertAlmostEqual(sin_0, 0.0)
        with self.assertRaises(TypeError):
            self.calc.sin("hello")

    def test_cos(self):
        cos_0, cos_neg_90, cos_90 = self.calc.cos(0), self.calc.cos(-90), self.calc.cos(90)
        self.assertAlmostEqual(cos_0, 1.0)
        self.assertAlmostEqual(cos_neg_90, 0.0)
        self.assertAlmostEqual(cos_90, 0.0)
        with self.assertRaises(TypeError):
            self.calc.cos("hello")

    def test_tan(self):
        tan_45, tan_neg_45, tan_0 = self.calc.tan(45), self.calc.tan(-45), self.calc.tan(0)
        self.assertAlmostEqual(tan_45, 1.0)
        self.assertAlmostEqual(tan_neg_45, -1.0)
        self.assertAlmostEqual(tan_0, 0.0)
        with self.assertRaises(TypeError):
            self.calc.tan("hello")

    def test_sqrt(self):
        sqrt_4, sqrt_0 = self.calc.sqrt(4), self.calc.sqrt(0)
        self.assertAlmostEqual(sqrt_4, 2.0)
        self.assertAlmostEqual(sqrt_0, 0.0)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)
        with self.assertRaises(TypeError):
            self.calc.sqrt("hello")

    def test_log(self):
        log_1 = self.calc.log(1)
        self.assertAlmostEqual(log_1, 0.0)
        with self.assertRaises(ValueError):
            self.calc.log(0)
        with self.assertRaises(ValueError):
            self.calc.log(-1)
        with self.assertRaises(TypeError):
            self.calc.log("hello")

    def test_exp(self):
        exp_0, exp_neg_1 = self.calc.exp(0), self.calc.exp(-1)
        self.assertAlmostEqual(exp_0, 1.0)
        self.assertAlmostEqual(exp_neg_1, 1 / math.e)
        with self.assertRaises(TypeError):
            self.calc.exp("hello")

if __name__ == '__main__':
    unittest.main()

