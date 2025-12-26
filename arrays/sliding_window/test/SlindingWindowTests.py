import unittest

from arrays.sliding_window.SlidingWindow import SlidingWindow


class MyTestCase(unittest.TestCase):

    def test_minCommonSubstring(self):

        #Input: s = "ADOBECODEBANC", t = "ABC" Output: "BANC"
        self.assertEqual("BANC", SlidingWindow.minCommonSubstring(self,"ADOBECODEBANC", "ABC"))
        # Input: s = "OUZODYXAZV", t = "XYZ" Output: "YXAZ"
        self.assertEqual("YXAZ", SlidingWindow.minCommonSubstring(self, "OUZODYXAZV", "XYZ"))

    def test_maxSlidingWindow(self):
        # nums [1,2,1,0,4,2,6]; k =3, output = [2,2,4,4,6]
        self.assertEqual([2,2,4,4,6], SlidingWindow.maxSlidingWindow(self,[1,2,1,0,4,2,6], 3))
        # nums=[9,10,9,-7,-4,-8,2,-6] k=5, output = [10,10,9,2]
        self.assertEqual([10,10,9,2], SlidingWindow.maxSlidingWindow(self, [9,10,9,-7,-4,-8,2,-6], 5))

if __name__ == '__main__':
    unittest.main()
