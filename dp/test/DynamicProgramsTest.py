import unittest

from dp.DynamicPrograms import DynamicPrograms


class MyTestCase(unittest.TestCase):
    def test_fb(self):
        dp = DynamicPrograms()
        self.assertEqual(0, dp.fib(0))
        self.assertEqual(1, dp.fib(1))
        self.assertEqual(8, dp.fib(6))

    def test_rob_houses(self):
        dp = DynamicPrograms()
        self.assertEqual(4, dp.rob([1,1,3,3]))
        self.assertEqual(16, dp.rob([2,9,8,3,6]))

if __name__ == '__main__':
    unittest.main()
