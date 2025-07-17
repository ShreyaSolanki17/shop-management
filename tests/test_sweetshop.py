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

    def test_search_sweets(self):
        store = SweetStore()
        item1 = SweetItem(1001, "Kaju Katli", "Nut-Based", 60.0, 10)
        item2 = SweetItem(1002, "Gulab Jamun", "Milk-Based", 30.0, 15)
        item3 = SweetItem(1003, "Rasgulla", "Milk-Based", 40.0, 12)
        store.add_sweet(item1)
        store.add_sweet(item2)
        store.add_sweet(item3)

        # Search by name
        results = store.search_sweets(name="Gulab")
        self.assertEqual(results, [item2])

        # Search by category
        results = store.search_sweets(category="Milk-Based")
        self.assertIn(item2, results)
        self.assertIn(item3, results)
        self.assertEqual(len(results), 2)

        # Search by price range
        results = store.search_sweets(min_price=35.0, max_price=65.0)
        self.assertIn(item1, results)
        self.assertIn(item3, results)
        self.assertEqual(len(results), 2)

    def test_sort_sweets(self):
        store = SweetStore()
        item1 = SweetItem(1001, "Kaju Katli", "Nut-Based", 60.0, 10)
        item2 = SweetItem(1002, "Gulab Jamun", "Milk-Based", 30.0, 15)
        item3 = SweetItem(1003, "Barfi", "Milk-Based", 45.0, 8)
        store.add_sweet(item1)
        store.add_sweet(item2)
        store.add_sweet(item3)

        # Sort by price
        sorted_by_price = store.sort_sweets(by="price")
        self.assertEqual(sorted_by_price, [item2, item3, item1])

        # Sort by name
        sorted_by_name = store.sort_sweets(by="name")
        self.assertEqual(sorted_by_name, [item3, item2, item1])

    def test_purchase_sweet(self):
        store = SweetStore()
        item = SweetItem(1001, "Gulab Jamun", "Milk-Based", 50.0, 20)
        store.add_sweet(item)
        store.purchase_sweet(1001, 5)
        self.assertEqual(store.get_item_by_id(1001).quantity, 15)

    def test_purchase_insufficient_stock(self):
        store = SweetStore()
        item = SweetItem(1002, "Kaju Katli", "Nut-Based", 60.0, 3)
        store.add_sweet(item)
        with self.assertRaises(ValueError) as cm:
            store.purchase_sweet(1002, 5)
        self.assertEqual(str(cm.exception), "Insufficient stock")

    def test_purchase_nonexistent_sweet(self):
        store = SweetStore()
        with self.assertRaises(ValueError) as cm:
            store.purchase_sweet(9999, 2)
        self.assertEqual(str(cm.exception), "Sweet ID does not exist")

    def test_purchase_negative_quantity(self):
        store = SweetStore()
        item = SweetItem(1003, "Barfi", "Milk-Based", 40.0, 10)
        store.add_sweet(item)
        with self.assertRaises(ValueError) as cm:
            store.purchase_sweet(1003, -1)
        self.assertEqual(str(cm.exception), "Quantity must be greater than zero")

    def test_restock_sweet(self):
        store = SweetStore()
        item = SweetItem(1001, "Gulab Jamun", "Milk-Based", 50.0, 10)
        store.add_sweet(item)
        store.restock_sweet(1001, 5)
        self.assertEqual(store.get_item_by_id(1001).quantity, 15)

    def test_restock_negative_quantity(self):
        store = SweetStore()
        item = SweetItem(1002, "Kaju Katli", "Nut-Based", 60.0, 8)
        store.add_sweet(item)
        with self.assertRaises(ValueError) as cm:
            store.restock_sweet(1002, -3)
        self.assertEqual(str(cm.exception), "Restock quantity must be greater than zero")

    def test_restock_nonexistent_sweet(self):
        store = SweetStore()
        with self.assertRaises(ValueError) as cm:
            store.restock_sweet(9999, 10)
        self.assertEqual(str(cm.exception), "Sweet ID does not exist")
