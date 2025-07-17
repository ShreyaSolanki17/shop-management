import unittest
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from store.sweet_store import SweetStore
from store.sweet_item import SweetItem

class TestSweetStore(unittest.TestCase):
    def test_add_sweet(self):
        store = SweetStore()
        item = SweetItem(1001, "Gulab Jamun", "Milk-Based", 50.0, 20)
        store.add_sweet(item)  
        self.assertEqual(store.get_item_by_id(1001), item)
        self.assertEqual(len(store.list_items()), 1)

    def test_sweet_negative_price(self):
        with self.assertRaises(ValueError) as context:
            SweetItem(1002, "Rasgulla", "Milk-Based", -10.0, 10)
        self.assertEqual(str(context.exception), "Price cannot be negative")

    def test_sweet_negative_quantity(self):
        with self.assertRaises(ValueError) as context:
            SweetItem(1003, "Barfi", "Milk-Based", 15.0, -5)
        self.assertEqual(str(context.exception), "Quantity cannot be negative")

    def test_sweet_invalid_id_type(self):
        with self.assertRaises(TypeError) as context:
            SweetItem("id1004", "Ladoo", "Festival", 10.0, 10)
        self.assertEqual(str(context.exception), "ID must be an integer")

    def test_sweet_invalid_price_type(self):
        with self.assertRaises(TypeError) as context:
            SweetItem(1005, "Ladoo", "Festival", "free", 10)
        self.assertEqual(str(context.exception), "Price must be a number")

    def test_sweet_invalid_category_type(self):
        with self.assertRaises(TypeError) as context:
            SweetItem(1006, "Ladoo", 123, 10.0, 10)
        self.assertEqual(str(context.exception), "Name and category must be strings")

#Delete feature for the SweetStore
    def test_delete_sweet(self):
        store = SweetStore()
        item = SweetItem(1001, "Gulab Jamun", "Milk-Based", 50.0, 20)
        store.items[1001] = item  

        store.delete_sweet(1001)
        self.assertIsNone(store.get_item_by_id(1001))
        self.assertEqual(len(store.list_items()), 0)

    def test_delete_nonexistent_sweet(self):
        store = SweetStore()
        with self.assertRaises(ValueError) as context:
            store.delete_sweet(9999)
        self.assertEqual(str(context.exception), "Sweet ID does not exist")

    def test_view_sweets(self):
        store = SweetStore()
        item1 = SweetItem(1001, "Gulab Jamun", "Milk-Based", 50.0, 20)
        item2 = SweetItem(1002, "Kaju Katli", "Nut-Based", 60.0, 15)
        store.add_sweet(item1)
        store.add_sweet(item2)

        sweets = store.view_sweets()
        self.assertEqual(len(sweets), 2)
        self.assertIn(item1, sweets)
        self.assertIn(item2, sweets)



if __name__ == '__main__':
    unittest.main()

    
