import datetime
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Predefined categories
categories = ["Food", "Transportation", "Entertainment", "Bills", "Other"]

# Database setup
def setup_database():
    conn = sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT NOT NULL,
                        category TEXT NOT NULL,
                        amount REAL NOT NULL,
                        description TEXT
                    )''')
    conn.commit()
    conn.close()

# Function to validate date
def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to log a new expense 
def add_expense():
    print("\n***!!Add a New Expense!!***")
    
    
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if validate_date(date):
            break
        else:
            print("Invalid date format. Please try again.")

    while True:
        print("Available categories:")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        category_choice = input("Select a category by number (or type a new category): ")

        if category_choice.isdigit() and 1 <= int(category_choice) <= len(categories):
            category = categories[int(category_choice) - 1]
            break
        elif category_choice.strip():
            category = category_choice.strip()
            if category not in categories:
                categories.append(category)  # Add new category
            break
        else:
            print("Invalid choice. Please try again.")

    # Get and validate the amount
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    # Get the optional description
    description = input("Enter a description (optional): ")

    # Save the expense to the database
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
                   (date, category, amount, description))
    conn.commit()
    conn.close()

    print("\nExpense logged successfully!")

# Function to display all logged expenses
def show_expenses():
    print("\n***!!Logged Expense!!***")
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No expenses recorded.")
        return

    for row in rows:
        print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: ${row[3]:.2f}, Description: {row[4]}")

# Function to calculate total spending over a specific period
def total_spending(period='monthly'):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    
    if period == 'monthly':
        today = datetime.date.today()
        first_day = today.replace(day=1)
        cursor.execute("SELECT SUM(amount) FROM expenses WHERE date >= ?", (str(first_day),))
    elif period == 'weekly':
        today = datetime.date.today()
        last_week = today - datetime.timedelta(days=7)
        cursor.execute("SELECT SUM(amount) FROM expenses WHERE date >= ?", (str(last_week),))

    total = cursor.fetchone()[0]
    conn.close()
    
    return total if total else 0.0

# Function to get spending breakdown by category
def spending_by_category():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    category_spending = cursor.fetchall()
    conn.close()
    
    return category_spending

# Function to generate insights from spending data
def generate_insights():
    category_spending = spending_by_category()
    if not category_spending:
        print("No data to generate insights.")
        return

    # Find highest spending category
    highest_category = max(category_spending, key=lambda x: x[1])
    print(f"Highest Spending Category: {highest_category[0]} with ${highest_category[1]:.2f}")

# Function to visualize spending (pie chart for category breakdown)
def visualize_spending():
    category_spending = spending_by_category()
    if not category_spending:
        print("No data to visualize.")
        return

    categories, amounts = zip(*category_spending)
    
    # Pie chart
    plt.figure(figsize=(7, 7))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title('Spending Breakdown by Category')
    plt.show()
    

def visualize_monthly_trends():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT strftime('%Y-%m', date) AS month, SUM(amount) FROM expenses GROUP BY month ORDER BY month")
    monthly_spending = cursor.fetchall()
    conn.close()

    if not monthly_spending:
        print("No data to visualize trends.")
        return

    # Filter out rows with None values
    monthly_spending = [(month, amount) for month, amount in monthly_spending if month and amount is not None]

    if not monthly_spending:
        print("No valid data to visualize trends.")
        return

    months, amounts = zip(*monthly_spending)

    # Line chart
    plt.figure(figsize=(10, 6))
    plt.plot(months, amounts, marker='o', color='b')
    plt.title('Monthly Spending Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Spending ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main Program Workflow
def main():
    setup_database()

    while True:
        print("\n***!! Expense Tracker!!***")
        print("1. Add a New Expense")
        print("2. View Logged Expenses")
        print("3. View Total Spending (Monthly)")
        print("4. View Total Spending (Weekly)")
        print("5. View Spending Breakdown by Category")
        print("6. Generate Insights")
        print("7. Visualize Spending Breakdown")
        print("8. Visualize Monthly Spending Trends")
        print("9. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            total = total_spending(period='monthly')
            print(f"Total spending this month: ${total:.2f}")
        elif choice == "4":
            total = total_spending(period='weekly')
            print(f"Total spending this week: ${total:.2f}")
        elif choice == "5":
            category_spending = spending_by_category()
            for category, amount in category_spending:
                print(f"{category}: ${amount:.2f}")
        elif choice == "6":
            generate_insights()
        elif choice == "7":
            visualize_spending()
            input("\nPress Enter to return to the main menu...")
        elif choice == "8":
            visualize_monthly_trends()
            input("\nPress Enter to return to the main menu...")
        elif choice == "9":
            print("Exiting the program........")
            print("\nByeee :(")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
