import unittest
from math_quiz import random_int, random_math_operator, math_operation


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)  # Make sure the value is within the range

    def test_random_math_operator(self):
        # Test if random operator returns one of the expected values ('+', '-', or '*')
        for _ in range(1000):  # Test a large number of random values
            operator = random_math_operator()
            self.assertIn(operator, ['+', '-', '*'])  # Make sure the operator is one of the valid options

    def test_math_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (1, 10, '+', '1 + 10', 11),
            (5, 2, '-', '5 - 2', 3),
            (10, 5, '-', '10 - 5', 5),
            (5, 2, '*', '5 * 2', 10),
            (3, 4, '*', '3 * 4', 12),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # Run math operation function
            problem, answer = math_operation(num1, num2, operator)
            
            # Test that the problem is correctly formed
            self.assertEqual(problem, expected_problem)

            # Test that the result matches the expected answer
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
