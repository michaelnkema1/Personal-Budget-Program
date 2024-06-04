import json

# Function to load transactions from a file
def load_transactions(filename):
    try:
        with open(filename, 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = {"income": [], "expenses": []}
    return transactions

# Function to save transactions to a file
def save_transactions(filename, transactions):
    with open(filename, 'w') as file:
        json.dump(transactions, file, indent=4)

# Function to add income
def add_income(transactions):
    amount = float(input("Enter income amount: "))
    description = input("Enter income description: ")
    transactions["income"].append({"amount": amount, "description": description})
    print("Income added successfully.")

# Function to add an expense
def add_expense(transactions):
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense description: ")
    transactions["expenses"].append({"amount": amount, "description": description})
    print("Expense added successfully.")

# Function to view all transactions
def view_transactions(transactions):
    print("\nIncome:")
    for income in transactions["income"]:
        print(f"Amount: {income['amount']}, Description: {income['description']}")
    print("\nExpenses:")
    for expense in transactions["expenses"]:
        print(f"Amount: {expense['amount']}, Description: {expense['description']}")

# Function to calculate total income
def calculate_total_income(transactions):
    return sum(income["amount"] for income in transactions["income"])

# Function to calculate total expenses
def calculate_total_expenses(transactions):
    return sum(expense["amount"] for expense in transactions["expenses"])

# Function to calculate balance
def calculate_balance(transactions):
    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    return total_income - total_expenses

# Main function
def main():
    filename = "transactions.json"
    transactions = load_transactions(filename)

    while True:
        print("\nPersonal Budget Program")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Calculate Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income(transactions)
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            view_transactions(transactions)
        elif choice == "4":
            balance = calculate_balance(transactions)
            print(f"Your current balance is: {balance}")
        elif choice == "5":
            save_transactions(filename, transactions)
            print("Transactions saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
