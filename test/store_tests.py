import unittest

from src.store_interface import *

class TestStore(unittest.TestCase):

    def setUp(self):
        self.store_comp = store_interface()
    
    def test_Canary(self):
        self.assertTrue(True)

    def test_store_retains_the_arr_we_give_it(self):
        self.store_comp.store(["good", "bad", "ugly"])

        self.assertEqual(["good", "bad", "ugly"], self.store_comp.get_entries())

    def test_store_appends_new_entries(self):
        self.store_comp.store(["good", "bad"])
        self.store_comp.store(["ugly"])

        self.assertEqual(["good", "bad", "ugly"], self.store_comp.get_entries())