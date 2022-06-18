from kata import *
import unittest


class Test_Generate_Hashtag(unittest.TestCase):
    def test1(self):
        array = [[1,2,3],
                 [4,5,6],
                 [7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(snail(array), expected)

    def test2(self):
        array = [[1,2,3],
                [8,9,4],
                [7,6,5]]
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(snail(array), expected)

    def test3(self):
        array = [[ 1, 2, 3, 4],
                 [ 5, 6, 7, 8],
                 [ 9,10,11,12],
                 [13,14,15,16]]
        expected = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
        self.assertEqual(snail(array), expected)

if __name__ == '__main__':
    unittest.main()