import unittest

from utils import print_time

from practical_algorithm_design.introduction_to_algorithm_design.alg.basic_string_sort import basic_string_sort


class TestBasicStringSort(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @print_time
    def test_lower(self):
        val = basic_string_sort("abccba")
        self.assertEqual(val, "aabbcc")

    @print_time
    def test_caps(self):
        val = basic_string_sort("INSERTIONSORT")
        self.assertEqual(val, "EIINNOORRSSTT")

    @print_time
    def test_blend(self):
        val = basic_string_sort("ABCbca")
        self.assertEqual(val, "ABCabc")
