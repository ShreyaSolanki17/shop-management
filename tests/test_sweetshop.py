import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from store.sweet_store import SweetStore
from store.sweet_item import SweetItem

class TestSweetStore(unittest.TestCase):
    def test_add_sweet(self):
        store = SweetStore()
        item = SweetItem(1001, "Gulab Jamun", "Milk-Based", 50.0, 20)
        store.add_sweet(item)  # This will raise NotImplementedError
        self.assertEqual(store.get_item_by_id(1001), item)
        self.assertEqual(len(store.list_items()), 1)

if __name__ == '__main__':
    unittest.main()

    
