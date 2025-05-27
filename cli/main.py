# cli/main.py

from db.setup import Session, init_db
from models.category import Category
from models.menu_item import MenuItem

def print_menu():
    print("\nRestaurant Menu Manager")
    print("1. View Categories")
    print("2. Add Category")
    print("3. View Menu Items")
    print("4. Add Menu Item")
    print("5. Delete Category")
    print("6. Delete Menu Item")
    print("7. Exit")

def start_cli():
    init_db()
    session = Session()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            categories = session.query(Category).all()
            for cat in categories:
                print(f"{cat.id}: {cat.name}")
                for item in cat.menu_items:
                    print(f"  - {item.name} (${item.price}): {item.description}")

        elif choice == "2":
            name = input("Enter category name: ").strip()
            if session.query(Category).filter_by(name=name).first():
                print("Category already exists.")
            else:
                session.add(Category(name=name))
                session.commit()
                print("Category added.")

        elif choice == "3":
            items = session.query(MenuItem).all()
            for item in items:
                print(f"{item.id}: {item.name} (${item.price}) - {item.description} [Category: {item.category.name}]")

        elif choice == "4":
            name = input("Item name: ").strip()
            description = input("Description: ").strip()
            price = float(input("Price: "))
            category_id = int(input("Category ID: "))
            category = session.query(Category).get(category_id)
            if not category:
                print("Invalid category.")
            else:
                session.add(MenuItem(name=name, price=price, description=description, category=category))
                session.commit()
                print("Menu item added.")

        elif choice == "5":
            cat_id = int(input("Category ID to delete: "))
            category = session.query(Category).get(cat_id)
            if category:
                session.delete(category)
                session.commit()
                print("Category deleted.")
            else:
                print("Category not found.")

        elif choice == "6":
            item_id = int(input("Menu Item ID to delete: "))
            item = session.query(MenuItem).get(item_id)
            if item:
                session.delete(item)
                session.commit()
                print("Item deleted.")
            else:
                print("Item not found.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
