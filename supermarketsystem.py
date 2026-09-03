
#       SUPERMARKET MANAGEMENT SYSTEM

products = {
    1: {"name": "Sugar", "price": 5000, "stock": 20},
    2: {"name": "Bread", "price": 4000, "stock": 15},
    3: {"name": "Milk", "price": 3500, "stock": 25},
    4: {"name": "Rice", "price": 6000, "stock": 30},
    5: {"name": "Soap", "price": 3000, "stock": 18}
}

sales = []

# DISPLAY PRODUCTS


def display_products():
    print("\nPRODUCTS ")
    print("ID\tProduct\t\tPrice\tStock")
    print("------------------------------------------")

    for product_id, product in products.items():
        print(
            f"{product_id}\t{product['name']:<12}\t"
            f"UGX {product['price']:<6}\t{product['stock']}"
        )



# ADD PRODUCT

def add_product():
    print("\n========== ADD PRODUCT ==========")

    product_id = int(input("Enter product ID: "))

    if product_id in products:
        print("Product ID already exists.")
        return

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter quantity in stock: "))

    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully!")


# SEARCH PRODUCT

def search_product():
    print("\n========== SEARCH PRODUCT ==========")

    search = input("Enter product name: ").lower()

    found = False

    for product_id, product in products.items():

        if search in product["name"].lower():

            print("\nProduct found:")
            print("ID:", product_id)
            print("Name:", product["name"])
            print("Price: UGX", product["price"])
            print("Stock:", product["stock"])

            found = True

    if not found:
        print("Product not found.")


# ------------------------------------------
# MAKE SALE
# ------------------------------------------

def make_sale():

    cart = []
    total = 0

    print("\n========== MAKE SALE ==========")

    while True:

        display_products()

        product_id = int(input("\nEnter product ID (0 to finish): "))

        if product_id == 0:
            break

        if product_id not in products:
            print("Invalid product ID.")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if quantity > products[product_id]["stock"]:
            print("Not enough stock available.")
            continue

        product = products[product_id]

        cost = product["price"] * quantity

        cart.append({
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity,
            "cost": cost
        })

        total += cost

        # Reduce stock
        products[product_id]["stock"] -= quantity

        print(f"{quantity} x {product['name']} added to cart.")

    if len(cart) == 0:
        print("No items purchased.")
        return

    # --------------------------------------
    # PRINT RECEIPT
    # --------------------------------------

    print("\n==========================================")
    print("              SUPERMARKET RECEIPT")
    print("==========================================")

    for item in cart:
        print(
            f"{item['name']:<12} "
            f"{item['quantity']} x UGX {item['price']} = "
            f"UGX {item['cost']}"
        )

    print("------------------------------------------")
    print(f"TOTAL: UGX {total}")
    print("==========================================")

    # Payment
    while True:

        payment = float(input("Enter amount paid: UGX "))

        if payment < total:
            print("Insufficient money. Please enter a larger amount.")
        else:
            break

    change = payment - total

    print(f"Amount Paid: UGX {payment}")
    print(f"Change: UGX {change}")
    print("Thank you for shopping with us!")

    # Record sale
    sales.append({
        "items": cart,
        "total": total
    })


# ------------------------------------------
# SALES SUMMARY
# ------------------------------------------

def sales_summary():

    print("\n========== SALES SUMMARY ==========")

    if len(sales) == 0:
        print("No sales have been made yet.")
        return

    total_sales = 0

    for number, sale in enumerate(sales, start=1):

        print(f"Sale {number}: UGX {sale['total']}")

        total_sales += sale["total"]

    print("-----------------------------------")
    print(f"TOTAL SALES: UGX {total_sales}")


# ------------------------------------------
# UPDATE STOCK
# ------------------------------------------

def update_stock():

    print("\n========== UPDATE STOCK ==========")

    display_products()

    product_id = int(input("\nEnter product ID: "))

    if product_id not in products:
        print("Product not found.")
        return

    quantity = int(input("Enter quantity to add: "))

    products[product_id]["stock"] += quantity

    print("Stock updated successfully!")
    print(
        f"{products[product_id]['name']} now has "
        f"{products[product_id]['stock']} units."
    )


# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

def main():

    while True:

        print("\n")
        print("==========================================")
        print("       SUPERMARKET MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. View Products")
        print("2. Add Product")
        print("3. Search Product")
        print("4. Make Sale")
        print("5. Update Stock")
        print("6. Sales Summary")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_products()

        elif choice == "2":
            add_product()

        elif choice == "3":
            search_product()

        elif choice == "4":
            make_sale()

        elif choice == "5":
            update_stock()

        elif choice == "6":
            sales_summary()

        elif choice == "7":
            print("\nThank you for using the Supermarket System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()
students = []


def calculate_grade(mark):
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")
    mark = float(input("Enter student's mark: "))

    grade = calculate_grade(mark)

    student = {
        "name": name,
        "mark": mark,
        "grade": grade
    }

    students.append(student)

    print(f"{name} added successfully.")
    print(f"Grade: {grade}")


def display_students():
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENTS =====")

    for student in students:
        print(
            f"Name: {student['name']} | "
            f"Mark: {student['mark']} | "
            f"Grade: {student['grade']}"
        )


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found!")
            print(f"Name: {student['name']}")
            print(f"Mark: {student['mark']}")
            print(f"Grade: {student['grade']}")
            return

    print("Student not found.")