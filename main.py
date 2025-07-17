from store.sweet_store import SweetStore
from store.sweet_item import SweetItem

def main():
    store = SweetStore()

    while True:
        print("\n=== Sweet Shop CLI ===")
        print("1. Add Sweet")
        print("2. Delete Sweet")
        print("3. View All Sweets")
        print("4. Search Sweets")
        print("5. Sort Sweets")
        print("6. Purchase Sweet")
        print("7. Restock Sweet")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        try:
            if choice == "1":
                id = int(input("Enter ID: "))
                name = input("Enter Name: ")
                category = input("Enter Category: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                item = SweetItem(id, name, category, price, quantity)
                store.add_sweet(item)
                print(" Sweet added successfully.")

            elif choice == "2":
                id = int(input("Enter ID to delete: "))
                store.delete_sweet(id)
                print(" Sweet deleted.")

            elif choice == "3":
                items = store.list_items()
                if not items:
                    print("📭 No sweets in inventory.")
                else:
                    for item in items:
                        print(item)

            elif choice == "4":
                name = input("Search by Name (leave empty to skip): ").strip() or None
                category = input("Search by Category (leave empty to skip): ").strip() or None
                min_price = input("Min Price (leave empty to skip): ").strip()
                max_price = input("Max Price (leave empty to skip): ").strip()

                min_price = float(min_price) if min_price else None
                max_price = float(max_price) if max_price else None

                results = store.search_sweets(name=name, category=category, min_price=min_price, max_price=max_price)
                if results:
                    for item in results:
                        print(item)
                else:
                    print(" No matching sweets found.")

            elif choice == "5":
                by = input("Sort by 'price' or 'name': ").strip()
                sorted_items = store.sort_sweets(by)
                for item in sorted_items:
                    print(item)

            elif choice == "6":
                id = int(input("Enter ID to purchase: "))
                qty = int(input("Enter Quantity: "))
                store.purchase_sweet(id, qty)
                print("🛒 Purchase successful.")

            elif choice == "7":
                id = int(input("Enter ID to restock: "))
                qty = int(input("Enter Quantity: "))
                store.restock_sweet(id, qty)
                print(" Restock complete.")

            elif choice == "8":
                print("Exiting...")
                break

            else:
                print(" Invalid choice. Try again.")

        except ValueError as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()
