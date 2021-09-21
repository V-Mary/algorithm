import unittest
from hash_table import *


class TestHashTable(unittest.TestCase):

    def test_search(self):
        table = [[(0, 'Nepal')], [(1, 'Ukraine')], [(2, 'UK')]]
        self.assertEqual( search(table, 2), "UK" )


    def test_delete(self):
        table = [[(0, 'Nepal')], [(1, 'Ukraine')], [(2, 'UK')]]
        self.assertEqual(delete(table, 1),  [[(0, 'Nepal')], [], [(2, 'UK')]])

    def test_insert(self):
        table = [[], [], []]
        self.assertEqual( insert(table, 0, 'Nepal'), [[(0, 'Nepal')], [], []] )