import unittest

from arrays.strings.StringOperations import StringOperations


class MyTestCase(unittest.TestCase):

    def test_minParanRemoveToMakeValid(self):
      input = "nee(t(c)o)de)"
      self.assertEqual( "nee(t(c)o)de" , StringOperations.minParanRemoveToMakeValid(self,input))


if __name__ == '__main__':
    unittest.main()
