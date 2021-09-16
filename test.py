import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_asc(self):
        array = [0, 4, 6, 10, 8, 2]
        self.assertEqual(merge_sort(array, "asc"), [0, 2, 4, 6, 8, 10])

    def test_decs_asc(self):
        array = [10, 8, 6, 4, 2, 0]
        self.assertEqual(merge_sort(array, "asc"), [0, 2, 4, 6, 8, 10])

    def test_asc_asc(self):
        array = [0, 2, 4, 6, 8, 10]
        self.assertEqual(merge_sort(array, "asc"), [0, 2, 4, 6, 8, 10])


    def test_decs(self):
        array = [0, 4, 6, 10, 8, 2]
        self.assertEqual(merge_sort(array, "desc"), [10, 8, 6, 4, 2, 0])

    def test_asc_decs(self):
        array = [0, 2, 4, 6, 8, 10]
        self.assertEqual(merge_sort(array, "desc"), [10, 8, 6, 4, 2, 0])


    def test_decs_decs(self):
        array = [10, 8, 6, 4, 2, 0]
        self.assertEqual(merge_sort(array, "desc"), [10, 8, 6, 4, 2, 0])

