from datetime import date

FILE_NAME = "expenses.txt"


def add_expense():
    """Naya expense add karke file mein save karta hai."""
    try:
        amount = float(input("Amount (Rs): "))
    except ValueError:
        print("Galat amount! Number daalo.\n")
        return

    category = input("Category (food/travel/study/other): ").strip().lower()
    today = date.today().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a") as f:
        f.write(f"{today},{category},{amount}\n")

    print("Expense add ho gaya!\n")


def read_expenses():
    """File se saare expenses padhke list return karta hai."""
    expenses = []
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    expenses.append((parts[0], parts[1], float(parts[2])))
    except FileNotFoundError:
        pass  # file abhi bani nahi, matlab koi expense nahi
    return expenses


def view_expenses():
    """Saare expenses table jaisa dikhata hai."""
    expenses = read_expenses()
    if not expenses:
        print("Abhi tak koi expense nahi hai.\n")
        return

    print(f"\n{'Date':<12}{'Category':<12}{'Amount':>10}")
    print("-" * 34)
    for d, cat, amt in expenses:
        print(f"{d:<12}{cat:<12}{amt:>10.2f}")
    print()


def show_total():
    """Total aur category-wise summary dikhata hai."""
    expenses = read_expenses()
    if not expenses:
        print("Abhi tak koi expense nahi hai.\n")
        return

    total = sum(amt for _, _, amt in expenses)
    print(f"\nTotal kharcha: Rs {total:.2f}")

    by_category = {}
    for _, cat, amt in expenses:
        by_category[cat] = by_category.get(cat, 0) + amt

    print("\nCategory-wise:")
    for cat, amt in by_category.items():
        print(f"  {cat}: Rs {amt:.2f}")
    print()


def main():
    while True:
        print("=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Galat choice, dobara try karo.\n")


if __name__ == "__main__":
    main()
