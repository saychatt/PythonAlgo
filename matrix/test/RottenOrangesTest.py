import unittest

from matrix.RottenOranges import RottenOranges


class MyTestCase(unittest.TestCase):

    def test_minTimeToRot(self):
        rottenOranges = RottenOranges()

        #Use case 1
        grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
        self.assertEqual(4, rottenOranges.minTimeToRot(grid))

        #Use case 2: No fruits get rotten
        grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
        self.assertEqual(-1, rottenOranges.minTimeToRot(grid))

if __name__ == '__main__':
    unittest.main()
