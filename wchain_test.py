import unittest

from wchain import WChain


class WChainTest(unittest.TestCase):

    def test_chain1(self):
        w = WChain("test_wchain1.in")
        self.assertEqual(6, w.count_of_chains())

    def test_chain2(self):
        w = WChain("test_wchain2.in")
        self.assertEqual(3, w.count_of_chains())

    def test_chain3(self):
        w = WChain("test_wchain3.in")
        self.assertEqual(1, w.count_of_chains())



if __name__ == '__main__':
    unittest.main()

