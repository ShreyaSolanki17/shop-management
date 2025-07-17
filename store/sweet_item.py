class SweetItem:
    def __init__(self, id: int, name: str, category: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if not isinstance(name, str) or not isinstance(category, str):
            raise TypeError("Name and category must be strings")       
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity