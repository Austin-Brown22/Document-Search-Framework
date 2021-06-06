import unittest

from src.search_interface import *

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.search_comp = search_interface()
    
    def test_Canary(self):
        self.assertTrue(True)

    def test_search_chooses_match_from_generator(self):
        def gen():
            for i in ["good", "bad", "ugly"]:
                yield i
        
        self.search_comp.store = gen

        self.assertEqual("good", self.search_comp.search("good"))

    def test_search_returns_neg_one_when_no_match_found(self):
        def gen():
            for i in ["good", "bad", "ugly"]:
                yield i
        
        self.search_comp.store = gen

        self.assertEqual(-1, self.search_comp.search("foo"))
