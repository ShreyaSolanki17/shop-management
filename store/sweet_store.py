class SweetStore:
    def __init__(self):
       
        self.items = {}

    def add_sweet(self, item):
        # This method is left blank (pass) to cause a logical test failure.
        # The test will fail because this method doesn't actually store the item yet.
        pass

    def get_item_by_id(self, item_id):
        return self.items.get(item_id)

    def list_items(self):
        return list(self.items.values())
