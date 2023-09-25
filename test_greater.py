import unittest

def check(x):

    return x >= 100

class test_greater(unittest.TestCase):
    def test(self):
        self.assertTrue(check(120))

if __name__=='__main__':

    unittest.main()