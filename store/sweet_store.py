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

