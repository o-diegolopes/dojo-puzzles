import unittest
from evaluating_mathematical_expressions import mathematical_expressions as me


class TestMathematicalExpressions(unittest.TestCase):

    def test_mathematical_expressions(self):
        result = me.evaluate(expressions='3 * ( 2 + 5 )')

        self.assertEqual(result, 21)

        print(f"\n\nMathematical Expressions Evaluated. Result of expression is: {result}\n\n")


if __name__ == '__main__':
    unittest.main()
