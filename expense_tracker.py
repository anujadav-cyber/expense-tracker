import csv
import os
from datetime import date

FILENAME = "expenses.csv"

def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])
        print("Created new expenses file.")

def add_expense():
    """Prompt user to add a new expense."""
    print("\n--- Add Expense ---")
    category = input("Category (Food/Transport/Shopping/Bills/Other): ").strip()
    description = input("Description: ").strip()
    
    try:
        amount = float(input("Amount (₹): ").strip())
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    today = date.today().strftime("%Y-%m-%d")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, category, description, amount])
    
    print(f"✅ Added: {description} — ₹{amount:.2f}")

def view_expenses():
    """Display all expenses in a readable format."""
    print("\n--- All Expenses ---")
    total = 0

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.")
        return

    for row in rows:
        print(f"{row['Date']} | {row['Category']:<12} | {row['Description']:<20} | ₹{float(row['Amount']):.2f}")
        total += float(row['Amount'])

    print(f"\nTotal Spent: ₹{total:.2f}")

def view_summary():
    """Show total spending grouped by category."""
    print("\n--- Summary by Category ---")
    summary = {}

    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cat = row['Category']
            summary[cat] = summary.get(cat, 0) + float(row['Amount'])

    if not summary:
        print("No expenses recorded yet.")
        return

    for category, total in sorted(summary.items()):
        print(f"{category:<15} ₹{total:.2f}")

def main():
    initialize_file()
    
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()