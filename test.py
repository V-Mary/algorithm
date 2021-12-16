import unittest
import main


class TestRabinKarp(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main.search("vev", "hevevhjbevbwjwvbvne", 101), [2])


if __name__ == '__main__':
    unittest.main()