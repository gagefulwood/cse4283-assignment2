import unittest
from bmi import classify_bmi, calculate_bmi

class TestCalculateBMI(unittest.TestCase):
    #######################
    # Calculate BMI Tests #
    #######################
    def test_known_value(self):
        self.assertAlmostEqual(calculate_bmi(5,3,125), 22.7, places=1)

    def test_zero_weight(self):
        self.assertIsNone(calculate_bmi(4,9,0))

    def test_negative_weight(self):
        self.assertIsNone(calculate_bmi(4,9,-1))

    def test_zero_height(self):
        self.assertIsNone(calculate_bmi(0,0,50))

class TestClassifyBMI(unittest.TestCase):
    ######################
    # Classify BMI Tests #
    ######################

    # Boundary 1 - 18.5 Line
    def test_just_below_18_5(self):
        self.assertEqual(classify_bmi(18.4), "Underweight")

    def test_at_18_5(self):
        self.assertEqual(classify_bmi(18.5), "Normal weight")

    def test_just_above_18_5(self):
        self.assertEqual(classify_bmi(18.6), "Normal weight")

    # Boundary 2 - 25.0 Line
    def test_just_below_25(self):
        self.assertEqual(classify_bmi(24.9), "Normal weight")
    
    def test_at_25(self):
        self.assertEqual(classify_bmi(25), "Overweight")
    
    def test_just_above_25(self):
        self.assertEqual(classify_bmi(25.1), "Overweight")

    # Boundary 3 - 30.0 Line
    def test_just_below_30(self):
        self.assertEqual(classify_bmi(29.9), "Overweight")
    def test_at_30(self):
        self.assertEqual(classify_bmi(30), "Obese")
    def test_just_above_30(self):
        self.assertEqual(classify_bmi(30.1), "Obese")

    # Invalid BMI
    def test_negative_bmi(self):
        self.assertIsNone(classify_bmi(-1))

    def test_zero_bmi(self):
        self.assertIsNone(classify_bmi(0))

if __name__ == "__main__":
    unittest.main()