import unittest
import Calculator

class CalculatorTest(unittest.TestCase):
    """
    Test cases for the Calculator module.
    """

    def test_run_operation_add(self):
        """
        Test addition operation.
        """
        self.assertEqual(9, Calculator.run_operation(4, 5, '+'), "Addition test case 1 failed")
        self.assertEqual(4.5, Calculator.run_operation(2, 2.5, '+'), "Addition test case 2 failed")
    
    def test_run_operation_subtract(self):
        """
        Test subtraction operation.
        """
        self.assertEqual(3, Calculator.run_operation(8, 5, '-'), "Subtraction test case 1 failed")
        self.assertEqual(-0.5, Calculator.run_operation(2, 2.5, '-'), "Subtraction test case 2 failed")

    def test_run_operation_multiple(self):
        """
        Test multiplication operation.
        """
        self.assertEqual(9, Calculator.run_operation(3, 3, '*'), "Multiplication test case 1 failed")
        self.assertEqual(13.5, Calculator.run_operation(3, 4.5, '*'), "Multiplication test case 2 failed")

    def test_run_operation_divide(self):
        """
        Test division operation.
        """
        self.assertEqual(2, Calculator.run_operation(10, 5, '/'), "Division test case 1 failed")
        with self.assertRaises(ZeroDivisionError, msg="Division by zero test case failed"):
            Calculator.run_operation(9, 0, '/')

    def test_run_operation_invalid(self):
        """
        Test invalid operation.
        """
        with self.assertRaises(Exception, msg="Invalid operation test case failed"):
            Calculator.run_operation(9, 0, '8')

    def test_run_operation_large_numbers(self):
        """
        Test addition with large numbers.
        """
        self.assertEqual(10000000000, Calculator.run_operation(5000000000, 5000000000, '+'), "Large numbers addition test case failed")

    def test_run_operation_small_numbers(self):
        """
        Test addition with small numbers.
        """
        self.assertEqual(0.0002, Calculator.run_operation(0.0001, 0.0001, '+'), "Small numbers addition test case failed")

if __name__ == "__main__":
    unittest.main()
