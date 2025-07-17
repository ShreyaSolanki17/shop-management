class SweetStore:
    def __init__(self):
        self.items = {}

    def add_sweet(self, item):
        
        if item.id in self.items:
            raise ValueError("Sweet ID already exists")
        
        self.items[item.id] = item

    def get_item_by_id(self, item_id):
        return self.items.get(item_id)

    def list_items(self):
        return list(self.items.values())
    
    def delete_sweet(self, item_id):
        if item_id not in self.items:
            raise ValueError("Sweet ID does not exist")
        del self.items[item_id]

    def view_sweets(self):
        return list(self.items.values())
    
    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        results = list(self.items.values())
        if name:
            results = [item for item in results if name.lower() in item.name.lower()]
        if category:
            results = [item for item in results if item.category.lower() == category.lower()]
        if min_price is not None:
            results = [item for item in results if item.price >= min_price]
        if max_price is not None:
            results = [item for item in results if item.price <= max_price]
        return results

    def sort_sweets(self, by="price"):
        if by not in ["price", "name"]:
            raise ValueError("Sort by 'price' or 'name' only")
        return sorted(
            self.items.values(),
            key=lambda x: x.price if by == "price" else x.name
        )

    def purchase_sweet(self, item_id, quantity):
        item = self.get_item_by_id(item_id)
        if not item:
            raise ValueError("Sweet ID does not exist")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        if item.quantity < quantity:
            raise ValueError("Insufficient stock")
        item.quantity -= quantity

    def restock_sweet(self, item_id, quantity):
        item = self.get_item_by_id(item_id)
        if not item:
            raise ValueError("Sweet ID does not exist")
        if quantity <= 0:
            raise ValueError("Restock quantity must be greater than zero")
        item.quantity += quantity

